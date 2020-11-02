from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='arithmaticpy',
    packages=find_packages(include=['arithmaticpy']),
    version='0.1.3',
    description='Simple Arithmatic Python Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vladyslavnUA/arithmaticpy",
    author='vladyslavn',
    license='MIT',
)