import discord
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
    teams += [fullManc, fullSpurs] #response only returns 'Man City, Man U, Spurs'

else:
    print("Cannot access Premier League API to grab active teams. Try again later or manually populate the 'teams' list.")
    exit()

mediaSites = ['streamwo.com', 'streamja.com', 'streamable.com', 'stream', 'clippituser.tv']

client = discord.Client()

@client.event
async def on_ready():
    print("pyGoalBot connected")
    #add reddit bot info below
    reddit = asyncpraw.Reddit(
        client_id="your_redditbot_id",
        client_secret="your_redditbot_secret",
        user_agent="Goal Bot")

    newSubmission = ""
    oldSubmission = ""
    

    subreddit = await reddit.subreddit("soccer")
    channel = client.get_channel(id=728287924495319120) # replace with your channel_id
    
    async for submission in subreddit.stream.submissions():
        for t in teams:
            if t in submission.title and " W " not in submission.title:
                for s in mediaSites:
                    if s in submission.url:
                        newSubmission = submission.title + " - " + submission.url
                            
        if oldSubmission != newSubmission:
            if len(submission.title) <= 128:
                embed=discord.Embed(title="GOAL")
                embed.add_field(name=submission.title, value=submission.url, inline=False)
                await channel.send(embed=embed)
                print("New submission: " + newSubmission)
                oldSubmission = newSubmission 
                await asyncio.sleep(1)               
            else:
                await channel.send(newSubmission)
                print("New submission: " + newSubmission)
                oldSubmission = newSubmission 
                await asyncio.sleep(1)      

client.run('your_discordbot_token')
