# pyGoalBot

Simple utility to scrape reddit.com/r/soccer for new Premier League goal videos and post them to a discord channel.

## Dependencies

* asyncpraw
* discordpy

## How to use

Install required dependencies and insert your discord and reddit bot information. Currently the program derives team names from the FPL api. A custom team list can be used and manually populated. The mediasites list is based on the commonly used hosting sites at the times of writing. This changes often and might be out of date so check the domains of recent goal posts and ammend as needed.
