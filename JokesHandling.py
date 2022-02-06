
# //ChuckNorris
import json
from matplotlib.font_manager import json_load
import requests
import os
from dotenv import load_dotenv
load_dotenv();

DJURL = os.getenv("DJURL");
response_API = requests.request("GET", DJURL, headers={
    'x-rapidapi-key': os.getenv("DJAPIKEY"),
    'x-rapidapi-host': os.getenv("DJHOST")
})

print(response_API.status_code);

data = response_API.text

parse_json = json.loads(data)

print(parse_json)
# print(parse_json["body"][0]["punchline"])









# jokeSetup = parse_json['setup']


# print(parse_json["setup"])
# print(setup + punchline)
