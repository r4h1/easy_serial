from setuptools import setup, find_packages

setup(
    name="easy_serial",
    version="0.1.0",
    author="Robson C. Augusto",
    author_email="r4electrics@gmail.com",
    description="A simple package for serial communication with Arduino & ESP32.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/r4h1/easy_serial",  # Change to your GitHub repo
    packages=find_packages(),
    install_requires=[
        "pyserial",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)