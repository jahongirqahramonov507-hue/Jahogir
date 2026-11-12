# film=input("film: ")
# yosh=int(input("yosh: "))
         
# if yosh<12:
#     a="Animatsiya"
#     b="Oila"
# elif 12<=yosh<=18:
#     a="Action"
#     b="Sarguzasht"
# elif 18<yosh<=60:
#     a="Drama"
#     b="Komediya"
# elif yosh>60:
#     a="Dokumental"
#     b="Klassik"
# print(f"{yosh} yoshli foydalanuvchi uchun {a} yoki {b} filmlarini tavsiya qilamiz!")

# 2-masala

# mahsulot1=float(input("mahsulot 1 narxi: "))
# mahsulot2=float(input("mahsulot 2 narxi: "))
# mahsulot3=float(input("mahsulot 3 narxi: "))

# jami= mahsulot1+mahsulot2+mahsulot3

# if jami>=500:
#     print(f"Jami narx: ${jami}")
#     print("Chegirma: 20%")
# elif 200<=jami:
#     print(f"Jami narx: ${jami}")
#     print("Chegirma: 15%")
# elif jami>=100:
#     print(f"Jami narx: ${jami}")
#     print("Chegirma: 10%")
# else:
#     print(f"Jami narx: ${jami}")
#     print("Chegirma: 0%")

# 3-masala

# while True:    
#     C = input("C: ")

#     if C.islower() == "exit":
#         exit()

#     F = float(C) * (9/5) + 32

#     if F <= 32:
#         print("Muzlash!")
#     elif F>=85:
#         print("Issiq!")
#     else:
#         print("Yaxshi kun!")

# 4-masala

# yosh=int(input("yosh: "))
# obuna=float(input("obuna yillari: "))

# narx=15
# print(f"Asosiy narx: $15")
# if yosh>=50:
#     narx*=0.8
#     print("yosh bo'yicha chegirma 20%")
    
# if obuna>=5:
#     narx*=0.85
#     print("obuna davomiyligi bo'yicha chegirma: 15%")
# elif obuna>=3:
#     narx*=0.9
#     print("obuna davomiyligi bo'yicha chegirma: 10%")



# print(f"yakuniy narx: ${narx}")

# 5-masala

# while True:
    
#     parol=input("parol: ")

#     raqam,Kharf,belgi= False,False,False
#     for i in parol:
#         if i.isupper():
#             Kharf=True

#         if i.isdigit():
#             raqam=True

#         if i in "@#$":
#             belgi=True
    
#     if len(parol)<8:
        
#         print("kamida 8 ta belgi bo'lsin!")

#     if not raqam:
#         print("kamida bitta raqam bo'lsin!")

#     if not Kharf:
#         print("kamida bitta katta harf bo'lsin")
#     if not belgi:
#         print("kamida bitta bu @ , # , $ belgilardan bo'lsin")

#     if len(parol) >= 8 and raqam and Kharf and belgi:
#         break
    

# print("parol kuchli")
    
# 6-masala

# for i in range(3):
#     kompaniya = input(f"Kompaniya {i+1}: ")
#     narx = float(input("Narx: "))

#     if narx > 100:
#         print(f"{kompaniya} aktsiyasi qimmat.")
#     elif narx < 50:
#         print(f"{kompaniya} aktsiyasi arzon.")
#     else:
#         print(f"{kompaniya} aktsiyasi o'rtacha.")
    
    

