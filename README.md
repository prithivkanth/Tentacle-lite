# 🐙 Tentacle Robot – ROS 2 + MoveIt 2

A **ROS 2-based tentacle-style robotic arm** simulation with full **MoveIt 2 motion planning**, controller integration, and visualization support.  
This project demonstrates a **complete robotic manipulation pipeline** — from URDF modeling to motion planning and execution.

---

## 🚀 Project Overview

The **Tentacle Robot** is a 3-DOF articulated robotic arm designed for simulation and motion planning experiments using **ROS 2** and **MoveIt 2**.

### Key Highlights
- ✅ Modular ROS 2 workspace structure  
- ✅ Fully configured **MoveIt 2** pipeline  
- ✅ ros2_control-based controllers  
- ✅ RViz visualization & planning interface  
- ✅ Ready for Gazebo simulation extension  

---

---

## 🧠 Core Packages Explained

### 🔹 `tentacle_description`
- Contains **URDF/XACRO**, meshes, and visualization launch files
- Responsible for robot modeling and TF tree

### 🔹 `tentacle_controller`
- Uses **ros2_control**
- Defines joint controllers and hardware interfaces
- YAML-based controller configuration

### 🔹 `tentacle_moveit`
- Auto-generated & customized **MoveIt 2 configuration**
- Handles:
  - Motion planning
  - Kinematics
  - Planning pipelines
  - RViz planning interface

---

## ▶️ How to Run the Project

### 1️⃣ Build the Workspace
    
              cd ~/tentacle2
              colcon build
              source install/setup.bash
---
2️⃣ Launch MoveIt (Final Launch File)

This single command brings up:

  Robot model

  Controllers

  MoveIt 2

  RViz planning interface

     ros2 launch tentacle_moveit moveit.launch.py
---

🕹️ What You Can Do in RViz

 🎯 Set interactive goal poses

 🧭 Plan joint-space & Cartesian paths

 ▶️ Execute trajectories

 🔍 Visualize collision objects

🔄 Inspect TF frames & joint states

---

📌 Future Improvements

 🔧 Gazebo hardware interface

 🤖 Real motor driver integration

 🧠 Inverse kinematics optimization

 🧪 Trajectory smoothing & constraints

 🌐 ROS 2 control via external nodes

---

⭐ Support

If you find this project useful:

 🌟 Star the repository

 🍴 Fork and experiment

 🧠 Use it as a learning reference

Happy Planning! 🤖✨
