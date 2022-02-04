import discord
from discord.ext import commands
from time import sleep
import os
import pyautogui as pygui
from subprocess import *
import win32gui, win32con
import pywinauto
from playsound import playsound

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

    

client = commands.Bot(command_prefix='/')
bot = discord.Client


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="with Boulders"))
    print('Mainframe powered on! beep boop!')


@client.command()
async def start(ctx):
    await ctx.send("Server starting...")
    jimmyPath = 'C:\Program Files (x86)\Steam\steamapps\common\Terraria\TerrariaServer.exe'
    Popen(jimmyPath, creationflags=CREATE_NEW_CONSOLE)
    sleep(2)
    window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
    sleep(2)
    pygui.typewrite('4\n', interval=1)
    await ctx.send("Selected world")
    sleep(1)
    pygui.typewrite('\n', interval=1)
    await ctx.send("Set player limit to 16")
    sleep(1)
    pygui.typewrite('\n', interval=1)
    await ctx.send("Set port")
    sleep(1)
    pygui.typewrite('\n', interval=1)
    await ctx.send("Forwarded Port")
    sleep(1)
    pygui.typewrite('j\n', interval=1)
    await ctx.send ("Set password to 'j'")
    sleep(1)
    await ctx.send (":thinking: Thinking about Boulder Colorado")
    sleep(3)
    await ctx.send("All inputs complete. Server should be online!\nConnect at boulderserver.ddns.net with port 7777!")
    await client.change_presence(activity=discord.Game(name="Server Online!"))

@client.command()
async def wiki(ctx):
    await ctx.send('https://terraria.gamepedia.com/Terraria_Wiki')


@client.command()
async def forceonlinestatus(ctx):
    await client.change_presence(activity=discord.Game(name="Server Online!"))
    await ctx.send('Forced status to **Online**')

@client.command()
async def forceofflinestatus(ctx):
    await client.change_presence(activity=discord.Game(name="Server Offline!"))
    await ctx.send('Forced status to **Offline**')

@client.command()
async def stop(ctx):
    await ctx.send('The stop function is currently broken. Submitting a request to world host to shut down the world.')
    user = client.get_user(186538091744460800)
    await user.send('Someone has requested to shut down the world!')
    await client.change_presence(activity=discord.Game(name="Stop Requested!"))

@client.command()
async def hungry(ctx):
    await ctx.send('https://images.wikia.com/terraria_gamepedia/images/archive/e/eb/20200614214934%21Emote_Emote_Eating.gif')

client.run('token')
