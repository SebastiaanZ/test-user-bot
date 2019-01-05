from discord.ext.commands import Bot, Context, group


class Cogs:
    """Cog management cog to load, unload, reload the testing cogs"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @group(name='cogs', invoke_without_command=True)
    async def cogs_group(self, ctx: Context):
        await ctx.send(f"No cog action specified!")

    @cogs_group.command(name='load')
    async def load_command(self, ctx: Context, cog: str = ""):
        cog = cog.lower()

        if cog:
            full_cog = f"bot.cogs.{cog}"

            if full_cog not in self.bot.extensions:
                try:
                    self.bot.load_extension(full_cog)
                except ImportError:
                    await ctx.send(f"ImportError while loading {cog}")
                except Exception as e:
                    await ctx.send(f"{e} while loading {cog}")
                else:
                    await ctx.send(f"Loaded {cog}!")
            else:
                await ctx.send(f"The cog {cog} was already loaded... Try reloading it!")
        else:
            await ctx.send(f"You didn't specify a cog to load!")

    @cogs_group.command(name='unload')
    async def unload_command(self, ctx: Context, cog: str = ""):
        cog = cog.lower()

        if cog:
            full_cog = f"bot.cogs.{cog}"

            if full_cog == "bot.cogs.cogs":
                await ctx.send(f"Can't unload the cogs cog!")
            elif full_cog in self.bot.extensions:
                try:
                    self.bot.unload_extension(full_cog)
                except Exception as e:
                    await ctx.send(f"{e} while unloading {cog}!")
                else:
                    await ctx.send(f"Unloaded {cog}!")
            else:
                await ctx.send(f"Can't unloaded {cog}, as it wasn't loaded!")
        else:
            await ctx.send(f"You didn't specify a cog to unload!")

    @cogs_group.command(name='reload')
    async def reload_command(self, ctx: Context, cog: str = ""):
        cog = cog.lower()

        if cog:
            full_cog = f"bot.cogs.{cog}"

            if full_cog == "bot.cogs.cogs":
                await ctx.send(f"Can't reload the cogs cog!")
            elif full_cog in self.bot.extensions:
                try:
                    self.bot.unload_extension(full_cog)
                    self.bot.load_extension(full_cog)
                except Exception as e:
                    await ctx.send(f"{e} while reloading {cog}!")
                else:
                    await ctx.send(f"Reloaded {cog}!")
            else:
                await ctx.send(f"Can't reloaded {cog}, as it wasn't loaded!")
        else:
            await ctx.send(f"You didn't specify a cog to reload!")


def setup(bot):
    bot.add_cog(Cogs(bot))
