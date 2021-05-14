from datetime import datetime

import discord
from discord.ext import commands


class userInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Info: Perms müssen gesetzt werden
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        rollen = ''
        for role in member.roles:
            if not role.is_default():
                rollen += '{} \r\n'.format(role.mention)

        embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                              description='Dies ist eine Userinfo für den User {}'.format(member.mention),
                              color=discord.Color.random())
        embed.add_field(name="Id:", value=member.id, inline=True)
        embed.add_field(name='Server beigetreten am', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                        inline=False)
        embed.add_field(name='Discord beigetreten am', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                        inline=False)
        embed.add_field(name='Rollen', value=rollen, inline=False)
        embed.set_footer(text="Requested by: " + datetime.now().strftime("%H:%M  |  %d.%m.%Y"))
        embed.set_thumbnail(url=member.avatar_url)

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(userInfo(bot))
    print("userInfoCog Loaded")
