from calendar import week, weekday
from random import *
import discord 
from discord.ext import commands
import string
from time import *
import asyncio
import os
from discord.ext import commands, tasks
from discord.utils import get
from datetime import datetime, timedelta
from colorama import Fore, Back, Style
import logging
import json

all = string.digits


bot = commands.Bot(command_prefix="!")
bot.remove_command('help')
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="!help for help",description="Created By PolarisWolf"))
    print("Ready !")  





@bot.event
async def on_command_error(ctx, error):
    now = datetime.now()
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply('Commande invalid ou mal ecrite :(')
        await ctx.message.add_reaction('\N{CROSS MARK}')
        
    else:
        raise error





@bot.command()
async def coucou(ctx):
    await ctx.reply("Coucou !")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def annonce(ctx, *text):
    message = " ".join(text)
    messages = f"**======================================**\n\n@everyone **ANNONCES** {message}\n\n**======================================**"
    await ctx.send(messages)

#659807812888690718
#983033394411737098
@bot.event
async def on_reaction_add(reaction, user):
    await reaction.message.add_reaction(reaction.emoji)

@bot.command()
async def info(infos):
    server = infos.guild
    numberoftextchannels = len(server.text_channels)
    numberofvoicechannels = len(server.voice_channels)
    serverdescription = server.description
    numberofperson = server.member_count
    servername = server.name
    emojie = ":red_car:"
    message = f"Le Serveur **{servername}** {emojie} contient **{numberofperson}** personne \n La description du serveur *{serverdescription}* \n ce serveur possède *{numberoftextchannels}* salon textuel ainsi que *{numberofvoicechannels}* vocaux"
    await infos.reply(message)

@bot.command()
async def bonjour(ctx):
    server = ctx.guild
    servername = server.name
    message = f"Bonjour Jeune Hirriens Le Savais tu que le Serveur {servername} \n etait un super serveur car je suis dedans :grin:"
    await ctx.reply(message)

@bot.command()
async def say(ctx, *texte):
    await ctx.send(" ".join(texte))

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, nombre : int):
    messages = await ctx.channel.history(limit = nombre + 1).flatten()
    for message in messages:
        await message.delete()

@bot.command()
@commands.has_permissions(kick_members = True)

async def kick(ctx, user : discord.User,  *,reason="Aucune Raison Donné"):
    if user == None:
        await ctx.send("*Erreur*:**Tu Dois Mettre un Joueur**")
    else:
        
        await ctx.guild.kick(user, reason = reason)
        embed = discord.Embed(title = "**Banissement**", description = "Un modérateur a frappé !", color=0xfa8072)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = "https://discordemoji.com/assets/emoji/BanneHammer.png")
        embed.add_field(name = "Membre Expulsé", value = user.name, inline = True)
        embed.add_field(name = "Raison", value = reason, inline = True)
        embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
      
        await ctx.send(embed = embed)
        server = ctx.guild
        servername = server.name
        await user.send(f"\n\n Tu As été Kick De **{servername}** \n Raison: {reason} \n Par: {ctx.author.name} \n Join: https://discord.gg/mfKSRtVPkS ")
        
	

        

@bot.command()
@commands.has_permissions(ban_members = True)
   
async def ban(ctx, user : discord.User, *, reason = "Aucune raison n'a été donné"):
    if user == None:
        await ctx.send("*Erreur*:**Tu Dois Mettre un Joueur**")
	
    else:
        await ctx.guild.ban(user, reason = reason)
        embed = discord.Embed(title = "**Banissement**", description = "Un modérateur a frappé !", color=0xfa8072)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = "https://discordemoji.com/assets/emoji/BanneHammer.png")
        embed.add_field(name = "Membre banni", value = user.name, inline = True)
        embed.add_field(name = "Raison", value = reason, inline = True)
        embed.add_field(name = "Modérateur", value = ctx.author.name, inline = True)
        await ctx.send(embed = embed)
        server = ctx.guild
        servername = server.name
        await user.send(f"\n\n Tu As été Ban De **{servername}** \n Raison: {reason} \n Par: {ctx.author.name}")
        

        

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user, *reason):

	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
            
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans ")
commandban = "Bannir Un Membre Du Serveur"
@bot.command()
async def help(ctx):
        embed = discord.Embed(title = "**!Help**", description = "Liste Des Commande", color=0xfa8072) 
        embed.set_author(name = "HirraBot", icon_url = "https://ibb.co/FnDshDv")
        embed.add_field(name = "!ban", value = commandban , inline = False)
        embed.add_field(name = "!Kick", value = "Expulser Un Membre Du Serveur", inline = False)
        embed.add_field(name = "!unban", value = "Debannir Un Membre Du Serveur ", inline = False)
        embed.add_field(name = "!say", value = "Envoie Un Message Avec le Bot",inline = False)
        embed.add_field(name = "!clear (number)", value = "Permet D'enlever Un Nombre Spécial de message",inline = False)
        embed.add_field(name = "!mute", value = "Permet De Mettre Le Membre Choisi Muet",inline = False)
        embed.add_field(name = "!unmute", value = "Permet De Rendre La Parole à la personen Chosi",inline = False)
        embed.add_field(name = "!lancer", value = "Lance Des Dé est choisi un nombre aléatoire",inline = False)
        embed.add_field(name = "!genie", value = "Pause Une Question Au Génie",inline = False)
        embed.add_field(name = "!ip", value = "permet de connaitre l'ip de omicraft ",inline = False)
        await ctx.send(embed = embed)
        
async def createMutedRole(ctx):
    mutedRole = await ctx.guild.create_role(name = "Muted",
                                            Permissions = discord.Permissions(
                                                send_messages = False,
                                                speak = False),
                                            reason = "Creation du role Muted pour mute des gens.")
    for channel in ctx.guild.channels:
        await channel.set_permissions(mutedRole, send_messages = False, speak = False)
    return mutedRole

async def getMutedRole(ctx):
    roles = ctx.guild.roles
    for role in roles:
        if role.name == "Muted":
            return role
    
    return await createMutedRole(ctx)

@bot.command()
@commands.has_permissions(mute_members=True)
async def mute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    
    mutedRole = await getMutedRole(ctx)
    await member.add_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été mute !")
    server = ctx.guild
    servername = server.name
    await member.send(f"**==============================**\n\n Tu As été Mute De **{servername}** \n Raison: {reason} \n Par: {ctx.author.name}\n\n **==============================** ")
        

@bot.command()
@commands.has_permissions(mute_members=True)
async def unmute(ctx, member : discord.Member, *, reason = "Aucune raison n'a été renseigné"):
    
    mutedRole = await getMutedRole(ctx)
    
    await member.remove_roles(mutedRole, reason = reason)
    await ctx.send(f"{member.mention} a été unmute !")
    server = ctx.guild
    servername = server.name
    await member.send(f"**==============================**\n\n Tu As été UnMute De **{servername}** \n Raison: {reason} \n Par: {ctx.author.name} \n\n **==============================** ")
        
    

@bot.command()
async def genie(ctx,*text):
    list = ["oui","Non","Je pense que oui", "Je pense que Non","Absolument","Pas Dutout","J'aime Beaucoup l'idée","Je Vais Essayer","C'est Sur","C'est Certain"]
    
    
    await ctx.send(str(" ".join(text)) + "....")
    penser = choice(list)
    sleep(0.6)
    await ctx.send("".join(penser))

@bot.command()
async def lancer(ctx):
    dé = randint(1,6)
    
    await ctx.send("Entre 0 et 6 Je Choisi....")
    sleep(0.8)
    await ctx.send(str(dé))

@bot.command()
async def ip(ctx):
    await ctx.reply("omicraft.mine.fun")


        

bot.run("OTg3NDUwNzI1MTg3NTg4MTM2.GO48g4.nWJNW26Oez6AXEVeWai381NK_9yfOq3_XwXICc")






