# name = input("Ismingizni kiriting: ")
# second = input("Familiyangizni kiriting: ")
# natija = name[:3] + second[:4]
# natija = natija.lower()
# print(natija)


# M18
# son = int(input())
# print(natija:=son // 100 % 10)

# son = input()
# print(son[len(son)//2])

# M19
# son = input("s: ")
# natija = son[0]*2+son[1]*2+son[2]*2+son[3]*2  "5"*2 -> belgi 2 marta takrorlanadi

# print(natija)

# U5
# print("BILET: [40000]")
# odam_soni = int(input("Nechta bilet kerak: "))
# print(f"Jami to'lov: {40000*odam_soni}")

# U6
# kitob_nomi = input()
# kitob_nomi = kitob_nomi.title()
# print("%30s -> %d" %(kitob_nomi, len(kitob_nomi))) # tekkislagich %30

# kitob_nomi = input()
# kitob_nomi = kitob_nomi.title()
# kitob_nomi = kitob_nomi.center(30)
# print(kitob_nomi)


# ism ="jahongir"
# ism=ism.title()
# ism = ism.center(30)

# print(f"|{ism}|")


# kitob_nomi = input(">>> ").title().center(30)
# print(kitob_nomi)


# U10
# harf = input("Harf kiriting: ")
# print(chr(ord(harf)+3))


# -------------------------------------------------------------------------------------


# method   =   function

# ''
# ""
# str()
# f""
# input()
# ''''''
# """"""
# a = "salom"
# a[:]


# matn = "+998-90-902-22-12"
# matn = matn.replace("-", "/")
# print(matn)

# matn = "Salom kim nima qachon Salom telegram instagram salom gramula Salom"
# # matn = matn.replace("gram", "#"*len("gram"))
# matn = matn.lower().replace("salom", "hi")
# print(matn)

# -----------------------------------

# data = input().strip()
# print(data)

# old = "y1234"
# new = input().strip().lower()
# if old == new:
#     print("Welcome")
# else:
#     print("Block")

# ------------------------------------

# print(natija:=input().count("a"))
# students = "Karim,Vali,Axmadxo'ja,Sarvarbek,Odilxo'ja"
# print(students.count("xo'ja"))

# ------------------------------------

# matn = "salom dunyo kim nima qachon"
# natija = matn.split() # " " yoki "\n" bo'yicha chopadi
# natija = matn.split("a")
# print(natija)

# ------------------------------------

# data = input()
# if data.isdigit():
#     data = int(data)
# else:
#     print("son kiritmadingiz")


# print(ism.center(100,'@'))
# print()
# print(ism.center(100,'*'))


# ---------------------------------------------------------------------------------------------------------------------------------------

# method   =   function

# ''
# ""
# str()
# f""
# input()
# ''''''
# """"""
# a = "salom"
# a[:]


# matn = "+998-90-902-22-12"
# matn = matn.replace("-", "/")
# print(matn)

# matn=matn.replace("/" , "#")
# print(matn)

# matn = "Salom kim nima qachon Salom telegram instagram salom gramula Salom"
# matn = matn.replace("gram", "#"*len("gram"))
# # # matn = matn.lower().replace("salom", "hi")
# # print(matn)
# matn=matn.lower().replace("sal","*"*len("sal"))
# print(matn)
# # -----------------------------------

# data = input().strip()
# print(data)

# old = "y1234"
# new = input().strip().lower()
# if old == new:
#     print("Welcome")
# else:
#     print("Block")

# ------------------------------------

# print(natija:=input("salom: ").count("a"))
# students = "Karim,Vali,Axmadxo'ja,Sarvarbek,Odilxo'ja"
# print(students.count("xo'ja"))
# print(students.count("a"))

# ------------------------------------

# matn = "salom dunyo kim nima qachon"
# natija = matn.split() # " " yoki "\n" bo'yicha chopadi
# natija = matn.split("a")
# print(natija)
# print(natija:=matn.split("n"))
# # ------------------------------------

# data = input()
# if data.isdigit():
#     data = int(data)
# else:
#     print("son kiritmadingiz")

# -----------------------------------------------------------------------------------------------
# import random 

# # son= random.randint(1,100)
# # print(son)

# b=random.randint(1,100)

# while True:
#     a=int (input("son: "))

#     if a==b:
#         break
#     elif a>b:
#         print("bu katta")
#     elif b>a:
#         print("bu kichik")
    


# ---------------------------------------------------------------------

#   MASALALAR

# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))
# c=int (input("c sonni kiriting: "))

# if a<=b<=c or c<=b<=a:
#     print("ha")
# else :
#     print("yo'q")


# 11-masala

# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))
# c=int (input("c sonni kiriting: "))

# i=0
# if a>0:
#     i+=1
# if b>0:
#     i+=1
# if c>0:
#     i+=1
# print(f"{i} tasi musbat ")

# 12-masala

# a=int (input("a sonni kiriting: "))
# # b=int (input("b sonni kiriting: "))
# # c=int (input("c sonni kiriting: "))# 

# mini=min(a,b,c)

# if mini==a:
#     print(b+c)
# if mini==c:
#     print(b+a)
# if mini==b:
#     print(a+c)

# 13-masala

# a=int(input("a: "))

# count=0

# # for i in  range(1,a+1):
# #     if a%i==0:
# #         count+=1

# # if count==2:
# #     print("tub son")
# # else:
# #     print("tub emas")

# i=1

# #  2-usul

# # while i!=a+1:
# #     if a%i==0:
# #         count+=1
# #     i+=1

# # if count==2:
# #     print("tub son")
# # else:
# #     print("tub emas")

# # 3-usul while true
# while True:
#     if i ==a+1:
#         break
#     if a%i==0:
#         count+=1
#     i+=1

# if count==2:
#     print("tub son")
# else:
#     print("tub emas")

# 14-masala


# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))

# if a%2!=0 and b%2!=0:
#     print("ikkisi ham toq")

# 15-masala

# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))

# if a%2!=0 and b%2!=0:
#     print("ikkisi ham toq")
# elif a%2!=0 and b%2==0:
#     print("faqat a toq")
# elif b%2!=0 and a%2==0:
#     print("faqat b toq")

# else:
#     print("ular juft")

# 16-masala


# a=int (input("a sonni kiriting: "))
# b=int (input("b sonni kiriting: "))
# c=int (input("c sonni kiriting: "))

# if a>0:
#     print("a musbat")

# if b>0:
#     print("b musbat")
# if c>0:
#     print("c musbat")

# 17-masala

# a=int(input("a: "))

# if a%2==0:
#     print("juft",end="")
#     if a//10!=0 and (a//10)//10==0:
#         print(" va ikki xonali")
#     else:
#          print(" lekin ikki xonali emas")
# else: 
#     print("juft emas", end="")
#     if  a//10!=0 and (a//10)//10==0:
#             print(" lekin ikki xonali")
#     else:
#              print(" lekin ikki xonali emas")

# 18-masala

# a=int(input("a: "))

# if a%2==0:
#     print("juft",end="")
#     if a//10!=0 and (a//10)//10!=0 and ((a//10)//10)//10==0:
    
#         print(" va uch xonali")
#     else:
#         print(" lekin uch xonali emas")
# else: 
#     print("toq", end="")
#     if a//10!=0 and (a//10)//10!=0 and ((a//10)//10)//10==0:
#             print(" va uch xonali")
#     else:
#         print(" lekin uch xonali emas")

# 19-masla

# a=int(input("a (uch xonali): "))

# b=a//10

# c=b//10
# s=b%10
# d=a%10

# # print(f"{c},{d},{s}")
# #  a=c s d

# if c==d==s:
#     print("bir xil ")
# else:
#     print("bir xil emas")

# 20-masala

# a=int(input("a (1-999 oraliqda): "))

# if a>0 :
#     print("musbat " ,end="")
# elif a<1:
#     print("aytilgan sonni kirit!")

# i=1


# while a//10!=0:
#     a=a//10
#     i+=1
# print(f" {i} xonali")

# 21-masala

# a=int(input("a (uch xonali): "))

# b=a//10

# c=b//10
# s=b%10
# d=a%10


# #  a=c s d

# if c<s<d :
#     print("o'sish tartibida")

# elif c>s>d:
#     print("kamayish tartibida")
# else:
#     print("unaqa emas")


