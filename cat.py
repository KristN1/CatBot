import discord
import time
import requests
from discord.ext import commands
from datetime import datetime

prefix = (".")
client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

def sendCat(message):
    response = requests.get('https://aws.random.cat/meow')
    data = response.json()
    embed = discord.Embed(
        title = 'Cat 🐈',
        description = ':pleading_face:',
        colour = discord.Colour.purple()
        )
    embed.set_image(url=data['file'])            
    embed.set_footer(text="")
    return embed

@client.event 
async def on_ready():
    activity = discord.Game(name="say CAT", type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)

    print("Bot is ready")

@client.event
async def on_message(message):
    if message.content == "cat":
        embed = sendCat(message)
        await message.channel.send(embed=embed)

client.run("YOUR TOKEN")
