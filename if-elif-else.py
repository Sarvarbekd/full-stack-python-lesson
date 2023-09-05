# IF-ELIF-ELSE

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4:
#     print("Sizga kirish bepul")
# elif yosh <= 12:
#     print("Sizga kirish 5000 so'm")
# else:
#     print("Sizga kirish 10000 so'm")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# else:
#     price = 10000
#
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun qanday kun? ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print(f"Bugun {kun} dam olish kuni.")
# else:
#     print(f"Bugun {kun} ish kuni.")

# kun = input("Bugun qanday kun? ")
# harorat = float(input("Havo harorati qanaqa? "))
# if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
#     print(f"Bugun {kun} dam olish kuni ekan, harorat ham {harorat} ekan."
#           f"\nCho'milgan borsak bo'ladi.")
# else:
#     print("Uyda dam olamiz.")

# narh = 15000
# choy = True
# salat = False
#
# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
#
# print(f"Jami {narh} so'm bo'di")

# narh = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
#
# if choy:
#     print("Mijoz choy oldi")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi")
#     narh = narh + 3000
# if kompot:
#     print("MIjoz kompot oldi")
#     narh = narh + 8000
# if assorti:
#     print("Mijoz assorti oldi")
#     narh = narh + 10000
#
# print(f"Jami {narh} so'm bo'ldi")

# menu = ['osh', 'shashlik', 'qozonkabob', 'mastava']
# ovqat = input("Nima ovqat yeysiz? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print("Kechirasiz bizda bunday ovqat yo'q.")

# menu = ['osh', 'mastava', 'somsa']
# ovqat = input("NIma ovqat yeysiz? ")
# if ovqat.lower() not in menu:
#     print("Kechirasi bunday ovqat yo'q")
# else:
#     print("Buyurtma qabul qilindi")

# menu = ['osh', 'mastava', 'somsa', 'manti']
# buyurtmalar = ['osh', 'somsa', 'shashlik', 'qozonkabob']
#
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz menuda {taom} yo'q")


# menu = ['osh', 'mastava', 'somsa', 'manti']
# buyurtmalar = ['osh', 'somsa', 'shashlik', 'qozonkabob']
#
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz menuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <= 4 or yosh >= 60:
#     narh = 0
# elif yosh <= 18:
#     narh = 10000
# else:
#     narh = 20000
#
# print(f"Sizga kirish {narh} so'm")

# print("Ikkita son kiriting!")
# son1 = float(input("1-son: "))
# son2 = float(input("2-son: "))
# if son1 == son2:
#     print(f"{son1} va {son2} o'zaro tengdir.")
# elif son1 > son2:
#     print(f"{son1} > {son2}")
# else:
#     print(f"{son1} < {son2}")


# mahsulotlar = ['sabzi', 'piyoz', 'guruch', 'kartoshka', 'banan', 'non', 'tuz', 'un']
# savat = []
# print("Mahsulotlar ro'yxatini kiriting!")
#
# for n in range(5):
#     savat.append(input(f"{n+1}-mahsulotni kiriting: "))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Bizda {mahsulot} bor")
#     else:
#         print(f"Bizda {mahsulot} yo'q")


# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print(f"Do'konimzda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar bor.")


# users = ['sarvar', 'sardor', 'sanjar', 'odil', 'nodir']
# login = input("Yangi Login tanlang: ")
# if login in users:
#     print(f"{login.title()} logini band")
# else:
#     print(f"Xush kelibsiz {login.title()}")


# son = int(input("Istalgan butun son kiriting: "))
# for n in range(2, 11):
#     if son % n == 0:
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi")



