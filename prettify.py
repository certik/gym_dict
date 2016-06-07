#! /usr/bin/env python3

import csv

from utils import read_dict, write_dict

filename = "dict.csv"

rows = read_dict(filename)
write_dict(filename, rows)
