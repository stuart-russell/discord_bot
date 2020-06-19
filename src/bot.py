import aiohttp
import asyncio
import os
import json
from discord.ext import commands

TOKEN = os.environ['DISCORD_BOT_TOKEN']
ANCHOR_API_ENDPOINT = os.environ['ANCHORMAN_API_URL']

bot = commands.Bot(command_prefix='!')

insult_endpoint = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
anchorman_endpoint = ANCHOR_API_ENDPOINT

HEADERS = {"Accept": "application/json/text/html", "User-Agent": "Shen"}

async def insult(): 
    async with aiohttp.ClientSession() as session: 
        async with session.get(url=insult_endpoint, headers=HEADERS) as res:             
            return await res.text()

async def anchorman(tags=None): 
    if tags:
        final_endpoint = f"{anchorman_endpoint}tags?tags={','.join(tags)}"
    else:
        final_endpoint = anchorman_endpoint
    async with aiohttp.ClientSession() as session: 
        async with session.get(url=final_endpoint, headers=HEADERS) as res:             
            return await res.text()

@bot.command(name='fuckyou', help="You shouldn't need any fucking help.")
@commands.cooldown(1, 10, commands.BucketType.user)
async def insult_someone(ctx): 
    result = await insult()
    await ctx.send(json.loads(result)['insult'])

@bot.command(name='anchorman',
             help="e.g. !anchorman | !anchorman Ron | !anchorman Ron, Veronica",
             )
@commands.cooldown(1, 10, commands.BucketType.user)
async def anchorman_quote(ctx, tags=None):
    names = {'Ron': 'Ron Burgundy', 'Veronica': 'Veronica Corningstone',
             'Brick': 'Brick Tamland', 'Brian': 'Brian Fantana',
             'Champ': 'Champ Kind', 'Ed': 'Ed Harken'}
    if isinstance(tags, str):
        tags = [tags]
    result = await anchorman(tags)
    res = json.loads(result)
    res_final = f"\"{res['quote']}\" - {names[res['tags'][0]]}"
    await ctx.send(res_final)

@bot.event
async def on_ready(): 
    print(f"Bite yer pillow hen, {bot.user.name}'s comin in dry!")

bot.run(TOKEN)
