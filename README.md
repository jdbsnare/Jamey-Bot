# Jamey Bot

A Discord soft-moderation bot for an Indoor Percussion server.

## Features

- Responds when users mention drum etiquette keywords like `squeeze`, `tight grip`, `tense`, or `hard hits`
- Sends friendly tips such as "keep your taps low" and "play with relaxed hands"
- Includes `!ping`, `!jamey`, and `!softtip` commands

## Setup

1. Install Python 3.10 or newer.
2. Install `discord.py`:

```bash
pip install -U discord.py
```

3. Set your bot token in an environment variable named `DISCORD_BOT_TOKEN`.

On Windows PowerShell:

```powershell
$env:DISCORD_BOT_TOKEN = "your-token-here"
```

4. Run the bot:

```bash
python discord_bot.py
```

## Hosting for free

You can host this bot online on free tiers so it stays logged in:

- **Replit**: Create a Python repl, add `DISCORD_BOT_TOKEN` as a secret, install `discord.py`, and run `python discord_bot.py`.
- **Railway**: Deploy from GitHub, set the environment variable, and use the free tier for small bots.
- **Render**: Create a free Python service with `python discord_bot.py` as the start command.

> Note: many free hosts may sleep after inactivity or limit uptime, so choose a platform that fits your needs.

## Replit import ready

This folder is now ready to upload to Replit using either:

- `Import any repository or existing app` if you push this folder to GitHub first.
- `Zip file` by zipping the project contents and uploading it directly.

The Replit project includes:

- `discord_bot.py` — the bot code
- `main.py` — a simple Replit entrypoint
- `requirements.txt` — dependencies
- `.replit` — Replit startup command
- `README.md` — setup instructions

### If you import via GitHub

1. Push this folder to a GitHub repository.
2. In Replit, choose `Import any repository or existing app`.
3. Enter the repository URL.
4. In Replit, add `DISCORD_BOT_TOKEN` as a secret.
5. Run the project.

### If you import via Zip file

1. Zip these files: `discord_bot.py`, `main.py`, `requirements.txt`, `.replit`, `README.md`.
2. In Replit, choose `Zip file` and upload.
3. Add `DISCORD_BOT_TOKEN` as a secret.
4. Run the project.

## Notes

- `message_content` intent is enabled in the code to allow keyword detection.
- Keep your bot token private and never share it publicly.
