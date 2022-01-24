    if message.content.startswith("!서버"):
        id = message.author.id
        if id == 639032101278318612:
            for guild in client.guilds:
                sname = guild.name
                slist = []
                slist.append(sname)
                sid = guild.id
                sdlist = []
                sdlist.append(sid)
                await message.channel.send(slist + sdlist)
        else:
            await message.channel.send("권한이 부족합니다")
    
    if message.content.startswith("!유저"):
        id = message.author.id
        if id == 639032101278318612:
            N1 = message.content.split(" ")
            NT = ""
            vrsize = len(N1)
            vrsize = int(vrsize)
            for i in range(1, vrsize): 
                NT = NT+" "+N1[i]
            NT = NT.lstrip()
            guild = client.get_guild(int(NT)) 
            for member in guild.members:
                sname = member.name
                slist = []
                slist.append(sname)
                sid = member.id
                sdlist = []
                sdlist.append(sid)
                await message.channel.send(slist + sdlist)
        else:
            await message.channel.send("권한이 부족합니다")

    if message.content.startswith("!채널"):
        id = message.author.id
        if id == 639032101278318612:
            N1 = message.content.split(" ")
            NT = ""
            vrsize = len(N1)
            vrsize = int(vrsize)
            for i in range(1, vrsize): 
                NT = NT+" "+N1[i]
            NT = NT.lstrip()

            guild = client.get_guild(int(NT))
            for channel in guild.channels:
                sd = channel.name
                slist = []
                slist.append(sd)
                sid = channel.id
                sdlist = []
                sdlist.append(sid)
                sidt = channel.type
                sidtlist = []
                sidtlist.append(sidt)
                await message.channel.send(slist + sdlist + sidtlist)
        else:
            await message.channel.send("권한이 부족합니다")

    if message.content.startswith("@채널분석"):
        if id == 639032101278318612:
            N1 = message.content.split(" ")

            channel = client.get_channel(int(N1[1]))
            channelname = channel.name
            channeltype = channel.type
            channelcategory = channel.category
            date = datetime.datetime.utcfromtimestamp(((int(N1[1]) >> 22) + 1420070400000) / 1000)#지랄맞게 썸머타임 계산안됨
            embed = discord.Embed(title =str(channelname), colour = discord.Colour.blue())   
            embed.add_field(name ='속해있는 카테고리채널: ', value = channelcategory, inline = False)
            embed.add_field(name ='채널타입: ', value = channeltype ,inline = False)
            embed.set_footer(text="채널생성일: " + str(date.year) + "/" + str(date.month) + "/" + str(date.day))
            await message.channel.send(embed=embed) 
        else:
            await message.channel.send("권한이 부족합니다") 

    if message.content.startswith("@서버분석"):
        if id == 639032101278318612:
            N1 = message.content.split(" ")

            guild = client.get_guild(int(N1[1]))
            guildname = guild.name
            guildbenner = guild.icon_url
            serverowner = guild.owner
            serverownerid = guild.owner_id
            member = guild.member_count
            date = datetime.datetime.utcfromtimestamp(((int(N1[1]) >> 22) + 1420070400000) / 1000)#지랄맞게 썸머타임 계산안됨
            embed = discord.Embed(title =str(guildname), colour = discord.Colour.blue()) 
            embed.set_thumbnail(url=guildbenner)
            embed.add_field(name ='길드생성일: ', value = str(date.year) + "/" + str(date.month) + "/" + str(date.day) , inline = False)
            embed.add_field(name ='멤버수: ', value = str(member) ,inline = False)
            embed.set_footer(text="관리자: " + str(serverowner) + " 아이디: " + str(serverownerid))
            await message.channel.send(embed=embed) 
        else:
            await message.channel.send("권한이 부족합니다")

    if message.content.startswith("!히스토리"):
        id = message.author.id
        if id == 639032101278318612:
            N1 = message.content.split(" ")
            channel = client.get_channel(int(N1[1]))
            messages_list = await channel.history(limit=10).flatten()  
            StrA = " ".join(str(m) for m in messages_list)
            StrA_list = StrA.split()
            matching = [s for s in StrA_list if "id=" in s]
            f = open("채팅히스토리.txt", 'a', encoding="UTF-8") 
            f.write(str(matching))
            f.close()   
            await message.channel.send('분석완료')
        else: 
            await message.channel.send("권한이 부족합니다")

    if message.content.startswith("@메세지분석"):
        if id == 639032101278318612:
            N1 = message.content.split(" ")

            channel = client.get_channel(int(N1[1]))
            msg = await channel.fetch_message(N1[2])
            co = msg.content
            author = msg.author.name
            authoravatar = msg.author.avatar_url
            authorid = msg.author.id
            date = datetime.datetime.utcfromtimestamp(((int(N1[2]) >> 22) + 1420070400000) / 1000)#지랄맞게 썸머타임 계산안됨s
            embed = discord.Embed(title =str(author), description ="유저아이디: " + str(authorid), colour = discord.Colour.blue()) 
            embed.set_thumbnail(url=authoravatar)
            embed.add_field(name ='메세지: ', value= co ,inline = False)
            embed.set_footer(text="작성시간: " + str(date.year) + "/" + str(date.month) + "/" + str(date.day) + "[" + str(date.hour) + str(date.minute) + "]")
            await message.channel.send(embed=embed) 
        else: 
            await message.channel.send("권한이 부족합니다")

    if message.content.startswith("@유저정보"):
        mt = message.mentions[0]
        user = mt
        userid = mt.id 
        userav = mt.avatar_url
        date = datetime.datetime.utcfromtimestamp(((int(userid) >> 22) + 1420070400000) / 1000)#지랄맞게 썸머타임 계산안됨s
        embed = discord.Embed(title =str(user), description ="유저아이디: " + str(userid), colour = 0x56b8f5) 
        embed.set_thumbnail(url=userav)
        embed.set_footer(text="계정생성일: " + str(date.year) + "/" + str(date.month) + "/" + str(date.day) + "[" + str(date.hour) + str(date.minute) + "]")
        await message.channel.send(embed=embed)


    if message.content.startswith("!k"):
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            NT = NT+" "+N1[i]
        NT1 = NT.lstrip()
        characters = "'!?.,"

        for x in range(len(characters)):
            NT2 = NT1.replace(characters[x],"")


        
    if message.content.startswith("!e"):
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            NT = NT+" "+N1[i]
        NT1 = NT.lstrip()

        characters = "'!?.,"

        for x in range(len(characters)):
            NT2 = NT1.replace(characters[x],"")

        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        try:
            await message.author.voice.channel.connect() 
            for vc in client.voice_clients:
                if vc.guild == message.guild:
                    voice = vc
            if voice.is_playing(): 
                for vc in client.voice_clients:
                    if vc.guild == message.guild:
                        voice = vc
                voice.stop() 
                tts = gTTS(text=NT1, lang='en', slow=True)
                tts.save("tts file/e/" + NT2 + ".mp3")
                voice.play(discord.FFmpegPCMAudio(executable = './ffmpeg/bin/ffmpeg.exe', source="tts file/e/" + NT1 + '.mp3'))
                await message.channel.send("내용: " + NT + "/" + message.author.display_name + "시킴")
            else:
                for vc in client.voice_clients:
                    if vc.guild == message.guild:
                        voice = vc
                tts = gTTS(text=NT1, lang='en', slow=True)
                tts.save("tts file/e/e/" + NT2 + ".mp3")
                voice.play(discord.FFmpegPCMAudio(executable = './ffmpeg/bin/ffmpeg.exe', source="tts file/e/" + NT1 + '.mp3'))
                await message.channel.send("내용: " + NT + "/" + message.author.display_name + "시킴")
        except:
            for vc in client.voice_clients:
                if vc.guild == message.guild:
                    voice = vc
            if voice.is_playing(): 
                for vc in client.voice_clients:
                    if vc.guild == message.guild:
                        voice = vc
                voice.stop() 
                tts = gTTS(text=NT1, lang='en', slow=True)
                tts.save("tts file/e/" + NT2 + ".mp3")
                voice.play(discord.FFmpegPCMAudio(executable = './ffmpeg/bin/ffmpeg.exe', source="tts file/e/" + NT1 + '.mp3'))
                await message.channel.send("내용: " + NT + "/" + message.author.display_name + "시킴")
            else:
                for vc in client.voice_clients:
                    if vc.guild == message.guild:
                        voice = vc
                tts = gTTS(text=NT1, lang='en', slow=True)
                tts.save("tts file/e/" + NT2 + ".mp3")
                voice.play(discord.FFmpegPCMAudio(executable = './ffmpeg/bin/ffmpeg.exe', source="tts file/e/" + NT1 + '.mp3'))
                await message.channel.send("내용: " + NT + "/" + message.author.display_name + "시킴")

    if message.content.startswith("!leave"):
        for vc in client.voice_clients:
            if vc.guild == message.guild:
                voice = vc
        
        await voice.disconnect()
        await message.channel.send("나가기")