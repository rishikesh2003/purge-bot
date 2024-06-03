import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()  # take environment variables from .env.

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def purge(ctx, channel: discord.TextChannel):
    messages = [message async for message in channel.history()]
    for message in messages:
        await message.delete()
        await asyncio.sleep(0.5)
    print("Purging done.")# sleep for 1 second to avoid rate limits


bot.run(os.getenv('DISCORD_BOT_TOKEN'))
