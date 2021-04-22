from setuptools import setup


setup(
    name="scripture-burrito",
    version="0.0.2",
    description="Python library for the Scripture Burrito data interchange format",
    url="http://github.com/bible-technology/scripture-burrito-python",
    author="BT Tech Consortium",
    author_email="jtauber@jtauber.com",
    license="MIT",
    packages=["scripture_burrito"],
    package_data={
        "scripture_burrito": ["schema"]
    },
    install_requires=["jsonschema"],
    entry_points={
        "console_scripts": [
            "validate-sb = scripture_burrito.validate:main",
        ],
    },
)
