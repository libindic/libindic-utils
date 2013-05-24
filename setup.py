from setuptools import setup

name = 'common'

setup(
    name=name,
    version="0.1",
    url="",
    license="LGPL 3.0",
    description="Common Library for SILPA modules",
    author='Santhosh Thottingal',
    author_email="santhosh.thottingal@gmail.com",
    long_description="""This library helps other modules in
their functioning.""",
    include_package_data=True,
    setup_requires=['setuptools-git'],
    install_requires=['setuptools'],
    zip_safe=False,
)
