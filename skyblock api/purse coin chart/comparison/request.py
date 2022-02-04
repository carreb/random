import requests
import csv
import math
import time
#Hypixel Variables
key = 'eadac583-92c0-4178-85b8-d2e14a4679db'
profile = 'ef15b7336b104fe9bd0b9bef53f30b2d'
uuid = 'df6d7868f55544c28e3aa3148414c232'
#CSV Variables
x = 0
#x = amount of times checked
fieldnames = ["x", "purse"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        r = requests.get('https://api.hypixel.net/skyblock/profile?key=eadac583-92c0-4178-85b8-d2e14a4679db&profile=ef15b7336b104fe9bd0b9bef53f30b2d').json()
        purse = int(r['profile']['members'][uuid]['coin_purse'])
        info = {
            "x": x,
            "purse": purse
        }

        csv_writer.writerow(info)
        x += 1
        print(x, "|", purse)

    time.sleep(30)