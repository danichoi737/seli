import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    # Parameters
    param_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(get_package_share_directory('seli_bringup'), 'param')
    )

    # Description(URDF) launch directory
    description_pkg_dir = LaunchConfiguration(
        'description_pkg_dir',
        default=os.path.join(get_package_share_directory('seli_description'), 'launch')
    )

    return LaunchDescription([

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([description_pkg_dir, '/description.launch.py'])
        ),
    ])
