import config

if len(sys.argv)>1:
    token = sys.argv[1]
else:
    token = config.DISCORD_BOT_TOKEN

client = commands.Bot(command_prefix=config.DISCORD_BOT_PREFIX)