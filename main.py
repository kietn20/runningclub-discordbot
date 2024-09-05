import discord
from discord.ext import commands
from config import TOKEN, PREFIX
import os
import asyncio

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.load_extension('cogs.run_management')

async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                await bot.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename}')
            except Exception as e:
                print(f'Failed to load extension {filename}: {e}')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Command not found. Error: {error}")
    else:
        await ctx.send(f"An error occurred: {error}")
    
# Load cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'Loaded {filename}')


async def main():
    await load_extensions()
    await bot.start(TOKEN)

# Run the bot
asyncio.run(main())