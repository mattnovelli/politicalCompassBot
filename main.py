import discord
from discord import guild
from key import key

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-dm'):
        print(message.guild.members)
        for members in message.guild.members:
            await message.channel.send(members.mention)
client.run(key)