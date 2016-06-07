#! /usr/bin/env python3

import csv

from utils import read_dict, write_md

filename = "dict.csv"

rows = read_dict(filename)
write_md("dict.md", rows)
