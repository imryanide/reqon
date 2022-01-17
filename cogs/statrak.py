from os import name
import disnake 
from disnake import user
from disnake import channel
from disnake import client
from disnake.ext.commands import bot
from disnake.utils import get
from disnake.ext import commands, tasks

class statrak(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Statrak plugged in.")
        


    @commands.group(invoke_without_command=True)
    async def stat(self,ctx):
        await ctx.send("Placeholder for stats")


    

def setup(bot):
    bot.add_cog(statrak(bot))

