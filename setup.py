from setuptools import find_packages, setup

package_name = 'materov'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kevinle',
    maintainer_email='kevinle@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'key_mapping = materov.key_mapping:main', # RHS: name of the topic, LHS: name of the file
            'communication = materov.communication:main',
            'spatial = materov.spatial:main'
        ],
    },
)
