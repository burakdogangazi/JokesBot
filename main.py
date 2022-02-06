import discord;
import os
import requests;
import json;
from dotenv import load_dotenv;
load_dotenv();

TOKEN = os.getenv("TOKEN");

client = discord.Client()


def get_EmojiCode(): #public api
    url = "https://ranmoji.herokuapp.com/emojis/api/v.1.0/"
    emoji_API =  requests.request("GET",url)
    
    emojiJson = json.loads(emoji_API.text)
    
    emojiSection = emojiJson["emoji"]
    
    return(emojiSection)
    

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

    a = djSetup = djJson["body"][0]["setup"]
    b = djPunchline =  djJson["body"][0]["punchline"]

    djReturnString = "🤣🤣🤣 --- " + djSetup + " --- 🤣🤣🤣\n🤣🤣🤣 --- "  + djPunchline + " --- 🤣🤣🤣"
    return(djReturnString)


@client.event
async def on_ready():
	guild_count = 0

	for guild in client.guilds:
		print(f"- {guild.id} (name: {guild.name})");

		guild_count = guild_count + 1

	print("Meme Bot is in " + str(guild_count) + " guilds.");


@client.event
async def on_member_join(member):
    print(f'{member} has joined a server');
     

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server');
    

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
    
    elif(message.content.startswith("-emjc")):
        emj = get_EmojiCode()
        await message.channel.send(emj)


client.run(os.getenv("TOKEN"));

