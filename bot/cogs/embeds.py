from discord import Colour, DMChannel, Embed, Message
from discord.ext.commands import Bot, Context, group

from bot.constants import DEV_LOGS, DEV_TEST


class Embeds:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def on_message(self, msg: Message):
        if isinstance(msg.channel, DMChannel):
            formatted = f"{msg.author}: {msg.content}"
            await self.bot.get_channel(DEV_LOGS).send(formatted)

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
    async def link_embed(self, ctx: Context, url: str = None):
        if not url:
            url = "https://sebastiaanzeeff.nl"
        await self.bot.get_channel(DEV_TEST).send(url)

    @embeds_group.command(name="gifv")
    async def gifv_embed(self, ctx: Context):
        gifv = "https://giphy.com/gifs/vintage-so-what-miles-davis-26tk1JgKQifXINxkc"
        await self.bot.get_channel(DEV_TEST).send(gifv)


def setup(bot):
    bot.add_cog(Embeds(bot))
