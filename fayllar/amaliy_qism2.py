# f=open("davlatlar.txt","w")
# f.write("salom")
# f.close()

# 1.3-masala

# f=open("davlatlar.txt")

# data=f.read().split("\n")

# for qator in data:
#     raqam=qator.split(",")[0]
#     valuta=qator.split(",")[2]
#     korxona=qator.split(",")[-2]
#     davlat=qator.split(",")[-1]

#     raqam=set(raqam)

#     if len(raqam)==10:
#         raqam=qator.split(",")[0]
        
#         print(f"""{davlat}, {raqam}, {valuta}, {korxona}""")


# f.close()

# 2.1-masala

# f=open("internet.txt","w")

# f.write("salom")

# f.close()

# f=open("internet.txt")

# data=f.read().split("\n")

# for qator in data :
#     bolak=qator.split(",")
#     mac=bolak[-2].split("-")

#     for adres in mac:
#         if adres.isdigit():
#             break


#     else:
#         print(f"{bolak[0]} , {bolak[-3]}")
# f.close()

# 2.2-masala


# f=open("internet.txt")

# data=f.read().split("\n")

# new={}

# for qator in data:

#     # print(f"{qator}\n")
#     email=qator.split(",")[0]
#     davlat=email.split(".")[1]

#     if davlat not in new:
#         new[davlat]=1
#     else:
#         new[davlat]+=1
# print(new)
# f.close()


# 3.1-masala


# f=open("aholi.txt","w")

# f.write("salom insonlar")

# f.close()

# f=open("aholi.txt")

# data=f.read().split("\n")

# for qator in data:
#     t_sana=qator.split(",")[2]
#     yil=t_sana.split("-")[-1]

#     if int(yil)>=1976:
#         print(f"{qator}\n")
        
# f.close()

# 3.2-masala

# f=open("aholi.txt")

# data=f.read().split("\n")
# new={}

# for qator in data:
#     t_sana=qator.split(",")[2]
#     yil=t_sana.split("-")[-1]

#     if yil not in new:
#         new[yil]=1
#     else:
#         new[yil]+=1

# print(new)
        
# f.close()


# -------------------Vazifa ---------------------------------------

with open("mashina.txt","r") as f:
    data=f.read().split("\n")
    dct={}
    for qator in data:
        # print(f"{qator}\n")
        brand=qator.split(",")[4]
        if brand not in dct:
            dct[brand]=1
        else:
            dct[brand]+=1
# 1.1----------------------------------------------------
    natija_dct=sorted(dct,key=dct.get,reverse=True)
    birinchi = list(natija_dct)[0]

    # print(birinchi)  

# 1.2 ------------------------------------------------------
    new={}
    for qator in data:
        davlat=qator.split(",")[-1]
        brand=qator.split(",")[4]
        if brand==list(natija_dct)[0]:
            if davlat not in new:
                new[davlat]=1
            else:
                new[davlat]+=1
    natija2=sorted(new , key=new.get, reverse=True)

    kopi=list(natija2)[0]
    kami=list(natija2)[-1]
    # print(new)
    # print(kopi)
    # print(kami)


# ---------------------natijalar--------------------

print(f"eng ko'p uchragan brand - {birinchi}")
print(f"eng ko'p {kopi} da uchragan")
print(f"eng kam esa {kami} da uchragan")


        






    






