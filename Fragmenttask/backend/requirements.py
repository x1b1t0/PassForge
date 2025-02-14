from setuptools import setup, find_packages

setup(
    name='Fragmenttask',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'sqlalchemy',
        'requests',
        'pytest',
    ],
    entry_points={
        'console_scripts': [
            'fragmenttask=fragmenttask.cli:main',
        ],
    },
)