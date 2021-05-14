import asyncio
import sys
import traceback

import discord
from discord.ext import commands

import SECRET
import STATICS

bot = commands.Bot(command_prefix=STATICS.PREFIX, case_insensitive=True)

# Info: Die Zeile hier drunter deaktiviert den eingebauten help Befehl. Um einen eigenen help Befehl nutzen zu können einfach das HashTag für den Kommentar in Zeile 13 entfernen.
bot.remove_command('help')


# Info: Bot wird gestartet und loggt sich ein.

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    print('Running on servers:\n')
    for s in bot.guilds:
        print(' - %s (%s)' % (s.name, s.id))

    # Info: Funktion zum wechseln des Status wird im Loop aufgerufen.
    bot.loop.create_task(status_task())

    # Info: Cogs werden geladen und initialisiert. In die eckigen Klammern trägst du die Cogs ein. Nach dem Schema, wie vorgegeben.
    COGS = [
        'cogs.maintainCog',
        'cogs.qrcodeCog',
        'cogs.userinfoCog',
        'cogs.mongoDB_testCog'
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


async def status_task():
    # Info: In dieser Methode wird der Status des Bots definiert und alle 10 Sekunden gewechselt. Nach jedem Wechsel muss ein asyncio.sleep von mindestens 10 Sekunden vorhanden sein.
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{bot.users} users"), status=discord.Status.idle)
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{STATICS.PREFIX}help"), status=discord.Status.idle)
        await asyncio.sleep(10)


bot.run(SECRET.TOKEN)
