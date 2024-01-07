async def powiedz(ctx):
    # Bot pyta użytkownika, co powiedzieć
    await ctx.send("Co chcesz, żebym powiedział?\n 1 - Czy zdamy kolosa z algebry\n 2 - może z analizy?\n 3 - a z innych przedmiotow")
    
    # Opcje do wyboru
    options = ["Moze", "Na bank nie", "pewnie taaak, oby"]

    # Tworzenie reakcji na wiadomość jako opcje
    for index, option in enumerate(options, start=1):
        emoji = f"{index}\N{variation selector-16}\N{combining enclosing keycap}"
        await ctx.send(f"{emoji} : {option}")

    def check(reaction, user):
        return user == ctx.author and reaction.message.channel == ctx.channel

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
        choice = int(reaction.emoji[0]) - 1
        if 0 <= choice < len(options):
            await ctx.send(f"Wybrano: {options[choice]}")
        else:
            await ctx.send("Nieprawidłowy wybór.")
    except asyncio.TimeoutError:
        await ctx.send("Czas na wybór minął.")
