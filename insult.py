import aiohttp
import asyncio
import os
import json
from discord.ext import commands
from discord_token import BOT_TOKEN

TOKEN = os.environ['DISCORD_BOT_TOKEN']


bot = commands.Bot(command_prefix='!')

insult_endpoint = "https://evilinsult.com/generate_insult.php?lang=en&type=json"

HEADERS = {"Accept": "application/json/text/html", "User-Agent": "Shen"}

async def insult(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url=insult_endpoint, headers=HEADERS) as res:             
            return await res.text()

@bot.command(name='fuckyou')
@commands.cooldown(1, 10, commands.BucketType.user)
async def insult_someone(ctx): 
    result = await insult()
    await ctx.send(json.loads(result)['insult'])

@bot.event
async def on_ready(): 
    print(f"Bite yer pillow hen, {bot.user.name}'s comin in dry!")

bot.run(TOKEN)
