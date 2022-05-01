import spg_manager
import logging
import os
from dotenv import load_dotenv

# auth token from environment file
load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# enable logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# start bot
bot = spg_manager.SPG_Manager()
bot.run(DISCORD_BOT_TOKEN)