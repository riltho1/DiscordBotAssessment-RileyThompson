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
    self.attack_value = P_attack
    #self.s_attack= P_s_attack leaving for later
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

def user_attack():
  damage = random.randint(1,5)
  #print(damage)
  if damage == 1:
    P_attack = 0
  elif damage == 2:
    P_attack = 5
  elif damage == 3:
    P_attack = 10
  else:
    P_attack = 20
  print(P_attack)
  Player.attack_value = P_attack
  return P_attack

user = Player(user_attack(), 40, 75, 100, 15, "Phillip")

#Enemy class containing enemy stats
class Enemy:
  def __init__(self, E_attack, E_s_attack, E_hp, E_max_hp, E_heal, E_Name):
#Giving variables for stats
    self.attack_value = E_attack
    #self.s_attack = E_s_attack
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

#Randomised attac value
def enemy_attack():
  damage = random.randint(1,5)
  if damage == 1:
    E_attack = 4
  elif damage == 2:
    E_attack = 6
  elif damage == 3:
    E_attack = 8
  else:
    E_attack = 10
  print(E_attack)
  Enemy.attack_value = E_attack
  return E_attack
    
enemy = Enemy(enemy_attack(), 50, 75, 90, 15, "Zombie")

#Commands
@client.command(name = "start")
async def start(ctx):
  await ctx.channel.send(f"You encounter a {enemy.get_name()}, what will you do (Attack) (Heal)")

@client.command (name = "stats")
async def stats(ctx):
  await ctx.channel.send(f"{user.get_name()} has {user.get_hp()} hp out of {user.get_max_hp()} hp")
  
@client.command (name = "attack")
async def attack(ctx):
  #Generates attack values
  user_attack_value = user_attack()
  #enemy_attack_value = enemy_attack()
  #Asigns the value of the user to a damage variable
  damage = user_attack_value

  #Enemys HP calculation
  enemy_hp = enemy.get_hp()
  enemy_hp -= damage
  enemy_hp = max(0, enemy_hp)
  enemy.hp = enemy_hp

  await ctx.channel.send(f"{user.get_name()} attacks {enemy.get_name()} for {damage} damage {enemy.get_name()} has {enemy_hp} HP left.")


  
client.run(TOKEN)