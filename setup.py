from setuptools import find_packages
from setuptools import setup

package_name = 'desired_joint_publisher'

setup(
    name=package_name,
    version='0.2.0',
    packages=[],
    py_modules=[
        'desired_joint_publisher', 'ut_param_server'
    ],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Poh Zhi-Ee',
    author_email='zhiee.poh@httechnology.com',
    keywords=['ROS', 'ROS2'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: MIT',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'A python node to publish `ros2_control_interfaces/msg/JointControl` messages for a robot described with URDF.'
    ),
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'desired_joint_publisher = desired_joint_publisher:main',
        ],
    },
)
