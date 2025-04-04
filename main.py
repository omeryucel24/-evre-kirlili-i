
import discord
import random
pass_length=6




# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('/merhaba'):
        await message.channel.send("/Selam!")
    elif message.content.startswith('/bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('/help'):
        await message.channel.send("/çevre kirlilik , /bye ,/merhaba ,help, /çevre kirlilik önlemek")
    if message.content.startswith('/çevre kirlilik'):
        await message.channel.send("Çevre kirliliği, doğadaki dengeyi bozan ve insan sağlığını tehdit eden bir sorundur. Hava, su ve toprak kirliliği, en yaygın çevre kirliliği türlerindendir. Hava kirliliği, fosil yakıtların yakılması, sanayi atıkları ve ulaşım araçlarının saldığı zararlı gazlar nedeniyle artmaktadır. Su kirliliği ise atıkların, kimyasal maddelerin ve plastiklerin su kaynaklarına karışmasıyla oluşur. Toprak kirliliği de tarımda kullanılan zararlı kimyasallar ve sanayi atıkları ile meydana gelir.")
    if message.content.startswith('/çevre kirlilik önlemek'):
        await message.channel.send("Çevre kirliliğinin önlenmesi için atılacak birkaç önemli adım vardır. İlk olarak, geri dönüşüm teşvik edilerek, atıkların tekrar kullanımı sağlanabilir. Fosil yakıtların yerine yenilenebilir enerji kaynakları (güneş, rüzgar, hidroelektrik) kullanılmalı, bu sayede hava kirliliği azaltılabilir. Plastik kullanımını azaltmak için biyobozunur malzemelere yönelmek önemlidir. Ayrıca, doğal kaynakların korunması ve atık yönetimi konusunda halkı bilinçlendirmek gerekmektedir. Yeşil alanların arttırılması ve ormanların korunması da doğayı temiz tutmada etkili olur. Bu önlemler, çevreyi koruyarak sağlıklı bir yaşam alanı oluşturulmasına katkı sağlar.")
        
client.run("token")
