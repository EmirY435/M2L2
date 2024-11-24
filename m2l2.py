import discord
# Discord botları için komut tabanlı bir framework sağlar. 
# Bu framework sayesinde, botumuzun belirli komutlara yanıt vermesini kolayca tanımlayabiliriz.
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True # botun mesaj içeriğine erişimini aktif hale getiriyoruz.

bot = commands.Bot(command_prefix='$', intents=intents)
#Bu özellik, botun kendisine gönderilen komutları tanıması için bir ön ek tanımlar.
#  $ işareti komut ön eki olarak belirlenmiştir. Yani bot sadece $ ile başlayan komutlara yanıt verir.

@bot.event # bot belirli bir olay gerçekleştiğinde tetiklensin.
async def on_ready(): # bot başarılı bir şekilde Discord'a bağlandığında tetiklenir
    print(f'{bot.user} olarak giriş yaptik')

@bot.command()
async def hangi_maddeler_yeniden_dönüştürülebilir(ctx):
    await ctx.send("Kâğıt, metal, motor yağları, cam, karton, alüminyum, strafor, yeşil atık, ahşap, plastik pil maddeleri geri dönüştürülebilir")
@bot.command()
async def geri_dönüşüm_süreci_nasıl_gerçekleşiyor(ctx):
    await ctx.send("Değerlendirilebilir atıklar, oluştukları yerde çöplerden ayrılarak biriktirilir. Sınıflama: Kaynağında ayrı toplanan atıklar, cam, metal-plastik ve kağıt bazında sınıflandırılır. Değerlendirme: Atıklar, fiziksel ve kimyasal değişimler geçirerek yeni bir malzeme olarak ekonomiye geri döner.")

  
bot.run("token")
