import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

token = '' #paste your discord bot token here

@tasks.loop(seconds=60)
async def update_presence():
    await bot.change_presence(
        activity=discord.Game(
            name=" spamming time!",
            type=discord.ActivityType.playing,
            large_image="large_image",
            small_image="small_image",
        )
    )

@bot.command(name="spam")
async def spam(ctx, user: discord.User):

    await ctx.send(f"Spamming {user}")

    while True:
        try:
            await user.send(f"SPAMMER 3.0!!")
            print(f"Spammed '{user}'")
            await asyncio.sleep(1)
        except discord.Forbidden:
            await ctx.send(f"Unable to send a message to {user.name}. They may have DMs disabled or have blocked the bot.")

    await ctx.message.delete()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    update_presence.start()

if __name__ == "__main__":
    bot.remove_command("help")

    bot.run(token)