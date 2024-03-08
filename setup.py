from setuptools import setup, find_packages

setup(
    name='encryption_package',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'encryption_package=encryption_package.enctool:main',
        ],
    },
)
