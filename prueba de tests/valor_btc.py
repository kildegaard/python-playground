import requests
from datetime import date


def get_btc_value():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice/BTC.json")
    data = response.json()
    btc_value = data["bpi"]["USD"]["rate"]
    return btc_value


def main():
    btc_value = get_btc_value()
    today = date.today()
    print(f"The current BTC value is {btc_value} USD on {today}")


if __name__ == "__main__":
    main()
