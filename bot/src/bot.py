import discord
from discord import app_commands
from dotenv import dotenv_values

config = dotenv_values(".env")
BOT_TOKEN = config['BOT_TOKEN']
GUILD_ID = config['GUILD_ID']

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
    name="repeat",
    description="Repeat message",
    guild=discord.Object(id=GUILD_ID)
)
async def repeat(interaction: discord.Interaction, message: str = None):
    await interaction.response.send_message(f"Repeat: {message}")

@tree.command(
    name="sayhello",
    description="Say hello to user",
    guild=discord.Object(id=GUILD_ID)
)
async def sayhello(interaction: discord.Interaction, member:discord.Member, message: str = None):
    await interaction.response.send_message(f"Hello {member.mention}")


# sync commands to discord app when the client is ready
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print("Sync commands to discord bot successfully")

client.run(BOT_TOKEN)