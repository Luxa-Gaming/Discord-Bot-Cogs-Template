from discord.ext import commands


# Info: Cogs sind in Klassen aufgebaut:
#  (wenn du das nicht kennst, such mal auf YouTube nach Python von Morpheus)


class maintainCog(commands.Cog, name="MaintainCog"):
    # Info: Die Cog wird initialisiert, das muss standardmäßig in jede Cog rein
    def __init__(self, bot):
        self.bot = bot

    # Info: Commands werden statt mit '@bot.command()' mit '@commands.command()' geschrieben,
    #  als Parameter brauchen sie neben den Standardmäßigen noch den Parameter 'self'

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        # Info: 'Prefix + load cog.qrcodeCog'
        #  aktiviert die qrCodeCog
        try:
            self.bot.load_extension(cog)
        except (AttributeError, ImportError) as error:
            await ctx.message.add_reaction('👎')
            await ctx.send(f'```py\nCould not load {cog}: {type(error).__name__} - {error}\n```')
        else:
            await ctx.message.add_reaction('👌')

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        # Info: 'Prefix + unload cog.qrcodeCog'
        #  deaktiviert die qrCodeCog
        try:
            self.bot.unload_extension(cog)
        except (AttributeError, ImportError) as error:
            await ctx.message.add_reaction('👎')
            await ctx.send(f'```py\nCould not unload {cog}: {type(error).__name__} - {error}\n```')
        else:
            await ctx.message.add_reaction('👌')

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        # Info: 'Prefix + unload cog.qrcodeCog'
        #  lädt die Cog neu (deaktivieren + aktivieren) die qrCodeCog, falls du was an den Cogs änderst, den Bot aber nicht neustarten möchtest.
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except (AttributeError, ImportError) as error:
            await ctx.message.add_reaction('👎')
            await ctx.send(f'```py\nCould not reload {cog}: {type(error).__name__} - {error}\n```')
        else:
            await ctx.message.add_reaction('👌')

    @commands.command()
    @commands.is_owner()
    async def stop(self, ctx):
        # Info: Stoppt den Bot
        msg = await ctx.send('*Goodbye.*')
        await msg.add_reaction('👋')
        await self.bot.logout()


def setup(bot):
    bot.add_cog(maintainCog(bot))
    print('Maintain Cog loaded')
