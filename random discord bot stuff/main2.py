import discord
from time import sleep
from discord.ext import commands, tasks
import asyncio


BOT_PREFIX = ">"
bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True, self_bot=True)
item = "deeez"
booleable = False


@tasks.loop(seconds=10.0)
async def sendmessage():
    global booleable
    global item
    channel = bot.get_channel(590640127370461227)
    while booleable == True:
        await channel.send(item)

@bot.event
async def on_ready():
    print('------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    sendmessage.start()


@bot.command()
async def send(ctx):
    channel = bot.get_channel(590640127370461227)
    await channel.send(item)
@bot.command()
async def Toggle(ctx):
    global booleable
    if booleable == True:
        booleable = False
        await ctx.send("Toggled off")
    else:
        if booleable == False:
            booleable = True
            await ctx.send("Toggled on")

@bot.command()
async def obtain(ctx):
    await ctx.send(booleable)

bot.run("token")