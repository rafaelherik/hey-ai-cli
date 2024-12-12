from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="hey-ai-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool for interacting with various AI assistants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelherik/hey-ai-cli",
    project_urls={
        "Bug Tracker": "https://github.com/rafaelherik/hey-ai-cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        'requests>=2.25.1',
        'python-dotenv>=0.19.0',
        'click>=8.0.0',
        'pyyaml>=5.4.1',
    ],
    entry_points={
        'console_scripts': [
            'hey=hey_ai.cli:main',
        ],
    },
    include_package_data=True,
    package_data={
        "hey_eai": ["config/*.yaml"],
    },
)