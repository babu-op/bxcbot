import discord
from discord.ext import commands
import os

TOKEN = "YOUR_BOT_TOKEN"

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user.name}#{bot.user.discriminator} ({bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"👋 Hello, {ctx.author.mention}!")

@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

bot.run(TOKEN)
