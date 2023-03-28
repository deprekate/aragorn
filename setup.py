#!/usr/bin/env python3
# encoding: utf-8

import os
#from distutils.core import setup, Extension
from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext
from distutils import sysconfig

#os.environ["CC"] = "gcc"
compile_args = ["-O3 -ffast-math -finline-functions"] 
link_args	= []

module = Extension('aragorn',
			language='gcc',
			extra_compile_args=compile_args,
			extra_link_args=link_args,
			include_dirs=[
						 '.',
						 '...',
						 os.path.join(os.getcwd(), 'src')
			],
			library_dirs = [os.getcwd(),],
			sources = ['src/python.cpp'] ) #, 'src/aragorn.c']  )

def readme():
	with open("README.md", "r") as fh:
		long_desc = fh.read()
	return long_desc

def get_version():
	with open("VERSION.md", 'r') as f:
		v = f.readline().strip()
		return v

def main():
	setup (
		name = 'Aragorn',
		version = get_version(),
		author = "Katelyn McNair, Dean Laslett* and Bjorn Canback* (*who did all the real work)",
		author_email = "deprekate@gmail.com",
		description = "A tool to predict tRNAs and tmRNAs",
		long_description = readme(),
		long_description_content_type="text/markdown",
		url =  "https://github.com/deprekate/aragorn",
		scripts=[],
		classifiers=[
			"Programming Language :: Python :: 3",
			"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
			"Operating System :: OS Independent",
		],
		python_requires='>3.5.2',
		packages=find_packages(),
		install_requires=['genbank'],
		ext_modules = [module],
		#cmdclass={"build_ext":custom_build_ext}
		#cmdclass={"build_ext":build_ext}
	)


if __name__ == "__main__":
	main()
