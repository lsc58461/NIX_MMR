import os
import nextcord
from api import Rank, Normal, ARAM
from nextcord.ext import commands

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
                .set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url))
                
            await ctx.send(embed=embed)

bot = commands.Bot(command_prefix='!', case_insensitive=True)
bot.add_cog(MMR_Check(bot))
Token = os.environ["Token"]

@bot.event
async def on_ready():
    print('클라이언트로 로그인했습니다:\n{0.user.name}\n{0.user.id}'.format(bot))


bot.run(Token)
