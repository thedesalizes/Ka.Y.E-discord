import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# load credentials
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')


# instantiate a bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print('Ready.')

@bot.event
async def on_message(message):
    if type(message.channel) == discord.channel.DMChannel:
        if message.content == "ping":
            await message.reply("pong")

bot.run(BOT_TOKEN)