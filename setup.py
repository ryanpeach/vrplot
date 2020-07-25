import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vrplot",
    version="0.0.1",
    author="Ryan Peach",
    author_email="ryan.peach@outlook.com",
    description="A 3D+ plotting tool for easy data visualization in VR.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ryanpeach/vrplot",
    packages=setuptools.find_packages(),
    data_files=[('templates', [])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)