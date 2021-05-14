import sqlite3
from discord.ext import commands


class sql_testCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


@commands.Cog.listener()
async def on_message(message):
    user_id = message.author.id
    name = message.author.name
    discriminator = message.author.discriminator
    fullname = name + '#' + discriminator
    db = sqlite3.connect("./data/db/main.sqlite")
    cursor = db.cursor()
    cursor.execute(f'SELECT user_id, name FROM user WHERE user_id = {user_id}')
    result = cursor.fetchone()
    print(result)
    if result is None:
        sql = 'INSERT INTO user(name, user_id) VALUES(?,?)'
        val = (fullname, user_id)
    elif result is not None:
        sql = 'UPDATE user SET name = ? WHERE user_id = ?'
        val = (fullname, user_id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()


def setup(bot):
    bot.add_cog(sql_testCog(bot))
    print("sql_testCog Loaded")
