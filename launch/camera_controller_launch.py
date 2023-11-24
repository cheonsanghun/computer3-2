from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camera_controller_package',  # 카메라 컨트롤러 패키지 이름으로 수정
            executable='camera_controller_node',
            name='camera_controller_pr001',
            output='screen',
            parameters=[
                {'camera_name': LaunchConfiguration('car_name') + '_camera_pr001'},
                # 추가적인 카메라 컨트롤러 파라미터 설정
            ]
        ),

        # 카메라 컨트롤러 추가 - PR002
        Node(
            package='camera_controller_package',  # 카메라 컨트롤러 패키지 이름으로 수정
            executable='camera_controller_node',
            name='camera_controller_pr002',
            output='screen',
            parameters=[
                {'camera_name': LaunchConfiguration('car_name') + '_camera_pr002'},
                # 추가적인 카메라 컨트롤러 파라미터 설정
            ]
        ),
    ])
