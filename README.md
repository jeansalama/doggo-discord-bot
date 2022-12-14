# doggo-discord-bot
A simple discord bot posting doggo gifs

## Requirements

- Python 3.8+
- Discord server and admin account
- [discord.py](https://discordpy.readthedocs.io/)
- [Creating a Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html)

## Install

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt --upgrade
```

## Env variables

Create a `.env` file based on [`.env.emtplate`](.env.template) to configure 
your bot.

## Run

```sh
python doggo_bot.py
```

## Usage

Go to your chat and run one of these commands

- `/test` : send a test message `'Some random doggo meme!'`
- `/doggo` : send a "random" doggo gif

