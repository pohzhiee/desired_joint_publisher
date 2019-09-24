from setuptools import find_packages
from setuptools import setup

package_name = 'desired_joint_publisher'

setup(
    name=package_name,
    version='0.1.0',
    packages=[],
    py_modules=[
        'desired_joint_publisher',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Poh Zhi-Ee',
    author_email='zhiee.poh@httechnology.com',
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'A python node to publish `ros2_control_interfaces/msg/JointControl` messages for a robot described with URDF.'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'desired_joint_publisher = desired_joint_publisher:main',
        ],
    },
)