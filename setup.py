#!/usr/bin/env python
import os
# from wpc.utils import get_version
from setuptools import setup, find_packages
# import wpc.conf

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="wpc",
    version='2.0.1',
    author="pentestmonkey",
    author_email="pentestmonkey@pentestmonkey.net",
    description="Windows privilege escalation check",
    license="GPL",
    keywords="Windows privilege escalation",
    url="https://github.com/pentestmonkey/windows-privesc-check",
    packages=['wpc', 'wpc.audit', 'wpc.report'],
    include_package_data=True,
    install_requires=['pywin32', 'lxml'],
    entry_points='''
        [console_scripts]
        wpc=wpc.main:main
    ''',
    long_description=read('README.txt'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
