from setuptools import setup

name = 'silpa_common'

setup(
    name=name,
    version="0.1",
    url="",
    license="LGPL 3.0",
    description="Common Library for SILPA modules",
    author='Santhosh Thottingal',
    author_email="santhosh.thottingal@gmail.com",
    long_description="""This module is bundle of common functions used by modules developed for Project SILPA""",
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools'],
    zip_safe=False,
)
