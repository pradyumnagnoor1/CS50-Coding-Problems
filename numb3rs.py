import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^([0-9])+\.([0-9])+\.([0-9])+\.([0-9])+$", ip):
        listOfNums = ip.split('.')

        for i in listOfNums:
            if int(i) > 255 or int(i) < 0:
               return False
        return True

    else:
        return False














if __name__ == "__main__":
    main()