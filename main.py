import discord
import requests

API_KEY = "9ed4d470b65d491f947171658251004"
TOKEN = "TOKENI BURAYA EKLEYEBİLİRSİNİZ"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

kullanici_verileri = {}

@client.event
async def on_ready():
    print(f"{client.user} olarak giriş yapıldı!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()
    user = message.author

    # Basit komutlar
    if content.startswith("/merhaba"):
        await message.channel.send("/Selam!")
    elif content.startswith("/bye"):
        await message.channel.send("🙂")
    elif content.startswith("/help"):
        await message.channel.send("/çevre kirlilik , /bye , /merhaba , /help , /çevre kirlilik önlemek, /konum")
    elif content.startswith("/çevre kirlilik önlemek"):
        await message.channel.send("Çevre kirliliğinin önlenmesi için atılacak birkaç önemli adım vardır...")
    elif content.startswith("/çevre kirlilik"):
        await message.channel.send("Çevre kirliliği, doğadaki dengeyi bozan ve insan sağlığını tehdit eden bir sorundur...")
    elif content.startswith("/konum"):
        await message.channel.send("Konum gönderirseniz, o konuma en yakın geri dönüşüm alanlarını yazabilirim (Türkiye illeri için).")
    elif content.startswith("/istanbul"):
        await message.channel.send("İstanbul'daki geri dönüşüm alanları: ...")
    elif content.startswith("/atık türleri"):
        await message.channel.send("♻️ Atık Türleri: Kağıt, plastik, cam, metal, organik...")

    # Kullanıcı kayıt sistemi
    elif content.startswith("!kaydet"):
        veri = {
            "id": user.id,
            "isim": str(user),
            "takma_ad": user.nick if hasattr(user, 'nick') else None,
            "durum": str(user.status),
            "aktivite": str(user.activity.name if user.activity else "Yok")
        }
        kullanici_verileri[user.id] = veri
        await message.channel.send(f"{user.mention}, bilgilerin başarıyla kaydedildi ✅")

    elif content.startswith("!bilgilerim"):
        if user.id in kullanici_verileri:
            veri = kullanici_verileri[user.id]
            mesaj = "\n".join([f"{key.capitalize()}: {value}" for key, value in veri.items()])
            await message.channel.send(f"👤 Kullanıcı Bilgilerin:\n{mesaj}")
        else:
            await message.channel.send("Önce `!kaydet` komutu ile bilgilerini kaydetmelisin.")

    elif content.startswith("!ekle"):
        if user.id not in kullanici_verileri:
            await message.channel.send("Önce `!kaydet` yazmalısın.")
            return
        try:
            _, anahtar, *deger = content.split()
            deger = " ".join(deger)
            kullanici_verileri[user.id][anahtar] = deger
            await message.channel.send(f"{anahtar} bilgisi '{deger}' olarak eklendi ✅")
        except ValueError:
            await message.channel.send("Kullanım: `!ekle <anahtar> <değer>`")

    elif content.startswith("!sil"):
        try:
            _, anahtar = content.split()
            if user.id in kullanici_verileri and anahtar in kullanici_verileri[user.id]:
                del kullanici_verileri[user.id][anahtar]
                await message.channel.send(f"{anahtar} silindi 🗑️")
            else:
                await message.channel.send(f"{anahtar} adlı bir bilgin bulunamadı.")
        except ValueError:
            await message.channel.send("Kullanım: `!sil <anahtar>`")

    elif content.startswith("!degistir"):
        if user.id not in kullanici_verileri:
            await message.channel.send("Önce `!kaydet` komutu ile kayıt olmalısın.")
            return
        try:
            _, anahtar, *yeni_deger = content.split()
            yeni_deger = " ".join(yeni_deger)
            if anahtar in kullanici_verileri[user.id]:
                kullanici_verileri[user.id][anahtar] = yeni_deger
                await message.channel.send(f"{anahtar} bilgisi '{yeni_deger}' olarak güncellendi 🔁")
            else:
                await message.channel.send(f"{anahtar} bilgisi bulunamadı. Eklemek için `!ekle` kullan.")
        except ValueError:
            await message.channel.send("Kullanım: `!degistir <anahtar> <yeni_değer>`")

    # Hava durumu komutu
    elif content.startswith("!hava"):
        try:
            city = message.content.split("!hava ")[1].strip()
            url = f"http://api.weatherapi.com/v1/current.json?q={city}&key={API_KEY}&lang=tr"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = data['current']['condition']['text']
                temp = data['current']['temp_c']
                city_name = data['location']['name']
                await message.channel.send(f"{city_name} için hava durumu:\n{weather}\nSıcaklık: {temp}°C")
            else:
                await message.channel.send(f"{city} için hava durumu alınamadı. Şehir adını kontrol edin.")
        except IndexError:
            await message.channel.send("Kullanım: `!hava <şehir_adı>` şeklinde olmalı.")

client.run(TOKEN)
