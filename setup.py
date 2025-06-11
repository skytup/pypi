from setuptools import setup, find_packages

setup(
    name="skytup",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Skytup",
    author_email="skytup91@gmail.com",
    description="A sample Python package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/skytup/pypi.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)