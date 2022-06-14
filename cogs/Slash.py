import disnake
from disnake.ext import commands
# from interactions import cog_ext, SlashContext

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Test command")
    async def test(ctx):
        embed = disnake.Embed(title="Working")
        await ctx.response.send_message(embeds=[embed])
    
def setup(bot):
    bot.add_cog(Slash(bot))