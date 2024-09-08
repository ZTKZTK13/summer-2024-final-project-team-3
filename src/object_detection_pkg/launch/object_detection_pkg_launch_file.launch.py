from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()
    object_detection_node = Node(
        package="object_detection_pkg",
        executable="object_detection_node.py",
        output="screen",
    )
    ld.add_action(object_detection_node)

    pid_node = Node(
        package="object_detection_pkg",
        executable="pid.py",
        output="screen",
    )
    ld.add_action(pid_node)

    vesc_twist_node = Node(
        package="object_detection_pkg",
        executable="vesc_twist_node.py",
        output="screen",
    )
    ld.add_action(vesc_twist_node)

    return ld
