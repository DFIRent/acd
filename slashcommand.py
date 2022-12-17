import disnake
from disnake.ext import commands

bot = commands.Bot()

@bot.event
async def on_ready():
    print("The bot is ready!")

@bot.slash_command(description="ABC")
async def hello(inter):
    await inter.response.send_message("DEF")

bot.run("TOKENGOESHERE")