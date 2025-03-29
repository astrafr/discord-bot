import discord
from discord.ext import commands
import config
import moderation
import general

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Load commands
bot.add_command(general.hello)
bot.add_command(moderation.kick)
bot.add_command(moderation.ban)
bot.add_command(moderation.clear)
bot.add_command(moderation.timeout)
bot.add_command(moderation.untimeout)

bot.run(config.TOKEN)
