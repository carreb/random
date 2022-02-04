import requests
import csv
import math
import time
#Hypixel Variables
key = 'c4ee9e0d-42ac-4f3f-a9de-bd8234aff6ba'
profile = 'ef15b7336b104fe9bd0b9bef53f30b2d'
uuid = 'df6d7868f55544c28e3aa3148414c232'
uuid2 = '079e3684dd5940d6bfcece8895b1aa39'
uuid3 = '46d81103d4234099ba5947c6bbec01a0'
#CSV Variables
x = 0
#x = amount of times checked
fieldnames = ["x", "purse1", "purse2", "purse3"]

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

while True:
    with open('data.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        r = requests.get('https://api.hypixel.net/skyblock/profile?key=c4ee9e0d-42ac-4f3f-a9de-bd8234aff6ba').json()
        r2 = requests.get('https://api.hypixel.net/skyblock/profile?key=c4ee9e0d-42ac-4f3f-a9de-bd8234aff6ba').json()
        r3 = requests.get('https://api.hypixel.net/skyblock/profile?key=c4ee9e0d-42ac-4f3f-a9de-bd8234aff6ba').json()
        purse = int(r['profile']['members'][uuid]['coin_purse'])/1000000
        purse2 = int(r2['profile']['members'][uuid2]['coin_purse'])/1000000
        purse3 = int(r3['profile']['members'][uuid3]['coin_purse'])/1000000
        info = {
            "x": x,
            "purse1": purse,
            "purse2": purse2,
            "purse3": purse3
        }

        csv_writer.writerow(info)
        x += 1
        print(x, "|", purse, "|", purse2, "|", purse3)

    time.sleep(30)