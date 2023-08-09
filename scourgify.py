import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")


if len(sys.argv) == 3:
    dict = []
    try:
        with open(sys.argv[1]) as file:
            csvreader = csv.DictReader(file)
            for row in csvreader:
                last, first = row["name"].split(',')

                dict.append({'first': first.lstrip(), 'last': last.lstrip(), 'house': row["house"]})



    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames= ["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
        for row in dict:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})





