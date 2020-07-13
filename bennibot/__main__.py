#!/usr/bin/env python
import os
import sys
import logging
from bennibot.bot import BenniBot


log_format = "%(asctime)s - %(levelname)s - %(threadName)s - %(message)s"
logging.basicConfig(level=logging.WARN, format=log_format)
logging.getLogger('bennibot').setLevel(logging.DEBUG)
log = logging.getLogger(__name__)

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    log.fatal("DISCORD_TOKEN must be set")
    sys.exit(1)


def main() -> None:
    bot = BenniBot()
    bot.run(TOKEN)


if __name__ == '__main__':
    main()
