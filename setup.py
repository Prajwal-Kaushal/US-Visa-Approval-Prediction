# setup.py looks for the constructor file in each folder wherever it gets the constructor file that will be useed as the local folder.
from setuptools import setup, find_packages

setup(
    name="us_visa",
    version="0.0.0",
    author="Prajwal Kaushal",
    author_email="prajwalkkp@gmail.com",
    packages=find_packages()
)

# if we want to install some folder as the local package then we have to use this code.
# this is copieed from internet.
