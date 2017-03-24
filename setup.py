import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(
    name = 'Neon',
    version='0.0.4',
    author='Rajat Gupta, Abhishek Khandelwal , Siddhant Dash',
    packages = ['Neon'],
)