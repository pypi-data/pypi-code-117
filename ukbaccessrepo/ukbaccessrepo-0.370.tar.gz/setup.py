import setuptools
import ukbaccessrepo
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ukbaccessrepo",                     # This is the name of the package
    version=ukbaccessrepo.__version__,                        # The initial release version
    author="Tigmanshu Chaudhary",                     # Full name of the author
    description="UKB Access Repo",
    long_description=long_description,      # Long description read from the the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["ukbaccessrepo"],             # Name of the python package
    #package_dir={'':'ukbaccessrepo/src'},     # Directory of the source code of the package
    install_requires=['pandas','datalad','pandas-plink','numpy','dataclasses']                     # Install other dependencies if any
)
