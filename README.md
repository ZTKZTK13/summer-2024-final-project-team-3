<div id="top"></div>

<h1 align="center">The Scanner 3.0!</h1>

<!-- PROJECT LOGO -->
<br />
<div align="center">

<img width="1370" alt="Screen Shot 2024-09-07 at 10 14 00 PM" src="https://github.com/user-attachments/assets/23ed5c43-0378-4a74-9677-2915f6d3f65c">

<h3>MAE148 Final Project, Summer Session II 2024</h3>
<p>
Team 3
</p>

<img width="785" alt="Screen Shot 2024-09-07 at 10 12 54 PM" src="https://github.com/user-attachments/assets/2336dfc5-b0aa-4330-b909-51a0198543bb">

</div>

## Table of Contents
  <ol>
    <li><a href="#team-members-and-major">Team Members and Major</a></li>
    <li><a href="#final-project">Final Project</a></li>
    <li><a href="#demonstrations">Demonstrations</a></li>
    <li><a href="#robot-design">Robot Design</a></li>
    <li><a href="#contact-information">Contact Information</a></li>
  </ol>

<!-- TEAM MEMBERS -->
## Team Members and Major

<div align="center">
    <p align = "center">Guanjin Li, Electrical Engineering and Mathematics
    </p> Jonathan Dela Cruz, Mechanical Engineering
    </p> Peter Chang, Electrical Engineering</p>

  <br>
Special Acknowledgements to: Conor Norris, Eric Foss, Alexander Haken, Dr. Jack Silberman
</div>

<!-- Final Project -->
## Final Project
The initial goal of our final project was to develop a self-driving robot with the capability of detecting and avoiding obstacles while staying on its path. However, due to the time constraints of taking this course, MAE 148, over the summer, we had to shift our goal into a more realistic one by having the robot just detect and avoid objects and people. Below is a summary of our goals, what we achieved, and further discussion regarding what challenges we faced along with what we could have done with more time.

<!-- Original Goals -->
### Goals
- Obstacle Detection by Robot
    - RoboFlow implementation onto OAKD-Lite camera for obstacle detection
    - Further software implementation via Depth-AI for detecting more complex obstacles 
- Robot Reaction to Obstacle Detection
    - Robot to stop before resuming motion
- Robot To Not Deviate From Its Path
    - Robot to return to its path after obstacle avoidance
    - Further utilization of ROS2 via node addition

<!-- What We Accomplished -->
### Goals We Met
- Simple Obstacle Detection by Robot
    - Collected data of two objects (gym bottle and shoe) for obstacle detection
    - Trained and utilized Roboflow model of robot to have it identify obstacles
- Robot Reaction to Obstacle Detection
    - Robot reacted to different objects by stopping before resuming its motion

<!-- Challenges and Issues -->
### Challenges and Issues We Ran Into
- Getting Robot to Steer Around Object
    - Getting the robot to loop around objects in its path didn't quite work out
    - While robot detected and avoided the objects, the robot only turned away and didn't straighten out to go around the objects for resuming its path

<!-- What We'd Have Done If More Time -->
### What We Could Have Accomplished Had Time Allowed...
- Detection of and Reaction to More Complex Obstacles
    - More obstacles such as walls would have been tested
- More Thorough and Extensive Training of Roboflow Model
    - Integration of depth feature of OAK-D Lite to stop robot based on its distance away from object
    - More datasets would have been taken to ensure more consistency of model
- Robot Staying On Course after Detecting and Reacting to Obstacles
    - Addition of path detection node to ROS2 package to prevent the robot from deviating off its path
 
<!-- Model Training -->
## Demonstrations
Below are the demonstrations for our Roboflow model training, where we trained our robot to detect objects in its path, along with live demonstrations of our robot in action detecting and reacting to a stationary and moving object.

### Roboflow Training
![video](https://github.com/user-attachments/assets/9d9e0c58-1f48-4268-ab7c-9e6054efac88)

### Live Demo (Stationary Object)
![video](https://github.com/user-attachments/assets/ec922d81-780b-403e-bd7f-cf7e924ee2d1)

### Live Demo (Moving Object)
![video](https://github.com/user-attachments/assets/a59d9f0e-fc64-4db9-a010-92b666f66c5b)

![video](https://github.com/user-attachments/assets/dfcd699f-c9bb-4920-a1c8-6ca6afe581e3)

<!-- Robot Design and CAD Parts -->
## Robot Design

### CAD Parts
| Part | CAD Model |
|------|--------------|
| Nanobox (Top), by Guanjin Li | ![NanoBox_Top](https://github.com/user-attachments/assets/b6644c03-2f58-4f59-93f8-c730754946b2) |
| Nanobox (Bottom), by Guanjin Li | ![NanoBox_Bottom](https://github.com/user-attachments/assets/5f37eca3-dc13-4baf-ae14-bbcea524cd8b) |
| Robot Baseplate, by Conor Norris | <img width="634" alt="robot_baseplate" src="https://github.com/user-attachments/assets/c58225a6-1382-48f0-9053-e894711d9c2c"> |
| Camera Base, by Conor Norris | <img width="680" alt="camera_base" src="https://github.com/user-attachments/assets/c58ac54e-daeb-432f-a687-c8e055cc2940">|
| Camera Mount, by Conor Norris | <img width="633" alt="camera_mount" src="https://github.com/user-attachments/assets/a8a51167-2908-47d5-a221-c73adff04d0a"> |

### Wiring Diagram
Below is the wiring diagram that shows how the robot's electronic components were wired.
<img width="898" alt="Screen Shot 2024-09-08 at 12 29 02 AM" src="https://github.com/user-attachments/assets/a2103001-e63e-4a94-b147-64c41da78b2d">

### Software Implemented
- ROS2
- Roboflow
- Embedded Systems
- DonkeyCar AI

## Contact Information
- Guanjin Li, gul007@ucsd.edu
- Jonathan Dela Cruz, j3delacruz@ucsd.edu
- Peter Chang, p8chang@ucsd.edu
