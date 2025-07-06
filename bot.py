import discord
from discord.ext import commands
from discord import app_commands
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()


TOKEN = os.getenv('BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!' , intents=intents)

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
    'options': '-f s16le -ar 48000 -ac 2'
}

GUILD_ID = int(os.getenv('GUILD_ID'))
GUILD_ID_OBJ = discord.Object(id=GUILD_ID)

@bot.event
async def on_ready():
    print("Bot is ready")
    # bot.tree.clear_commands(guild=GUILD_ID_OBJ)
    
    try:
        
        synced = await bot.tree.sync(guild=GUILD_ID_OBJ)
        print(f"synced {len(synced)} commands.")
        
    except Exception as e:
        
        print(f"failed to sync commands.{e}")

@bot.tree.command(name="join",description="joins a voice channel and starts streaming audio from given m3u8 link", guild=GUILD_ID_OBJ)
@app_commands.describe(m3u8_url = "specify the m3u8 url to stream audio from")
async def join(interaction: discord.Interaction, m3u8_url: str):
    
    if interaction.user.voice:
        
        channel = interaction.user.voice.channel
        vc = await channel.connect()
        audio_src = discord.FFmpegPCMAudio(m3u8_url, **FFMPEG_OPTIONS)
        vc.play(audio_src)
        await interaction.response.send_message(f"Joined #{channel.id}")
        
    else:
        
        await interaction.response.send_message("Join a VC first")

@bot.tree.command(name="leave",description="leaves the joined channel", guild=GUILD_ID_OBJ)
async def leave(interaction: discord.Interaction):
    
    if interaction.guild.voice_client:
        
        await interaction.guild.voice_client.disconnect()
        await interaction.response.send_message("left the channel.")
        
    else:
        await interaction.response.send_message("Not in any channel")


bot.run(TOKEN)
