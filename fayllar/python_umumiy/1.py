# Bir qatorli izohga olish 

# sep= , o'rniga defalt " " qo'yib beradi
# end= print() yakuniga default '\n' joylalb beradi puts() kabi

# print("Salom",50,"kalxoz", sep="*")
# print("O'zbekiston")
# print(f"{5}-maktab {5+5}-sinf")
# print("""O ota makonim onajon o'lkam, jonim to'shay soyanga, 
# Senday mehribon yo'q seningdek ko'rkam rim ni alishmasman bedapoyanga""")

# ---------------------------

# a = 90
# a = "salom"
# a = [12, 45, 3]
# print(a)

# son = int(90.7) # 90
# son = int("123") # 123
# son = int("123.5") # ERROR
# son = float("123.5") # 123.5
# son = int(float("123.5")) # 123

# ---------------------------

# a = input() # o'zidan har doyim str qaytaradi
# print(f"{a} {type(a)}")

# name = input("Ismingizni kiriting: ")
# second = input("Familiyangizni kiriting: ")
# age = int(input("Yoshingizni kiriting: "))

# print(f"""Name: {name}
# Second: {second}
# Age: {age}""")

# ---------------------------

# + -> qo'shish
# - -> ayirish
# * -> ko'paytirish 
# / -> kasrli bo'lish 
# // -> butun bo'lish
# %  -> foizli bo'lish 
# ** -> darajani aniqlashga yordam beradi 

# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")
# print(f"{a} // {b} = {a//b}")
# print(f"{a} % {b} = {a%b}")
# print(f"{a} ** {b} = {a**b}")


#  1 - masala 
# day = int (input("Tug'ilgan sanangizni kiriting: "))
# month = int (input("Tug'ilgan oyingizni kiriting(1-12): "))

# print(f"Birthday is {day}-{month}!!!")

#  2-masala

# son = int (input("Sonni kiriting (3 xonali): "))
# summa=0

# while son:
#     c=son%10
#     son=son//10
#     summa +=c
# print(f"summa={summa**3}")

#  3- masala

# a=int (input("Birinchi sonni kiriting: "))
# b=int (input("Ikkinchi sonni kiriting: "))

# c=(a+b)/2  

# print(c)

#  4- masala
# a=int (input("Sonni kiriting: "))


# b=(a%10) * 10 + a//10

# print(f"teskari son: {b}")

#  5-masala

# ism=input("Ismingizni kiriting: ")
# familya= input("Familyangizni kiriting: ")

# print(f"""ism: {ism}
# familya: {familya}""")

#  6- masala

# a=int (input("Birinchi sonni kiriting: "))
# b=int (input("Ikkinchi sonni kiriting: "))


# print(f"""{a} + {b} = {a+b})
# {a} - {b} = {a-b}
# {a} * {b} = {a*b}
# {a} / {b} = {a/b}""")

# 7-masala
# harf= input ("Harfni kiriting: ")

# print(f"Alafabetda {ord(harf)}-o'rinda turadi")


#  8-masala
# word= input ("So'zni kiriting: ")

# print((len(word)**3))

# 9-masala

# yil=int(input("Tug'ilgan yilingizni kiriting: "))

# print(f"siz {2026-yil+1} yoshdasiz")


#  10- masala
# harf= input ("Harfni kiriting: ")

# # print(harf.upper())

# print(chr(ord(harf)-32))

#  11-masala

# harf= input ("Harfni kiriting: ")
# print(f"output: {chr(ord(harf)+1)}")

#  12-masala

# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))

# a,b=b,a

# print(f"a={a}")
# print(f"b={b}")

# 2-usul


# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))


# print(f"a={b}")
# print(f"b={a}")


# --------------------------------------

# 1-masala

# yil=int(input("Tug'ilgan yilingizni kiriting: "))

# print(f"siz {2026-yil+1} yoshdasiz")

#  2-masala

# sekund= int(input("sekund: "))
# print(f"{sekund} sekund = {sekund/3600} soat")

#  3 - masala

# ism=input("Ism: ")
# friend=int(input("Do'stlariz soni: "))
# print(f"{ism} ning {friend} ta do'sti bor")

# #  4 - masala

# narx = float(input("narx: "))
# soni= int("nechta oldingiz: ")

# print(f"summa={narx * soni}")

# # 5-masala

# print("---- PROFIL ----")
# print(f"""Ism: {input("ism: ")}
# Yosh: {input("yosh: ")}
# Shahar: {input("shahar: ")}""")

#  6 - masala

# son = str (input("Sonni kiriting (3 xonali): "))

# if son==son[::-1]:
#     print("Ha")
# else:
#     print("Yo'q")

# # 7-masala
# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))
# c=int (input("c sonni kiriting: "))

# if a<b<c or a>b>c:
#     print(f"{a*2},{b*2},{c*2}")

# else :
#     print(f"{a*(-1)},{b*(-1)}, {c*(-1)}")

# # 8-masala
# son=int (input("son sonni kiriting: "))

# musbat=0
# manfiy=0
# for i in range (3):
#     if son>=0:
#         musbat+=1
#     else :
#         manfiy+=1
# print(f"""manfiylar={manfiy}
# musbatlar={musbat}""")

# 9-masala
# n=int (input("n ni kiriting: "))
# katta=0
# for i in range (n):
#     son=int (input(f"{i+1}-sonni kiriting: "))
#     if i==0:
#         katta=son
#     if son>katta:
#         katta = son

# print(katta)

# komp tarmoqlari

# m=int(input())
# satr=""
# n=17

# for i in range (m):
#     a=(n and 2**i)
#     satr=satr+a
    

#  DAVOMI------------------------------------------

# 1-masala

# son=int(input())

# if son%2==0:
#     print(f"{son}-juft son")
# else :
#     print(f"{son}-toq son")

# # 3-masala

# matn=input()
# print(matn[::-1])

# # 5-masala

# son=int(input("sonni kiriting: "))

# if 100>=son>=90:
#     print("bahoyingiz -  A")
# elif 89>=son>=70:
#         print("bahoyingiz -  B")
# elif 69>=son>=50:
#         print("bahoyingiz -  C")
# elif son<50:
#         print(" bahoyingiz -  F")
# else :
#     print("Noto'g'ri ball!!!")

# # 6-masala

# id=input("ID ni kiriting: ")

# yil=id[:4]    
# raqam=id[4:]
# print(f"""yil - {yil}
# raqam - {raqam}""")

# 7-masala

# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))
# c=int (input("c sonni kiriting: "))

# if a+b<=c or b+c<=a or a+c<=b:
#     print("bunday uchburchak mavjud emas!!!")
# else :    
#     if a==b and a==c:
#         print("teng tomonli")
#     elif a==b and a!=c:
#         print("teng yonli")
#     elif a==c and a!=b:
#         print("teng yonli")
#     elif b==c and a!=c:
#         print("teng yonli")
#     else:
#         print("turli tomonli")

# 8-masala

# email=input("emailni kiriting to'liq shsaklda (masalan: ali@najottalim.uz) ")

# indeks=email.find("@")

# print(f"domen: {email[indeks+1:]}")

# 9-masala

# narx=float(input("narx: "))
# azo=bool(input("azomi? "))

# if azo:
#     narx=0.85*narx
# else:
#     narx*=0.95

# print(f"Yakuniy narx: {narx:.2f} so'm")

# 10-masala

# parol=input("parol: ")

# son_bormi=0

# if len(parol)>=8:
#     for i in range(len(parol)):
#         if parol[i] in "1234567890":
#             son_bormi+=1
#     if son_bormi==0:
#         print("raqam ham kiriting")
#     else:
#         print("yaxshi parol")
# else :
#     print("kuchsiz parol")

# 11-masala

# yosh = int(input("yoshni kiriting: "))

# if 0 <= yosh <= 12:
#     toifa = "bola"
# elif 13 <= yosh <= 19:
#     toifa = "o'smir"
# elif 20 <= yosh <= 59:
#     toifa = "kattalar"
# elif yosh >= 60:
#     toifa = "keksa"
# else:
#     toifa = "Noto'g'ri yosh"

# print(f"Yosh: {yosh}, toifa: {toifa}")

#  12-masala

# ism=input("ism: ")
# familya=input("surname: ")

# bosh_ism=ism[:1].upper()
# bosh_fam=familya[:1].upper()

# print(f"{bosh_ism}.{bosh_fam}.")

# 14-masala



# raqam=input("raqamni kiriting +998")

# print(f"+998 {raqam[:2]} {raqam[2:5]} {raqam[5:7]} {raqam[7:]}")

# 15-masala

# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))
# c=int (input("c sonni kiriting: "))

# katta=0
# kichik=0
# orta=0

# if a>b:
#     if a>c:
#         katta=a
#     orta=a

# elif a>c:
#     orta = a 
# else:
#     kichik = a   

# if c>b:
#     if c>a:
#         katta=c
#     orta=c

# elif c>a:
#     orta = c 
# else:
#     kichik = c 
# if b>c:
#     if b>a:
#         katta=b
#     orta=b

# elif b>a:
#     orta = b 
# else:
#     kichik = b 

# print(f"katta: {katta}, kichik: {kichik}, o'rta: {orta}")


#  16- masala

# demon=input("demon: ")

# oxiri=demon[demon.find(".")+1:]

# if oxiri=="uz":
#     print("uzb sayti")

# elif oxiri=="com":
#     print("international")

# 17-masala

# height=float(input("bo'y metrda: "))
# weight=float(input("vazn kg da: "))

# bmi=weight/ (height**2)

# if bmi<18.5:
#     print("kam vazn")
# elif 24.9>=bmi>=18.5:
#     print("normal")
# elif 29.9>=bmi>=25:
#     print("ortiqcha vazn")
# elif bmi>=30:
#     print("semizlik")
# else :
#     print("who are you!!!")

# 18-masala

# matn=input("matn: ")

# son = 0

# for i in matn:
#     if i in "aouei":
#         son+=1
# print(f"unlilar soni: {son}")

# 19-masala

# yosh = int( input ("yosh: "))
# talaba= bool(input("talabami: "))
# narx=2000
# if yosh <=7:
#     narx=0
    
# elif yosh >=60:
#     narx*=0.5
# elif talaba:
#     narx=0.7*narx
# print(f"umumiy narx - {narx} so'm")

# 20-masala


ism=input("Ismingizni kiriting: ")
familya= input("Familyangizni kiriting: ")

print(f"{ism[:3]}{familya[:4]}")






    
