import discord
import datetime
def date_():
    embed_date = discord.Embed(
        colour=discord.Colour.from_rgb(0, 102, 204)
    )
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    day_week = datetime.datetime.now().weekday()
    day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', "August", 'September', 'October', 'November', 'December']
    embed_date.add_field(name="Day: ", value=day_name[day_week])
    embed_date.add_field(name="Date: ", value=date, inline=False)
    embed_date.add_field(name="Month: ", value=month_name[month-1], inline=False)
    embed_date.add_field(name="Year: ", value=year, inline=False)
    
    return embed_date