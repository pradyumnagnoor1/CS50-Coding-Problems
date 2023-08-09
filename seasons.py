from datetime import date
import sys
import inflect

p = inflect.engine()


def main():
    birth_date = input("Date of Birth: ")

    try:
        year, month, day = birth_date.split("-")

    except ValueError:
        sys.exit("Invalid date")

    minutes_lived(year, month, day)







def minutes_lived(year, month, day):

    try:
        dt = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid Date"

    today = date.today()

    sub = today - dt

    minutes = int(sub.total_seconds() / 60)

    msg = p.number_to_words(minutes)

    print(f"{msg} minutes")







if __name__ == "__main__":
    main()