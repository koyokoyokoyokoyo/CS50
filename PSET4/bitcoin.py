import requests
import json
import sys

def main():
    r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=585a16123645c0339668da9c878c83d82017c73c1bb8d9919538c9b611b5c5f4")
    bitcoin = r.json()
    price = float((bitcoin["data"]["priceUsd"]))

    if len(sys.argv) < 2:
        print("Missing command-line argument")
    else:
        total = price * float(sys.argv[1])
        print(f"${total:,.4f}")
if __name__ == "__main__":
    main()