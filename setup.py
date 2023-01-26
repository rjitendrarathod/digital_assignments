from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in digital/__init__.py
from digital import __version__ as version

setup(
	name="digital",
	version=version,
	description="Digital",
	author="Jitendra",
	author_email="rjitendrarathod@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
