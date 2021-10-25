import nextcord
from nextcord.ext import commands
import config

class SchoolBot(commands.AutoShardedBot):
    async def on_ready(self):
        print(f"Login {self.user}\nStarting Discord Bot.")
    
    def __init__(self):
        intent = nextcord.Intents.default()
        intent.members = True
        intent.presences = True
        super().__init__(commands.when_mentioned_or(*config.PREFIX), intent=intent, shard_count=8)
        for extension in config.EXTENSION_LIST:
            self.load_extension(extension)
        # self.remove_command("help")
        print("Complete Loading Extensions")
        print("Extension List: "+", ".join(config.EXTENSION_LIST).replace("extensions.", ""))

bot = SchoolBot()
bot.run(config.BOT_TOKEN)