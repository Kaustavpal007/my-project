#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import exists
from setuptools import setup, find_packages

author = "Kaustav Pal"
email = "kaustavpal007@gmail.com"
description = "Utility Life Terminal Tool"
name = "utility-life"
year = "2026"
url = "https://github.com/Kaustavpal007/my-project"
version = "0.0.1"

setup(
    name=name,
    author=author,
    author_email=email,
    url=url,
    version=version,
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    description=description,
    long_description=open("README.md").read() if exists("README.md") else "",
    long_description_content_type="text/markdown",
    install_requires=[
        "requests"
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "utility-life=myproject.main:main"
        ]
    },
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
