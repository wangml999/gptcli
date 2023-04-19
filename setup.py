from setuptools import setup, find_packages

setup(
    name='gptcli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'pynput',
    ],
    entry_points = {
        'console_scripts': ['abc=src.gptcli:main'],
    },
    python_requires='>=3.6',
)
