import discord
from discord.ext import commands
from discord.message import Message
from discord import Permissions
from discord.utils import get
import random

botToken = 'OTc5MjI2NDQxNTc5MzY0Mzgy.G22NmU.tRWyTNh5SpZGzEqwqmZC2X9y-zlKpH_E2Shlt4'
bot = commands.Bot(command_prefix='&&')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))

@bot.event
async def on_guild_join(guild):
    pass

@bot.event
async def on_message(message):
    diegoTroll = ["Be a good boy",
        "Whatever daddy wants, daddy gets",
        "I HAVE YOUR ADDRESS",
        "It's time for bed, kitten",
        "Come here and drink some milk sweetie",
        "Look behind you"
    ]

    images = ["https://preview.redd.it/1d5e4b8yter81.jpg?width=585&format=pjpg&auto=webp&s=a335e20591361625ce69c362034425a2039f78aa",
    "https://preview.redd.it/si1wp6zh72i81.jpg?auto=webp&s=d5a57d157b7a9c5f1984b7c60b47324e483cbe3f",
    "https://theprofilehhs.com/wp-content/uploads/2022/02/boisvert.jpeg",
    "https://preview.redd.it/kjklub8yter81.jpg?width=640&crop=smart&auto=webp&s=d748b6eb8a68f5310b0e7e840426cd72a8d01879",
    "https://upload.wikimedia.org/wikipedia/en/6/67/This_Man_original_drawing.jpg",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS66-UIbBHec-Fqx5le1Jlo8Pva0Cze7qAzUAesmspMGF2zr6UDhZtiomuY5v5FAaMwpvQ&usqp=CAU",
    "https://image.scoopwhoop.com/q30/s4.scoopwhoop.com/anj/kb/421214978.jpg",
    "https://i.ytimg.com/vi/QBaIyCHGLlg/maxresdefault.jpg",
    ]

    if message.author.id == 322969966309670912:
        embed = discord.Embed(title=random.choice(diegoTroll), color=discord.Color.dark_red())    
        embed.set_thumbnail(url=random.choice(images))
        await message.channel.send(f"{message.author.mention}")
        await message.channel.send(embed=embed)
""""
@bot.command(pass_context = True)
async def append(ctx, user: discord.Member):
    guild = ctx.guild
    role = ctx.guild.get_role(979234181840257059)
    await user.add_roles(role)
    print(ctx.message.author, "added admin")
"""

@bot.command()
async def forceclear(ctx, amount=1):
    if ctx.author.id == 322969966309670912:
        await ctx.channel.purge(limit=amount)
        print(ctx.message.author, "attempted to clear", amount, "messages")

bot.run(botToken)