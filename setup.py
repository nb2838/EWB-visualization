import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EWB-Visualization"
    version="0.1-dev",
    author="EWB-Ghaana Columbia"
    description="A package for viewing maps"
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nb2838/EWB-visuzlization"
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
