import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.substitutions import Command, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    # Get package directories
    tentacle_description_pkg = get_package_share_directory("tentacle_description")
    ros_gz_sim_pkg = get_package_share_directory("ros_gz_sim")

    # Declare launch argument for model
    model_arg = DeclareLaunchArgument(
        name="model",
        default_value=os.path.join(tentacle_description_pkg, "urdf", "tentacle.xacro"),
        description="Absolute path to robot xacro file"
    )

    # Set Gazebo resource path to support models, meshes, etc.
    gazebo_resource_path = SetEnvironmentVariable(
        name="GZ_SIM_RESOURCE_PATH",
        value=[str(Path(tentacle_description_pkg).parent.resolve())]
    )

    # Detect ROS distribution to decide Ignition/Gazebo classic toggle
    ros_distro = os.environ.get("ROS_DISTRO", "")
    is_ignition = "True" if ros_distro == "humble" else "False"

    # Robot description processed via xacro
    robot_description = ParameterValue(
        Command([
            "xacro ",
            LaunchConfiguration("model"),
            " is_ignition:=",
            is_ignition
        ]),
        value_type=str
    )

    # Load bridge config YAML path
    ros_gz_bridge_config = os.path.join(tentacle_description_pkg, "config", "ros_gz_bridge_gazebo.yaml")

    # Node: robot_state_publisher
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[
            {"robot_description": robot_description},
            {"use_sim_time": True}
        ]
    )

    # Launch Gazebo Sim
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_pkg, "launch", "gz_sim.launch.py")
        ),
        launch_arguments=[("gz_args", "-v 4 -r empty.sdf")]
    )

    # Spawn robot in simulation
    gz_spawn_entity = Node(
        package="ros_gz_sim",
        executable="create",
        output="screen",
        arguments=[
            "-topic", "robot_description",
            "-name", "tentacle",
            "-allow_renaming", "false",
            "-z", "0.32",
            "-x", "0.0",
            "-y", "0.0",
            "-Y", "0.0"
        ]
    )

    # Start ros_gz_bridge node
    gz_ros2_bridge = Node(
        package="ros_gz_bridge",
        executable="parameter_bridge",
        parameters=[{
            'config_file': ros_gz_bridge_config,
        }],
        output="screen"
    )

    return LaunchDescription([
        model_arg,
        gazebo_resource_path,
        robot_state_publisher_node,
        gazebo,
        gz_spawn_entity,
        gz_ros2_bridge
    ])
