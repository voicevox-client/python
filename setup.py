from setuptools import setup
import re


def get_version():
    with open("voicevox/__init__.py", "r") as f:
        return re.search(r'__version__ = "([^"]+)"', f.read()).group(1)


with open("README.md", "r",  encoding='utf-8') as f:
    long_description = f.read()


with open("requirements.txt", "r") as f:
    requirements = f.readlines()


setup(
    name="voicevox-client",
    description="Voicevox engine unoffical wrapper",
    url="https://github.com/voicevox-client/python",
    project_urls={
        "Documentation": "https://voicevox-client.tuna2134.jp",
        "Source": "https://github.com/tuna2134/voicevox-client",
    },
    version=get_version(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="tuna2134",
    license="MIT",
    packages=["voicevox", "voicevox.types"],
    package_data={
        "voicevox": ["py.typed"]
    },
    install_requires=requirements,
    extras_require={
        "tests": [
            "pytest",
            "pytest-asyncio"
        ],
        "docs": [
            "pdoc3"
        ]
    }
)
