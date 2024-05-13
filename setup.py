from setuptools import find_packages, setup
import os

entry_point = "spaceflight310 = spaceflight310.main:main"

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

# List of directories to include
dirs_to_include = ["conf", "logs", "notebooks", "docs"]

# Create a list of all files in these directories
data_files = []
for dir_to_include in dirs_to_include:
    for dirname, _, filenames in os.walk(dir_to_include):
        for filename in filenames:
            data_files.append(os.path.join(dirname, filename))

setup(
    name="spaceflight310",
    version="1.0",
    packages=find_packages(),
    install_requires=required_packages,
    entry_points={"console_scripts": [entry_point]},
    data_files=[("", data_files)],  # Include the files in the root of the package
)