import sys

from PIL import Image, ImageOps






if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if (".jpg") not in (sys.argv[1] and sys.argv[2]):
    if ("png") not in (sys.argv[1] and sys.argv[2]):
        sys.exit("Invalid Output")



arg1 = sys.argv[1]
arg2 = sys.argv[2]



if (arg1.endswith(".jpg") != arg2.endswith(".jpg")) or (arg1.endswith(".png") != arg2.endswith(".png")):
    sys.exit("Input and output have different extensions")






if len(sys.argv) == 3:
    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
             sys.exit("File not found")

    shirtfile = Image.open("shirt.png")

    size = shirtfile.size

    muppet = ImageOps.fit(imagefile, size)


    muppet.paste(shirtfile, shirtfile)

    muppet.save(sys.argv[2])

