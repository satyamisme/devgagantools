# Github/devgagan

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="SpyLib",
    version="2.0.1",
    description="This repository aimed to be fast uploading and fast downloading via Telethon (user and bots both supported)",
    packages=find_packages(),
    install_requires=["telethon", "telethon-tgcrypto"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devgaganin/spylib",
    author="devgagan",
    author_email="business@devgagan.in"
)
