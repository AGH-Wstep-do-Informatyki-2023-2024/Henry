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
    channel_id = 1176270133338066994  # Zastąp swoim ID kanału
    channel = bot.get_channel(channel_id)

    if channel:
        # Wyślij wiadomość na określony kanał
        await channel.send("Cześć, jestem gotowy!")

# Uruchom bota
bot.run('MTE3NjI1MjQzOTM5ODE5MTIwNQ.GPxO_3.S2pNn7fchNHuzFK7bJjNYoC7kN57AN-U5zkcZw')