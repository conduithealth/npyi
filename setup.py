import io

from setuptools import setup, find_packages

version = "1.0.0"
requirements = ["requests==2.28.1"]

with io.open("README.rst", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name="npyi",
    packages=find_packages(exclude=["test", "test.*"]),
    version=version,
    long_description=readme,
    description="API wrapper around the NPPES API",
    author="Conduit Health",
    author_email="admin@conduithealth.com",
    url="https://github.com/conduithealth/npyi",
    keywords=["npyi", "npi", "nppes"],
    install_requires=requirements,
)
