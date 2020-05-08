import discord, re, aiohttp, asyncio, config, random, time

client = discord.Client()

@client.event
async def on_ready():
    print('{0.user.name} is online'.format(client))
    await client.change_presence(activity = discord.Game(name = config.status))

@client.event
async def on_member_join(member):
    if config.welcomesEnabled == True:
        welcome_channel = client.get_channel(config.welcomeChannel)
        time.sleep(random.randrange(2,4))
        await welcome_channel.send("{0} ".format(member) + random.choice(config.welcome_messages))

@client.event
async def on_message(message):

    User = "<@"+str(message.author.id)+">, "
    if config.mentionReply == False:
        User = "("+message.author.name+") "

    if message.author == message.author.bot or message.author == client.user:
        return
    if client.user in message.mentions or isinstance(message.channel, discord.channel.DMChannel):
        async with message.channel.typing():
            try:
                input = re.sub('<@!?{0.user.id}>'.format(client), '', message.content).strip()
                print(input)
                params = {'botid': config.botID, 'custid': message.author.id, 'input': input.strip('?') or 'Hello'}
                async with aiohttp.ClientSession().get('https://www.pandorabots.com/pandora/talk-xml', params = params) as resp:
                    if resp.status == 200:
                        text = await resp.text()
                        text = text[text.find('<that>') + 6:text.rfind('</that>')]
                        text = text.replace('&quot;', '"').replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&').replace(
                            '<br>', ' ')
                        await message.channel.send(User + text)
                    else:
                        await message.channel.send("<@"+str(message.author.id)+">, " + random.choice(config.error_message))
            except asyncio.TimeoutError:
                await message.channel.send('i think im drunk')

client.run(config.token)
