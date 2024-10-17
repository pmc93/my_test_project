from setuptools import setup, find_packages

setup(
    name="hello-world-project",
    version="0.1.0",
    description="A simple hello world Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Paul McLachlan",
    author_email="paul@example.com",
    url="https://github.com/yourusername/hello-world-project",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "say-hello=hello_world: say_hello",
        ],
    },
)
