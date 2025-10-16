from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Ecom-Chat",
    version="1.0",
    author="ManikS10",
    packages=find_packages(),
    install_requires = requirements,
)