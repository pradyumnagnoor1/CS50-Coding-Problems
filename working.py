import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.search(r"^(\d{1,2})(?::)?(\d{2})?\s+(AM|PM) to (\d{1,2})(?::)?(\d{2})?\s(AM|PM)$", s, re.IGNORECASE)

    if match:
        hour1 = int(match.group(1))
        minute1 = match.group(2)
        am_pm1 = match.group(3).upper()
        hour2 = int(match.group(4))
        minute2 = match.group(5)
        am_pm2 = match.group(6).upper()

        if hour1 > 12 or hour2 > 12:
            raise ValueError


        if minute1 is None:
            minute1 = '00'
        if minute2 is None:
            minute2 = '00'

        if (minute1 or minute2) == '60':
            raise ValueError





        if am_pm1 == 'AM':
            if hour1 == 12:
                hour1 = 0
        elif am_pm1 == 'PM':
            if hour1 != 12:
                hour1 += 12


        if am_pm2 == 'AM':
            if hour2 == 12:
                hour2 = o
        elif am_pm2 == 'PM':
            if hour2 != 12:
                hour2 += 12

        else:
            raise ValueError

        return f"{hour1:02d}:{minute1} to {hour2:02d}:{minute2}"

    else:
        raise ValueError




















if __name__ == "__main__":
    main()