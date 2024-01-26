import random
import time
import discord

from discord import app_commands
from discord.ext import commands

from apikeys import *

bot = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot está rodando")
    print("________________")

    try:
        synced = await bot.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(e)

@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá, {interaction.user.mention}! Isso é um comando de barra")

@bot.tree.command(name="roll", description="Roll a dice")
@app_commands.describe(dice_type = "Dice type", times_to_roll = "Times to roll the dice", dice_modifier = "Dice modifier")
# async def roll(interaction: discord.Interaction, dice_type: int, times_to_roll: int = 1, dice_modifier: int = 0):
#     final_dice = ""
#     soma = 0
#     for i in range(times_to_roll):
#         dice_roll = random.randint(1, dice_type)
#         dice_result = dice_roll + dice_modifier
#         if dice_modifier > 0:
#             final_dice += f'{dice_result} = [**{dice_roll}**+{dice_modifier}]\n'
#             soma += dice_result
#         else:
#             final_dice += f'{dice_result} = [**{dice_roll}**{dice_modifier}]\n'
#             soma += dice_result
#     await interaction.response.send_message(f'__{times_to_roll}d{dice_type}__\n{final_dice}\nSoma: {soma}')
async def roll(interaction: discord.Interaction, dice_type: int, times_to_roll: int = 1, dice_modifier: int = 0):
    final_dice = ""
    soma = 0
    for i in range(times_to_roll):
        dice_roll = random.randint(1, dice_type)
        dice_result = dice_roll + dice_modifier
        if dice_modifier > 0:
            final_dice += f'{dice_result} = [**{dice_roll}**+{dice_modifier}]\n'
            final_dice = 0 if dice_result < 0 else final_dice
        else:
            final_dice += f'{dice_result} = [**{dice_roll}**{dice_modifier}]\n'
            final_dice = 0 if dice_result < 0 else final_dice
        soma += dice_result

    modifier_str = f' {"" if dice_modifier == 0 else "+" if dice_modifier > 0 else ""}{dice_modifier}' if dice_modifier != 0 else ""
    await interaction.response.send_message(f'__**{times_to_roll}d{dice_type}{modifier_str}**__\n{final_dice}\nSoma: {soma}')


@bot.command()
async def ajuda(ctx):
    await ctx.author.send("Os comandos disponíveis são:\n !ajuda\n !roll\n !ping")
    time.sleep(1)
    await ctx.message.delete()

@bot.command()
async def ping(ctx):
    await ctx.send("pong")

bot.run(TOKEN)