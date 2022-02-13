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


@bot.command()
async def sendembed(ctx):
          channel = bot.get_channel(820824879011856425)
          incomingmessage = discord.Embed(
            title = ":wave:", color=0x8cb2e1, description="test"
          )
          incomingmessage.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
          await channel.send(embed=incomingmessage)


bot.run("token")
