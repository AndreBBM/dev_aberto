from setuptools import setup

setup(name='dev_aberto_andrebbm',
    version='0.1',
    packages=['dev_aberto'],
    author='André Melo',
    python_requires='>=3.6',
    install_requires=['requests'],
    scripts=['scripts/hello.py']
    )