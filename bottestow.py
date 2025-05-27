import discord
from discord.ext import commands, tasks
import itertools

intents = discord.Intents.all()
client = commands.Bot(command_prefix="/", intents=intents)
client.remove_command("help")

statusy = itertools.cycle([
    "🙋‍♂️Rekrutacja Otwarta! Podania Składamy w Zakładce KONTAKT ",
    "🏢Wpadnij do nas i sprawdz Naszą Oferte",
    "🚘Skup oraz Sprzedaż Pojazdów.",
    "📱 886864 DZWOŃ! ",
    "🙋‍♂️Rekrutacja Otwarta! Podania Składamy w Zakładce KONTAKT ",
    "🏢Wpadnij do nas i sprawdz Naszą Oferte",
    "🚘Skup oraz Sprzedaż Pojazdów.",
    "📱 886864 DZWOŃ! ",
    "🙋‍♂️Rekrutacja Otwarta! Podania Składamy w Zakładce KONTAKT ",
    "🏢Wpadnij do nas i sprawdz Naszą Oferte",
    "🚘Skup oraz Sprzedaż Pojazdów.",
    "📱 886864 DZWOŃ! ",
    "🙋‍♂️Rekrutacja Otwarta! Podania Składamy w Zakładce KONTAKT ",
    "🏢Wpadnij do nas i sprawdz Naszą Oferte",
    "🚘Skup oraz Sprzedaż Pojazdów.",
    "📱 886864 DZWOŃ! ",
    "🙋‍♂️Rekrutacja Otwarta! Podania Składamy w Zakładce KONTAKT ",
    "🏢Wpadnij do nas i sprawdz Naszą Oferte",
    "🚘Skup oraz Sprzedaż Pojazdów.",
    "📱 886864 DZWOŃ! ",
    "🙋‍♂️Rekrutacja Otwarta! Podania Składamy w Zakładce KONTAKT ",
    "🏢Wpadnij do nas i sprawdz Naszą Oferte",
    "🚘Skup oraz Sprzedaż Pojazdów.",
    "📱 886864 DZWOŃ! ",
    "🙋‍♂️Rekrutacja Otwarta! Podania Składamy w Zakładce KONTAKT ",
    "🏢Wpadnij do nas i sprawdz Naszą Oferte",
    "🚘Skup oraz Sprzedaż Pojazdów.",
    "📱 886864 DZWOŃ! ",    
])

@tasks.loop(seconds=5)  # Zmieniaj status co 5 sekund
async def change_status():
    await client.change_presence(activity=discord.Game(name=next(statusy)))

@client.event
async def on_ready():
    print(f'Zalogowano jako Totalnie Wypierdolony W Kosmos Twór Edwarda Pryncypałka. Zostałem Stworzony po to aby Komis Evans Cars Funkcjonował jak przykładna Patologiczna Rodzina.')
    change_status.start()

# Funkcja do sprawdzania, czy użytkownik ma określoną rolę
def ma_role(nazwa_roli):
    async def predicate(ctx):
        role = discord.utils.get(ctx.guild.roles, name=nazwa_roli)
        if role in ctx.author.roles:
            return True
        raise commands.MissingRole(nazwa_roli)
    return commands.check(predicate)

@client.command()
@ma_role("Pracownik Komisu")
async def komendys(ctx):
    embed=discord.Embed(title="Komendy SERWER", description="Poniżej znajdziesz spis komend dostępnych na Serwerze Gry.")
    embed.set_thumbnail(url="https://forum.v-rp.pl/uploads/monthly_2025_03/vibe-logo-kwadrat.webp.86d3f6fd0601f98d49b1b7d06edcef26.webp")
    embed.add_field(name="Przypisanie Pojazdu do Komisu.", value="/v przypisz", inline=True)
    embed.add_field(name="Ustawienie Ceny Pojazdu.", value="/komis wycena CENA", inline=True)
    embed.add_field(name="Sprawdzanie pojazdu w bazie danych (kradziony itp).", value="/komis vin", inline=True)
    embed.add_field(name="Sprawdzamy Tuning / Modyfikacje Auta.", value="/komis tuning", inline=True)
    embed.add_field(name="Sprawdzamy Aktualną cenę pojazdu na serwerze oraz w jakim salonie go znajdziemy.", value="/salon znajdz NAZWA POJAZDU ", inline=True)
    embed.add_field(name=" Sprzedanie Pojazdu Graczowi o podanym ID.", value="/komis sprzedaj ID", inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
@ma_role("Pracownik Komisu")
async def komendyd(ctx):
    embed=discord.Embed(title="Komendy DISCORD", description="Poniżej znajdziesz spis komend dostępnych na naszym DISCORDZIE.")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1219595258137153629/1368785675708792873/bannersamnapis.png?ex=68197c7f&is=68182aff&hm=432e2084134fb6c68ae2e6c3cd5c0db757622debd36f447847607d318bb4bd25&=&format=webp&quality=lossless&width=1312&height=834")
    embed.add_field(name="Dodanie Nowego Ogłoszenia Sprzedaży.", value="/dodaj", inline=True)
    embed.add_field(name="Wysłanie Numeru Konta Naszego Komisu.", value="/konto", inline=True)
    embed.add_field(name="Wystawienie Pojazdu na Licytacje.", value="/licytacja", inline=True)
    embed.add_field(name="Wyświetla Monit o Czasie pozostałym do zakończenia Licytacji", value="/czas", inline=True)
    embed.add_field(name="Tą Komendą Zakończysz Trwającą Licytację.", value="/koniec ", inline=True)
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
@ma_role("Pracownik Komisu")
async def pisanie(ctx):
    embed=discord.Embed(title="ZAKAZ PISANIA", description="NA KANAŁACH LICYTACYJNYCH ZAKAZANE JEST PROWADZENIE DYSKUSJI!")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1219595258137153629/1368785675708792873/bannersamnapis.png?ex=68197c7f&is=68182aff&hm=432e2084134fb6c68ae2e6c3cd5c0db757622debd36f447847607d318bb4bd25&=&format=webp&quality=lossless&width=1312&height=834")
    await ctx.send(embed=embed)
    await ctx.message.delete()

@client.command()
@ma_role("Członek Zarządu")
async def i(ctx, *, message):
    await ctx.send(message)
    await ctx.message.delete()
     
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"Nie masz uprawnień do użycia tej komendy. Wymagana rola: {error.missing_role}")
        await ctx.message.delete()
    raise error # Podnieś inne błędy, aby można je było zobaczyć
client.run("MTM2Njg3ODM0ODU4ODA5MzYxMg.GI2zYm.DmcEPdxIKrzdd4VVFYItFQI90ESB-fU_MBQMno")