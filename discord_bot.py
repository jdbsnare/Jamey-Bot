import os
import random
import discord
from discord.ext import commands

BOT_NAME = "Jamey Bot"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

MODERATION_TRIGGERS = [
    "squeeze",
    "squeezing",
    "tight grip",
    "tightness",
    "tense",
    "tension",
    "locked wrists",
    "stiff",
    "clench",
    "choke",
    "hard hits",
    "too hard",
    "forceful",
    "death grip",
]

MODERATION_RESPONSES = [
    "Keep your taps low and your hands relaxed.",
    "Remember, a relaxed hand and low taps help you play better.",
    "Try to stay loose in your wrists and avoid squeezing the stick.",
    "Soft hands let the line breathe better than a forceful grip.",
    "Relax your hands and keep those taps low and controlled.",
]

@bot.event
async def on_ready():
    activity = discord.Game(name="soft percussion etiquette")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"{BOT_NAME} is online as {bot.user}!")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.guild:
        return

    content = message.content.lower()
    if any(trigger in content for trigger in MODERATION_TRIGGERS):
        response = random.choice(MODERATION_RESPONSES)
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command(name="jamey")
async def jamey(ctx):
    await ctx.send(
        "I'm Jamey Bot. I help keep percussion chat friendly by sharing soft-moderation tips when drum etiquette keywords appear."
    )

@bot.command(name="softtip")
async def softtip(ctx):
    await ctx.send(random.choice(MODERATION_RESPONSES))

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if not TOKEN:
    raise RuntimeError("Please set the DISCORD_BOT_TOKEN environment variable.")

bot.run(TOKEN)
