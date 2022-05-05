import discord
from discord.ext import commands
from discord_slash import SlashCommand

class SPG_Manager(commands.Bot):        
    """A discord bot that can create and manage user roles"""

    def __init__(self, command_prefix=commands.when_mentioned, help_command=commands.DefaultHelpCommand(), description=None, **options):
        """Instantiates bot and adds all relevant slash commands"""
        super().__init__(command_prefix, help_command, description, **options)    
        
        # instantiate relevant discord_slash tools
        slash = SlashCommand(self, sync_commands=True)
        
        # load cogs
        self.load_extension(name="control_roles")

    async def on_ready(self):
        """old demo logging code"""
        print('Logged on as {0}!'.format(self.user))
    
    async def on_message(self, message):
        """old demo logging code"""
        print(' Message from {0.author}: {0.content}'.format(message))
