# Discord
import discord
from discord.ext import commands

# Reszta istotnych bibliotek
import asyncio
import datetime

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

# KOMENDA hm!usun
@bot.command(name='usun', help='Usuwa określoną liczbę wiadomości.')
async def usun(ctx, amount=5):
    if ctx.message.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'Usunięto {amount} wiadomości.')
        await asyncio.sleep(3)
        await ctx.channel.purge(limit=1)
    else:
        await ctx.send('Nie masz wystarczających uprawnień do użycia tej komendy.')

# KOMENDA hm!kolos
kolokwium_plik = 'dane/kolokwium.txt'        

@bot.command(name='kolos')
async def kolowium(ctx):
    events = load_events()
    
    if not events:
        await ctx.send("Brak kolosów!")
    else:
        embed=discord.Embed(title="**Nadchodzące kolosy 😈**", color=0xe95858)
        upcoming_events = get_upcoming_events(events, 5)
        for event in upcoming_events:
            embed.add_field(name=f"{event}", value="", inline=False)
        await ctx.send(embed=embed)

# Funkcja do wczytywania kolosów z pliku
def load_events():
    try:
        with open(kolokwium_plik, 'r', encoding='utf-8') as file:
            events = file.readlines()
        return [event.strip() for event in events]
    except FileNotFoundError:
        return []
    
# Funkcja do sprawdzania i zwracania nadchodzących kolosów
def get_upcoming_events(events, count):
    upcoming_events = []
    today = datetime.datetime.today()
    
    for event in events:
        parts = event.split(' - ')
        if len(parts) == 2:
            date_str = parts[0].strip()
            event_name = parts[1].strip()
            
            try:
                event_datetime = datetime.datetime.strptime(date_str, '%d.%m.%Y %H:%M')
                if event_datetime >= today:
                    upcoming_events.append((event_datetime, f"{date_str} - {event_name}"))
            except ValueError:
                pass
    
    upcoming_events.sort(key=lambda x: x[0])
    return [event[1] for event in upcoming_events[:count]]

# Reszta komend przyszłości ;-)

# Uruchom bota
bot.run('TOKEN')