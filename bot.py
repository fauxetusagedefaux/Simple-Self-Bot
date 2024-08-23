import discord
import time
from discord.ext import commands

PREFIX = "!"
TOKEN = ""

bot = commands.bot(command_prefix=PREFIX, self_bot=True)

@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong")



@bot.command()
async def chatspam(ctx, message: str, count: int, delay: float):
    sentmessages = 0
    for i in range(count):
        sentmessages += 1
        time.sleep(delay)
        await ctx.send(message)
        print(f"Message {message} sent | {sentmessages}/{count}")




bot.run(TOKEN, bot=False)