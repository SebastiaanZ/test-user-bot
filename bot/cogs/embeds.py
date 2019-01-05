from discord import Colour, Embed
from discord.ext.commands import Bot, Context, group

from bot.constants import DEV_TEST


class Embeds:
    def __init__(self, bot: Bot):
        self.bot = bot

    @group(name='embeds', invoke_without_command=True)
    async def embeds_group(self, ctx: Context):
        await ctx.send(f"No embed type specified!")

    @embeds_group.command(name="rich")
    async def rich_embed(self, ctx: Context):
        embed = Embed()
        embed.colour = Colour.red()

        embed.set_author(
            name="Test User Bot",
        )
        embed.description = "Sending a rich embed!"

        await self.bot.get_channel(DEV_TEST).send(embed=embed)

    @embeds_group.command(name="link")
    async def link_embed(self, ctx: Context):
        url = "https://sebastiaanzeeff.nl"
        await self.bot.get_channel(DEV_TEST).send(url)

    @embeds_group.command(name="gifv")
    async def gifv_embed(self, ctx: Context):
        gifv = "https://giphy.com/gifs/vintage-so-what-miles-davis-26tk1JgKQifXINxkc"
        await self.bot.get_channel(DEV_TEST).send(gifv)


def setup(bot):
    bot.add_cog(Embeds(bot))
