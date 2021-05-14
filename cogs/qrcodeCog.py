import discord
import pyqrcode
from discord.ext import commands


class qrCodeCog(commands.Cog, name="qrCodeCog"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def qr(self, ctx, url):
        url1 = pyqrcode.create(url, error='H')
        url1.png("qrcode.png", module_color=(0, 255, 0, 255), background=(0, 0, 0, 255), scale=5)
        await ctx.send(file=discord.File('qrcode.png'))


def setup(bot):
    bot.add_cog(qrCodeCog(bot))
    print('QR-Code Cog loaded')
