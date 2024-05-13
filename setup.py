from setuptools import find_packages, setup


with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="spaceflight310",
    version="1.0",
    packages=find_packages(),
    install_requires=required_packages,
)
