from setuptools import setup, find_packages

name = 'silpa_common'

setup(
    name=name,
    version="0.1.1",
    url="",
    license="LGPL 3.0",
    description="Common Library for SILPA modules",
    author='Santhosh Thottingal',
    author_email="santhosh.thottingal@gmail.com",
    long_description="""This module is bundle of common functions used by modules developed for Project SILPA.
Currently it includes charmap and langdetect functions.""",
    include_package_data=True,
    packages=find_packages(),
    setup_requires=['setuptools-git'],
    install_requires=['setuptools'],
    zip_safe=False,
)
