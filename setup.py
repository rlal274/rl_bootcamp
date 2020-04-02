import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='rl_bootcamp',
    version='0.0.1',
    author='Ravi Lal',
    author_email='rlal@caltech.edu',
    description='Utilities for use in bootcamp.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)