from setuptools import setup, find_packages

setup(
    name="auto_requirements",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pip"],
    entry_points={
        "console_scripts": [
            "auto-req=auto_requirements.tracker:write_requirements"
        ]
    },
    author="Your Name",
    description="Automatically generate requirements.txt for your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/auto_requirements",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
