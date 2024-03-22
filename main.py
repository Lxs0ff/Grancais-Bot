import discord

token = 0;
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
def translate():
    pass

@client.event
async def on_ready():
    print(f'Bot Started as {client.user}')

@client.event
async def on_message(message):
    message_s = message.content
    result = "";
    if message.author == client.user:
        return
    if message_s.startswith('/Grançais'):
        message_s.replace('/Grancais ','')
        result = translate(message_s)
        await message.channel.send(result)
client.run(token)