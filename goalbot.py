import discord
from discord import team
import praw
import requests
import json

#array of teams
#testing below, grab json, filter to teams, store in array
response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")

teams = []

if response.status_code == requests.codes.ok:
    jsonResponse = response.json()
    teamsPrelim = jsonResponse['teams']
    teams = [t['name'] for t in jsonResponse['teams']]

mediaSites = ['streamwo.com', 'streamja.com', 'streamable.com', 'stream', 'clippituser.tv']


reddit = praw.Reddit(
    client_id="your_redditbot_id",
    client_secret="your_redditbot_secret",
    user_agent="Goal Bot",
)

submissionURL = ""

subreddit = reddit.subreddit("soccer")
for submission in subreddit.stream.submissions():
        for t in teams:
            if t in submission.title:
                for s in mediaSites:
                    if s in submission.url:
                        submissionURL = submission.url

print(submissionURL)        


            

""" client = discord.client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event """

#send message of 

 