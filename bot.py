import discord
from discord.utils import get
from discord.ext import commands
import os

t = True
intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix='!', intents=intents)
ida = 0


@bot.event
async def on_ready():   #What the bot does when it starts up
  print("Ready")
  await bot.change_presence(activity=discord.Game(name="Giving roles")) #He is permaplaying "giving roles with this"

@bot.event
async def on_raw_reaction_add(reaction): #When someone reacts to some message this triggers
    global ida
    msg = "858061816310792262" #id of the message meant for react
    id = str(reaction.message_id) #converts the id of the message who triggered this in a string
    guild = bot.get_guild(855846757203443713) #know the id of the server
    usuario = guild.get_member(int(reaction.user_id)) #know the id of who reacted


    if msg == id or ida: #if the id of the message who triggered this is the same of the message meant to be reacted
        print("si") #comprobation
        reaccion = str(reaction.emoji) #know the id of the reacion
        print(reaccion)
        if "<:assettoicon:856622922453614612>" == reaccion: #if the id of the reaction mathches the id of the reaction meant for this triggers
            print("si")
            
            role = discord.utils.get(guild.roles, id=858064599243554826) #know the id of the role wanted
            await usuario.add_roles(role) #give the role to the user who reacted
        elif "<:acc:858073968379428868>" == reaccion:
            print("si2")
            
            role = discord.utils.get(guild.roles, id=858074298153304064)
            await usuario.add_roles(role)
        elif "<:f1icon:856622870359703582>" == reaccion:
            print("si3")
            
            role = discord.utils.get(guild.roles, id=858074668606423120)
            await usuario.add_roles(role)
        elif "<:f2icon:856622883110518784>" == reaccion:
            print("si3")
            
            role = discord.utils.get(guild.roles, id=858075262410555442)
            await usuario.add_roles(role)


@bot.event
async def on_member_join(member): #when someone joins a server this triggers
    global ida
    if member.dm_channel == None: #if the user hasn't a dm channel with the bot creates it
        await member.create_dm()
    message = await member.dm_channel.send("React to get a role!") #the bot sends a dm to the person who joined
    ida = message.id #saves the id of the message
    await message.add_reaction("<:f2icon:856622883110518784>") #reacts to the message with the logos of the different roles
    await message.add_reaction("<:f1icon:856622870359703582>")
    await message.add_reaction("<:acc:858073968379428868>")
    await message.add_reaction("<:assettoicon:856622922453614612>")
    return ida


@bot.event
async def on_message(message): #when someone sends a message this triggers
    global ida
    
    if message.content == "!role": #if the message is !role this triggers


        if message.author.dm_channel == None: #if the user hasn't a dm channel with the bot creates it
            await message.author.create_dm()
        message = await message.author.dm_channel.send("React to get a role!") #the bot sends a dm to the person who sent the message
        ida = message.id #saves the id of the message
        await message.add_reaction("<:f2icon:856622883110518784>") #reacts to the message with the logos of the different roles
        await message.add_reaction("<:f1icon:856622870359703582>")
        await message.add_reaction("<:acc:858073968379428868>")
        await message.add_reaction("<:assettoicon:856622922453614612>")
        return ida
        



bot.run("TOKEN") 