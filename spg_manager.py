import discord
from discord.ext import commands

class SPG_Manager(commands.Bot):        
    def __init__(self, command_prefix=commands.when_mentioned, help_command=commands.DefaultHelpCommand(), description=None, **options):
        super().__init__(command_prefix, help_command, description, **options)
        
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        print(' Message from {0.author}: {0.content}'.format(message))