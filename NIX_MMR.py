import os
import nextcord
from itertools import cycle
from api import Rank, Normal, ARAM
from nextcord.ext import commands, tasks

class MMR_Check(commands.Cog):
    @commands.command(name='mmr')
    async def _MMR(self, ctx: commands.Context, *, search: str):
        async with ctx.typing():
            _Rank = Rank(search)
            _Normal = Normal(search)
            _ARAM = ARAM(search)
            embed = (nextcord.Embed(title='소환사 정보', description='```css\n{}\n```'.format(search), color=nextcord.Color.blurple())
                .add_field(name='솔로랭크', value='```css\n{}\n```'.format(_Rank[0]), inline = False)
                .add_field(name='노말', value='```css\n{}\n```'.format(_Normal[0]), inline = False)
                .add_field(name='무작위 총력전', value='```css\n{}\n```'.format(_ARAM[0]), inline = False)
                .set_author(name=ctx.author.name, icon_url=ctx.author.display_avatar.url)
                .set_footer(text='API BY whatismymmr.com'))
                
            await ctx.send(embed=embed)
            await ctx.send('현재 API 문제로 인해 사용이 불가능합니다.\n빠른 해결을 위해 노력하겠습니다.')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id != bot.user.id:
            print(f"{message.guild}/{message.channel}/{message.author.name}>{message.content}")
        if message.embeds:
            print(message.embeds[0].to_dict())
        if message.attachments:
            print(message.attachments[0].url)

bot = commands.Bot(command_prefix='!', case_insensitive=True)
bot.add_cog(MMR_Check(bot))
Token = os.environ["Token"]

@bot.event
async def on_ready():
    print('클라이언트로 로그인했습니다:\n{0.user.name}\n{0.user.id}\n{1}개의 서버'.format(bot, len(bot.guilds)))
    
    status = cycle(['Produced By JeongYun','NIX MMR', '{}개의 서버에서 사용'.format(len(bot.guilds))])
    
    @tasks.loop(seconds=3)
    async def change_status():
        await bot.change_presence(status = nextcord.Status.online, activity = nextcord.Game(next(status)))
        
    change_status.start()
    
bot.run(Token)
