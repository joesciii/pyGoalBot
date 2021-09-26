from asyncio.tasks import sleep
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import asyncpraw
import requests
import json


response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

teams = []

if response.status_code == requests.codes.ok:
    jsonResponse = response.json()
    teamsPrelim = jsonResponse['teams']
    teams = [t['name'] for t in jsonResponse['teams']]

mediaSites = ['streamwo.com', 'streamja.com', 'streamable.com', 'stream', 'clippituser.tv']


reddit = asyncpraw.Reddit(
    client_id="your_redditbot_id",
    client_secret="your_redditbot_secret",
    user_agent="Goal Bot",
)

submissionURL = ""

async def search_subreddit():
    subreddit = await reddit.subreddit("soccer")
    async for submission in subreddit.stream.submissions():
        for t in teams:
            if t in submission.title:
                for s in mediaSites:
                    if s in submission.url:
                        submissionURL = submission.url
                        print("URL A: " + submissionURL)
                        return submissionURL
                            
                            
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

async def run_in_background():
    oldURL = ""
    await client.wait_until_ready()
    channel = client.get_channel(id=728287924495319120) # replace with channel_id
    submissionURL = await search_subreddit()
    while not client.is_closed():
        
        if oldURL != submissionURL:
            await channel.send(submissionURL)   
        await asyncio.sleep(5) # task runs every 30 seconds
        oldURL = submissionURL
        print("Old URL: " + oldURL)
        print("URL: " + submissionURL)



client.loop.create_task(run_in_background())
client.run('your_discord_token')


    









            


 