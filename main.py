import os
import discord
import random
from discord.ext import commands

TOKEN = os.environ['TOKEN']#Importing token for bot to run script
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = "!", intents = intents)

@client.event
async def on_ready():
  print(f"{client.user} has connected to discord")

#User class containing player stats
class Player:
  def __init__(self, P_attack, P_s_attack, P_hp, P_max_hp, P_heal, P_Name):
    
#Giving variables for stats
    self.attack = P_attack
    self.s_attack= P_s_attack
    self.hp = P_hp
    self.max_hp = P_max_hp
    self.heal = P_heal
    self.name = P_Name

  #Assinging the variables to User functions
  def get_attack(self):
    return self.attack

  def get_hp(self):
    return self.hp

  def get_max_hp(self):
    return self.max_hp

  def get_heal(self):
    return self.heal

  def get_name(self):
    return self.name

user = Player(20, 40, 75, 100, 15, "Phillip")

#Enemy class containing enemy stats
class Enemy:
  def __init__(self, E_attack, E_s_attack, E_hp, E_max_hp, E_heal, E_Name):
#Giving variables for stats
    self.attack = E_attack
    self.s_attack = E_s_attack
    self.hp = E_hp
    self.max_hp = E_max_hp
    self.heal = E_heal
    self.name = E_Name

#Asigning the variables to Enemy functions
  def get_attack(self):
    return self.attack

  def get_hp(self):
    return self.hp

  def get_max_hp(self):
    return self.max_hp

  def get_heal(self):
    return self.heal

  def get_name(self):
    return self.name
    
enemy = Enemy(15, 50, 75, 90, 15, "Zombie")

#Commands
#In progress
@client.command(name = "start")
async def start(ctx):
  await ctx.channel.send

@client.command (name = "stats")
async def stats(ctx):
  await ctx.channel.send(f"{user.get_name()} has {user.get_hp()} hp out of {user.get_max_hp()} hp")
  await ctx.channel.send(f"{user.get_name()} has an attack force of {user.get_attack()}")

#In progress
@client.command (name = "attack")
async def attack(ctx):
  

client.run(TOKEN)