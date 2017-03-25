import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__),fname)).read()

setup(
    name = 'Neon',
    version='0.0.5',
    author='Rajat Gupta, Abhishek Khandelwal , Siddhant Dash',
    packages = ['Neon','test','gspread'],
    license='Apache',
    url='https://github.com/abhi98khandelwal/HINT',
    long_description=read('README'),

)
