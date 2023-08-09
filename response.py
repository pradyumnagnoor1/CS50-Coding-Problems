from validator_collection import validators, checkers, errors


def main():
    response = input("What's your email address? ")

    try:
        validEmail = validators.email(response)

        print("Valid")


    except:
        print("Invalid")










if __name__ == "__main__":
    main()

