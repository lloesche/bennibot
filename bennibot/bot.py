import logging
import discord
from discord.ext import commands
from bennibot.shift import getshift


log = logging.getLogger(__name__)


class BenniBot(discord.Client):
    async def on_ready(self):
        log.info(f"{self.user.name} has connected to Discord!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!schicht"):
            await message.channel.send(f"{message.author.mention} {getshift()}")
