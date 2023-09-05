# LUG'AT ELEMENTLARI BILAN ISHLASH

# items() metodi
# Ushbu metod yordamida lug'at ichidagi barcha kalit-qiymat juftliklarini ko'rishimiz mumkin.

# talaba = {
#     'ism':'sarvar',
#     'familya':'xalilov',
#     'yosh':'25',
#     'fakultet':'matematika',
#     'kurs':4
# }
# print(talaba.items()) # Bu metodni to'g'ridan-to'g'ri emas, for tsikli
# yordamida chiqarish orqali lug'atdagi barcha elementlarni tushanarliroq
# shaklda ko'rishimiz mumkin.

# for kalit, qiymat in talaba.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")


# telefonlar = {
#     'sarvar':'samsung A32',
#     'sanjar':'iphone x',
#     'olim':'mi 10 pro',
#     'nodir':'nokia'
# }
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

# Agar lug'atdagi kalit so'zlarni ko'rish talab qilinsa keys() metodidan foydalanishimiz mumkin.

# mahsulotlar = {
#     'olma':10000,
#     'anor':15000,
#     'shaftoli':6000,
#     'anjir':8000,
#     'uzum':30000
#
# }
# print(mahsulotlar.keys())
# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot)

# bozorlik = ['anor', 'uzum', 'non', 'bodom']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
#
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningnizga {buyum} ham olib keling.")

# Lug'at lementlarini tartib bilan chiqarish

# print("do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# Agar lug'atdagi qiymatlarni chiqarish talab qilinsa values() metodidan foydalanamiz.

# print(mahsulotlar.values())

# telefonlar = {
#     'sarvar':'samsung A32',
#     'sanjar':'iphone x',
#     'nodir':'iphone x',
#     'olim':'galaxy s21',
#     'orif':'samsung A32',
#     'tohir':'iphone x'
# }
# print("Foydalanuvchilar ishlatadigan telefonlar:")
# for tel in telefonlar.values():
#     print(tel) # Bu yerda bir nechta foydalanuvchi bir xil telefon ishlatar ekan.
# Konsolga bularni qayta-qayta chiqarmaslik uchun biz set() funksiyasidan foydalanamiz.

# print("Foydalanuvchilar ishlatadigan telefonlar:")
# for tel in set(telefonlar.values()):
#     print(tel)

# !Pythonda set yana bitr ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta elementlarni
# saqlashga mo'ljallangan.Lug;at va ro'yxatdan farqli ravishda, set ichidagi elementlar biror tartibda saqlanmaydi
# Ularga indeks orqali murojaat qilib bo'lmaydi.

# py_iz_lu = {
#     'boolean':'mantiqiy qiymat',
#     'for':'Biror amalni qayta-qayta bajarish tsikli',
#     'if':'shartlarni tekshirish operatori',
#     'integer':'butun son',
#     'float':"o'nlik son",
#     'string':'matn',
#     'list':"ro'yxat",
#     'append':"Yangi element qo'shuvchi metod"
# }
# for kalit, qiymat in sorted(py_iz_lu.items()):
#     print(f"{kalit.title()}-{qiymat.title()}")

# davlat_poytaxt = {
#     "o'zbekiston":'toshkent',
#     'italiya':'rim',
#     'rossiya':'moskva',
#     'singapur':'sungapur',
#     'tojikiston':'dushanbe',
#     'aqsh':'washington',
#     "qirg'iziston":'bishkek',
#     "qozog'iston":'nursulton'
# }
# print("Dunyo Davlatlari:")
# for davlat in sorted(davlat_poytaxt.keys()):
#     print(davlat.upper())
# print("Davlatlarning poytaxti:")
# for poytaxt in sorted(davlat_poytaxt.values()):
#     print(poytaxt.upper())
#
# user = input("Qaysi davlatni poytaxtini bilishni istaysiz?: ").lower()
# poytaxt = davlat_poytaxt.get(user)
# if poytaxt == None:
#     print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
# else:
#     print(f"{user.upper()}ning poytaxti {poytaxt.title()}")


menu = {
    'osh':15000,
    'mastava':12000,
    'non':3000,
    'shashlik':16000,
    'manti':6000,
    'norin':9000,
    'xonim':5000,
    'salat':4000
}
print("3 ta buyurtma bering:")
buyurtma = []
for n in range(3):
    buyurtma.append(input(f"{n+1}-taom:").lower())

for taom in buyurtma:
    if taom in menu:
        print(f"{taom.title()} {menu[taom]} so'm")
    else:
        print(f"Kechirasiz, bizda {taom} yo'q")








