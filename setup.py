from setuptools import setup, find_packages

setup(
    name="dataset_checker",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "matplotlib>=3.1.0",
        "seaborn>=0.10.0",
        "scikit-learn>=0.22.0",
        "scipy>=1.4.0",
        "jinja2>=2.11.0",
    ],
    author="Dataset Checker Team",
    author_email="example@example.com",
    description="A comprehensive library for checking and improving dataset quality",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/JonusNattapong/Dataset-checker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
