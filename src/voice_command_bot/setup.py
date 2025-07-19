from setuptools import setup

package_name = 'voice_command_bot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sam',
    maintainer_email='your_email@example.com',
    description='Voice controlled robot using ROS 2 and speech recognition',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'voice_to_cmd = voice_command_bot.voice_to_cmd:main',
        ],
    },
)

