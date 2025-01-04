import discord
import Crawling
import time
import datetime
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.message_content = True
#client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    game = discord.Game("笑死")
    await client.change_presence(status=discord.Status.online, activity=game)
    await client.add_cog(TaskTime(client))
'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "MLB":
        probable = Crawling.show_probable() 
        string = ""
        for i in range(len(probable)):
            if i  == len(probable)//2:
                await message.channel.send(string)
                string = ""
                
            string += probable[i]
        await message.channel.send(string)
'''
class TaskTime(commands.Cog):
    tz = datetime.timezone(datetime.timedelta(hours = 8))
    everyday_time = datetime.time(hour = 17, minute = 0, tzinfo = tz)
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.everyday.start()

    @tasks.loop(time = everyday_time)
    async def everyday(self):
        now = datetime.datetime.now(self.tz)
        if now.hour == self.everyday_time.hour and now.minute == self.everyday_time.minute:
            channel_id = 1232217306659164180
            channel = self.bot.get_channel(channel_id)
            probable = Crawling.show_probable() 
            string = ""
            for i in range(len(probable)):
                if i  == len(probable)//2:
                    await channel.send(string)
                    string = ""
                    
                string += probable[i]
            await channel.send(string)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(TaskTime(bot))



file = open("token.txt","r")
token = file.read()
client.run(token)