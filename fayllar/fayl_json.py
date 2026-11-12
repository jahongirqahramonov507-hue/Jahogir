import json
import math

# with open ("matematika.json","w") as f:
#     json.dump("salom", f)

#--------------------- masala -----------------------

# with open("matematika.json") as f:
#     data=json.load(f)

#     for shaxs in data:
#         for fan in shaxs["subjects"]:
#             if fan =="Matematika":
#                 print(shaxs["name"])
#                 break

# 3-masala

# with open("do'kon.json", "w") as j:

#     lst=[] 
#     for i in range(int(input("necta mahsulot: "))):
#         dct={"nom":input("nom: "),
#              "narx":float(input("narx: ")),
#              "son":int(input("son: "))}
#         lst.append(dct)
#     json.dump(lst,j, indent=4)

# with open("do'kon.json") as j:
#     data=json.load(j)
#     jami=[]
#     for mahsulot in data:
#         summa=mahsulot["narx"]*mahsulot["son"]
#         jami.append(summa)
#     natija=sum(jami)
#     print(f"jami: {natija} so'm")

# 4-masala

# with open("shahar.json", "w") as f:
#     lst=[] 
#     for i in range(int(input("necta shahar: "))):
#         dct={"nom":input("nom: "),
#              "aholi":float(input("aholi: "))}
#         lst.append(dct)

#     json.dump(lst,f, indent=4)
    
    
# with open("shahar.json") as f:
#     data=json.load(f)
    
#     natija=max(data, key=lambda x: x["aholi"])
#     print(natija)

# 3.1-masala

# with open("ombor.json","w") as f:
#     json.dump("salom",f)

# with open("ombor.json") as f:
#     data=json.load(f)
#     for mahsulot in data:
#         if mahsulot["is_available"] and 500<int(mahsulot["price"])<1000:
#             print(f"ID: {mahsulot['id']}  material: {mahsulot['material']}")
    


# 3.2-masala

# with open("ombor.json") as f:
#     data=json.load(f)
#     material_i=input("material: ")
#     new=[]
#     for mahsulot in data:
#         if mahsulot["is_available"] and mahsulot["material"]==material_i:
#             new.append(mahsulot)
#     natija = sorted(new, key=lambda x: x["price"])

#     print(natija)

# 3.3-masala
# with open("ombor.json") as f:
#     data=json.load(f)

#     for mahsulot in data:
#         if mahsulot["is_available"] ==False and mahsulot["price"]<1000:
#             print(f"{mahsulot['product']} - {mahsulot['material']}")
        
# ---------------- O'RTA DARAJADA--------------------------

# 6-masala


# with open("students.json","w") as f:
#     json.dump("salomat", f)

# with open("students.json") as f:
#     data=json.load(f)
#     for student in data["students"]:
#         orta=sum(student["grades"])/len(student["grades"])
#         print(f"{student['name']} : {orta}")

# 7-masala
# with open("users.json","w") as f:
#     json.dump("salom", f)

with open("users.json") as f:
    data=json.load(f)
    lst=[]
    for user in data["users"]:
        if user["role"]=="admin":
            lst.append(user["name"])
    print(lst)













