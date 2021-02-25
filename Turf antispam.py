import requests, time, json, string, random, asyncio, discord, os, colorama
from bs4 import BeautifulSoup
from itertools import cycle
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from discord.ext import commands

client = commands.Bot(command_prefix=">", case_insensitive=True)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Prefix: >'))


## - vv Moderation Commands vv  - ##

@client.command()
@commands.has_permissions(administrator=True)
async def nuke(ctx, channel: discord.TextChannel = None):
    channel = channel if channel else ctx.channel
    await ctx.send(f"Nuking #{channel}...")
    newchannel = await channel.clone()
    await newchannel.edit(position=channel.position)
    await channel.delete()
    embed=discord.Embed

@client.command()
async def mute(ctx, member : discord.Member):
    embed=discord.Embed(title="**Turf Antispam | Mute**", description=f"{member.mention} Hes been muted!", color=0x40f181)
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await ctx.send(embed=embed)
    await member.add_roles(role)

@client.command()
async def purge(ctx, amount):
    if not amount.isdigit():
        await ctx.send("Please follow format: `>clear {amount}`")
        return
    if not ctx.author.guild_permissions.manage_messages:
        await ctx.send("You do not have the permissions to use this command.")
        return
    await ctx.channel.purge(limit = int(amount) + 1)
    embed=discord.Embed(colour=discord.Colour(0x40f181), title=f"Purged {amount} messages")
    embed.set_thumbnail(url=client.user.avatar_url)
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    embed=discord.Embed(colour=discord.Colour(0x40f181), description=f"**{member} was banned!**")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    embed=discord.Embed(colour=discord.Colour(0x40f181), description=f"**{member} was kicked!**")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(administrator = True)
async def addrole(ctx, member : discord.Member, role : discord.Role):
    await member.add_roles(role)

@client.command()
@commands.has_permissions(administrator = True)
async def removerole(ctx, member : discord.Member, role : discord.Role):
    await member.remove_roles(role)


## - ^^ Moderation Commands ^^  - ##

## - vv Furry fucking niggers Commands vv - ##

@client.command()
async def cat(ctx):
	r = requests.get("https://aws.random.cat/meow")
	res = r.json()
	em = discord.Embed(colour=discord.Colour(0x40f181))
	em.set_image(url=res['file'])
	await ctx.send(embed=em) 

@client.command()
async def dog(ctx):
	r = requests.get("https://random.dog/woof.json")
	res = r.json()
	em = discord.Embed(colour=discord.Colour(0x40f181))
	em.set_image(url=res['url'])
	await ctx.send(embed=em)

@client.command()
async def fox(ctx):
	r = requests.get("https://randomfox.ca/floof")
	res = r.json()
	em = discord.Embed(colour=discord.Colour(0x40f181))
	em.set_image(url=res['image'])
	await ctx.send(embed=em)



## NSFW niggers

@client.command()
@commands.is_nsfw()
async def pussy(ctx):
	r = requests.get("https://nekos.life/api/v2/img/pussy")
	res = r.json()
	em = discord.Embed()
	em.set_image(url=res['url'])
	await ctx.send(embed=em)

@client.command()
@commands.is_nsfw()
async def anal(ctx):
	r = requests.get("https://nekos.life/api/v2/img/anal")
	res = r.json()
	em = discord.Embed()   
	em.set_image(url=res['url'])
	await ctx.send(embed=em)

@client.command()
@commands.is_nsfw()
async def feet(ctx):
	r = requests.get("https://nekos.life/api/v2/img/feetg")
	res = r.json()
	em = discord.Embed()
	em.set_image(url=res['url'])
	await ctx.send(embed=em)

@client.command()
@commands.is_nsfw()
async def hentai(ctx):
	r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
	res = r.json()
	em = discord.Embed()
	em.set_image(url=res['url'])
	await ctx.send(embed=em)   

@client.command()
@commands.is_nsfw()
async def boobs(ctx):
	r = requests.get("https://nekos.life/api/v2/img/boobs")
	res = r.json()
	em = discord.Embed()
	em.set_image(url=res['url'])
	await ctx.send(embed=em)

@client.command()
@commands.is_nsfw()
async def tits(ctx):
	r = requests.get("https://nekos.life/api/v2/img/tits")
	res = r.json()
	em = discord.Embed()	
	em.set_image(url=res['url'])
	await ctx.send(embed=em)

@client.command()
@commands.is_nsfw()
async def blowjob(ctx):
	r = requests.get("https://nekos.life/api/v2/img/blowjob")
	res = r.json()
	em = discord.Embed()
	em.set_image(url=res['url'])
	await ctx.send(embed=em)

@client.command()
@commands.is_nsfw()
async def lewdneko(ctx):
	r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
	res = r.json()
	em = discord.Embed()
	em.set_image(url=res['url'])
	await ctx.send(embed=em)   

@client.command()
@commands.is_nsfw()
async def lesbian(ctx):
	r = requests.get("https://nekos.life/api/v2/img/les")
	res = r.json()
	em = discord.Embed()
	em.set_image(url=res['url'])
	await ctx.send(embed=em)

@client.command()
async def avatar(ctx, user: discord.User):
	x = user.avatar_url
	embed = discord.Embed(colour=discord.Colour(0x40f181))
	embed.set_image(url=x)
	try:
		await ctx.send(embed=embed)
	except:
		await ctx.send(f"||{x}||")
		
@client.command()
async def servercount(ctx):
    embed = discord.Embed(colour=discord.Colour(0x40f181), title="Turf Antispam | Server Count", description=f"Turf Antispam is currently in {(len(client.guilds))} servers!")

    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
	embed = discord.Embed(colour=discord.Colour(0x40f181), title="Turf Antispam | Help Command", description="\n**Moderation**\n`nuke - deletes and recreates the channel`\n`mute <user> - mutes the user pinged`\n`purge <number amount> - deletes a amount of messages`\n`ban <user> - bans the user pinged`\n`kick <user> - kicks the user pinged`\n`addrole <user> <role> - adds the role to the user`\n`removerole <user> <role> - removes the role to the user`\n\n**Animals**\n`cat - shows cute kitty!`\n`dog - shows cute puppy!`\n`fox - shows cute fox!`\n\n**NSFW (nsfw enabled channels only)**\n`pussy - prints a anime pussy`\n`anal - shows anime anal`\n`feet - feet hentai`\n`hentai - straight hentai`\n`boobs - shows some hentai boobs`\n`tits - shows some hentai titties`\n`blowjob - blowjob hentai`\n`lewdneko - lewd nekos`\n`lesbian - hentai thats lesbian`\n\n**Misc**\n`avatar <user> - gets a users profile picture`\n`servercount - checks how many servers the bot is in!`")

	await ctx.send(embed=embed)

client.run("   ")