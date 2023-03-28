#!/usr/bin/env python3
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 
import os
import sys
import argparse
from argparse import RawTextHelpFormatter
from subprocess import Popen, PIPE, STDOUT
from types import MethodType
from termcolor import colored
from itertools import tee, chain
import pkgutil
import pkg_resources
from packaging import version

sys.path.pop(0)

from genbank.file import File

def pairwise(iterable):
    # pairwise('ABCDEFG') --> AB BC CD DE EF FG
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def is_valid_file(x):
	if not os.path.exists(x):
		raise argparse.ArgumentTypeError("{0} does not exist".format(x))
	return x

def _print(self, item):
	if isinstance(item, str):
		self.write(item)
	else:
		self.write(str(item))

if __name__ == '__main__':
	usage = '%s [-opt1, [-opt2, ...]] infile' % __file__
	parser = argparse.ArgumentParser(description='', formatter_class=RawTextHelpFormatter, usage=usage)
	parser.add_argument('infile', type=is_valid_file, help='input file')
	parser.add_argument('-o', '--outfile', action="store", default=sys.stdout, type=argparse.FileType('w'), help='where to write output [stdout]')
	parser.add_argument('-p', '--param', type=str)
	parser.add_argument('-f', '--format', help='Output the features in the specified format', type=str, default='feature', choices=['tabular','genbank','structure'])
	args = parser.parse_args()
	args.outfile.print = _print.__get__(args.outfile)
	
	args.outfile.print("This package is not functional yet")
	genbank = File(args.infile)
	for name,locus in genbank.items():
		args.outfile.print(locus.name())

