import random
import discord


def pass_dm(passlen):
    allchars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&?"
    pass_ = "".join(random.sample(allchars, passlen))

    pass_embed_2 = discord.Embed(
        title="",
        description="",
        colour=discord.Colour.from_rgb(255,255,253)
    )
    pass_embed_2.add_field(name=pass_, value="***This is your randomly generated Password. (Dont Share it with anyone else!)***")
    return pass_embed_2

def error_pass():
    error_embed = discord.Embed(
        title="**Character Limit Reached!**",
        description="**The Lenght you have specified exceeds the Max. possible lenght for a Password!**",
        colour=discord.Colour.from_rgb(255,255,253)
    )
    return error_embed