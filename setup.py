# -*- coding: utf-8 -*-
"""
Flask ReactJS Bootstrap setup file.
"""
import setuptools
import versioneer


setuptools.setup(name="sample_app",
                 version=versioneer.get_version(),
                 packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
                 #test_suite="tests",
                 scripts=["bin/sample_app"],
                 package_data={"sample_app": ["static/*", "templates/*"]},
                 install_requires=["flask>=0.10"],
                 zip_safe=False,
                 cmdclass=versioneer.get_cmdclass())
