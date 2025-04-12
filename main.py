
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
        await message.channel.send("/çevre kirlilik , /bye ,/merhaba ,help, /çevre kirlilik önlemek, /konum")
    if message.content.startswith('/çevre kirlilik'):
        await message.channel.send("Çevre kirliliği, doğadaki dengeyi bozan ve insan sağlığını tehdit eden bir sorundur. Hava, su ve toprak kirliliği, en yaygın çevre kirliliği türlerindendir. Hava kirliliği, fosil yakıtların yakılması, sanayi atıkları ve ulaşım araçlarının saldığı zararlı gazlar nedeniyle artmaktadır. Su kirliliği ise atıkların, kimyasal maddelerin ve plastiklerin su kaynaklarına karışmasıyla oluşur. Toprak kirliliği de tarımda kullanılan zararlı kimyasallar ve sanayi atıkları ile meydana gelir.")
    if message.content.startswith('/çevre kirlilik önlemek'):
        await message.channel.send("Çevre kirliliğinin önlenmesi için atılacak birkaç önemli adım vardır. İlk olarak, geri dönüşüm teşvik edilerek, atıkların tekrar kullanımı sağlanabilir. Fosil yakıtların yerine yenilenebilir enerji kaynakları (güneş, rüzgar, hidroelektrik) kullanılmalı, bu sayede hava kirliliği azaltılabilir. Plastik kullanımını azaltmak için biyobozunur malzemelere yönelmek önemlidir. Ayrıca, doğal kaynakların korunması ve atık yönetimi konusunda halkı bilinçlendirmek gerekmektedir. Yeşil alanların arttırılması ve ormanların korunması da doğayı temiz tutmada etkili olur. Bu önlemler, çevreyi koruyarak sağlıklı bir yaşam alanı oluşturulmasına katkı sağlar.")
    if message.content.startswith('/konum'):
       await message.channel.send("bana herhangi bir konum gönderirseniz, o konuma en yakın olan geri dönüşüm alanlarını yazabilirim(sadece Türkiye'nin illeri için geçerlidir)") 
    if message.content.startswith('/istanbul'):
       await message.channel.send("Avrupa Yakası Geri Dönüşüm Alanları: Baruthane Katı Atık Aktarma İstasyonu (Şişli), Başakşehir Katı Atık Aktarma İstasyonu (Başakşehir), Yenibosna Katı Atık Aktarma İstasyonu (Bahçelievler), Silivri Katı Atık Aktarma İstasyonu (Silivri)Anadolu Yakası Geri Dönüşüm Alanları: Maltepe Hizmet Birimi (Maltepe), Ümraniye Hizmet Birimi (Ümraniye), Bakkalköy Katı Atık Aktarma İstasyonu (Kadıköy), Şile Katı Atık Aktarma İstasyonu (Şile)Özel ve İlçe Bazlı Geri Dönüşüm Merkezleri: Geri Dönüşüm İşçileri Atık Ara Toplama Merkezi (Dereağzı Mah., Beylikdüzü), Nahıl Geri Dönüşüm Parkı (şehir genelinde ikinci el eşya ve giysi toplama), Atatürk Kültür Merkezi (geri dönüşüm temalı etkinlikler ve atölyeler, Beyoğlu daha detaylı bir bilgi almak için İstanbul Büyükşehir Belediyesinin resmi sitesine bakabilirsiniz.")  
    if message.content.startswith('/atık türleri'):
        await message.channel.send("♻️ Atık Türleri Hakkında Kısa Bilgilendirme Günlük yaşantımızda farkında olmadan birçok atık üretiriz. Bu atıklar, doğaya olan etkilerine ve geri dönüşüm potansiyellerine göre farklı gruplara ayrılır. En yaygın atık türleri arasında kağıt, plastik, cam, metal, organik, tekstil ve tehlikeli atıklar yer alır.Kağıt ve karton atıklar, yeniden işlenerek defter, kitap gibi ürünlere dönüşebilir. Plastik atıklar, doğada yüzyıllarca çözünmeden kalabildiği için çevreye en fazla zarar veren türlerden biridir. Cam ve metal atıklar ise %100 oranında geri dönüştürülebilir. Organik atıklar kompost haline getirilerek doğaya geri kazandırılabilirken, tehlikeli atıklar (pil, elektronik, ilaç gibi) özel olarak toplanmalıdır. Tekstil atıkları da geri kazanılarak yeniden kullanılabilir malzemelere dönüştürülebilir.")
      





kullanici_verileri = {}

@client.event
async def on_ready():
    print(f"Bot {client.user} olarak giriş yaptı.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # !kaydet komutu
    if message.content.startswith("!kaydet"):
        user = message.author

        veri = {
            "id": user.id,
            "isim": str(user),
            "takma_ad": user.nick if hasattr(user, 'nick') else None,
            "durum": str(user.status),
            "aktivite": str(user.activity.name if user.activity else "Yok")
        }

        kullanici_verileri[user.id] = veri

        await message.channel.send(f"{user.mention}, bilgilerin başarıyla kaydedildi.")
        print(veri)

    # !bilgilerim komutu
    if message.content.startswith("!bilgilerim"):
        user = message.author
        if user.id in kullanici_verileri:
            veri = kullanici_verileri[user.id]
            mesaj = (
                f"👤 Kullanıcı Bilgilerin:\n"
                f"🆔 ID: {veri['id']}\n"
                f"📛 İsim: {veri['isim']}\n"
                f"📝 Takma Ad: {veri['takma_ad']}\n"
                f"💬 Durum: {veri['durum']}\n"
                f"🎮 Aktivite: {veri['aktivite']}"
            )
            await message.channel.send(mesaj)
        else:
            await message.channel.send("Önce `!kaydet` komutu ile bilgilerini kaydetmelisin.")
@client.event
async def on_ready():
    print(f"Bot {client.user} olarak giriş yaptı.")

@client.event
async def on_ready():
    print(f"Bot {client.user} olarak giriş yaptı.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user = message.author
    content = message.content

    if content.startswith("!kaydet"):
        veri = {
            "id": user.id,
            "isim": str(user),
            "takma_ad": user.nick if hasattr(user, 'nick') else None,
            "durum": str(user.status),
            "aktivite": str(user.activity.name if user.activity else "Yok")
        }
        kullanici_verileri[user.id] = veri
        await message.channel.send(f"{user.mention}, bilgilerin başarıyla kaydedildi.")

    elif content.startswith("!bilgilerim"):
        if user.id in kullanici_verileri:
            veri = kullanici_verileri[user.id]
            mesaj = f"👤 **Kullanıcı Bilgilerin:**\n"
            for key, value in veri.items():
                mesaj += f"🔸 {key.capitalize()}: {value}\n"
            await message.channel.send(mesaj)
        else:
            await message.channel.send("Önce `!kaydet` komutu ile bilgilerini kaydetmelisin.")

    elif content.startswith("!ekle"):
        if user.id not in kullanici_verileri:
            await message.channel.send("Önce `!kaydet` komutu ile kayıt olmalısın.")
            return

        try:
            _, anahtar, *deger_parcalari = content.split()
            deger = " ".join(deger_parcalari)
            kullanici_verileri[user.id][anahtar] = deger
            await message.channel.send(f"{anahtar} bilgisi '{deger}' olarak eklendi ✅")
        except ValueError:
            await message.channel.send("Kullanım: `!ekle <anahtar> <değer>` şeklinde olmalı.")

    elif content.startswith("!sil"):
        if user.id not in kullanici_verileri:
            await message.channel.send("Kayıtlı bir bilgin yok, önce `!kaydet` yazmalısın.")
            return

        try:
            _, anahtar = content.split()
            if anahtar in kullanici_verileri[user.id]:
                del kullanici_verileri[user.id][anahtar]
                await message.channel.send(f"'{anahtar}' bilgisi silindi. 🗑️")
            else:
                await message.channel.send(f"'{anahtar}' adlı bir bilgin bulunamadı.")
        except ValueError:
            await message.channel.send("Kullanım: `!sil <anahtar>`")

    elif content.startswith("!degistir"):
        if user.id not in kullanici_verileri:
            await message.channel.send("Önce `!kaydet` komutu ile kayıt olmalısın.")
            return

        try:
            _, anahtar, *yeni_deger_parcalari = content.split()
            yeni_deger = " ".join(yeni_deger_parcalari)
            if anahtar in kullanici_verileri[user.id]:
                kullanici_verileri[user.id][anahtar] = yeni_deger
                await message.channel.send(f"'{anahtar}' bilgisi '{yeni_deger}' olarak güncellendi. 🔁")
            else:
                await message.channel.send(f"'{anahtar}' bilgisi bulunamadı. Eklemek istersen `!ekle` komutunu kullanabilirsin.")
        except ValueError:
            await message.channel.send("Kullanım: `!degistir <anahtar> <yeni_değer>`")

import requests

client.run("token")
