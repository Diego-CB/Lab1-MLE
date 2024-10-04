from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    url= 'https://github.com/Diego-CB/Lab1-MLE',
    install_requires = [
        'pandas',
        'scikit-learn',
        'joblib',
        'fastapi',
        'pydantic',
    ]
)