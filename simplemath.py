# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""SimpleMath to do simple math

Author: Richard Camuccio
Copyright 2019
"""

MAX_ITER = 20
"Docstring appears under global variables"

def add(a, b):
	"Add two numbers"
	c = a + b
	return c

def main():
	"Execute script"
	print(add(2, 2))

if __name__ == "__main__":
	main()