from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()



setup(
    name="bmicalculator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['numpy','pandas','wheel','pyyaml'],
    author="Sairam Reddy Maddireddy",
    description='Python package for calculating BMI',
	python_requires=">=3.6",
)

