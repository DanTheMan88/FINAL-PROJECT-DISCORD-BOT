import discord
import os
import requests
import json
import random


client = discord.Client()


def get_truth():
    file = open("truth","r")
    file = file.readlines()
    randnum = random.randrange(1,85)
    return file[randnum]

def get_dare():
    file = open("dare","r")
    file = file.readlines()
    randnum = random.randrange(1,101)
    return file[randnum]

def get_inspiration():
    file = open("inspiration","r")
    file = file.readlines()
    randnum = random.randrange(1,92)
    return file[randnum]



@client.event


async def on_ready():
  print("we have logged in as {0.user}".format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!truth'):
        truthquote = get_truth()
        await message.channel.send(truthquote)
    if message.content.startswith('!dare'):
        darequote = get_dare()
        await message.channel.send(darequote)
    if message.content.startswith('!inspiration'):
        inspiration = get_inspiration()
        await message.channel.send(inspiration)
    




client.run('OTY3NTIwMDQ3MDA4NDU2NzY0.YmRfQg.oC8AQZZ7xzDucmequ3n02sp-dQM')










