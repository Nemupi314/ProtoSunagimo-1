import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("Botが起動しました")


@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！")


bot.run(os.environ["TOKEN"])
