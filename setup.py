import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kidney-disease-mlflow-dvc",
    version="0.0.1",
    author="Ravi Surapati",
    author_email="ravisurapati12@gmail.com",
    description="A simple MLFlow and DVC template for kidney disease prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/ravisurapati12/Kidney-disease-MLFlow-DVC.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)