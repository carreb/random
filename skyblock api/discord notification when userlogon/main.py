from time import sleep
import discord
import requests
import json
from discord_webhooks import DiscordWebhooks
from discord.ext import commands
import pickle

client = commands.Bot(command_prefix='>')
bot = discord.Client
client.remove_command('help')



# pip install anything u need lo
@client.command()
async def bot(ctx, arg=None):
    with open("test.txt", "r") as f:   
        lines = f.read().split('\n')
    length = len(lines)
    i = 0
    while True:
        print(lines[i])
        uuidreq = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'.format(lines[i])) #try run it!
        uuidresp = uuidreq.json()
        uuid = uuidresp["id"]

        statusUrl = ('https://api.hypixel.net/status?uuid={}&key=3a3829ed-405d-4cfa-a13d-ddc6e4721cc4'.format(uuid))

        statusReq = requests.get(statusUrl)
        statusResp = statusReq.json()
        statusCurrent = statusResp["session"]["online"]

        if statusCurrent == True: # ah yes thank you man! one sec let me add ekse 
            await ctx.send('<@!318772220166012929> {} online'.format(user))
        else:
            print('user offline')

        i += 1
        if i==length:
            i=0
        sleep(48)
@client.command()
async def math(ctx, user):

    with open("test.txt", "r") as f:   
        lines = f.read().split('\n')
        lines.append(user)
    with open("test.txt", "w") as f:
        f.write('\n'.join(lines))



    

        


client.run('token') # ok i s it ready