# TeleBot - Telegram UserBot

    

    
## Documentation
For passionate readers 😂 the documentation can be found [here]https://github.com/arupmandal/TeleBot/)

## The Easier Way to install

[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/arupmandal/TeleBot)

## Support
Join [TeleBot Support group](https://t.me/iamarupmandal) for updates and new plugin suggestions.
Do fork and star the repo 

### Session String 
<a href="https://telebot-sessionstring-generator.xditya.repl.run/" target="_blank"><img src="https://img.shields.io/badge/run-string__session.py-red?style=for-the-badge&logo=repl.it" alt="generate_string" /></a>

### The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/arupmandal/TeleBot
cd TeleBot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m telebot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Check [Line 111](https://github.com/Total-Noob-69/X-tra-Telegram/blob/master/userbot/uniborgConfig.py#L111) and start adding your vars there.
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.

# Disclaimer
```
/**
    	Improper use may lead to ban.
    	I am not responsible if you misuse this bot.
	This bot is just for managing groups more effectively and having some fun
	with your telegram account.
	No one is responsible for your actions.
	If you spammed and got reported again and again, 
	and, at last got your account banned, and you
	point your fingers at me, I'll be rolling on the floor laughing at you.
/**
```

## Follow on:
<p align="left">
<a href="https://telegram.me/arupbotsofficial"><img src="https://img.shields.io/badge/Join%20Our%20Channel-Arup%20Bots-darkblue?logo=telegram"></a>
</p>
<p align="left">
<a href="https://github.com/arupmandal"><img src="https://img.shields.io/badge/GitHub-Follow%20on%20GitHub-inactive.svg?logo=github"></a>
</p>
<p align="left">
<a href="https://twitter.com/iamarupmandal"><img src="https://img.shields.io/badge/Twitter-Follow%20on%20Twitter-informational.svg?logo=twitter"></a>
</p>
<p align="left">
<a href="https://instagram.com/iamarupmandal"><img src="https://img.shields.io/badge/Instagram-iamarupmandal-magenta?logo=instagram"></a>
</p>

## Donate:
[![Donate](https://img.shields.io/badge/Donate%20Us-UPI-orange?style=for-the-badge)](https://upayi.me/helloarup@paytm)

