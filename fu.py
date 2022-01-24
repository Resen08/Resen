from asyncore import read
import discord
import asyncio
import random
from discord import Member
from discord.ext import commands
from discord.flags import MessageFlags
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
import string
import linecache
from discord.ext import tasks
from typing import Awaitable

intents = discord.Intents.default()
intents.members = True
client = discord.Client(command_prefix=',', intents = intents)

def add(a, b): 
    return a + b

def sub(a, b):
    return a - b

def lc(list):
    random.shuffle(list) 
    return

def login(user_id, user_name):
    #유저아이디로된 디렉토리 생성
    path = '.\\마피아유저전용폴더\\' + user_id
    os.makedirs(path)

    user_info = ".\\마피아유저전용폴더\\" + user_id + "\\" + user_id + "info.txt"
    
    username = user_name
    joined_room = "플레이중인방: 없음" #접속중인 유저의 서버 코드 
    user_job = "유저직업: 0"#게임에서의 유저 직업 기본 설정은 시민 게임 시작시 직업이 변경되면 시민도 자신의 직업으로 변경
    user_title = "유저칭호: "#아직 개발예정
    user_is_joing = "접속여부: 0"
    f = open(user_info, 'w', encoding="UTF-8")
    f.write(str(username) + '\n' + str(joined_room) + '\n' + str(user_job) + "\n" + str(user_title) + "\n" + user_is_joing + "\n")
    f.close()
    return  

def createroom(NT2, nsnum, us):

    #방 디렉토리 생성
    path = '.\\마피아전용폴더\\' + nsnum
    os.makedirs(path)
    
    #방 데이터 파일 생성 

    rname = NT2 #방이름
    rcode = "방코드: " + nsnum #방코드: 
    rstart = "게임시작: 0" # 게임시작:
    rday = "날짜: 0" # 날짜:
    rtime = "시간: 0" # 시간: 
    ruserc = "유저수: 0" # 유저수:
    sr = "줄: 9" # 줄: (데이터 목록 줄수 확인)
    dieuser = "죽은유저: 0" # 무덤:
    user = "users:"# 유저 목록:
    # (유저이름):(유저이름으로 된 데이터파일을 또 생성 이곳엔 직업및 사망여부가 작성됨)

    room = ".\\마피아전용폴더\\" + nsnum + '\\' + nsnum + ".txt"
    roomdate = open(room, 'w', encoding="UTF-8")
    roomdate.write(rname +"\n" + rcode + "\n" + rstart + "\n"+ rday +"\n" + rtime + "\n" + ruserc + "\n" + sr + "\n" + dieuser + "\n" + user + "\n")
    roomdate.close() 

    user_list = ".\\마피아전용폴더\\" + nsnum + "\\" + nsnum + "user.txt"
    roomdate = open(user_list, 'w', encoding="UTF-8")
    roomdate.close() 

    room_owner = ".\\마피아전용폴더\\"+ nsnum + "\\" + us + "owner.txt"
    roomdate = open(room_owner, 'w', encoding="UTF-8")
    roomdate.close()
    return


def createuserinfo(us, rcode):

    #방 데이터 파일에 유저 이름 생성 및 멤버 카운트 증가
    user_info = ".\\마피아유저전용폴더\\" + us + "\\" + us + "info.txt"
    room = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + ".txt"

    roomdate = open(room, 'a', encoding="UTF-8")
    roomdate.write(str(us) + "\n")
    roomdate.close() 

    with open(room, 'r', encoding='utf-8') as f:
        tl = sum(1 for line in f)
    
    tlt = int(tl) - 9

    with open(room, 'r+', encoding="UTF-8") as f:          
        lines = []

        new_line = '유저수: ' + str(tlt) + "\n"
        for line in f:
            if(line.startswith('유저수:')):     
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                     
        f.writelines(lines)                          
        f.close()                                  


    with open(room, 'r+', encoding="UTF-8") as f:            
        lines = []

        new_line = '줄: ' + str(tl) + "\n"
        for line in f:
            if(line.startswith('줄:')):    
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                   
        f.writelines(lines)                        
        f.close()                                  


    #유저 데이터 파일 수정 유저가 참여중인 방 코드 입력 
    with open(user_info, 'r+', encoding="UTF-8") as f:            
        lines = []

        new_line = '방코드: ' + rcode
        for line in f:
            if(line.startswith('방코드:')):    
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                   
        f.writelines(lines)                        
        f.close()       

    user = ".\\마피아전용폴더\\" + rcode + "\\" + str(us) +  ".txt"      
    roomdate = open(user, 'w', encoding="UTF-8")
    roomdate.close()
    return

def gamestart(rcode):

    room = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + ".txt"

    with open(room, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = '게임시작: 1\n'
        for line in f:
            if(line.startswith('게임시작: ')):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         

    return  

def userlist(rcode):
    room = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + ".txt"        
    with open(room,encoding='UTF8') as f:
        list = []
        tl = sum(1 for line in f)
        tl = tl + 1

        for i in range(10, tl):
            data = linecache.getline(room, i).strip()
            list.append(data)

    return list

def listToString(userli):
    result = ""
    for s in userli:
        result += s + " "
    return result.strip()

def checkstart(rcode):
    room = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + ".txt"        
    with open(room,encoding='UTF8') as f:
        data = f.readlines()[2]
        data = data.replace("게임시작: ", "")
        data = data.replace(" ", "")
    return data

def check_user_result(rcode):
    room = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + ".txt"        
    with open(room,encoding='UTF8') as f:
        result = f.readlines()[5]
        result = result.replace("유저수: ", "")
        result = result.replace(" ", "")
    return result

def userjoblistappend(rcode):
    room = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + ".txt"   
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"             
    with open(room,encoding='UTF8') as f:
        list = []
        tl = sum(1 for line in f)
        tl = tl + 1

        for i in range(10, tl):
            data = linecache.getline(room, i).strip()
            userjob = open(user_list, 'a', encoding="UTF-8")
            userjob.write(data + "\n")
            userjob.close() 

    return


def leave_room(us, rcode):
    user = ".\\마피아전용폴더\\" + rcode + '\\' + us + ".txt" 
    finduser = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + ".txt"   

    #참가된 유저 기록 지우기
    with open(finduser, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = ''
        for line in f:
            if(line.startswith(us)):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         

    #유저 파일 지우기   
    if os.path.isfile(user):
        os.remove(user)

    return 

def replace_in_file(file_path, old_str, new_str):
    # 파일 읽어들이기
    fr = open(file_path, 'r',encoding='UTF8')
    lines = fr.readlines()
    fr.close()
    
    # old_str -> new_str 치환
    fw = open(file_path, 'w',encoding='UTF8')
    for line in lines:
        fw.write(line.replace(old_str, new_str))
    fw.close()
    return

def del_user(user_list, data):
    with open(user_list, "r",encoding='UTF8') as f: 
        lines = f.readlines() 
    with open(user_list, "w",encoding='UTF8') as f: 
        for line in lines: 
            if line.strip("\n") != data: # <= 이 문자열만 골라서 삭제 
                f.write(line)

def choosemafia(rcode):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = int(tl)
    i = random.randint(1, tl)
    data = linecache.getline(user_list, tl).strip()#정확한 파일 줄을 읽어줌 0부터 시작안함
    f.close()
    del_user(user_list, data)

    return data

def choosedoctor(rcode):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = int(tl)
    i = random.randint(1, tl)
    data = linecache.getline(user_list, tl).strip()#정확한 파일 줄을 읽어줌 0부터 시작안함
    f.close()
    del_user(user_list, data)

    return data


def choosepolice(rcode):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = int(tl)
    i = random.randint(1, tl)
    data = linecache.getline(user_list, tl).strip()#정확한 파일 줄을 읽어줌 0부터 시작안함
    f.close()
    del_user(user_list, data)

    return data

def p1_getresult(rcode):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = int(tl)

    return tl

def p2_user(rcode):
    user_list = ".\\마피아전용폴더\\" + rcode + '\\' + rcode + "user.txt"
    with open(user_list,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = int(tl)
    data = linecache.getline(user_list, tl).strip()#정확한 파일 줄을 읽어줌 파일 줄은 0부터 시작안함 
    f.close()
    del_user(user_list, data)

    return data

#직업 수정
def mafia_replace_data(user_id):#마피아 직업번호 1

    room = ".\\마피아유저전용폴더\\" + user_id + '\\' + user_id + "info.txt"

    with open(room, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = '유저직업: 1'
        for line in f:
            if(line.startswith('유저직업: ')):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         

    return  

def doctor_replace_data(user_id):#의사 직업번호 3

    room = ".\\마피아유저전용폴더\\" + user_id + '\\' + user_id + "info.txt"

    with open(room, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = '유저직업: 2'
        for line in f:
            if(line.startswith('유저직업: ')):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         

    return  

def police_replace_data(user_id):#경찰 직업번호 2

    room = ".\\마피아유저전용폴더\\" + user_id + '\\' + user_id + "info.txt"

    with open(room, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = '유저직업: 3'
        for line in f:
            if(line.startswith('유저직업: ')):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         

    return  

def check_is_user_joing(us):
    user = ".\\마피아전용폴더\\" + us + '\\' + us + "info.txt"        
    with open(user,encoding='UTF8') as f:
        userjob = f.readlines()[2]
        userjob = userjob.replace("접속여부: ", "")
        userjob = userjob.replace(" ", "")

    return

def checkjob(us):
    
    user = ".\\마피아유저전용폴더\\" + us + '\\' + us + "info.txt"        
    with open(user,encoding='UTF8') as f:
        userjob = f.readlines()[2]
        userjob = userjob.replace("유저직업: ", "")
        userjob = userjob.replace(" ", "")

    return userjob

def user_is_joined(us):
    user = ".\\마피아유저전용폴더\\" + us + '\\' + us + "info.txt"

    with open(user, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = '접속여부: 1'
        for line in f:
            if(line.startswith('접속여부: ')):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         

    return  

def user_data_file_replace_room(rcode, user_id):
    user = ".\\마피아유저전용폴더\\" + user_id + '\\' + user_id + "info.txt"

    with open(user, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = '플레이중인방: ' + rcode + '\n'
        for line in f:
            if(line.startswith('플레이중인방: 없음')):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         

    return

def reset_the_game(rcode, user_id):
    user = ".\\마피아유저전용폴더\\" + user_id + '\\' + user_id + "info.txt"

    with open(user, 'r+', encoding="UTF-8") as f:              
        lines = []

        new_line = '플레이중인방: 없음 \n'
        for line in f:
            if(line.startswith('플레이중인방: ')):      
                lines = lines + [new_line]
            else:
                lines = lines + [line]
        f.seek(0)                                    
        f.writelines(lines)                          
        f.close()         

    return

def choose_team_0(user_name):
    
    user_file = "내전용.txt"
    
    f = open(user_file, 'a', encoding="UTF-8")
    f.write(str(user_name) + "\n")
    f.close()
    return  

def choose_team_1():
    
    user_file = "내전용.txt"

    with open(user_file,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = int(tl)


    return tl

def choose_team_2():
    user_file = "내전용.txt"
    ul = []
    with open(user_file,encoding='UTF8') as f:
        tl = sum(1 for line in f)
        tl = int(tl)
        tl = tl + 1

    for i in range(1, tl):
        data = linecache.getline(user_file, i).strip()#정확한 파일 줄을 읽어줌 파일 줄은 0부터 시작안함 
        ul.append(data)


    return ul

# def end_choose_team():
    