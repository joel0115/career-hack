import discord 
import asyncio
from discord import app_commands
from discord.ext import commands

from dotenv import dotenv_values

config = dotenv_values(".env")
BOT_TOKEN = config['BOT_TOKEN']
GUILD_ID = config['GUILD_ID']

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(
    name="sayhello",
    description="Say hello to user",
    guild=discord.Object(id=GUILD_ID)
)
async def sayhello(interaction: discord.Interaction, member:discord.Member):
    await interaction.response.send_message(f"咖啡是一種豆漿...")
    # await interaction.followup.defer(ephemeral=True)
    await asyncio.sleep(5)
    await interaction.edit_original_response(content=f"Hello {member.mention}")

@tree.command(
    name="help",
    description="Show guides for using the bot",
    guild=discord.Object(id=GUILD_ID)
)
async def help(interaction: discord.Interaction):
    with open("./help.md", "r") as f:
        lines = f.read().splitlines()
    
    content = '\n'.join(lines)
    embed=discord.Embed(title="Manpage", description=content,color = 0xF1C40F)
    await interaction.response.send_message(embed=embed)
    

@tree.command(
    name="train",
    description="Train or re-train the model",
    guild=discord.Object(id=GUILD_ID)
)
async def train(interaction: discord.Interaction, file:discord.Attachment):
    await interaction.response.send_message(f'You have uploaded: {file.url}')

    print(file.content_type)
    if(not file.filename.endswith('.pdf') and not file.content_type == 'application/pdf'):
        await interaction.followup.send(f"Please upload .pdf file to update model")

    else:
        await file.save(f'./pdf/{file.filename}')



# sync commands to discord app when the client is ready
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print("Sync commands to discord bot successfully")

client.run(BOT_TOKEN)