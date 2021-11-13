from typing import Text
import discord
from webserver import keep_alive
from datetime import datetime
import requests
import json

with open('Token.txt') as f:
    token = f.readline()
client = discord.Client()


@client.event
async def on_connect():
    print("Yes, I am connected")


@client.event
async def on_message(message):
    if message.content.startswith('-help') or message.content.startswith('-Help'):
        await message.add_reaction("<:hackthisfall:860183680567476274>")
        embed = discord.Embed(
            title='Hack This Fall bot 🐿️ Commands List',
            description='Here is the list of commands!  📃 ',
            color=discord.Color.orange()
        )
        embed.set_footer(
            text=f"Author - Aditya Mangal#9378 💖", icon_url="https://cdn.discordapp.com/avatars/764388653480673311/d96ee5e9c07fe5fb459c248fbc3eb716.png")
        embed.add_field(name="🧛 Prefix", value="Use  `-` ")
        embed.add_field(
            name="💡 general", value=" `💻 website,` `devpost 💻,` `invite 🤘🏻,` `timeleft ⌛,` `workshops 🎉,` `socials 🐿️,` `meme 😜,` `thought 😇`")
        embed.set_image(
            url="https://i.ibb.co/B4n96wh/imageedit-1-9733467715.png")
        await message.channel.send(embed=embed)

    elif message.content.startswith('-schedule') or message.content.startswith('-Schedule'):
        await message.add_reaction("📝")
        embed = discord.Embed(
            title='',
            description=f'This Command might  be disabled! Type -help 🙌 to know the active commands',
            color=discord.Color.orange()
        )
        await message.channel.send(embed=embed)
        await message.channel.send(embed=embed)

    elif message.content.startswith('-invite') or message.content.startswith('-Invite'):
        await message.add_reaction("<:hackthisfall:860183680567476274>")
        await message.author.send("Thank You for communicating and being an important part of Hack This Fall! ❤️🐿️.Invite your friends to our server:")
        await message.channel.send("Details has been sent to your DM ✅")
        await message.author.send("https://discord.com/invite/V5KAfNQmTV")

    elif message.content.startswith('-devpost') or message.content.startswith('-Devpost'):
        await message.add_reaction("💻")
        await message.channel.send("Details has been sent to your DM ✅")
        await message.author.send("Thank You for communicating and being an important part of Hack This Fall! ❤️🐿️.")
        await message.author.send("https://hackthisfall.devpost.com")

    elif message.content.startswith('-website') or message.content.startswith('-Website'):
        await message.add_reaction("💻")
        await message.author.send("Thank You for communicating and being an important part of Hack This Fall! ❤️🐿️.")
        await message.channel.send("Details has been sent to your DM ✅")
        await message.author.send("https://hackthisfall.tech 🐿️")

    elif message.content.startswith('-timeleft') or message.content.startswith('-Timeleft'):
        await message.add_reaction("⏰")
        PYCON_DATE = datetime(year=2021, month=10,
                              day=24, hour=6, minute=1)
        countdown = PYCON_DATE - datetime.now().replace(microsecond=0)
        countdown = str(countdown)
        embed = discord.Embed(
            title='Hack This Fall 🐿️ timeleft for submission',
            color=discord.Color.orange()
        )
        embed.set_footer(
            text=f"Author - Aditya Mangal#9378 💖", icon_url="https://cdn.discordapp.com/avatars/764388653480673311/d96ee5e9c07fe5fb459c248fbc3eb716.png")
        embed.add_field(
            name="🎉", value="Hackathon has been ended. Thank You for communicating and being an important part of Hack This Fall! ❤️️. Keep a check on <#856184279967727616>. See you next year at Hack This Fall 3.0 🐿️")
        embed.set_image(
            url="https://c.tenor.com/kxzr3-r6XoIAAAAM/lets-get-this-party-started-yeah.gif")
        embed.set_thumbnail(
            url="https://media.giphy.com/media/CVhtectSd1IdV5HjLf/giphy.gif")
        await message.channel.send(embed=embed)

    elif message.content.startswith('-workshops') or message.content.startswith('-Workshop'):
        await message.add_reaction("<:hackthisfall:860183680567476274>")
        embed = discord.Embed(
            title='Hack This Fall 2.0 workshops 🐿️',
            description='Check out the Youtube chanel [here](https://www.youtube.com/channel/UCpdsmUIkLpfopjURSYF1gaA) 👈 ',
            color=discord.Color.orange()
        )
        embed.set_footer(
            text=f"Author - Aditya Mangal#9378 💖", icon_url="https://cdn.discordapp.com/avatars/764388653480673311/d96ee5e9c07fe5fb459c248fbc3eb716.png")
        embed.add_field(name=" `📁 Deploy using Filebase's S3 Compatible API` ",
                        value=" By Zac Cohen Click [here](https://www.youtube.com/watch?v=N-nk15cZfNg)")
        embed.add_field(name=" `☁️ Move your local dev env to the cloud` ",
                        value=" By Pauline Narvas Click [here](https://www.youtube.com/watch?v=uTB0h4uwcsg)")
        embed.add_field(name=" `🤓 Using GitHub to win hackathons` ",
                        value=" By Eddie Jaoude Click [here](https://www.youtube.com/watch?v=QTFQ41JJT8E)")
        embed.add_field(name=" `💖 Unleashing the Power of Communities` ",
                        value=" By Khushboo Verma Click [here](https://www.youtube.com/watch?v=-75wsmnqpqg)")
        embed.add_field(name=" `📊 Use Google Sheets as back-end for your project` ",
                        value=" By Abel Mathew Click [here](https://www.youtube.com/watch?v=hE12O0toT3w)")
        embed.add_field(name=" `🎯 Getting started with Symbl.ai` ",
                        value=" By Akanksha Bhasin & Eric Giannini Click [here](https://www.youtube.com/watch?v=1BP7mF54xgs)")
        embed.set_thumbnail(
            url="https://media.giphy.com/media/S9oreD3v1ph4fMWsQ0/giphy.gif")
        embed.add_field(name=" `Check out more past Hack This Fall Workshops uploaded on the given link below 🔗` ",
                        value="👉 Access link [here](https://www.youtube.com/channel/UCpdsmUIkLpfopjURSYF1gaA)")
        await message.channel.send(embed=embed)
    elif message.content.startswith('-thought') or message.content.startswith('-Thought'):
        await message.add_reaction("✨")
        data = requests.get("https://zenquotes.io/api/random")
        htmlcon = data.content
        resp_dict = json.loads(htmlcon)
        quote_dict = resp_dict[0]
        quote = quote_dict.get('q')
        embed = discord.Embed(
            title='',
            description=f'{quote} 😇 ',
            color=discord.Color.orange()
        )
        await message.channel.send(embed=embed)

    elif message.content.startswith('-socials') or message.content.startswith('-Socials'):
        await message.add_reaction("✨")
        embed = discord.Embed(
            title='Hack This Fall 2.0 Social handles 🐿️',
            description='Check out the links below 🔗',
            color=discord.Color.orange()
        )
        embed.set_footer(
            text=f"Author - Aditya Mangal#9378 💖", icon_url="https://cdn.discordapp.com/avatars/764388653480673311/d96ee5e9c07fe5fb459c248fbc3eb716.png")
        embed.add_field(name=" `Twitter` ",
                        value=" Click [here](https://twitter.com/hackthisfall/)")
        embed.add_field(name=" `Youtube` ",
                        value=" Click [here](https://www.youtube.com/channel/UCpdsmUIkLpfopjURSYF1gaA)")
        embed.add_field(name=" `Linked In` ",
                        value=" Cick [here](https://www.linkedin.com/company/hackthisfall/)")
        embed.add_field(name=" `Instagram` ",
                        value=" Click [here](https://www.instagram.com/hackthisfall/)")
        embed.set_image(
            url="https://i.ibb.co/B4n96wh/imageedit-1-9733467715.png")
        embed.set_thumbnail(
            url="https://cdn.dribbble.com/users/231139/screenshots/10949135/media/9ec9b3370de9b9a9bcbab786421d4b9f.gif")
        await message.channel.send(embed=embed)

    elif message.content.startswith('-prizes') or message.content.startswith('-Prizes') or message.content.startswith('-prize') or message.content.startswith('-Prize'):
        embed = discord.Embed(
            title='',
            description=f'This Command might  be disabled! Type -help 🙌 to know the active commands',
            color=discord.Color.orange()
        )
        await message.channel.send(embed=embed)

    elif message.content.startswith('-swags'):
        embed = discord.Embed(
            title='',
            description=f'This Command might  be disabled! Type -help 🙌 to know the active commands ',
            color=discord.Color.orange()
        )
        await message.channel.send(embed=embed)

    elif message.content.startswith('-meme') or message.content.startswith('-Meme'):
        await message.add_reaction("😜")
        data = requests.get(
            "https://meme-api.herokuapp.com/gimme/wholesomememes")
        htmlcon = data.content
        resp_dict = json.loads(htmlcon)
        sd = resp_dict.get('preview')
        memetitle = resp_dict.get('title')
        linklist = []
        for link in sd:
            if(link[48] == "2" or link[48] == "3" or link[48] == "1"):
                linklist.append(link)
        try:
            if (len(linklist) > 2):
                finalink = linklist[2]
            elif(len(linklist) == 2):
                finalink = linklist[1]
            else:
                finalink = linklist[0]
            if (finalink == "" or finalink == None):
                finalink = "https://www.funnybeing.com/wp-content/uploads/2016/08/Im-Loving-It-600x600.jpg"
                embed = discord.Embed(
                    title='🍔',
                    description='',
                    color=discord.Color.orange()
                )
                embed.set_footer(
                    text=f"Requested by - {message.author} 💖", icon_url=message.author.avatar_url)
                embed.set_image(url=finalink)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(
                    title=memetitle,
                    description='',
                    color=discord.Color.orange()
                )
                embed.set_footer(
                    text=f"Requested by - {message.author} 💖", icon_url=message.author.avatar_url)
                embed.set_image(url=finalink)
                await message.channel.send(embed=embed)
        except:
            pass

keep_alive()
client.run(token)
