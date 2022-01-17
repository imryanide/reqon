from os import name
import disnake 
from disnake import user
from disnake import channel
from disnake import client
from disnake.ext.commands import bot
from disnake.utils import get
from disnake.ext import commands, tasks

class general(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    
    @commands.Cog.listener()
    async def on_ready(self):
        print("General plugged in.")
        


    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        em=get_main_help_embed(description="Use `^help` Command for information.", picture=self.bot.user.avatar)

        em.add_field(name="Moderation", value = f"``` kick \n ban \n strike \n mute \n unmute \n trackuser \n dump```")
        em.set_footer(text="reqon | V0.01 | artixian#7260")
    

        await ctx.send(embed=em)

    @help.command()
    async def kick(self, ctx):

        em = get_help_embed(title="Kick", description= "Kicks a member from the server.",picture=self.bot.user.avatar)
        em.add_field(name="**Syntax**", value=f"`^kick <member> [reason]`")
        await ctx.send(embed=em)

    @help.command()
    async def ban(self, ctx):

        em = get_help_embed(title="Ban", description= "Bans a member from the server.",picture=self.bot.user.avatar)
        em.add_field(name="**Syntax**", value=f"`^ban <member> [reason]`")
        await ctx.send(embed=em)

    @help.command()
    async def strike(self, ctx):

        em = get_help_embed(title="Strike", description= "Adds a strike to a user.",picture=self.bot.user.avatar)
        em.add_field(name="**Syntax**", value=f"`^strike <member> [reason]` \n Using `!xp take <member>` will also add a strike to the user.")
        await ctx.send(embed=em)

    @help.command()
    async def mute(self,ctx):
        em = get_help_embed(title="Mute", description= "Mutes and adds a strike to a user.",picture=self.bot.user.avatar)
        em.add_field(name="**Syntax**", value=f"`^mute <member> <time> [reason]` \n.")
        await ctx.send(embed=em)


    


    

def setup(bot):
    bot.add_cog(general(bot))


def get_main_help_embed(description, picture):
    title = "Help Menu | Primordiax"
    symbol = "https://i.imgur.com/MSg2a9d.png"
    embed = disnake.Embed(description=description, color=7505388)
    embed.set_thumbnail(url=picture)
    embed.set_author(name=title, icon_url=symbol)
    embed.set_footer(text=f"Helpdesk for Primordiax.")
    return embed


def get_help_embed(title, description, picture):
    title = "Help Menu | Primordiax"
    symbol = "https://i.imgur.com/MSg2a9d.png"
    embed = disnake.Embed(description=description, color=7505388)
    embed.set_thumbnail(url=picture)
    embed.set_author(name=title, icon_url=symbol)
    embed.set_footer(text=f"Helpdesk for Primordiax.")
    return embed

# Permission check
def check_permissions(roles):
    for scan in roles:
        if scan.name == "Tester":
            return True
    return False