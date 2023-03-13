import os
import discord
import random
from discord.ext import commands

TOKEN = os.environ['TOKEN']#Importing token for bot to run script
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = "!", intents = intents)

name = "Bob"
hp = 20
max_hp = hp + 15
attack = 10 
defense = 15



@client.event
async def on_ready():
  print(f"{client.user} has connected to discord")

#This was copied from previous template and wasn't needed
"""
class rng:
  def __init__(self):
    self.secret_number = random.randint(0,10)

  def reset(self):
    self.secret_number = random.randint(0,10)
"""

class Stats():
  def __init__(self,name,hp,max_hp,attack,defense): #Defining variables
    self.name = name
    self.hp = hp
    self.max_hp = max_hp
    self.attack = attack
    self.defense = defense

  def user_attack(self,name,hp,max_hp,attack,defense):
    damage = random.randint(1,10)
    print(damage)

#This seems a bit complex and unnessasary so I have decided to make it simpler above
'''
  def fight(self,other):
    defense = min(other.defense, 19) #Gives maximum defense cap
    hit_chance = random.randint(0,20 - defense)
    if hit_chance:
      damage = self.attack
    else:
      damage = 0

    other.hp -= damage
    return (self.attack, other.hp <= 0) #Damage, fatal
'''
class Character(Stats):# Users stats
  def __init__(self, name, hp, max_hp, attack, defense):
    super().__init__(name, hp, max_hp, attack, defense)

class Enemy(Stats):#Enemy stats
    def __init__(self, name, hp, max_hp, attack, defense):
      super().__init__(name, max_hp, attack, defense)

#Enemies
class Zombie(Enemy):
  def __init__(self):
    super().__init__("Zombie",20,5,7)
  

s = Stats("Zombie", 20, 5, 7, 10)

#Trying to test the user_attack function (errors)
'''
@client.command (name = "stats")
async def stats(ctx,str):
  if str(str) == s.user_attack:
    await ctx.channel.send(Stats)
'''
client.run(TOKEN)