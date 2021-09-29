from asyncio.tasks import sleep
from logging import exception
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
    fullManc = "Manchester"
    fullSpurs = "Tottenham"
    teams += [fullManc, fullSpurs]
    print(teams)

mediaSites = ['streamwo.com', 'streamja.com', 'streamable.com', 'stream', 'clippituser.tv']

client = discord.Client()

@client.event
async def on_ready():
    print("pyGoalBot connected")
    reddit = asyncpraw.Reddit(
        client_id="your_redditbot_id",
        client_secret="your_redditbot_secret",
        user_agent="Goal Bot")

    newSubmission = ""
    oldSubmission = ""
    

    subreddit = await reddit.subreddit("soccer")
    channel = client.get_channel(id=728287924495319120) # replace with channel_id
    
    async for submission in subreddit.stream.submissions():
        for t in teams:
            if t in submission.title:
                if " W " not in submission.title:
                    for s in mediaSites:
                        if s in submission.url:
                            newSubmission = submission.title + " - " + submission.url
        if oldSubmission != newSubmission:
            embed=discord.Embed(title="GOAL")
            embed.add_field(name=submission.title, value=submission.url, inline=False)
            await channel.send(embed=embed)
            print("New submission: " + newSubmission)
            await asyncio.sleep(1)
            oldSubmission = newSubmission 



client.run('your_discord_token')
