from tkinter import *
from PIL import ImageTk,Image
import json
import requests
import nbt
import time

window = Tk()

#load name and api key and other
with open("apiKey.txt", "r+") as f:
	apiKey = [i.strip() for i in f.readlines()][0]

with open("name.txt", "r+") as f:
	name = [i.strip() for i in f.readlines()][0]

with open("profilename.txt", "r+") as f:
	pname = [i.strip() for i in f.readlines()][0]

#api on startup (does not need to be updated)
#subsection - get player uuid
getuuid = requests.get('https://api.mojang.com/users/profiles/minecraft/' + name).json
uuid = getuuid()['id']
#subsection - get profile id
sbdata = requests.get(f'https://api.hypixel.net/skyblock/profiles?key={apiKey}&uuid={uuid}').json()
for profile in sbdata['profiles']:
	if profile['cute_name'] == pname.capitalize():
		profileid = profile['profile_id']
#subsection - use correct profile id to get api shit woo
sbdata2 = requests.get(f'https://api.hypixel.net/skyblock/profile?key={apiKey}&profile={profileid}').json()
#subsection - get total gemstone collection
collection = int(sbdata2['profile']['members'][uuid]['collection']['GEMSTONE_COLLECTION'])
collectionstr = "{:,}".format(collection)

#variables that the api gets written to
printname = name + "'s Jade"
printcollection = 'Total Collection: ' + collectionstr
displaycoll = Label(window, text=printcollection, font='Minecraft 11', bg='black', fg='yellow')

#debug
print(name, apiKey, printname, uuid, profileid, collection, collectionstr)

#actual fucking window
img = ImageTk.PhotoImage(Image.open("perfectjade2.png"))
window.iconbitmap('pefect jade.ico')
window.title("Jade Tracker")
window.configure(width=550, height=300)
window.configure(bg='black')
canvas = Canvas(window, width = 550, height = 250,bg='black')
frame = Frame(window)
canvas.pack()
canvas.create_image(20, 20, anchor=NW, image=img)
canvas.create_text(305,30,fill='yellow',font='Minecraft',text=printname)
canvas.create_text(360,60,fill='yellow',font='Minecraft 11',text=printcollection)
displaycoll.pack()
window.update()
window.mainloop()
