from setuptools import setup
import os
from glob import glob

package_name = 'object_detection_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	(os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='j3delacruz@ucsd.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
		'object_detection_node.py = object_detection_pkg.object_detection_node:main',
		'camera.py = object_detection_pkg.camera:main',
		'inference.py = object_detection_pkg.inference:main',
		'pid.py = object_detection_pkg.pid:main',
		'vesc_client.py = object_detection_pkg.vesc_client:main',
		'vesc_twist_node.py = object_detection_pkg.vesc_twist_node:main',
        ],
    },
)
