# CBS_DiscordBot
(Code Breakers Studio Discord Bot)

CBS_DiscordBot is a Python base discord bot build on [discord](https://discordpy.readthedocs.io) library

## Installation

### Pip installation:
```bash
pip install git+https://github.com/CodeBreakersStudio/CBS_DiscordBot.git
```

Use button **Clone or download** to download .zip file or clone git repository

>### Clone command
>```bash
>git clone https://github.com/CodeBreakersStudio/CBS_DiscordBot.git
>```

>### .zip way:
>Extract .zip to place where you need it

#### Second step:
>Enter the CBS_DiscordBot project run cmd or bash in this directory and use this command:
>```bash
>python -m pip install -e .
>```
>that will install this library

### Requirments
>Install [python](https://www.python.org/downloads/) 3.7+ and when you install check checkbox to add python to your Path

---
## Usage
### Simple:
Enter to this directory ```CBS_DiscordBot```

You find example bot config file under ```./example/conf```

In conf you need to insert your bot token/tokens from [Discord](https://discordapp.com/developers/applications/)

#### run:
windows:
>```bash
>run.bat
>```
linux:
>```bash
>run.sh
>```

### Advanced:
>```python
>import cbs_db as discord_bot
>```

---
## Project structure
```
CBS_DiscordBot
| README.md
| .gitignore
| LICENCSE
| setup.py                <- module setup
| run.py                  <- run file in python
| run.bat                 <- run file for windows
| run.sh                  <- run file for linux
|-example
| | bot.py                <-example bot
| | conf                  <- configuration file of example bot
|-cbs_db                  <- src folder
| | __init__.py           <- main bot instance
| | config.py             <- pure config 
| |-bot_class
| | | __init__.py         <- bot builder class for new istances
| |-cogs                  <- cogs
| | |-musicbot
| | | | __init__.py       <- musicbot main cog
| | |-util
| | | | __init__.py       <- utilities
| | | ...                 <- other cogs in future
|-test                    <- unit test folder
```

---
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU](https://choosealicense.com/licenses/gpl-3.0/)
