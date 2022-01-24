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

def choose_team(user_id, user_name):
    
    user_info = "내전용.txt"
    
    f = open(user_info, 'a', encoding="UTF-8")
    f.write(str(user_name) + "\n")
    f.close()
    return  