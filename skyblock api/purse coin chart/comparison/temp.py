import requests

data = requests.get(
    url = "https://api.hypixel.net/skyblock",
    params = {
        "key": "eadac583-92c0-4178-85b8-d2e14a4679db",
        "profile": "ef15b7336b104fe9bd0b9bef53f30b2d"
    }
).json

purse_coins = data["profile"]["members"]["df6d7868f55544c28e3aa3148414c232"]["coin_purse"]

print(purse_coins)