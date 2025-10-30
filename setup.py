from setuptools import setup, find_packages

setup(
    name="pyvertools",
    version="0.1.0",
    packages=find_packages(),
    scripts=["scripts/is23", "scripts/f23"],
    install_requires=[],
    author="Your Name",
    description="Tools to detect Python version and convert Python 2 to 3",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)