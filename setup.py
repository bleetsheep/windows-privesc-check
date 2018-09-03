#!/usr/bin/env python
import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "wpc",
    version = "0.1.0",
    author = "pentestmonkey",
    author_email = "pentestmonkey@pentestmonkey.net",
    description = ("Windows privilege escalation check"),
    license = "GPL",
    keywords = "Windows privilege escalation",
    url = "https://github.com/pentestmonkey/windows-privesc-check",
    packages=['wpc'],
    include_package_data=True,
    install_requires=['pywin32','lxml'],
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
