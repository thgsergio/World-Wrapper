# World-Wrapper
A ROS2 package used to choose your own world file for UAV simulation dynamically.


## How to use

1. Clone the repository
```bash
mkdir -p ~/git
cd ~/git
git clone https://github.com/thgsergio/World-Wrapper.git
```

2. Create a symlink of the package into your own ROS2 workspace
```bash
ln -s ~/git/World-Wrapper/world_wrapper ~/your_ws/src
```

3. Compile your workspace
```bash
cd ~/your_ws
colcon build --packages-select world_wrapper
```

4. Source your workspace
```bash
source ~/your_ws/install/setup.bash
```

5. Run the launch file
```bash
ros2 launch world_wrapper wrapper.launch.py world_package:=your_pkg world_name:=your_world real_time:=1.0 
```


## Launch Arguments

- **world_package:** refers to the package where the desired world is located.
- **world_name:** refers to the name of the world without the ".world" extension.
- **real_time:** argument needed for the UAV simulation.
