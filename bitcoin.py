import requests
import sys
import json








try:

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")
    try:
        argv = float(sys.argv[1])

    except (ValueError, SyntaxError):
        sys.exit("Command line argument is not a number")




    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    data = response.json()

    rate = data['bpi']['USD']['rate_float']


    total_amount = (rate * argv)

    print(f"${total_amount:,.4f}")




except requests.RequestException:
    pass