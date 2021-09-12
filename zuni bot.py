import discord, asyncio, datetime, pytz

client = discord.Client()

@client.event
async def on_ready(): # 봇이 실행되면 한 번 실행됨
    print("이 문장은 Python의 내장 함수를 출력하는 터미널에서 실행됩니다\n지금 보이는 것 처럼 말이죠")
    await client.change_presence(status=discord.Status.online, activity=discord.Game("봇의 상태매세지"))

@client.event
async def on_message(message):
    if message.content == "!영구": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))

    if message.content == "특정입력":
        ch = client.get_channel(886485429141012561)
        await ch.send ("{} | {}, User, Hello".format(ch.author, ch.author.mention))

    if message.content == "임베드": # 메세지 감지
        embed = discord.Embed(title="🚨서버제한안내", description="해당유저는 영구적으로 서버이용이 제한되었습니다",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)

        embed.add_field(name="디스코드 닉네임 로 책정", value="라인 이름에 해당하는 값", inline=True)
        embed.add_field(name="디스코드 아이디 로 책정", value="라인 이름에 해당하는 값", inline=True)

        embed.add_field(name="사유 1 로 책정", value="라인 이름에 해당하는 값", inline=False)
        embed.add_field(name="사유 2 로 책정", value="라인 이름에 해당하는 값", inline=False)

        embed.set_footer(text="Made by 쭈니#2875", icon_url="이미지 링크 - 최하단 부분")
        embed.set_thumbnail(url="이미지 링크2 - https://cdn.discordapp.com/attachments/886458137450782733/886490609907556402/befdae514f446de7.jpg")
        await message.channel.send(embed=embed)

    # 봇을 실행시키기 위한 토큰을 작성해주는 곳
    client.run('ODg2NDkxMjIzODY5NzY3NzMx.YT2XSQ.hmoy4C2M7wU24Kn6M80z2i7s8JA')