# WHILE, LIST, DICTIONARY

# ismlar = []
#
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n = 1
# while True:
#     savol = f"{n}-do'stingini ismini kiriting: "
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q: ")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         print("Do'stlaringiz ro'yxati:")
#         for ism in ismlar:
#             print(ism.title())
#         break

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
#
#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q: ")
#     if javob == "yo'q":
#         ishora = False
#
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")


# talabalar = ['husan', 'hasan', 'sarvar', 'sanjar']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho

