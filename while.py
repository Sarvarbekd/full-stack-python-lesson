# WHILE LOOP

# ismlar = []
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n = 1 # Do'stlaringizni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingizni ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q): ")
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         print("Sizning do'stlaringiz ro'yxati:")
#         for ism in ismlar:
#             print(ism.title())
#         break


# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {} # Bo'sh lug'atni while yordamida to'ldiramiz.
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q: ")
#     if javob == "yo'q":
#         ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# RO'YXAT ELEMENTLARINI O'CHIRISH
# cars = ['lacetti', 'nexia', 'toyota', 'audi', 'nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH

# talabalar = ['sarvar', 'sardor', 'anvar', 'sanjar']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho

# mahsulotlar = []
# print("Buyurtmalaringizni kiriting:")
# n = 1
# while True:
#     savol = f"{n}-buyurtmangizni kiriting: "
#     buyurtma = input(savol)
#     mahsulotlar.append(buyurtma)
#     javob = input(f"Yana buyurtma qo'shasizmi? (ha/yo'q): ")
#     if javob == 'ha':
#         n += 1
#         continue
#     else:
#         print("Sizning buyurtmalaringiz:")
#         for mahsulot in mahsulotlar:
#             print(mahsulot.title())
#         break
#
#
# mahsulotlar = ['sabzi', 'kartoshka', 'non', 'nok']
# mahsulotlar_narhlari = {}
# ishora = True
# while ishora:
#     mahsulot = mahsulotlar.pop()
#     narh = input(f"{mahsulot.title()}ning narhini kiriting:")
#     mahsulotlar_narhlari[mahsulot] = float(narh)
#
#     javob = input(f"Yana ma'lumot qo'shasizmi? (ha/yo'q): ")
#     if javob == "yo'q":
#         ishora = False
# for mahsulot, narh in mahsulotlar_narhlari.items():
#     print(f"{mahsulot.title()} {narh} so'm")

# buyurtmalar = ['sabzi', 'kartoshka', 'olma', 'uzum']
# mahsulotlar = {'olma':20000, 'shaftoli':30000, 'tarvuz': 14000, 'uzum': 15000}
#
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()} {narh} so'm")
#     else:
#         print(f"Bizda {buyurtma} yo'q")












