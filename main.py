import discord


client = discord.Client()
@client.event
async def on_ready():
    print('目前登入身份：', client.user)
    game=discord.Game("tag")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg_content = message.content.lower()

    #edit curseWord for more cursewords 
    curseWord = ["arse",
                 "ass ",
                 "asz",
                 "asshole",
                 "bastard",
                 "bitch",
                 "bollocks",
                 "brotherfucker",
                 "bullshit",
                 "child-fucker",
                 "Christ on a bike",
                 "Christ on a cracker",
                 "cocksucker ",
                 "crap ",
                 "cunt",
                 "damn",
                 "diu",
                 "dick head",
                 "dickson",
                 "dick",
                 "effing",
                 "fatherfucker",
                 "frigger",
                 "fuck",
                 "fuck off",
                 "fack",
                 "fk",
                 "frick",
                 "goddamn",
                 "godsdamn",
                 "holy shit",
                 "horseshit",
                 "Jesus fuck",
                 "Jesus H. Christ",
                 "Jesus Harold Christ",
                 "Jesus wept",
                 "Jesus, Mary and Joseph ",
                 "Judas Priest",
                 "motherfucker",
                 "nigga",
                 "piss",
                 "prick",
                 "shit",
                 "sht",
                 "shiit",
                 "what the",
                 "feddrick ",
                 "shit ass",
                 "sisterfucker",
                 "slut",
                 "son of a bitch",
                 "son of a whore",
                 "sweet Jesus",
                 "🖕"
                 ]
    
    if any(word in msg_content for word in curseWord):
        await message.delete()
        await message.channel.send(f'{message.author.mention} Do Not Swear')

client.run("token")
