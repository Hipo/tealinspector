from setuptools import find_packages, setup

PACKAGE_NAME = "tealinspector"
VERSION = "0.0.1"
DESCRIPTION = "A teal inspector."
KEYWORDS = "teal algorand blockchain"
LICENSE = "MIT"
URL = "https://github.com/Hipo/tealinspector"
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    keywords=KEYWORDS,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    package_data={"tealinspector": ["*.tx", "*.json"]},
    install_requires=["py-algorand-sdk >= 1.20"],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        "console_scripts": [
            "tealinspector = tealinspector.cli:run",
        ],
    },
)