from time import sleep
import discord
import requests
import json
from discord_webhooks import DiscordWebhooks
from discord.ext import commands

client = commands.Bot(command_prefix='>')
bot = discord.Client
client.remove_command('help')

# pip install anything u need lo
@client.command()
async def bot(ctx, user, arg=None):
    while True:
        await ctx.send("{} offline".format(user))#we must do this down here in my new if statemtn
        uuidreq = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'.format(user)) #try run it!
        uuidresp = uuidreq.json()
        uuid = uuidresp["id"]

        print(uuidresp)

        statusUrl = ('https://api.hypixel.net/status?uuid={}&key=3a3829ed-405d-4cfa-a13d-ddc6e4721cc4'.format(uuid))

        statusReq = requests.get(statusUrl)
        statusResp = statusReq.json()
        statusCurrent = statusResp["session"]["online"]

        if statusCurrent == True: # ah yes thank you man! one sec let me add ekse 
            await ctx.send('<@!318772220166012929> {} online'.format(user))
        else:
            print('user offline')
        

        if arg == 'stop':
            print('stopped checking')
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="nothing :("))
            break

        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="{}".format(user)))
        sleep(120)


client.run('token') # ok i s it ready