# LUG'AT BILAN TANISHUV

# car_0 = {'model':'ferrari', 'rangi':'qizil'}
# print(car_0['model'])
# print(car_0['rangi'])

# Lug'atdagi qiymatlar son, matn, ro'yxat va hatto boshqa lug'at ham bo'lishi mumkin.

# talaba = {'ism':'sarvar xalilov', 't_yil':'1998', 'yosh':'25'}
# print(f"{talaba['ism'].title()}, {talaba['t_yil']}-yilda tug'ilgan,"
#       f" {talaba['yosh']} yoshda.")
# # Lug'atga yangi kalit so'z va qiymat qo'shishimiz ham mumkin.
# talaba['kurs'] = 4
# talaba['fakultet'] = 'informatika'
# print(talaba) # Lug'atga yangi kalit so'z va qiymat qo'shdik.

# Bo'sh lug'at quyidagicha yaratiladi.
# talaba_1 = {}
# Bo'sh lug'atga quyidagicha kalit so'z va qiymat qo'shib boramiz.
# talaba_1['ism'] = 'sarvar xalilov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 25
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()}, {talaba_1['kurs']}-kursda o'qiydi."
#       f" Hozir {talaba_1['yosh']} yoshda.")

# Lug'atdagi biror juftlik kerak bo'lmasa, uni del operatori yordamida olib tashlaymiz.
# del talaba_1['kurs'] # mana shunday qilib

# Uzun lug'atlarni bir necha qatorlarga bo'lib yozishimiz mumkin.
telefonlar = {
      'sanjar':'iphone',
      'sarvar':'samsung A32',
      'nodir':'honor',
      'mansur':'nokia lumia'
}


# get() metodi
# phohe = telefonlar['sanjar']
# print(f"Sarjarning telefoni {phohe} ")

# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}") # Bu yerda KeyError beradi. Chunki lug'at yo'q bo'lgan kalitni kiritdik.

# phone = telefonlar.get('hasan', 'Bu yerda bunday ism mavjud emas.')
# print(phone)

# otam = {
#       'ism':'odiljon',
#       't_yil':'1971',
#       't_joy':'andijon'
# }
# print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda, "
#       f"{otam['t_joy'].title()} viloyatida tug'ilgan.")

# sevimli_taom = {
#       'otam':'osh',
#       'onam':'mastava',
#       'akam':'shashlik',
#       'ukam':'manti',
#       "o'zim":'moshkichiri'
# }
# print(f"Otamning sevimli taaomi {sevimli_taom['otam']}"
#       f"\nOnamning sevimli taomi {sevimli_taom['onam']}"
#       f"\nAkamning sevimli taomi {sevimli_taom['akam']}")

# py_iz_lu = {
#       'integer':'butun son',
#       'float':"o'nlik son",
#       'string':'matn',
#       'if':'agar',
#       'else':'aks holda',
#       'elif':'aks holda agar',
#       'list':"ro'yxat",
#       'dictionary':"lug'at"
# }
# # user = input("Kalit so'z kiriting: ")
# # user = py_iz_lu.get(user, "Bunday so'z mavjud emas")
# # print(user.title())
#
# kalit_soz = input("Kalit so'z kiriting:")
# if kalit_soz.lower() in py_iz_lu:
#       print(f"{kalit_soz.title()} so'zi {py_iz_lu.get(kalit_soz).title()} deb tarjima qilinadi.")
# else:
#       print("Bunday so'z mavjud emas.")






