import nextcord
from nextcord.ext import commands
import base64, codecs
import os
import urllib.request

intents = nextcord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.all()

bot = commands.Bot(command_prefix='!', help_command=None, intents=intents)

BotSever1 = 1207935568839966740  # ไอดี เซิฟเวอร์ดิสคอส
BotSever2 = 1216397701567090733  # ไอดี ห้องที่จะให้บอทลง

@bot.event
async def on_ready():
    await bot.change_presence(activity=nextcord.Streaming(
        name="DUX ONLINE🟢", url="https://www.twitch.tv/phakaphpop"))
    vc = nextcord.utils.get(bot.get_guild(BotSever1).channels, id=BotSever2)
    await vc.guild.change_voice_state(channel=vc, self_mute=False, self_deaf=True)
    print('Bot is ready.')

@bot.event
async def on_voice_state_update(member, before, after):
   
    if after.channel and after.self_stream:
        print(f'{member.name} is in {after.channel.name} and started speaking.')



bot.run(os.environ['token'])
