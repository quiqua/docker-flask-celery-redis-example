# -*- coding: utf-8 -*-

from setuptools import setup

install_requires = ["Flask", "click", "simplejson", "PyYAML",
                    "konf", "requests"]

setup(
    name="myapp",
    version="0.1.0",
    packages=["myapp"],
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)