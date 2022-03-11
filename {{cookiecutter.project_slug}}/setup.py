#!/usr/bin/env python3

"""The setup script."""

from setuptools import setup, find_packages
import sys
import os

sys.path.append(os.path.dirname(__file__))
import dependencies
import versioneer

tests_require = dependencies.ci_requires
install_requires = dependencies.install_requires
setup_requires = dependencies.setup_requires()
install_suggests = dependencies.install_suggests

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="{{cookiecutter.short_description}}",
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_slug}}={{cookiecutter.project_slug}}.cli:main",
        ],
    },
    tests_require=tests_require,
    install_requires=install_requires,
    extras_require=dependencies.extras(),
    license="BSD license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="{{cookiecutter.project_slug}}",
    name="{{cookiecutter.project_slug}}",
    packages=find_packages(include=["{{cookiecutter.project_slug}}", "{{cookiecutter.project_slug}}.*"]),
    url="https://github.com/WWU-AMM/{{cookiecutter.project_slug}}",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
