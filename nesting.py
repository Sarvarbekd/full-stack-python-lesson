# NESTING

car_0 = {
    'model':'lacetti',
    'rang':'oq',
    'yil':2018,
    'narh':14000,
    'km':50000,
    'korobka':'avtomat'
}

car_1 = {
    'model':'nexia 3',
    'rang':'qora',
    'yil':2022,
    'narh':12000,
    'km':10000,
    'korobka':'mexanika'
}

car_2 = {
    'model':'gentra',
    'rang':'qizil',
    'yil':2021,
    'narh':14000,
    'km':15000,
    'korobka':'mexanika'
}
# Agar biz har luga'tga alohida murajaat qilsak,
# luga'tlarning nomlarini yodlab qolishimiz talab qilinar edi.

# car = car_0
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang,"
#       f"{car['yil']}-yil, {car['narh']}$")
#
# car = car_1
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang,"
#       f"{car['yil']}-yil, {car['narh']}$")
#
# car = car_2
# print(f"{car['model'].title()}, "
#       f"{car['rang']} rang,"
#       f"{car['yil']}-yil, {car['narh']}$")
# Keling, barcha avtolarni bitta ro'yxatga joylaymiz va
# for tsikli yordamida birma-bir konsolga chiqaramiz.

# cars = [car_0, car_1, car_2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#           f"{car['rang']} rang, "
#           f"{car['yil']}-yil, {car['narh']}$")
# Endi ishimiz bir muncha yengillashdi va kodimiz ham qisqardi.
# Endi biz ro'yxat ichidagi istalga nlug'atga indeks bo'yicha
# murajaat qilaolamiz, nomini yodlab olishimiz shart emas.

# print(cars[0])

# Biror lug'atdagi elementga murajaat qilish uchun esa
# quyidagi usuldan foydalanishimiz mumkin.
# print(cars[0]['model'])
# print(f"{cars[2]['rang'].title()} {cars[2]['model']}")

# For tsikli yordamida biz bo'sh lug'atlar ro'yxatini ham yaratib olishimiz mumkin.
# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil':2021,
#         'narh':None,
#         'km':0,
#         'korobka':'avto'
#     }
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
# for malibu in malibus[6:]:
#     malibu['rang'] = 'oq'
#     malibu['korobka'] = 'mexanika'
#
# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 35000
#     print(malibu)


# dasturchilar = {
#     'sarvar':['python', 'c++'],
#     'sanjar':['html', 'css', 'js'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'tohir':['c++', 'c#']
# }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())

# Pythondagi print() funksiyasi jar bir marndan so'ng yangi qator tashlaydi.
# Buni olish uchun quyidagi usuldan foydalanish mumkin:

# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper(), end=' ')

# Lug'at ichida lug'at
# Bunday qilish tavsiya etilmasada, istisno holatlarda lug'at
# ichidagi qiymatlarni lug'at korinishida ham saqlash mumkin.

# hamkasblar = {
#     'ali':{
#         'familya':'valiyev',
#         'tyil':1997,
#         'malumot':'oliy',
#         'tillar':['python', 'c++']
#     },
#     'vali':{
#         'familya':'aliyev',
#         'tyil':1998,
#         'malumot':"o'rta-maxsus",
#         'tillar':['html', 'css', 'js']
#     },
#     'hasan':{
#         'familya':'husanov',
#         'tyil':1999,
#         'malumot':'oliy',
#         'tillar':['python', 'php']
#     }
# }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. Ma'lumoti {info['malumot']}."
#           f"\nU quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())


# person1 = {
#     'ism':'alisher navoiy',
#     'tyil':1441,
#     'tjoy':'hirot',
#     'umr':60,
#     'asarlar':['layli va majnun', 'hayrat-ul abror']
# }
#
# person2 = {
#     'ism':'erkin vohidov',
#     'tyil':1936,
#     'tjoy':"farg'ona",
#     'umr':80,
#     'asarlar':['oltin devor', 'nido dostoni']
# }
#
# person3 = {
#     'ism':'muhammad yusuf',
#     'tyil':1954,
#     'tjoy':'andijon',
#     'umr':47,
#     'asarlar':['vatanim', "lolaqizg'aldog'", 'turkman qiz']
# }
#
# person4 = {
#     'ism':'abdullo oripov',
#     'tyil':1939,
#     'tjoy':'qarshi',
#     'umr':77,
#     'asarlar':['madhiya', "o'zbekiston vatanim manim",]
# }
#
# persons = [person1, person2, person3, person4]
# for person in persons:
#     print(f"\n{person['ism'].title()}, {person['tyil']}-yilda, "
#           f"{person['tjoy'].title()}da tug'ilgan. U {person['umr']} yil umr ko'rgan."
#           f"\n{person['ism'].title()} quyidagi asarlarni yozgan:")
#     for asar in person['asarlar']:
#         print(asar.upper())


# kinolar = {
#     'sarvar':['terminator', 'rambo', 'titanic'],
#     'sanjar':['tenet', 'inception', 'intersteller'],
#     'nodir':['abdullajon', 'bomba', 'shaytanat'],
#     'qodir':['mahallada duv-duv gap', 'john wick', 'chingachkuk']
# }
# for ism, kinolar in kinolar.items():
#     print(f"{ism.title()}ning sevimli kinolari:")
#     for kino in kinolar:
#         print(kino.title())


davlatlar = {
    "o'zbekiston":{
        'poytaxt':'toshkent',
        'hududi':'448978 kv.km',
        'aholisi':33_000_000,
        'valyuta':"so'm"
    },

    'rossiya':{
        'poytaxt':'moskva',
        'hududi':'17098246 kv.km',
        'aholisi': 144_000_000,
        'valyuta':'rubl'
    },

    'aqsh':{
        'poytaxt':'washington',
        'hududi':'9631418 kv.km',
        'aholisi':327_000_000,
        'valyuta':'dollar'
    }
}


# for davlat, info in davlatlar.items():
#     if davlat.lower() == 'aqsh':
#         davlat = davlat.upper()
#     else:
#         davlat = davlat.capitalize()
#     print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi:{info['hududi']}\nAholisi:{info['aholisi']}"
#           f"\nPul birligi:{info['valyuta']}")


# user = input("Qaysi davlat haqida ma'lumot bilmoqchisiz?:").lower()
# if user in davlatlar:
#     info = davlatlar[user]
#     print(f"\n{user.title()}ning poytaxti {info['poytaxt'].title()}"
#           f"\nHududi:{info['hududi']}\nAholisi:{info['aholisi']}"
#           f"\nPul birligi:{info['valyuta']}")
# else:
#     print(f"Kechirasiz, bizda {user.title()} davlati haqida ma'lumot yo'q.")




