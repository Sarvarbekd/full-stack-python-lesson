# FUNCTION

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()

# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilb unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")
# salom_ber('sarvar')

# Funksiya yaratishning asl maqsadlaridan biri, biz unga
# qayta-qayta yangi qiymatlar bilan murajaat qilishimiz mumkin.

# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")
# salom_ber('sarvar')
# salom_ber('sanjar')

# def toliq_ism(ism, familya):
#     """Foydalanuvchi ismi va familyasini konsolga chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familyasi: {familya.title()}")
# toliq_ism('sarvar', 'xalilov')

# def yosh_hisobla(ism, yosh):
#     """Foydalanuvchini tug'ilgan yilini hisoblovchi funksiya"""
#     print(f"{ism.title()} {2023-yosh}-yili tug'ilgan.")
# yosh_hisobla('sarvar', 25)

# def kvadrat_kub(son):
#     """Foydalanuvchidan son olib uning kvadrati va kubini
#     hisoblovchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga teng\n"
#           f"{son} ning kubi {son**3} ga teng")
# kvadrat_kub(5)

# def juft_toq(son):
#     """Foydalanuvchidan son olib uni juft yoki
#     toq ekanini aniqlovchi funksiya"""
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
# juft_toq(6)

# def sonlar(son1, son2):
#     """Foydalanuvchiddan 2 ta son olib ulardan
#     kattasini konsolga chiaruvchi funksiya"""
#     if son1 > son2:
#         print(son1)
#     elif son1 < son2:
#         print(son2)
#     else:
#         print("Sonlar teng")
# sonlar(2, 2)

# def sonlar(x, y):
#     """Foydalanuvchidan ikkita son olib birinchi sonning
#     ikkinchi son darajasini chiqaruvchi funksiya"""
#     print(x**y)
# sonlar(2, 3)

# def sonlar(x, y=2):
#     """Foydalanuvchidan ikkita son olib birinchi sonning
#     ikkinchi son darajasini chiqaruvchi funksiya"""
#     print(x**y)
# sonlar(5)

# def bolinish_alomatlari(son):
#     """Sonning 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz
#     bo'linishini chiqaruvchi funksiya"""
#     for n in range(2, 11):
#         if son % n == 0:
#             print(f"{son} soni {n} ga qoldiqsiz bo'linadi.")
# bolinish_alomatlari(88)




