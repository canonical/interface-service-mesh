import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="interface-service-mesh",
    version="0.0.1",
    author="Dominik Fleischmann",
    author_email="dominik.fleischmann@canonical.com",
    description="Service Mesh Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["interface_service_mesh"],
    install_requires=[
        "serialized-data-interface",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
