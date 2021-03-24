import sys
import traceback

import discord
from discord.ext import commands

import SECRET
import STATICS

bot = commands.Bot(command_prefix=STATICS.PREFIX, case_insensitive=True)
bot.remove_command('help')


# Info: Bot wird gestartet und loggt sich ein.

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    print('Running on servers:\n')
    for s in bot.guilds:
        print(' - %s (%s)' % (s.name, s.id))
    await bot.change_presence(status=discord.Status.idle)


# Info: Cogs werden geladen und initialisiert. In die eckigen Klammern trägst du die Cogs ein. Nach dem Schema, wie vorgegeben.
    COGS = [
        'cogs.maintainCog',
        'cogs.qrcodeCog'
    ]

    if __name__ == '__main__':
        for cog in COGS:
            try:
                bot.load_extension(cog)
            except Exception as e:
                print(f'Failed to load extension {cog}', file=sys.stderr)
                traceback.print_exc()


# Info: Test Command [Ping]
@bot.command()
async def ping(ctx):
    await ctx.send(':ping_pong:')


bot.run(SECRET.TOKEN)
