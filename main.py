import os
import discord
import random
from discord.ext import commands

TOKEN = os.environ['TOKEN']#Importing token for bot to run script
intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = "!", intents = intents)

user_hp = 20
basic_attack = 10 

@client.event
async def on_ready():
  print(f"{client.user} has connected to discord")

class Stats:
  def __init__(self,name,hp,max_hp,attack,defense): #Defining variables
    self.name = name
    self.hp = hp
    self.max_hp = max_hp
    self.attack = attack
    self.defense = defense

  def fight(self,other):
    defense = min(other.defense, 19) #Gives maximum defense cap
    hit_chance = random.randint(0,20 - defense)
    if hit_chance:
      damage = self.attack
    else:
      damage = 0

    other.hp -= damage
    return (self.attack, other.hp <= 0) #Damage, fatal

  class Enemy(Stats):
    def __init__(self,name,hp,max_hp,attack,defense):
      super().__init__(self,name,hp,max_hp,attack,defense)
      
    

client.run(TOKEN)