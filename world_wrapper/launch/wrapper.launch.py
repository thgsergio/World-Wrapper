from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, EnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    world_package = LaunchConfiguration('world_package')
    world_name = LaunchConfiguration('world_name')
    real_time = LaunchConfiguration('real_time')

    pkg_share = FindPackageShare(world_package)

    world_path = PathJoinSubstitution([pkg_share, 'worlds', world_name])
    models_path = PathJoinSubstitution([pkg_share, 'models'])

    return LaunchDescription([
        DeclareLaunchArgument('world_package', default_value='laser_gazebo_resources'),
        DeclareLaunchArgument('world_name', default_value='custom_empty'),
        DeclareLaunchArgument('real_time', default_value='1.0'),

        SetEnvironmentVariable(
            'GAZEBO_MODEL_PATH',
            [models_path, ':', EnvironmentVariable('GAZEBO_MODEL_PATH', default_value='')]
        ),
        SetEnvironmentVariable(
            'GAZEBO_RESOURCE_PATH',
            [pkg_share, ':', EnvironmentVariable('GAZEBO_RESOURCE_PATH', default_value='')]
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('laser_uav_simulation'), '/launch/gazebo.launch.py'
            ]),
            launch_arguments={
                'world': world_path,
                'real_time': real_time
            }.items()
        ),
    ])
