import discord
from discord import app_commands
import os
import threading
from flask import Flask

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

# ---- ここからRender用ダミーWebサーバー ----
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

threading.Thread(target=run_web).start()
# --------------------------------------------

client.run(TOKEN)
