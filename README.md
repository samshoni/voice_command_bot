# Voice Command Robot in ROS 2

🎙️ Control a robot using your real voice with ROS 2 and Python!

## Features
- Speech recognition using Google's API
- Publishes `/cmd_vel` messages
- Works with TurtleBot3 Gazebo simulation

## To Run

```bash
cd ~/voice_ws
source install/setup.bash
ros2 run voice_command_bot voice_to_cmd

Say commands like:

    "go forward"

    "turn left"

    "stop"
