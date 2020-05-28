import discord 
from discord.ext import commands
bot = commands.Bot (command_prefix =  '.' )
@bot.event 
async def on_ready():
 	print ('bot is ready.')
 	
 	bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
	



bot.run('NzE1NjI3Mjk0NDA4MDQ4NzIw.XtAeTQ.FdvTqIqCFR-osFZ-4XdnBiHFjqc')