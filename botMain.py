# https://discord.com/api/oauth2/authorize?client_id=905799101520691201&permissions=8&scope=bot  ====> to invite discord bot to server
import discord
import asyncio
import weather_file
import Translate_file
import help_file
import pass_generator as p_g
import wikipedia_file
import todays_date

# from pass_generator import pass_mkr
from discord.ext.commands import CommandNotFound
from discord.ext import commands

client = commands.Bot(command_prefix="/")
client.remove_command('help')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("Command not found!")

async def status():
    while True:
        await client.wait_until_ready()
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Anime!!"))
        await asyncio.sleep(70*10)
        await client.change_presence(activity=discord.Game(name='Albion.gg | /help'))
        await asyncio.sleep(70*10)
        
@client.event
async def on_ready():
    print(client.users)
    channel_id_test = client.get_channel(905488013285552208)
    print('Logged in as : {0.user.name}'.format(client))
    await channel_id_test.send("**Bot is ready to go!**")
    await client.wait_until_ready()
    await client.loop.create_task(status())

@client.command(name='ts')
async def ts(ctx, lang, *, args):
    await ctx.send(embed=Translate_file.translate_(lang, args))
@client.command(name="wt")
async def weather(ctx, *, location):
    try:
        await ctx.send(embed=weather_file.find_(location))
    except Exception as e:
        print(e)
        await ctx.send(embed=weather_file.error_message(location))

@client.command(name="ps")
async def pass_generator(ctx, passlen: int):
    if passlen <=70:
        await ctx.send(embed=discord.Embed(
            title="Password Generator",
            description=f"***A Password has been generated and has been sent to your DMs, {ctx.author.mention}!***",
            colour=discord.Colour.from_rgb(255,255,253))
            )
        await ctx.author.send(embed=p_g.pass_dm(passlen))
    elif passlen>70:
        await ctx.send(embed=p_g.error_pass())
    
@client.command(name="wiki")
async def wikipedia__(ctx, *, _term:str):
    await ctx.send(embed=wikipedia_file.wiki_search(_term))
    
@client.command(name="date")
async def date__(ctx):
    await ctx.send(embed=todays_date.date_())
    
@client.command(name='help')
async def help_(ctx):
    await ctx.send(embed=help_file._help_())

client.run("Bot Token")