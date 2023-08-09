import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if not sys.argv[1].endswith('.py'):
    sys.exit("Not a python file")



if len(sys.argv) == 2:
    try:
        with open(sys.argv[1]) as file:
            nLines = 0
            for line in file:
                if not line.lstrip().startswith("#") and line.lstrip != ' ':
                    nLines += 1
        print(nLines)

    except FileNotFoundError:
        sys.exit("File does not exist")

