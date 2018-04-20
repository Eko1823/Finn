# FinnBot 1.2.3 by Soul#0001

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import time
import random

# Options
version = '1.2.3'
prefix = '.'
logs_channel = 'logs'
#admin_role = 'Admin' # Case Sensitive
#mod_role = 'Moderator' # Case Sensitive
colors_enabled = True

# Do not touch, edit with Options
Client = discord.Client()
bot = commands.Bot(command_prefix=prefix)

# Start Up
@bot.event
async def on_ready():
    print('Setting status ...')
    await bot.change_status(game=discord.Game(name='VERSION {}'.format(version)))
    print('===================================================')
    print('| Captain ' + bot.user.name + ' on duty!')
    print('| Running VERSION {} by Soul#0001'.format(version))
    print('| My ID is: ' + bot.user.id)
    print('| ')
    print('| Type {}cmds for a list of commands'.format(prefix))
    print('===================================================')

# List Commands
@bot.command(pass_context=True)
async def cmds(ctx):
    emb = (discord.Embed(title='Commands', color=0x0ac6cf))
    emb.add_field(name='{}cmds'.format(prefix), value='Displays this message', inline=False)
    emb.add_field(name='{}info'.format(prefix), value='Lists all Info commands', inline=False)
    emb.add_field(name='{}kick <@user>'.format(prefix), value='Kicks a user (permission based)', inline=False)
    emb.add_field(name='{}ping'.format(prefix), value='Pings the bot', inline=False)
    emb.add_field(name='{}roll [type] [# of rolls]'.format(prefix), value='Rolls a die', inline=False)
    if colors_enabled == True:
        emb.add_field(name='{}colors'.format(prefix), value='Change your name color', inline=False)
    emb.add_field(name='{}miko'.format(prefix), value='Sends a random Miko', inline=False)
    emb.add_field(name='{}cukie'.format(prefix), value='?', inline=False)
    emb.set_footer(text='<> = Required, [] = Optional')
    await bot.say(embed=emb)
    
# Ping
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(ctx.message.author.mention + ' :poop:')

# Degenerate
@bot.command(pass_context=True)
async def cukie(ctx):
    ian = [
        'Who?',
        'Ew. Don\'t say that.',
        '<@303575436607356929>? What a loser!',
        'Degenerate!!!',
        'Don\'t say that name.',
        'Stop that!',
        'What a degenerate!',
        'Oh, that guy? I hear he\'s a DEGENERATE!',
        'You degenerate!!',
        'Shut up, you degenerate!',
        'You mean <@303575436607356929>? He\'s a degenerate.',
        'Look at that guy. Fucking degenerate.',
        'D E G E N E R A T E',
        'Can you talk about someone who\'s not a degenerate?',
    ]
    
    await bot.say(random.choice(ian))

# Miko
@bot.command(pass_context=True) 
async def miko(ctx):
    mikos = [
        'https://i.soulsartshop.com/p0G-52S-08i.gif',
        'https://i.soulsartshop.com/B6O-AD0-rTU.gif',
        'https://i.soulsartshop.com/tp8-k1g-JaG.gif',
        'https://i.soulsartshop.com/p0G-52S-08i.gif',
        'https://i.soulsartshop.com/B6O-AD0-rTU.gif',
        'https://i.soulsartshop.com/tp8-k1g-JaG.gif',
        'https://i.soulsartshop.com/tIE-AsL-G3Y.jpg',
        'https://i.soulsartshop.com/Ben-GEY-x3w.jpg',
        'https://i.soulsartshop.com/fsT-Mfx-3QH.jpg',
        'https://i.soulsartshop.com/uez-lyi-oNx.jpg',
        'https://i.soulsartshop.com/wC2-1Mm-54c.png',
        'https://i.soulsartshop.com/VBE-JDy-puP.jpg',
        'https://i.soulsartshop.com/pc4-fDo-PbB.jpg',
        'https://i.soulsartshop.com/20D-2t9-Rwp.jpg',
        'https://i.soulsartshop.com/j8l-doH-jSs.jpg',
        'https://i.soulsartshop.com/5Yy-1iX-RlN.jpg',
        'https://i.soulsartshop.com/iLf-UWk-XDn.jpg',
        'https://i.soulsartshop.com/qTS-gsR-b6l.jpg',
        'https://i.soulsartshop.com/DNm-PdI-yLO.png',
        'https://i.soulsartshop.com/eBn-mvl-vgF.jpg',
    ]

    emb = discord.Embed(color=0xffe153)
    emb.set_image(url=random.choice(mikos))
    await bot.say(embed=emb)

# Info
@bot.command(pass_context=True)
async def info(ctx):
    emb = discord.Embed(title='Info Commands', color=0x0ac6cf)
    emb.add_field(name='{}serverinfo'.format(prefix), value='Displays server info', inline=False)
    emb.add_field(name='{}userinfo [@user]'.format(prefix), value='Displays info on a specific user', inline=False)
    emb.add_field(name='{}botinfo'.format(prefix), value='Displays info the bot', inline=False)
    emb.set_footer(text='<> = Required, [] = Optional')
    await bot.say(embed=emb)

# Server Info
@bot.command(pass_context=True)
async def serverinfo(ctx):
    emb = discord.Embed(title='{}'.format(ctx.message.server.name), color=0x0ac6cf)
    emb.add_field(name='Server ID', value='{}'.format(ctx.message.server.id), inline=False)
    emb.add_field(name='Date Created', value='{}'.format(ctx.message.server.created_at), inline=False)
    emb.add_field(name='Member Count', value='{}'.format(ctx.message.server.member_count), inline=False)
    emb.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=emb)

# User Info
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member=None):
    if not user:
        emb = discord.Embed(title='Your Info', color=ctx.message.author.color)
        emb.add_field(name='Username', value='{}'.format(ctx.message.author), inline=True)
        emb.add_field(name='Status', value='{}'.format(ctx.message.author.status), inline=True)
        emb.add_field(name='Joined At', value='{}'.format(ctx.message.author.joined_at), inline=True)
        emb.set_thumbnail(url=ctx.message.author.avatar_url)
        await bot.say(embed=emb)
    else:
        emb = discord.Embed(title='{}\'s Info'.format(user.display_name), color=user.color)
        emb.add_field(name='Username', value='{}'.format(user), inline=True)
        emb.add_field(name='Status', value='{}'.format(user.status), inline=True)
        emb.add_field(name='Joined At', value='{}'.format(user.joined_at), inline=True)
        emb.set_thumbnail(url=user.avatar_url)
        await bot.say(embed=emb)

# Bot Info
@bot.command(pass_context=True)
async def botinfo(ctx):
    emb = discord.Embed(title='FinnBot', color=0x0ac6cf)
    emb.add_field(name='Version', value='Version {}'.format(version), inline=True)
    emb.add_field(name='Author', value='Soul#0001', inline=True)
    emb.set_thumbnail(url=bot.user.avatar_url)
    await bot.say(embed=emb)

# Embed
@bot.command(pass_context=True)
async def testembed(ctx):
    emb = discord.Embed(title='Test Title', description='Embed Description', color=0x00ff00)
    emb.set_author(name='Name')
    emb.add_field(name='This is a field.', value='Field value.', inline=True)
    emb.add_field(name='This is another field.', value='Field value.', inline=True)
    emb.set_footer(text='This is a footer.')
    await bot.say(embed=emb)

# Kick
@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member=None):    
    if ctx.message.author.server_permissions.kick_members:
        if not user:
            emb = (discord.Embed(title='Missing Arguments', description='Correct Usage: {}kick <@user>'.format(prefix), color=0xfc3c3c))
            await bot.say(embed=emb)
        else:
            botlogs = discord.utils.get(bot.get_all_channels(), server__name=ctx.message.server.name, name=logs_channel)
            if ctx.message.author == user:
                emb = discord.Embed(description='You cant kick yourself, idiot', color=0xfc3c3c)
                await bot.say(embed=emb)
            #elif user.server_permissions.kick_members:
                #emb = discord.Embed(description='You can\'t kick other Memers, ya fuck', color=0xfc3c3c)
                #await bot.say(embed=emb)
            else:
                emb = discord.Embed(title='CASE: KICK', color=0xfc3c3c)
                emb.add_field(name='Offender', value='{}'.format(user), inline=True)
                emb.add_field(name='Issued By', value='{}'.format(ctx.message.author), inline=True)
                emb.set_thumbnail(url=user.avatar_url)
                await bot.send_message(botlogs, embed=emb)
                #await bot.kick(user)
                emb = discord.Embed(description='{} has been kicked.'.format(user), color=0x25c318)
                await bot.say(embed=emb)
    else:
        emb = discord.Embed(description='You can\'t kick anyone, you hoe', color=0xfc3c3c)
        await bot.say(embed=emb)

# Colors
@bot.command(pass_context=True)
async def colors(ctx):
    if colors_enabled == True:
        emb = (discord.Embed(color=0x0ac6cf))
        emb.add_field(name='Available Colors', value='red, orange, gold, yellow, lime, green, aqua, blue, indigo, violet, magenta, pink, reset')
        emb.set_footer(text='Use "{}color <name of color>" to set your name color'.format(prefix))
        await bot.say(embed=emb)
    else:
        emb = (discord.Embed(title='Invalid Command', description='Name colors are not enabled', color=0xfc3c3c))
        await bot.say(embed=emb)

# Color
@bot.command(pass_context=True)
async def color(ctx, arg1: str=None):
    if colors_enabled == True:
        if not arg1:
            emb = (discord.Embed(title='Missing Arguments', description='Correct Usage: .color <color name>', color=0xfc3c3c))
            emb.set_footer(text='For a list of available colors, type "{}colors"'.format(prefix))
            await bot.say(embed=emb)
        else:

            user = ctx.message.author
            narg = arg1.capitalize()

            colors = [
            'Red',
            'Orange',
            'Gold',
            'Yellow',
            'Lime',
            'Green',
            'Aqua',
            'Blue',
            'Indigo',
            'Violet',
            'Magenta',
            'Pink'
            ]

            async def remove_colors(user):
                await bot.remove_roles(user,
                    discord.utils.get(ctx.message.server.roles, name='Red'), 
                    discord.utils.get(ctx.message.server.roles, name='Orange'),
                    discord.utils.get(ctx.message.server.roles, name='Gold'),
                    discord.utils.get(ctx.message.server.roles, name='Yellow'),
                    discord.utils.get(ctx.message.server.roles, name='Lime'),
                    discord.utils.get(ctx.message.server.roles, name='Green'),
                    discord.utils.get(ctx.message.server.roles, name='Aqua'), 
                    discord.utils.get(ctx.message.server.roles, name='Blue'),
                    discord.utils.get(ctx.message.server.roles, name='Indigo'),
                    discord.utils.get(ctx.message.server.roles, name='Violet'),
                    discord.utils.get(ctx.message.server.roles, name='Magenta'),
                    discord.utils.get(ctx.message.server.roles, name='Pink')
                    )

            if narg in colors:
                col = discord.utils.get(ctx.message.server.roles, name='{0}'.format(narg))
                await remove_colors(user)
                await bot.remove_roles(user, col)
                await bot.add_roles(user, col)
                emb = (discord.Embed(description='Your name color is now {0}'.format(col), color=col.color))
                await bot.say(embed=emb)
            elif narg == 'Reset':
                await remove_colors(user)
                emb = (discord.Embed(description='Your name color has been reset'))
                await bot.say(embed=emb)
            else:
                emb = (discord.Embed(title='Invalid Arguments', description='"{0}" is not a valid color'.format(narg), color=0xfc3c3c))
                emb.set_footer(text='For a list of available colors, type "{}colors"'.format(prefix))
                await bot.say(embed=emb)
    else:
        emb = (discord.Embed(title='Invalid Command', description='Name colors are not enabled', color=0xfc3c3c))
        await bot.say(embed=emb)

# D&D Dice - It's long and tedious, needs better execution
@bot.command(pass_context=True)
async def roll(ctx, arg1: str=None, arg2: int=1):
    user = ctx.message.author.display_name

    D4 = [1,2,3,4]
    D6 = [1,2,3,4,5,6]
    D8 = [1,2,3,4,5,6,7,8]
    D10 = [1,2,3,4,5,6,7,8,9,10]
    D12 = [1,2,3,4,5,6,7,8,9,10,11,12]
    D20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    dice = ['D4','D6','D8','D10','D12','D20']
    maxrolls = [1,2,3,4,5,6,7,8,9,10]

    if not arg1:
        die = random.choice(D6)
        emb = (discord.Embed(description='{0} rolled a {1}'.format(user, die)))
        await bot.say(embed=emb)
    else:
        narg = arg1.capitalize()

        if narg in dice:
            if arg2 == 0:
                emb = (discord.Embed(description='{0} just tried to roll a die {1} times. What a retard.'.format(user, arg2)))
                await bot.say(embed=emb)
            elif arg2 in maxrolls:
                die1 = random.choice(eval(narg))
                die2 = random.choice(eval(narg))
                die3 = random.choice(eval(narg))
                die4 = random.choice(eval(narg))
                die5 = random.choice(eval(narg))
                die6 = random.choice(eval(narg))
                die7 = random.choice(eval(narg))
                die8 = random.choice(eval(narg))
                die9 = random.choice(eval(narg))
                die10 = random.choice(eval(narg))
                
                if arg2 == 1:
                    emb = (discord.Embed(description='{0} rolled a {1}'.format(user, die1)))
                    await bot.say(embed=emb)
                elif arg2 == 2:
                    result = die1 + die2
                    emb = (discord.Embed(description='{0} rolled {1} + {2} = {3}'.format(user, die1, die2, result)))
                    await bot.say(embed=emb)
                elif arg2 == 3:
                    result = die1 + die2 + die3
                    emb = (discord.Embed(description='{0} rolled {1} + {2} + {3} = {4}'.format(user, die1, die2, die3, result)))
                    await bot.say(embed=emb)
                elif arg2 == 4:
                    result = die1 + die2 + die3 + die4
                    emb = (discord.Embed(description='{0} rolled {1} + {2} + {3} + {4} = {5}'.format(user, die1, die2, die3, die4, result)))
                    await bot.say(embed=emb)
                elif arg2 == 5:
                    result = die1 + die2 + die3 + die4 + die5
                    emb = (discord.Embed(description='{0} rolled {1} + {2} + {3} + {4} + {5} = {6}'.format(user, die1, die2, die3, die4, die5, result)))
                    await bot.say(embed=emb)
                elif arg2 == 6:
                    result = die1 + die2 + die3 + die4 + die5 + die6
                    emb = (discord.Embed(description='{0} rolled {1} + {2} + {3} + {4} + {5} + {6} = {7}'.format(user, die1, die2, die3, die4, die5, die6, result)))
                    await bot.say(embed=emb)
                elif arg2 == 7:
                    result = die1 + die2 + die3 + die4 + die5 + die6 + die7
                    emb = (discord.Embed(description='{0} rolled {1} + {2} + {3} + {4} + {5} + {6} + {7} = {8}'.format(user, die1, die2, die3, die4, die5, die6, die7, result)))
                    await bot.say(embed=emb)
                elif arg2 == 8:
                    result = die1 + die2 + die3 + die4 + die5 + die6 + die7 + die8
                    emb = (discord.Embed(description='{0} rolled {1} + {2} + {3} + {4} + {5} + {6} + {7} + {8} = {9}'.format(user, die1, die2, die3, die4, die5, die6, die7, die8, result)))
                    await bot.say(embed=emb)
                elif arg2 == 9:
                    result = die1 + die2 + die3 + die4 + die5 + die6 + die7 + die8 + die9
                    emb = (discord.Embed(description='{0} rolled {1} + {2} + {3} + {4} + {5} + {6} + {7} + {8} + {9} = {10}'.format(user, die1, die2, die3, die4, die5, die6, die7, die8, die9, result)))
                    await bot.say(embed=emb)
                elif arg2 == 10:
                    result = die1 + die2 + die3 + die4 + die5 + die6 + die7 + die8 + die9 + die10
                    emb = (discord.Embed(description='{0} rolled {1} + {2} + {3} + {4} + {5} + {6} + {7} + {8} + {9} + {10} = {11}'.format(user, die1, die2, die3, die4, die5, die6, die7, die8, die9, die10, result)))
                    await bot.say(embed=emb)
            else:
                emb = (discord.Embed(title='Invalid Arguments', description='You tried to roll the die "{0}" times. Please choose a number between 1 and 10.'.format(arg2), color=0xfc3c3c))
                emb.set_footer(text='{}roll <type> <# of rolls>'.format(prefix))
                await bot.say(embed=emb)
        else:
            emb = (discord.Embed(title='Invalid Arguments', description='"{0}" is not a valid die'.format(narg), color=0xfc3c3c))
            emb.set_footer(text='Valid Types: D4, D6, D8, D10, D12, D20')
            await bot.say(embed=emb)

# Token
bot.run('Token')
