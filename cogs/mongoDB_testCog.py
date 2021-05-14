from discord.ext import commands
import pymongo


class MongoDBCog(commands.Cog, name="MongoDB"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="AddMe")
    async def _addMe(self, ctx):
        myclient = pymongo.MongoClient("mongodb://luca:mC2yDXbNo8dafWKifqmCY4EWWRbreXL@bernerdev.de:25564/")
        mydb = myclient["testDB"]
        mycol = mydb["user"]

        user_id = ctx.author.id
        name = ctx.author.name
        discriminator = ctx.author.discriminator
        fullname = name + '#' + discriminator

        userInfo = {
            "name": fullname,
            "user_id": user_id
        }
        mycol.insert_one(userInfo)
        await ctx.send("Tut!")

    @commands.command(name="FindMe")
    async def _findMe(self, ctx):
        myclient = pymongo.MongoClient("mongodb://luca:mC2yDXbNo8dafWKifqmCY4EWWRbreXL@bernerdev.de:25564/")
        mydb = myclient["testDB"]
        mycol = mydb["user"]

        user_id = ctx.author.id

        daten = mycol.find_one({"user_id": user_id})
        await ctx.send(daten)


def setup(bot):
    bot.add_cog(MongoDBCog(bot))
    print('MongoDBCog loaded')
