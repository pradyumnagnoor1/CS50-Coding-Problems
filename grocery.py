grocery_list = {
}

while True:
    try:

        item = input()


        grocery_list[item] = grocery_list.get(item, 0) + 1




    except (EOFError, KeyError):
        print()
        break

for string, count in grocery_list.items():

    print(f"{count} {string.upper()}")

