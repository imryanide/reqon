
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
import os


#set bot token
load_dotenv('.env')
TOKEN = os.getenv('TOKEN')

description = """An recon bot."""

intents = disnake.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="^", description=description, intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    game = disnake.Game("with nzu balls")
    await bot.change_presence(activity=game)

    print(f"Connected to client {bot.user}") 


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


if __name__ == "__main__":
    bot.remove_command("help")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
    bot.run(TOKEN)