import random, time, discord, re

from discord.ext import commands
from discord import Message, app_commands

from apikeys import *

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot está rodando")
    print("________________")

@bot.command()
async def roll(ctx, dice: str, dice_modifier: int = 0):

    type_and_times = re.findall('[0-9]+', dice)

    times_to_roll = int(type_and_times[0])  if len(type_and_times) > 1 else 1
    dice_type = int(type_and_times[1  if len(type_and_times) > 1 else 0])
    
    if times_to_roll == 1 or times_to_roll == "":
        dice_roll = random.randint(1, dice_type)
        dice_result = dice_roll + dice_modifier
        
        if dice_modifier != 0:
           if dice_modifier > 0:
               await ctx.reply(f'**{dice_result}** = [{dice_roll}+{dice_modifier}]')
           else:
               await ctx.reply(f'**{dice_result}** = [{dice_roll}{dice_modifier}]')
        else:
           await ctx.reply(f'**{dice_result}** = [{dice_roll}]')

    else:
        final_dice = ""
        soma = 0
        for i in range(times_to_roll):
            dice_roll = random.randint(1, dice_type)
            dice_result = dice_roll + dice_modifier
            if dice_modifier != 0:
                if dice_modifier > 0:
                    final_dice += f'{dice_result} = [**{dice_roll}**+{dice_modifier}]\n'
                    soma += dice_result
                else:
                    final_dice += f'{dice_result} = [**{dice_roll}**{dice_modifier}]\n'
                    soma += dice_result
            else:
                final_dice += f'{dice_result} = [**{dice_roll}**]\n'
                soma += dice_result
        await ctx.reply(f'{final_dice}\nSoma: {soma}')

@bot.command()
async def ajuda(ctx):
    await ctx.author.send("Os comandos disponíveis são:\n\n !roll")
    time.sleep(1)
    await ctx.message.delete()
    

bot.run(TOKEN)