# DISCORD
import discord
from discord.ext import commands

# RESZTA BIBLIOTEK
import asyncio

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True

# Utwórz instancję bota
bot = commands.Bot(command_prefix='hm!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

    # Wysłanie wiadomości powitalnej
    channel_id = 1176270133338066994  # Zastąp swoim ID kanału
    channel = bot.get_channel(channel_id)

    if channel:
        # Wyślij wiadomość na określony kanał
        await channel.send("Cześć, jestem gotowy!")

# Komenda do usuwania wiadomości
@bot.command(name='usun', help='Usuwa określoną liczbę wiadomości.')
async def usun(ctx, amount=5):
    # Sprawdź, czy użytkownik, który używa komendy, ma odpowiednie uprawnienia
    if ctx.message.author.guild_permissions.manage_messages:
        # Usuń wiadomości
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Usunięto {amount} wiadomości.')
        # Poczekaj 3 sekundy
        await asyncio.sleep(3)
        # Usuń wiadomość informacyjną
        await ctx.channel.purge(limit=1)
    else:
        await ctx.send('Nie masz wystarczających uprawnień do użycia tej komendy.')




# Uruchom bota
bot.run('MTE3NjI1MjQzOTM5ODE5MTIwNQ.GQQ8tA.U1fyKzJ8ijTndGB9pFpAvvGqxuZ370a5PqDM14')