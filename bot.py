import discord


from bot_logic import *

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith("contraseña"):
        await message.channel.send(f"{gen_pass(8)}")
    elif message.content.startswith("coin"):
        result = coin()
        await message.channel.send(result)
    elif message.content.startswith("emoji"):
        await message.channel.send(gen_emodji())
    elif message.content.startswith("buenos dias"):
        await message.channel.send("buenos dias a ti tambien! ¿Como te encuentras")
    elif message.content.startswith("bien"):
        await message.channel.send("me alegro")
    else:
        await message.channel.send(message.content)
client.run("MTI4NDI5Nzk3NTU1MTYyNzQyOA.GBoK_u.NEMmQ7UOhD4uUzU8cRjSDViuD0FSv7YKx-dbcs")
