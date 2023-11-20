import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

# Utwórz instancję bota
bot = commands.Bot(command_prefix='h!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

    # Wysłanie wiadomości powitalnej
    channel_id = 123213123123123123  # Zastąp swoim ID kanału
    channel = bot.get_channel(channel_id)

    if channel:
        # Wyślij wiadomość na określony kanał
        await channel.send("Cześć, jestem gotowy!")

# Uruchom bota
bot.run('WASZ TOKEN BOTA')