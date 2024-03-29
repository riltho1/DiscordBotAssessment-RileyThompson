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
  channel = client.get_channel(1082070053299683440)
  await channel.send(f"You encounter a {enemy.get_name()}, what will you do (Attack) (Heal) (Type !help for more information)")

#User class containing player stats
class Player:
  def __init__(self, P_attack, P_hp, P_max_hp, P_heal, P_Name):
    
#Giving variables for stats
    self.attack_value = P_attack
    self.hp = P_hp
    self.max_hp = P_max_hp
    self.heal = P_heal
    self.name = P_Name
#This is so the every time the user attacks the count increases until it is above the required number
    self.heal_count = 0

  #Assinging the variables to User functions
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

#Creates random hp value for the user to heal by if they input heal between the values 

def user_heal():
  heal_value = random.randint(5,10)
  return heal_value

#User profile
user = Player(user_attack(), 75, 100, 15, "Phillip")

#Enemy class containing enemy stats
class Enemy:
  def __init__(self, E_attack, E_hp, E_max_hp, E_heal, E_Name):
#Giving variables for stats
    self.attack_value = E_attack
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

#Enemy profile
enemy = Enemy(enemy_attack(), 75, 90, 15, "Zombie")

def reset_game(): #Resets the hp of the user and enemy to default amount when called
  user.hp = 75
  enemy.hp = 75
  return user.hp, enemy.hp

#Commands
@client.command(name = "stats")
async def stats(ctx):
  """
  
  Shows the user how much hp the user has
  """
  await ctx.channel.send(f"{user.get_name()} has {user.get_hp()} hp out of {user.get_max_hp()} hp")

@client.command(name = "heal")
async def heal(ctx):
  """

  Allows the user to heal every 3 attacks
  Enemy will not attack you during this time
  """
  #Checks is user is able to heal yet
  if user.heal_count < 3:
    await ctx.channel.send(f"You are not able heal yet try again in {3 - user.heal_count} turns.")
  #Shows heal_count in the console
    print(f"User heal count: {user.heal_count}")
    return
  else:
    user.heal_count = 0
    print(f"User heal count: {user.heal_count}")

  #Health added to user hp
  heal_value = user_heal()
  user_hp = user.get_hp()
  user_hp += heal_value
  
  #This makes it so the the players health cannot exceed the maximum
  if user_hp > user.get_max_hp():
    user_hp = user.get_max_hp()

  #Updates attribute in class
  user.hp = user_hp
  user.heal_count += 1

  
  await ctx.channel.send(f"{user.get_name()} healed for {heal_value} HP and now has {user_hp} HP")
  #Reset to 0 after a succesful heal
  user.heal_count = 0
  
@client.command(name = "attack")
async def attack(ctx):
  """
  
  Allows the user to attack the enemy zombie
  The zombie will attack you back
  """
  #Generates attack values
  user_attack_value = user_attack()
  #Asigns the value of the user to a damage variable
  user_damage = user_attack_value
  #Enemy attack value
  enemy_attack_value = enemy_attack()
  enemy_damage = enemy_attack_value

  #Enemys HP calculation
  enemy_hp = enemy.get_hp()
  enemy_hp -= user_damage
  enemy.hp = enemy_hp
  #Users hp calculation
  user_hp = user.get_hp()
  user_hp -= enemy_damage
  user.hp = user_hp

  #Prints how much damage is done by either user or enemy and shows their current hp
  if user.get_hp() > 0 and enemy.get_hp() > 0:
    await ctx.channel.send(f"{user.get_name()} attacks {enemy.get_name()} for {user_damage} damage, {enemy.get_name()} has {enemy_hp} HP left.")
    await ctx.channel.send(f"{enemy.get_name()} attacks you back for {user.get_name()} for {enemy_damage} damage, {user.get_name()} now has {user_hp} HP remaining.")
    user.heal_count += 1
    
  #This causes the game to reset after either the user or enemy dies
  if enemy_hp <= 0:
    await ctx.channel.send(f"{enemy.get_name()} has been eliminated, {user.get_name()} wins.")
    await ctx.channel.send("Restarting the game...")
    await ctx.channel.send(f"You encounter a {enemy.get_name()}, what will you do (Attack) (Heal) (Type !help for more information)")
    user.heal_count = 0
    reset_game()
    return
  elif user_hp <= 0:
    await ctx.channel.send(f"{user.get_name()} has been defeated by the {enemy.get_name()}, Game over!")
    await ctx.channel.send("Restarting the game...")
    await ctx.channel.send(f"You encounter a {enemy.get_name()}, what will you do (Attack) (Heal) (Type !help for more information)")
    user.heal_count = 0
    reset_game()
    return

client.run(TOKEN)