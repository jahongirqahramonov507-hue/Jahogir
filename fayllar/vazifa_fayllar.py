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



# ---------------------natijalar--------------------

print(f"eng ko'p uchragan brand - {birinchi}")
print(f"eng ko'p {kopi} da uchragan")
print(f"eng kam esa {kami} da uchragan")


        
