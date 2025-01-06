# Copyright 2020 Lukas Lösche <lloesche@fedoraproject.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import logging
import discord
from datetime import datetime
from bennibot.shift import getshift


log = logging.getLogger(__name__)


class BenniBot(discord.Client):
    def __init__(self, *args, week_offset=None, **kwargs):
        if week_offset is None:
            week_offset = datetime.now().year % 3
        else:
            week_offset = int(week_offset)
        self.week_offset = week_offset
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(*args, intents=intents, **kwargs)

    async def on_ready(self):
        log.info(f"{self.user.name} has connected to Discord!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!schicht"):
            await message.channel.send(
                f"{message.author.mention} {getshift(self.week_offset)}"
            )
