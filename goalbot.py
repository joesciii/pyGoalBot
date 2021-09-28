from asyncio.tasks import sleep
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import asyncpraw
import requests



response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

teams = []

if response.status_code == requests.codes.ok:
    jsonResponse = response.json()
    teamsPrelim = jsonResponse['teams']
    teams = [t['name'] for t in jsonResponse['teams']]

mediaSites = ['streamwo.com', 'streamja.com', 'streamable.com', 'stream', 'clippituser.tv']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print("test")
    reddit = asyncpraw.Reddit(
        client_id="your_redditbot_id",
        client_secret="your_redditbot_secret",
        user_agent="Goal Bot")

    submissionURL = ""
    oldURL = ""
    

    subreddit = await reddit.subreddit("soccer")
    channel = client.get_channel(id=728287924495319120) # replace with channel_id
    
    async for submission in subreddit.stream.submissions():
        for t in teams:
            if t in submission.title:
                for s in mediaSites:
                    if s in submission.url:
                        submissionURL = submission.title + " - " + submission.url
        if oldURL != submissionURL:
            await channel.send(submissionURL)
            await asyncio.sleep(1)
            oldURL = submissionURL 
            print("Old URL: " + oldURL)
            print("URL: " + submissionURL)

client.run('your_discord_token')



    









            


 