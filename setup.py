from setuptools import find_packages, setup
import os

entry_point = "spaceflight310 = spaceflight310.main:main"

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

# Include all files in the src, data, and conf directories
package_data = []
for directory in ["src", "data", "conf"]:
    for dirname, _, filenames in os.walk(directory):
        for filename in filenames:
            package_data.append(os.path.join(dirname, filename))

setup(
    name="spaceflight310",
    version="1.0",
    packages=find_packages(),
    install_requires=required_packages,
    entry_points={"console_scripts": [entry_point]},
    package_data={"spaceflight310": package_data},  # Include package data
)