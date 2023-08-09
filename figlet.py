from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    isRandomFont = True

elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    isRandomFont = False

else:
    sys.exit("Invalid usage")



styles = figlet.getFonts()

if isRandomFont == True:
    figlet.setFont(font = random.choice(styles))


if isRandomFont == False:
    figlet.setFont(font = sys.argv[2])

answer = input("Input: ")

print("Output: \n", figlet.renderText(answer))