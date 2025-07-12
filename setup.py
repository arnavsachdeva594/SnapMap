from setuptools import setup, find_packages

setup(
    name='snapmap',
    version='0.1.9',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
    'console_scripts': [
        'snapmap=snapmap.cli:main',
    ],
},
    author='__',
    description='AI powered geo-location to uncover the location of photos.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)