# RO'YXATLAR BILAN ISHLASH

# cars = ['bmw', 'mercedes benz', 'malibu', 'general motors', 'volvo']
# cars.sort()
# print(cars)

# cars = ['bmw', 'mercedes benz', 'volvo', 'generel motors', 'audi']
# cars.sort(reverse=True)
# print(cars)

# sort() metodi ro'yxatni tartiblaydi. Ba'zida esa ro'yxat ichidagi
# elementlarnining ketma-ketligini buzmagan holda ro'yxatni tartiblash
# talab qilinishi mumkin.Buning uchun sorted() funktsiyasidan
# foydalanamiz.

# mehmonlar = ['Odil', 'Anvar', 'Sarvar', 'Sanjar']
# print("sorted() qaytargan ro'yxat: ", sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi: ", mehmonlar)

# ages = [12, 14, 16, 18, 4, 7]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

# fruits = ['pear', 'banan', 'apple', 'orange']
# fruits.reverse()
# print(fruits)

# Ro'yxatning uzunligini bilish uchun len() funktsiyasidan foydalanamiz.

# fruits = ['pear', 'banan', 'apple', 'orange']
# print("Elementlar soni:", len(fruits))

# sonlar = list(range(0,10))
# print(sonlar)

# range() yordamida qadamni ham berishimiz mumkin.

# juft_sonlar = list(range(0, 20, 2))
# toq_sonlar = list(range(1, 20, 2))
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# narhlar = [12000, 15000, 9000, 13000]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, "\nEng qimmat narh ", qimmat, "\nJami ", jami)


# cars = ['bmw', 'volvo', 'gm', 'audi', 'tesla']
# may_cars = cars[0:3]
# print(may_cars)

# Ro'yxatdan nusxa olish
# sonlar = [1, 2, 3, 4, 5]
# sonlar2 = sonlar[:]
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)

# TUPLES-O'ZGARMAS RO'YXAT
# tomonlar = (20, 30, 55.2)
# print(tomonlar)
# print(tomonlar[0])

# toys = ('bus', 'car', 'bear', 'dino')
# print(toys[0])
# print(toys[-1])
# print(toys[2:4])

# Keling tuple ichidagi biror qiymatni o'zgartirib ko'ramiz
# toys = ('bus', 'bear', 'car', 'dino')
# toys[3] = 'dragon'

# toys = ('bus', 'car', 'bear', 'dino')
# toys = list(toys)
# toys.append('dragon')
# toys.append('sasha')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys)
# print(toys)

# davlatlar = ['uzbekistan', 'america', 'pokiston', 'hindiston', 'canada']
# print(davlatlar)
# print("Ro'yxatning uzunligi: ", len(davlatlar))
# print("Tartiblangan holda: ", sorted(davlatlar))
# print("Teskari tartibda: ", sorted(davlatlar, reverse=True))
# print("Asl ro'yxat:", davlatlar)
# davlatlar.reverse()
# print("Ro'yxatni oxiridan boshiga qarab chiqishi: ", davlatlar)
# davlatlar.sort()
# print("Alifbo tartibida: ", davlatlar)
# davlatlar.sort(reverse=True)
# print("Alifboga teskari tartibda: ", davlatlar)

# juft_sonlar = list(range(120, 1200, 2))
# print("120 dan 1200 gacha bo'lgan juft sonlar ro'yxati:\n", juft_sonlar)
# yigindi = sum(juft_sonlar)
# print("Ro'yxatning yig'indisi: ", yigindi)
# katta = max(juft_sonlar)
# kichik = min(juft_sonlar)
# ayirma = katta-kichik
# print("Ro'yxatdagi eng katta va kichik sonlarni ayirmasi: ", ayirma)
# print("Elementlar soni:", len(juft_sonlar))
# print(juft_sonlar[:20])
# print(juft_sonlar[-20:])
# print(juft_sonlar[530:550])

taomlar = ['osh', 'mastava', 'manti', 'somsa', 'shashlik']
nonushta = taomlar[:]
print(nonushta)
nonushta.remove('osh')
nonushta.remove('manti')
nonushta.remove('shashlik')
print(nonushta)
nonushta.append("saryog'")
nonushta.append('tuxum')
print("Taomlar:", taomlar, "\nNonushta:", nonushta)








