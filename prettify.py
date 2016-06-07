#! /usr/bin/env python3

import csv

filename = "dict.csv"

rows = []

with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        rows.append([x.strip() for x in row])

with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, lineterminator='\n')
    for row in rows:
        writer.writerow(row)
