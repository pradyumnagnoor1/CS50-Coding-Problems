expression = input("Expression: ")



x, y, z = expression.split()

sum = float(x) + float(z)

sub = float(x) - float(z)

div = float(x) / float(z)

mult = float(x) * float(z)




if "+" in y:
    print(round(sum,1))

if "-" in y:
    print(round(sub,1))

if "/" in y:
    print(round(div,1))

if "*" in y:
    print(round(mult,1))
