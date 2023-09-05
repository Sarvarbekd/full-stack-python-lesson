# IF-ELSE

# avtolar = ['audi', 'bmw', 'volvo', 'kia']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())


# ism = input("Ismingi nima? >>> ")
# if ism.lower() != 'ali':
#     print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
# else:
#     print("Salom Ali!")

# javob = float(input("12x6 nechiga teng? >>> "))
# if javob != 72:
#     print("Javob xato")

# yosh = int(input("Yoshingiz nechchida? >>>"))
# if yosh >= 18:
#     print('Xush kelibsiz!')
# else:
#     print('Kirish mumkin emas')

# login = input("Yangi login tanlang\n>>>")
# if len(login) >= 5:
#     print("Login qabul qilindi.")
# else:
#     print("Login kamida 5 ta belgidan iborat bo'lishi kerak.")

# yil = int(input("Tug'ilgan yilingizni kiriting: "))
# if 2023-yil < 18:
#     print(f"Siz {2023-yil} yoshda ekansiz.")
#     print("Sizga kirish mumkin emas")
# else:
#     print("Xush kelibsiz!")

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())

# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())

# user = input("ismingizni kiriting: ")
# if user.lower() == 'admin':
#     print("Xush kelibsiz Admin.Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz {user.title()}")

# print("Ikkita son kiriting!")
# son1 = float(input("Birinchi son:"))
# son2 = float(input("Ikkinchi son:"))
# if son1 == son2:
#     print("Sonlar teng.")
# else:
#     print("Sonlar teng emas.")

# son = float(input("Istalgan soningizni kiriting: "))
# if son < 0:
#     print("Manfiy son")
# else:
#     print("Musbat son")

son = float(input("Istalgan soningizni kiriting: "))
if son > 0:
    print(f"Kiritgan soningizni ildizi {son**(1/2)}")
else:
    print("Musbat son kiriting!")