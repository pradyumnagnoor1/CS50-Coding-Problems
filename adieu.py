import inflect


p = inflect.engine()

user_inputs = []

while True:
    try:
        name = input("Name: ")

        user_inputs.append(name)

        myList = p.join(user_inputs)



    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {myList}")





