
# --------------- VAZIFA ----------------------------


# 1-masala

# grades = {
#     "Ali": 85,
#     "Vali": 78,
#     "Hasan": 90
# }
# ism=input("ism: ")
# baho=int(input("baho: "))

# if ism not in grades:
#     print("bunday talaba topilmadi")
# else : 
#     grades[ism]=baho
#     print(grades)

# 2-masala

# store = {
#     "olma": 5000,
#     "banan": 7000
# }
# mahsulot=input("mahsulot nomi: ")
# narx=int(input("narx: "))

# if mahsulot in store:
#     print("Bu mahsulot allaqachon bor")
# else :
#     store [mahsulot]=narx
#     print(store)

# 3-masala

# employees = {
#     "101": "Ali",
#     "102": "Bobur",
#     "103": "Madina"
# }

# idsi= input("ID: ")

# if idsi not in employees:
#     print("Bunday ID topilmadi")
#     print(employees)
# else : 
#     employees.pop(idsi)
#     print(employees)

# # 4-masala

# prices = {
#     "Laptop": 700,
#     "Phone": 350,
#     "Camera": 500
# }
# nom=max(prices, key=lambda kalit: prices[kalit])
# print(f"""Eng qimmat mahsulot: {nom}
# Narxi: {prices[nom]}""")

# 5-masala

# cart = {
#     "olma": 3,
#     "banan": 5,
#     "uzum": 2
# }
# natija = sum(cart.values())
# print(natija)

# # 6-masala

# student = {
#     "name": "Aziz",
#     "age": 20,
#     "contact": {
#         "phone": "+998971234567",
#         "email": "aziz@mail.com"
#     }
# }

# print("telefon raqami: ", student["contact"]["phone"])

# 7-masala

# d1 = {"olma": 5000, "banan": 7000}
# d2 = {"shaftoli": 8000, "olcha": 10000}

# # d1.update(d2)
# # print(d1)

# result=d1|d2
# print(result)

# 8-masala


# orders = [
#     {"customer": "Ali", "amount": 15000},
#     {"customer": "Vali", "amount": 22000},
#     {"customer": "Ali", "amount": 8000}
# ]

# dct={

# }
# for i in orders:
#     name=i["customer"]
#     amount=i["amount"]

#     if name in dct:
#         dct[name]+=amount
#     else:
#         dct[name]=amount

    
# print(dct)

# 9-masala

# matn=input("matn: ")
# sozlar=matn.split()

# print(sozlar)
# dct={

# }

# for soz in sozlar :
#     value=sozlar.count(soz)
#     kalit=soz
    
#     dct[kalit]=value
# print(dct)

# 10-masala

# products = {
#     "Laptop": 700,
#     "Mouse": 25,
#     "Phone": 350,
#     "Camera": 500,
#     "Keyboard": 45
# }


# dct={

# }
# for kalit , qiymat in products.copy().items():
#     if products[kalit]<100:
#         dct[kalit]=qiymat
#         products.pop(kalit)

# print(dct)
