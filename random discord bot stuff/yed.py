import discord
from time import sleep
from discord.ext import commands, tasks
import asyncio

loop = asyncio.get_event_loop()
BOT_PREFIX = ">"
bot = commands.Bot(command_prefix=BOT_PREFIX, case_insensitive=True)
client_prefix = ">"
client = commands.Bot(command_prefix=client_prefix, case_insensitive=True)
item = "**Selling:**\n32 T1 Snow Minions\n**Want:**\n700k per, negotiable\n\n**DM ME**"
booleable = False


@bot.event
async def on_ready():
    print('------')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    sendmessage.start()
@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('------')


@tasks.loop(seconds=10.0)
async def sendmessage():
    global booleable
    global item
    channel = bot.get_channel(909935791386529825)
    while booleable == True:
        await channel.send(item)
        sleep(10)


@bot.command()
async def send(ctx):
    channel = bot.get_channel(590640127370461227)
    await channel.send(item)
@client.command()
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

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    else:
      if not message.guild:
          print(message.content)
          channel = bot.get_channel(909961787527548949)
          incomingmessage = discord.Embed(
            title = "New Message!", color=0x8cb2e1, description=message.content
          )
          incomingmessage.set_author(name=message.author.name, icon_url=message.author.avatar_url)
          await channel.send(embed=incomingmessage)

loop.create_task(client.start('token'))
bot.run('token', bot=False)

