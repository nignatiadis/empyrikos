from setuptools import setup, find_packages

setup(
    name="empyrikos",
    version="0.1.0",
    author="Nikos Ignatiadis",
    author_email="nikos.ignatiadis@gmail.com",
    description="Python interface to Empirikos.jl for empirical Bayes methods",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nignatiadis/empyrikos",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "juliacall>=0.9.14",
        "numpy>=1.20.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
    ],
    julia_requires=">=1.10",
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
            "mypy",
        ],
        "docs": [
            "quartodoc>=0.6.0",
            "jupyter",
        ],
    },
)