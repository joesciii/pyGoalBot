# pyGoalBot

Simple utility to scrape reddit.com/r/soccer for new Premier League goal videos and post them to a discord channel.

## Dependencies

* asyncpraw
* discordpy

## How to use

Create a reddit app and a discord app with a bot.

Install required dependencies and insert your discord and reddit bot information. 

Requires:

Reddit app client ID

Reddit app client secret

Discord bot secret token

Discord server channel ID to post in

Currently the program derives team names from the FPL api. A custom team list can be used and manually populated. The mediasites list is based on the commonly used hosting sites at the times of writing. Due to the nature of the video hosting you should update this regularly based on the currently used hosts at the time. This changes often and might be out of date so check the domains of recent goal posts and amend as needed.
