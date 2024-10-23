import setuptools
from distutils.core import setup
from io import open

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

setup(name='nkhandic', 
      version='0.1.0',
      author="Yoshinoir Sugai",
      author_email="okikirmui+github@gmail.com",
      description="NK-HanDic package for installation via pip.",
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/okikirmui/nkhandic-py",
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: Korean",
      ],
      package_data={'nkhandic': ['dicdir/*']}
      )
