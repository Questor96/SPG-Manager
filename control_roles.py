from discord import Embed, Role, Forbidden, utils
from discord.ext.commands import Bot, Cog
from discord_slash import cog_ext, SlashContext, manage_commands

def setup(bot: Bot):
    bot.add_cog(ControlRole(bot))

class ControlRole(Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @cog_ext.cog_slash(name="create-role",
                       description="Create a new role with default permissions",
                       options=[manage_commands.create_option(name="name", description="Role Name", option_type=3, required=True)]
                       )
    async def create_role_basic(self, ctx: SlashContext, name):
        role = self._get_role_by_name(ctx, name)
        if role:
            await ctx.send(f"Role {name} already exists")
        else:
            await ctx.guild.create_role(name=name)
            await ctx.send(f"Creating role {name}")
            
    @cog_ext.cog_slash(name="delete-role",
                       description="Delete an existing role",
                       options=[manage_commands.create_option(name="name", description="Role Name", option_type=3, required=True)]
                       )
    async def delete_role_basic(self, ctx: SlashContext, name):
        role = self._get_role_by_name(ctx, name)
        if role:
            try:
                await role.delete()
                await ctx.send(f"Deleted role {name}")
            except Forbidden:
                await ctx.send("Missing Permissions")
        else:
            await ctx.send(f"Role {name} does not exist")
    
    def _get_role_by_name(self, ctx: SlashContext, name: str) -> Role:
        return utils.get(ctx.guild.roles, name=name)
