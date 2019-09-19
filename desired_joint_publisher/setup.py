from setuptools import find_packages
from setuptools import setup

package_name = 'desired_joint_publisher'

setup(
    name=package_name,
    version='2.12.13',
    packages=[],
    py_modules=[
        'desired_joint_publisher',
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='David V. Lu!!',
    author_email='davidvlu@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'A python node to publish `ros2_control_interfaces/msg/JointControl` messages for a '
        'robot described with URDF.'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'desired_joint_publisher = desired_joint_publisher:main',
        ],
    },
)
