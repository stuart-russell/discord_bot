# Discord Bot

Simple Discord chat bot that has a couple of utilities.
> !fuckyou - This command returns a [random instult](https://evilinsult.com/)

> !anchorman Brick - This command fetches a [random quote](https://github.com/srussell91/anchorman-quote-api) from The Anchorman. Accepts a character from the film as an argument or no argument for any character.

### Setup

> Running directly

```shell
$ git clone https://github.com/srussell91/discord_bot.git
$ cd discord-bot
$ pip install src/requirements.txt
$ python src/bot.py
```

> Running with docker

```shell
$ git clone https://github.com/srussell91/discord_bot.git
$ cd discord-bot
$ docker build --build-arg anchorman_url=<url> --build-arg discord_token=<token> -t discord-bot .
$ docker run --rm -it discord-bot
```

---

## Usage (Optional)

Create a Discord application/bot and invite to desired server.
Useful docs:

[Discord Developer Portal](https://discord.com/developers/)

[How to Make a Discord Bot in Python](https://realpython.com/how-to-make-a-discord-bot-python/)