import discord
from discord import app_commands
import os

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print("スラッシュコマンド同期完了")

@tree.command(name="hello", description="挨拶するよ！")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello!!! 😎")

client.run(TOKEN)
