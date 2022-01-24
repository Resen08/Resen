import re
import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
from discord.flags import MessageFlags
from discord.gateway import ReconnectWebSocket
import youtube_dl
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
import os
import sys
import json
from selenium import webdriver
import time
import datetime
from gtts import gTTS
import asyncio
import functools
import itertools
import math
from async_timeout import timeout
from discord.utils import get
import shutil
import fu
from PIL import Image
from io import BytesIO
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import string
import os.path
import linecache


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents)
token = "ODIxMDUzMjkzNDc5NzIzMDI4.YE-Hdw.IPtY05vChYidvKDOWQ0pndZ2PZQ"



@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print(random.randrange.__doc__)
    print(discord.version_info)
    print(sys.version_info)

    print("Loading..")
    print("Success!")
    game = discord.Game("~help")
    await client.change_presence(status=discord.Status.online, activity=game)
    

@client.event
async def on_message(message):
    if message.content.startswith("~help"):
        embed = discord.Embed(title ="명령어 모음:", colour = discord.Colour.blue()) 
        embed.add_field(name = "!k + 단어 or 문장", value= "인식된 단어 or 문장을 영어 tts로 재생합니다" ,inline = False)
        embed.add_field(name = "!e + 단어 or 문장", value= "인식된 단어 or 문장을 영어 tts로 재생합니다" ,inline = False)
        embed.add_field(name = "!leave", value= "보이스채팅방을 나갑니다" ,inline = False)
        embed.add_field(name = "!초대링크생성", value= "서버 초대 링크를 생성합니다",inline = False)
        embed.add_field(name = "!뽑기 원하는 단어 or 숫자", value= "원하는 단어 or 숫자를 적으면 그중 랜덤으로 하나가 추출됩니다 ",inline = False)
        embed.add_field(name = "!순서 원하는 단어 or 숫자", value= "원하는 단어 or 숫자를 적으면 랜덤하게 순서가 매겨집니다 ",inline = False)
        embed.add_field(name = "!수배 원하는 유저 멘션", value= "원하는 유저를 멘션하면 수배 시킵니다 ",inline = False)
        embed.add_field(name = "!+ 숫자 숫자", value= "더하기",inline = False)
        embed.set_footer(text="Created by XX")
        await message.channel.send(embed=embed) 

    if message.content.startswith("!초대링크생성"):
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            NT = NT+" "+N1[i]
        NT = NT.lstrip()

        channel = client.get_channel(int(NT))
        invite = await channel.create_invite()
        await message.channel.send(invite)

    if message.content.startswith("!뽑기"):
        sys_random = random.SystemRandom()
        N1 = message.content.split(" ")
        NT = " "
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            NT = NT+" "+N1[i]
        NT1 = NT.lstrip()
        
        result = len(NT1.split())
        result = int(result)

        NT1 = NT1.split()
        msg = await message.channel.send(":one:")
         
        time.sleep(0.5)
        for d in range(2, 4):
            if d == 2:
                py = ":two:"
            elif d == 3:
                py = ":three:"
            await msg.edit(content=py)
            time.sleep(0.8)

        await msg.delete()

        NR = random.randint(1, result)
        
        embed = discord.Embed(title ="결과: \n" + NT1[NR], colour = discord.Colour.red()) 
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/897120714912583710/925369132298403871/87b02dede0f9296180965dcfc2d89493.png")
        await message.channel.send(embed=embed)
        await message.channel.send(NT1[NR]) 
        random.seed()

    if message.content.startswith("!+"):
        N1 = message.content.split(" ")
        a = int(N1[1])
        b = int(N1[2])
        add = fu.add(a, b)
        await message.channel.send(str(add))
    
    if message.content.startswith("!-"):
        N1 = message.content.split(" ")
        a = int(N1[1])
        b = int(N1[2])
        sub = fu.sub(a, b)
        await message.channel.send(str(sub))

    if message.content.startswith("!순서"):
        sys_random = random.SystemRandom()
        N1 = message.content.split(" ")
        NT = " "
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            NT = NT+" "+N1[i]
        NT1 = NT.lstrip()
        list = NT1.split()
        fu.lc(list)

        str_list = " ".join(str(l) for l in list)

        result = len(str_list.split())
        result = int(result)


        msg = await message.channel.send("1번: " + list[0])
        time.sleep(1.5)
        
        for i in range(1, result):
            si = i + 1 
            await msg.edit(content=str(si) + "번: " + list[i])
            time.sleep(1.5)
        
        await msg.delete()
        embed = discord.Embed(title ="결과: \n" + str_list, colour = discord.Colour.red())
        await message.channel.send(embed=embed)
        random.seed()

    if message.content.startswith("!수배"):
        user = message.mentions[0].avatar_url_as(size = 128)

        wanted = Image.open("wanted.jpg")
        date = BytesIO(await user.read())
        pfp = Image.open(date)
        
        pfp = pfp.resize((177, 177))

        wanted.paste(pfp, (118, 180))

        wanted.save("profile.jpg")

        await message.channel.send(file = discord.File("profile.jpg"))

    if message.content.startswith("!가입"):
        user_id = str(message.author.id)
        user_name = str(message.author.name)
        user_login_info = ".\\마피아유저전용폴더\\" + user_id 
        if os.path.isdir(user_login_info):
            await message.channel.send("이미 유저가입이 완료되었어요. ~help명령어에 게임을 즐기는 방법이 나와있어요!")
        else:
            fu.login(user_id, user_name)
            await message.channel.send("유저 가입이 완료되었습니다 이제부터 게임을 즐기실수 있어요!")

    if message.content.startswith("!방생성"):
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
        us = message.author.id
        us = str(us)
        user_login_info = ".\\마피아유저전용폴더\\" + us + "\\" + us + "info.txt"
        if os.path.isfile(user_login_info):
            num = 5
            lst = 8
            for x in range(num):
                nsnum = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(lst))

            us = message.author.id
            us = str(us)
            #방 코드디렉토리 파일생성 / 방 데이터 파일 생성 
            fu.createroom(NT2, nsnum, us)

            await message.channel.send("방이 생성되었습니다. [방코드: " + nsnum + "]")
        else: 
            await message.channel.send("가입을 하셔야 게임을 즐길실수있어요 !가입을 통해 유저 가입을 진행해주세요~")

    if message.content.startswith("!방참가"):
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            rcode = NT+" "+N1[i]
        rcode = rcode.lstrip()
        us = message.author.id

        us = str(us)
        roomtf = ".\\마피아전용폴더\\" + rcode
        user = ".\\마피아전용폴더\\" + rcode + "\\" + us +  ".txt"
        user_login_info = ".\\마피아유저전용폴더\\" + us + "\\" + us + "info.txt"
        if os.path.isfile(user_login_info):
            if os.path.isdir(roomtf):
                if os.path.isfile(user):
                    await message.channel.send("이미 참가하셨습니다.")

                else:
                    fu.user_is_joined(us)
                    fu.createuserinfo(us, rcode)
                    await message.channel.send("방에 참가했습니다.")
            else:
                await message.channel.send("방이 존재하지 않습니다. ")
        else:
            await message.channel.send("가입을 하셔야 게임을 즐길실수있어요 !가입을 통해 유저 가입을 진행해주세요~")

    if message.content.startswith("!방시작"):
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            rcode = NT+" "+N1[i]
        rcode = rcode.lstrip()
        roomtf = ".\\마피아전용폴더\\" + rcode
        us = str(message.author.id)
        user_id = us
        data = fu.checkstart(rcode)
        result = fu.check_user_result(rcode)
        result = " ".join(str(r) for r in result)
        result = int(result)
        room_owner = ".\\마피아전용폴더\\"+ rcode + "\\" + us + "owner.txt"
        user_login_info = ".\\마피아유저전용폴더\\" + us + "\\" + us + "info.txt"
        if os.path.isfile(user_login_info):
            if os.path.isdir(roomtf):
                if os.path.isfile(room_owner):
                    if int(data) == 1:
                        await message.channel.send("게임이 이미 시작됬습니다. 게임이 끝난 뒤 다시 참가해주세요")
                    else:
                        if int(result) < 5:
                            await message.channel.send("유저 수가 충족되지 않았습니다 [최소인원: 5]")
                        elif int(result) >= 8:
                            #참가한 유저 목록 
                            userlist = fu.userlist(rcode)
                            users = " ".join(str(u) for u in userlist)
                            userl = users.split()
                            result = len(users.split())
                            result = int(result)
                            us = []
                            
                            for i in range(0, result):
                                userli = userl[i]
                                usdq = fu.listToString(userli)
                                usdq = usdq.replace(" ", "")
                                user = client.get_user(int(usdq))
                                us.append(user)
                            use = " ".join(str(e) for e in us)
                            fu.userjoblistappend(rcode)
                            await message.channel.send("참가한 유저: " + str(use) + "\n게임이 시작되었습니다 지금부터 개인 DM으로 자신의 직업을 배정받습니다.\n랜덤으로 직업을 선택중입니다 시간이 좀 걸릴수있습니다.")
                            
                            #참가한 유저의 유저파일에 참가된 방 코드 입력

                            user_list_rep = []
                            for i in range(0, result):
                                userli = userl[i]
                                usdq = fu.listToString(userli)
                                usdq = usdq.replace(" ", "")
                                user_list_rep.append(usdq)

                            for i in range(0, result):
                                user = user_list_rep[i]
                                users = "".join(str(u) for u in user)
                                users_replace = fu.user_data_file_replace_room(rcode, users)
        

                            #마피아
                            data = fu.choosemafia(rcode)
                            mafia = client.get_user(int(data))
                            await mafia.send("당신은 마피아입니다. !킬 (유저아이디) 를 입력하여 마피아인걸 들키지 않고 모든 시민팀을 죽여 승리하세요!")
                            #마피아 유저 파일에 직업 수정
                            fu.mafia_replace_data(user_id)
                            

                            #마피아
                            data = fu.choosemafia(rcode)
                            mafia = client.get_user(int(data))
                            await mafia.send("당신은 마피아입니다. !킬 (유저아이디) 를 입력하여 마피아인걸 들키지 않고 모든 시민팀을 죽여 승리하세요!")
                            #마피아 유저 파일에 직업 수정
                            fu.mafia_replace_data(user_id)
                            
                            #의사
                            data = fu.choosemafia(rcode)
                            doctor = client.get_user(int(data))
                            await doctor.send("당신은 의사입니다. !치료 (유저아이디) 를 입력하여 마피아에게 죽을거 같은 유저를 살려내며 마피아를 찾아 승리하세요!")
                            #의사 유저 파일에 직업 수정
                            fu.doctor_replace_data(user_id)
                            
                            #경찰 
                            data = fu.choosemafia(rcode)
                            police = client.get_user(int(data))
                            await police.send("당신은 경찰입니다. !조사 (유저아이디) 를 입력하여 유저를 조사하고 마피아를 찾아네 승리하세요!")          
                            #경찰 유저 파일에 직업 수정
                            fu.police_replace_data(user_id)
                            
                            #나머진 시민으로
                            tl = fu.p1_getresult(rcode)
                            tl = tl + 1
                            for t in range(1, tl):
                                data = fu.p2_user(rcode)
                                p = client.get_user(int(data))
                                await p.send("당신은 시민입니다. 최대한 빠르게 경찰을 도와 마피아를 찾아네 승리하세요!")
                            
                        else:
                            
                            fu.gamestart(rcode) #메인 데이터 파일에 게임시작을 1로 바꿈으로써 더이상의 유저가 접속을 못하게함
                            
                            #참가한 유저 목록 
                            userlist = fu.userlist(rcode)
                            users = " ".join(str(u) for u in userlist)
                            userl = users.split()
                            result = len(users.split())
                            result = int(result)
                            us = []
                            
                            for i in range(0, result):
                                userli = userl[i]
                                usdq = fu.listToString(userli)
                                usdq = usdq.replace(" ", "")
                                user = client.get_user(int(usdq))
                                us.append(user)
                            use = " ".join(str(e) for e in us)
                            fu.userjoblistappend(rcode)
                            await message.channel.send("참가한 유저: " + str(use) + "\n게임이 시작되었습니다 지금부터 개인 DM으로 자신의 직업을 배정받습니다.\n랜덤으로 직업을 선택중입니다 시간이 좀 걸릴수있습니다.")
                            
                            #참가한 유저의 유저파일에 참가된 방 코드 입력

                            user_list_rep = []
                            for i in range(0, result):
                                userli = userl[i]
                                usdq = fu.listToString(userli)
                                usdq = usdq.replace(" ", "")
                                user_list_rep.append(usdq)

                            for i in range(0, result):
                                user = user_list_rep[i]
                                users = "".join(str(u) for u in user)
                                users_replace = fu.user_data_file_replace_room(rcode, users)
        

                            #마피아
                            data = fu.choosemafia(rcode)
                            mafia = client.get_user(int(data))
                            await mafia.send("당신은 마피아입니다. !킬 (유저아이디) 를 입력하여 마피아인걸 들키지 않고 모든 시민팀을 죽여 승리하세요!")
                            #마피아 유저 파일에 직업 수정
                            fu.mafia_replace_data(user_id)
                            
                            #의사
                            data = fu.choosemafia(rcode)
                            doctor = client.get_user(int(data))
                            await doctor.send("당신은 의사입니다. !치료 (유저아이디) 를 입력하여 마피아에게 죽을거 같은 유저를 살려내며 마피아를 찾아 승리하세요!")
                            #의사 유저 파일에 직업 수정
                            fu.doctor_replace_data(user_id)
                            
                            #경찰 
                            data = fu.choosemafia(rcode)
                            police = client.get_user(int(data))
                            await police.send("당신은 경찰입니다. !조사 (유저아이디) 를 입력하여 유저를 조사하고 마피아를 찾아네 승리하세요!")          
                            #경찰 유저 파일에 직업 수정
                            fu.police_replace_data(user_id)
                            
                            #나머진 시민으로
                            tl = fu.p1_getresult(rcode)
                            tl = tl + 1
                            for t in range(1, tl):
                                data = fu.p2_user(rcode)
                                p = client.get_user(int(data))
                                await p.send("당신은 시민입니다. 최대한 빠르게 경찰을 도와 마피아를 찾아네 승리하세요!")
                            

                else:
                    await message.channel.send("방장만이 게임을 시작시킬수 있습니다.")
            else:
                await message.channel.send("방이 존재하지 않습니다. ")
        else: 
            await message.channel.send("가입을 하셔야 게임을 즐길실수있어요 !가입을 통해 유저 가입을 진행해주세요~")
            
    if message.content.startswith("!방나가기"):
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            rcode = NT+" "+N1[i]
        rcode = rcode.lstrip()
        us = message.author.id
        us = str(us)
        fu.leave_room(us,rcode)

        await message.channel.send("방을 나갔습니다.")

    if message.content.startswith("!방삭제"):
        #방삭제
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            rcode = NT+" "+N1[i]
        rcode = rcode.lstrip()
        room = ".\\마피아전용폴더\\" + rcode
        if os.path.exists(room):
            shutil.rmtree(room)

    if message.content.startswith("!킬"):#마피아 전용
        user_id = message.author.id 
        us = str(user_id)
        user_login_info = ".\\마피아유저전용폴더\\" + us + "\\" + us + "info.txt"
        checking = fu.check_is_user_joing 
        checking = fu.checkjob(us)
        checking = " ".join(str(e) for e in checking)
        checking = int(checking)        
        if checking == 1:
            if os.path.isfile(user_login_info):
                userjob = fu.checkjob(us)
                userjob = " ".join(str(e) for e in userjob)
                userjob = int(userjob)
                if userjob == 1:
                    await message.channel.send("성공")
                else:
                    await message.channel.send("마피아만이 이명령어를 사용할수 있습니다.")
            else: 
                await message.channel.send("가입을 하셔야 게임을 즐길실수있어요 !가입을 통해 유저 가입을 진행해주세요~")
        else:
            await message.channel.send("게임 시작되지 않았거나 방이 존재하지 않아요")

    if message.content.startswith("!조사"):#경찰 전용
        user_id = message.author.id 
        us = str(user_id)
        user_login_info = ".\\마피아유저전용폴더\\" + us + "\\" + us + "info.txt"
        checking = fu.check_is_user_joing 
        checking = fu.checkjob(us)
        checking = " ".join(str(e) for e in checking)
        checking = int(checking)
        if checking == 1:
            if os.path.isfile(user_login_info):
                userjob = fu.checkjob(us)
                userjob = " ".join(str(e) for e in userjob)
                userjob = int(userjob)
                if userjob == 1:
                    await message.channel.send("성공")
                else:
                    await message.channel.send("경찰만이 이 명령어를 사용할수 있습니다.")
            else: 
                await message.channel.send("가입을 하셔야 게임을 즐길실수있어요 !가입을 통해 유저 가입을 진행해주세요~")
        else:
            await message.channel.send("게임 시작되지 않았거나 방이 존재하지 않아요")

    if message.content.startswith("!치료"):#의사 전용
        user_id = message.author.id 
        us = str(user_id)
        user_login_info = ".\\마피아유저전용폴더\\" + us + "\\" + us + "info.txt"
        checking = fu.check_is_user_joing 
        checking = fu.checkjob(us)
        checking = " ".join(str(e) for e in checking)
        checking = int(checking)
        if checking == 1:
            if os.path.isfile(user_login_info):
                userjob = fu.checkjob(us)
                userjob = " ".join(str(e) for e in userjob)
                userjob = int(userjob)
                if userjob == 1:
                    await message.channel.send("성공")
                else:
                    await message.channel.send("의사만이 이 명령어를 사용할수 있습니다.")
            else: 
                await message.channel.send("가입을 하셔야 게임을 즐길실수있어요 !가입을 통해 유저 가입을 진행해주세요~")
        else:
            await message.channel.send("게임 시작되지 않았거나 방이 존재하지 않아요")
        

    if message.content.startswith("!함수테스트"):
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            rcode = NT+" "+N1[i]
        rcode = rcode.lstrip()
        user_id = str(message.author.id)

        userlist = fu.userlist(rcode)
        users = " ".join(str(u) for u in userlist)
        userl = users.split()
        result = len(users.split())
        result = int(result)


        user_list_rep = []
        for i in range(0, result):
            userli = userl[i]
            usdq = fu.listToString(userli)
            usdq = usdq.replace(" ", "")
            user_list_rep.append(usdq)

        print(user_list_rep)
        print(result)
        for i in range(0, result):
            user = user_list_rep[i]
            users = "".join(str(u) for u in user)
            users_replace = fu.reset_the_game(rcode, users)
        
    if message.content.startswith("!내전참가"):
        user_name = message.author.display_name
        result = fu.choose_team_1()
        if result == 10:
            await message.channel.send("이미 열명 이상입니다.")
        else:
            await message.channel.send("참가하셨습니다.")
            fu.choose_team_0(user_name)

    if message.content.startswith("!팀뽑기"):
        sys_random = random.SystemRandom()
        result = fu.choose_team_1()
        red_team = []
        blue_team = []
        if result > 3:
            await message.channel.send("팀뽑기를 시작합니다.")
            data = fu.choose_team_2()
            fu.lc(data)

            for i in range(0, result):
                if i % 2 != 0: 
                    red_team.append(data[i])
                else: 
                    blue_team.append(data[i])


            red_team = " ".join(str(u) for u in red_team)
            blue_team = " ".join(str(u) for u in blue_team)


            embed = discord.Embed(title ="내전팀 뽑기", colour = discord.Colour.blue()) 
            embed.add_field(name = "내전 레드팀", value= red_team,inline = False)
            embed.add_field(name = "내전 블루팀", value= blue_team ,inline = False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/897120714912583710/935259427085373490/e4e965dfb9366f272ae81eba8364f3af37a55c06.png")
            embed.set_footer(text="팀 배정이 완료되었습니다! 행운을 빕니다 소환사님!")
            await message.channel.send(embed=embed) 

            file = '내전용.txt'
            if os.path.isfile(file):
                os.remove(file)
                
            f = open("내전용.txt", 'w', encoding="UTF-8")
            f.close
        else:
            await message.channel.send("최소 인원 4명이 충족되지 않았습니다.")


    if message.content.startswith("!도배"):
        N1 = message.content.split(" ")
        NT = ""
        vrsize = len(N1)
        vrsize = int(vrsize)
        for i in range(1, vrsize): 
            NT = NT+" "+N1[i]
        NT1 = NT.lstrip()

        for i in range(1, 4):
            await message.channel.send(NT1)
        


client.run(token)
