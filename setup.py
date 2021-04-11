import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="API REST OllivandersShop",
    version="1.0.0",
    author="Charlos16v, JuampaMolina",
    author_email="cdominguez@cifpfbmoll.eu, jruiz@cifpfbmoll.eu",
    description="API REST Flask with MongoDB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JuampaMolina/ollivanders_shop.git",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "click==7.1.2",
        "dnspython==2.1.0",
        "Flask==1.1.2",
        "Flask-Cors==3.0.10",
        "Flask-PyMongo==2.3.0",
        "Flask-RESTful==0.3.8",
        "Jinja2==2.11.3",
        "MarkupSafe==1.1.1",
        "mongoengine==0.23.0",
        "mongomock==3.22.1",
        "pymongo==3.11.3",
        "pytest==6.2.2",
        "Werkzeug==1.0.1"
    ],
)
