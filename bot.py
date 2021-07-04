import discord
from discord.utils import get
from discord.ext import commands
import os

ida = 0

t = True
intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
  print("Bienvenido al bot")
  await bot.change_presence(activity=discord.Game(name="Giving roles"))

@bot.event
async def on_raw_reaction_add(reaction):
    global ida
    msg = "858061816310792262"
    id = str(reaction.message_id)
    guild = bot.get_guild(855846757203443713)
    print(guild)
    try:
        usuario = guild.get_member(int(reaction.user_id))
    except Exception:
        pass


    if msg == id or ida:
        print("si")
        reaccion = str(reaction.emoji)
        print(reaccion)
        if "<:assettoicon:856622922453614612>" == reaccion:
            print("si")
            
            role = discord.utils.get(guild.roles, id=858064599243554826)
            await usuario.add_roles(role)
        elif "<:acc:858073968379428868>" == reaccion:
            print("si2")
            
            role = discord.utils.get(guild.roles, id=858074298153304064)
            await usuario.add_roles(role)
        elif "<:f1icon:856622870359703582>" == reaccion:
            print("si2")
            
            role = discord.utils.get(guild.roles, id=858074668606423120)
            await usuario.add_roles(role)
        elif "<:f2icon:856622883110518784>" == reaccion:
            print("si2")
            
            role = discord.utils.get(guild.roles, id=858075262410555442)
            await usuario.add_roles(role)

@bot.event
async def on_member_join(member):
    global ida
    if member.dm_channel == None:
        await member.create_dm()
    message = await member.dm_channel.send("React to get a role!")
    ida = message.id
    await message.add_reaction("<:f2icon:856622883110518784>")
    await message.add_reaction("<:f1icon:856622870359703582>")
    await message.add_reaction("<:acc:858073968379428868>")
    await message.add_reaction("<:assettoicon:856622922453614612>")
    return ida

@bot.event
async def on_message(message):
    global ida
    
    if message.content == "!role":


        if message.author.dm_channel == None:
            await message.author.create_dm()
        message = await message.author.dm_channel.send("React to get a role!")
        ida = message.id
        await message.add_reaction("<:f2icon:856622883110518784>")
        await message.add_reaction("<:f1icon:856622870359703582>")
        await message.add_reaction("<:acc:858073968379428868>")
        await message.add_reaction("<:assettoicon:856622922453614612>")
        return ida
        






bot.run("ODU4MDY1MjY2NTQ0ODY5Mzg2.YNYtjQ.4OYE5U1WrPyPO-YaMS6At6FPS8M")