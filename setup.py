from setuptools import setup, find_packages

setup(
    name="pip_test",
    version="0.1",
    py_modules=["test_library", 'mfclient'], 
    package_dir={"": "src"},
)
