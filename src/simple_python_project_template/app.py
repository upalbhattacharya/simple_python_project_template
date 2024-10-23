#!/usr/bin/env python

import argparse
import os

import polars

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--a_arg", type=str)
parser.add_argument("-b", "--b_arg", type=str)

args = parser.parse_args()
print(args)
print(polars)

ls = [
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
    "hello",
]
