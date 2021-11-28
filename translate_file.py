import discord
import googletrans

def translate_(language_, text_):
    lang_ = ""
    all_lang = googletrans.LANGUAGES
    for i in range(len(all_lang)):
        if list(all_lang.values())[i] == language_.lower():
            lang_ = list(all_lang.keys())[i]
    t = googletrans.Translator()
    a = t.translate(text_, dest=lang_)
    
    translate_embed = discord.Embed(
        title="Translate",
        description=f"From **{all_lang[a.src].capitalize()}** to **{language_.capitalize()}**",
        color=discord.Color.from_rgb(158, 158, 158)
    )
    translate_embed.add_field(name=f"**Text**: {a.origin}", value=f"**Translate: *{a.text}* **")
    return translate_embed