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
    channel = bot.get_channel(863159580292415529)
    incomingmessage = discord.Embed(
        title=":wave: 1.18 SMP Announcement", color=0x8cb2e1, description="WE ARE PROBABLY STARTING SOON!!!!!! (around 30 minutes)"
    )
    incomingmessage.set_author(
        name=ctx.author.name, icon_url=ctx.author.avatar)
    incomingmessage.set_footer(text="Timestamp is in your local timezone.")
    incomingmessage.add_field(name="How to join", value="Join by clicking 'interested' in the Event below.", inline=False)
    await channel.send("<@&801207950470545438>", embed=incomingmessage)
    await channel.send("https://discord.gg/48yUeKwa?event=915976152034730024")
@bot.command()
async def reply(ctx):
  channel = bot.get_channel(916079106964197446)
  message = await channel.fetch_message(916078944955015169)
  await message.reply("https://discord.com/events/712066956911575042/915976152034730024")

bot.run("token")
