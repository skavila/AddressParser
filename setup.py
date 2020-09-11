import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="address-parser-pkg-saratk", # Replace with your own username
    version="0.0.1",
    author="Sarat Kavila",
    author_email="sarat.kavila@gmail.com",
    description="Normalize the postal address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skavila/AddressParser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)