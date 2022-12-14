# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

description = '''A doggo bot to display doggo memes!'''

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def test(ctx):
    """Post random doggo meme"""
    await ctx.send(f'Some random doggo meme!')

@bot.command()
async def doggo(ctx):
    randomgifs = [
        "https://i.imgur.com/wNk88VW.gif",
        "https://i.imgur.com/BKsGPGJ.gif",
        "https://i.imgur.com/NFz9CbI.gif"
    ]
    
    embed = discord.Embed(
        title = "",
        description = "",
        color = ctx.author.color
    )

    randomgif = random.choice(randomgifs)
    embed.set_image(url = randomgif)
    await ctx.send(embed = embed)


load_dotenv()
BOT_TOKEN = os.environ["BOT_TOKEN"]
bot.run(BOT_TOKEN)