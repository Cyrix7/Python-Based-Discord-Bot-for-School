import discord
import wikipediaapi

def wiki_search(term):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(term)
    
    if page_py.exists() == True:
        print(term)
        term_summary = page_py.summary
        
        wiki_embed = discord.Embed(title="Wikipedia",description= f"[Click for more info]({page_py.fullurl})",colour=discord.Colour.from_rgb(255,255,253))
        wiki_embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/908067252300038195/908091539979378729/wikipedia_logo.png")
        wiki_embed.add_field(name=page_py.title, value=f"{term_summary[0:1021]}...")
        return wiki_embed
    else:
        return discord.Embed(title="No such page found", colour=discord.Colour.from_rgb(255,255,253))