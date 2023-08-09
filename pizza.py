import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

if len(sys.argv) == 2:
    table = []

    try:
        with open(sys.argv[1], "r") as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                table.append(row)

        print(tabulate(table[1:], headers=table[0], tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File not found")
