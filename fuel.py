# while loop with if statement



while True:
    try:
        value = (input("Fraction: "))

        x, y = value.split('/')

        new_x = int(x)
        new_y = int(y)

        ans = (new_x / new_y)

        if ans <= 1:
            break


    except (ValueError, ZeroDivisionError):
        pass


percent = round(ans * 100)

if percent < 1:
    print("E")

elif percent > 99:
    print("F")

else:
    print(f"{percent}%")




