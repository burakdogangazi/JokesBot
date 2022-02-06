from distutils import command
import discord;
import os;
import requests;
import json;
from discord.ext import commands
from dotenv import load_dotenv;
load_dotenv();

TOKEN = os.getenv("TOKEN");

client = discord.Client();


def get_cnJokes(): # private api .env
    CNURL = os.getenv("CNURL");

    cnresponse_API = requests.request("GET", CNURL, headers={
        'accept': os.getenv("CNACCEPT"),
        'x-rapidapi-key': os.getenv("CNAPIKEY"),
        'x-rapidapi-host': os.getenv("CNHOST")
    })

    cnJson = json.loads(cnresponse_API.text)

    cnJokeSection = cnJson['value']

    return(cnJokeSection)



def get_dadJokes(): #private api .env
    DJURL = os.getenv("DJURL");

    djresponse_API = requests.request("GET", DJURL, headers={
        'x-rapidapi-key': os.getenv("DJAPIKEY"),
        'x-rapidapi-host': os.getenv("DJHOST")
    })

    djJson = json.loads(djresponse_API.text)

    djSetup = djJson["body"][0]["setup"]
    djPunchline =  djJson["body"][0]["punchline"]

    djReturnString = "🤣🤣🤣 --- " + djSetup + " --- 🤣🤣🤣\n🤣🤣🤣 --- "  + djPunchline + " --- 🤣🤣🤣"
    return(djReturnString)



@client.event
async def on_ready():
	guild_count = 0

	for guild in client.guilds:
		print(f"- {guild.id} (name: {guild.name})");

		guild_count = guild_count + 1

	print("Chronos Bot is in " + str(guild_count) + " guilds.");


@commands.command()
async def displayMeme(ctx):
    request = requests.get("https://memes.blademaker.tv/api?lang=en") #public api
    res = request.json()
    title = res["title"]
    ups = res["ups"]
    downs = res["downs"]
    sub = res["subdreddit"]
    m = discord.Embed(title = f"{title}\nSubreddit:{sub}")
    m.set_image(url= res["image"])
    m.set_footer(text="👎: {ups}  👍: {downs}")
    await ctx.send(embed=m)
    

# müzik açsın youtube 
# random emoji api https://ranmoji.herokuapp.com/emojis/api/v.1.0/
# random meme apihttps://memes.blademaker.tv/ 
# weather api

@client.event
async def on_message(message):
    
    if (message.author == client.user): # mesaj bizdense dokunmayacak
        return
    
    elif(message.content.startswith('-help')):
        await message.channel.send("Contact : @github.com/burakdogangazi");

    elif(message.content.startswith('-cnjoke')):
        joke = get_cnJokes()
        await message.channel.send(joke);
   
    elif(message.content.startswith('-dadjoke')):
        joke = get_dadJokes()
        await message.channel.send(joke);
        
    elif(message.content.startswith('-meme')):
         await message.channel.send(displayMeme);
        

    
client.run(os.getenv("TOKEN"));

