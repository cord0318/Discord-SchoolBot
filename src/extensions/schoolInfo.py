from typing import Optional
import nextcord
from nextcord.ext import commands
import school
from datetime import datetime
import re

class SchoolInfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="school", aliases=["schoolInfo", "학교", "학교정보"])
    async def SchoolInfo(self, ctx: commands.Context, schoolName=None):
        if schoolName != None:
            data = await school.asyncSchoolData(school_name=schoolName)
            if data["error"]==False:
                embed = nextcord.Embed(title="{} ({})".format(data["school_name"], data["area_code"]+data["school_code"]), color=nextcord.Color.random())
                embed.add_field(name="교육청", value=data['area_name'])
                embed.add_field(name="영어이름", value=data['eng_school_name'])
                embed.add_field(name="학교등급", value=data['school_type'])
                embed.add_field(name="위치", value=data['location'])
                embed.add_field(name="전화번호", value=data["phone_number"])
                embed.add_field(name="웹사이트", value=data["website"])
                embed.add_field(name="성별", value=data["gender_type"])
                await ctx.reply(embed=embed)
            else:
                await ctx.reply("**{}**".format(data["message"]))
        else:
            await ctx.reply("**학교 이름을 적어주세요.**")

    @commands.command(name="schoolMeal", aliases=["급식", "schoolmeal"])
    async def schoolMeal(self, ctx: commands.Context, school_name=None, date: Optional[int]=datetime.now().strftime("%Y%m%d")):
        if school_name != None:
            data = await school.asyncMealToken(school_name)
            if data["error"]==False:
                data = await school.asyncMealTokenCheck(data["token"], date)
                if data["error"]==False:
                    data["meal"] = re.sub(r'[0-9]+', '', data["meal"])
                    data["meal"] = data["meal"].replace(".", " ")
                    data["nutrient"] = data["nutrient"].replace(".", " ")
                    data["nutrient"] = data["nutrient"].replace(" :", ",")
                    embed = nextcord.Embed(title="{}의 급식 [{}]".format(data["school_name"], date), color=nextcord.Color.random())
                    embed.add_field(name="급식", value=data["meal"])
                    embed.add_field(name="영양소", value=data["nutrient"])
                    await ctx.reply(embed=embed)
                else:
                    # await ctx.reply("**{}**".format(data["message"]))
                    await ctx.reply(f"**{date}일의 {school_name}의 급식을 찾을 수 없습니다.**")
            else:
                await ctx.reply("**{}**".format(data["message"]))
        else:
            await ctx.reply("**학교 이름을 적어주세요.**")

def setup(bot):
    bot.add_cog(SchoolInfoCog(bot))