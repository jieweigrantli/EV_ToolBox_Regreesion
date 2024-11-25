from setuptools import setup, find_packages

setup(
    name='ev_toolbox_regression',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
        'boxsdk',
        'scikit-learn',
        'dotenv',
    ],
    description='A Python package for Box file processing and regression modeling for EV Toolbox',
    author='Your Name',
    author_email='your.email@example.com',
)