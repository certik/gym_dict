import csv

def read_dict(filename):
    rows = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) != 3:
                print(row)
                raise Exception("Incorrect number of columns.")
            rows.append([x.strip() for x in row])
    return rows

def write_dict(filename, rows):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        for row in rows:
            writer.writerow(row)

def write_md(filename, rows):
    with open(filename, 'w', newline='') as mdfile:
        for n,row in enumerate(rows):
            if n == 1:
                mdfile.write("| --- | --- | --- |\n")
            mdfile.write("| %s | %s | %s |\n" % tuple(row))
