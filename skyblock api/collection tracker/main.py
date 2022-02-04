from tkinter import *
from PIL import ImageTk, Image
import json
import requests
import nbt
import time

window = Tk()
label = Label(window)

#load name and api key and other
with open("apiKey.txt", "r+") as f:
	apiKey = [i.strip() for i in f.readlines()][0]

with open("name.txt", "r+") as f:
	name = [i.strip() for i in f.readlines()][0]

with open("profilename.txt", "r+") as f:
	pname = [i.strip() for i in f.readlines()][0]

def getcollection():
    #subsection - get player uuid
    getuuid = requests.get(
        'https://api.mojang.com/users/profiles/minecraft/' + name).json
    uuid = getuuid()['id']
    #subsection - get profile id
    sbdata = requests.get(
        f'https://api.hypixel.net/skyblock/profiles?key={apiKey}&uuid={uuid}').json
    for profile in sbdata(['profiles']):
        if profile['cute_name'] == pname.capitalize():
            profileid = profile['profile_id']
    #subsection - use correct profile id to get api shit woo
    sbdata2 = requests.get(
        f'https://api.hypixel.net/skyblock/profile?key={apiKey}&profile={profileid}').json
    #subsection - get total gemstone collection
    collection = int(sbdata2['profile']['members'][uuid]['collection']['SPIDER_EYE'])
    collectionstr2 = "{:,}".format(collection)
    #variables that the api gets written to
    printname = name + "'s Spider Eye"
    printcollection = 'Total Collection: ' + collectionstr
    displaycoll.config(text=printcollection)
    #adds the shit to the window
    label.config(text=collectionstr2)
    window.after(30000, getcollection)

getcollection()

label.pack()
window.mainloop()