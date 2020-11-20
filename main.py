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
async def dmall(server):
    for member in server.members:
        print(member)
        channel = await member.dm_channel()
        await channel.send("ＢＯＲＮ ＴＯ ＤＩＥ WORLD IS A FUCK 鬼神 Kill Em All 1989 I am trash man 410,757,864,530 DEAD COPS")
    print("Done!")


# # error handler
# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, discord.ext.commands.errors.Forbidden):
#         print(f"[DM] {ctx.author} has DMs disabled.")
#     else:
#         print(error)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-dm'):
        await dmall(message.guild)
        # print(message.guild.members)
        # for members in message.guild.members:
        #     await message.channel.send(members.mention)


client.run(key)
