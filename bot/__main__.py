from os import getenv

from discord.ext.commands import Bot


BOT_TOKEN = getenv("BOT_TOKEN")

bot = Bot(
    command_prefix="@",
    case_insensitive=True,
    max_messages=10_000
)

bot.load_extension("bot.cogs.cogs")

bot.run(BOT_TOKEN)
