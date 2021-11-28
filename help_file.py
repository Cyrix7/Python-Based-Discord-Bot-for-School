import discord

def _help_():
    help_embed = discord.Embed(
        title="All available commands", 
        description=" *\"Don't include <>brackets in commands\"* ",
        colour=discord.Color.from_rgb(158, 158, 158)
    )
    help_embed.add_field(name="`/ts <language>  <text>`", value="Translate the <text> from given language to <language>", inline=False)
    help_embed.add_field(name="`/wt <location>`", value="Gives Temperature report of <location>", inline=False)
    help_embed.add_field(name="`/ps <password length>`", value="Generates a random password limited by the specified length. (Max. 70 Characters)", inline=False)
    help_embed.add_field(name="`/wiki <term>`", value="Gives short summary of <term>.", inline=False)
    help_embed.add_field(name="`/date`", value="Gives today's date.", inline=False)
    return help_embed
    