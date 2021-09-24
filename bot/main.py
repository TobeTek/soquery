import decouple
import discord
from discord.ext import commands
from utils import get_questions

DISCORD_KEY = decouple.config("DISCORD_KEY")

bot = commands.Bot(command_prefix="<->")

@bot.event
async def on_ready():
	print("Bot is locked and loaded!")

@bot.command(name='hello', help='Make bot to talk')
async def hello(ctx):
	await ctx.send(f"Hello {ctx.message.author.mention}!")

@bot.command(name='sq', help='Search StackOverflow for answers. Format "<title>-<tag1>,<tag2>"')
async def query_so(ctx):
	msg = ctx.message
	await ctx.send(f"{ctx.message.author.mention} your query is {msg.content[5:]}!")
	try:
		print(repr(msg.content))
		data = str(msg.content)[5:].strip(" ").split("-")
		print("My message is" + str(data))
		
		title = data[0]
		# act_title = title[-1]
		print("Title" + str(title))
		
		tags = data[-1].split(",")
		
		print(tags)
		
		output = get_questions(tags, title)
		print("Output is :" + str(output))
		if len(output) > 0:
			await ctx.send(f"Results from SO:\n{output}")
		else:
			await ctx.send(f"No results...")
	except Exception as e:
		print(e)
		await ctx.send("Wrong Input format.")

if __name__ == "__main__":
	bot.run(DISCORD_KEY)