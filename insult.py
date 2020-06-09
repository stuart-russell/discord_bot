import aiohttp
import asyncio
import os
from discord.ext import commands
from token import BOT_TOKEN


bot = commands.Bot(command_prefix='!')

insult_endpoint = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

HEADERS = {"Accept": "application/json", "User-Agent": "Shen"}

async def insult(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url=insult_endpoint, headers=HEADERS) as response_boi:             
            return await response_boi.json()

@bot.command(name='fuckyou')
@commands.cooldown(1, 10, commands.BucketType.user)
async def insult_someone(ctx): 
    json = await insult()
    await ctx.send(json['fuckyou'])

@bot.event
async def on_ready(): 
    print(f"{bot.user.name} has connected. Bit yer pillow hen, he's comin in dry!")

bot.run(BOT_TOKEN)
