from setuptools import setup
import re


def get_version():
    with open("voicevox/__init__.py", "r") as f:
        return re.search(r'__version__ = "([^"]+)"', f.read()).group(1)


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="voicevox",
    description="Voicevox engine unoffical wrapper",
    version=get_version(),
    long_description=long_description,
    author="tuna2134"
)