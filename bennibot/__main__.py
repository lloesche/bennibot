#!/usr/bin/env python
import os
import sys
import logging
import discord
from bennibot.shift import getshift

log_format = "%(asctime)s - %(levelname)s - %(threadName)s - %(message)s"
logging.basicConfig(level=logging.WARN, format=log_format)
logging.getLogger().setLevel(logging.INFO)
log = logging.getLogger(__name__)

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    log.fatal("DISCORD_TOKEN must be set")
    sys.exit(1)

client = discord.Client()


@client.event
async def on_ready():
    log.info(f"{client.user.name} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!schicht"):
        await message.channel.send(getshift())


client.run(TOKEN)
