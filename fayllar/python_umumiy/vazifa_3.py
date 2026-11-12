# # 1-masala

# a=[1,3,54,2,"s","salaom"]

# print(a)
# sanoq=0
# for i in a:
#     if type(i)==int:
#         sanoq+=1
# print(sanoq)

# 2-masala

# a=[1,3,54,2,38,387,2,1]

# print(max(a))

# 3-masala

# a=[]

# for i in range(int(input("n: "))):
#     a.append(input("element: "))
# print(a)
# count=0
# for i in a:
#     if len(i)>=2:
#         if i[0]==i[-1]:
#             count+=1
# print(count)

# 4 - masala

# a=[]

# for i in range(int(input("n: "))):
#     a.append(input("element: "))
# print(a)
# new=[]
# for i in a:
#     new.append(type(i))
# print(new)

# 5-masala

# a=[1,2,3,4,5,6,7,8,9]
# b=a.copy()
# new=[]

# for i in b:
#     if i%2==0:
#         new.append(i**2)
        
#     else:
#         new.append(i**3)

# print(new)

# 6-masala

# a=[]

# for i in range(int(input("n: "))):
#     a.append(input("element: "))
# print(a)
# a.sort(reverse=True)

# print(a)
# print(a[1])

# 7-masala

# a=[1,2,3,4,5,6,7,8]
# b=[11,22,33,44,55]

# orta1=sum(a)/len(a)
# orta2=sum(b)/len(b)

# orta_um=(orta1+orta2)/2
# print(f"{orta_um:.2f}")

# 8-masala

# a=["salom","g'ani","sarvar", "ava","arra"]

# for i in a:
#     if i==i[::-1]:
#         print(f"{i}-> palindrom")
#     else:
#         print(f"{i}-> palindrom emas")

# 9-masala

# a=["m","n"]
# new=[]
# n=int(input("n: "))

# for i in range(n):
#     b=str(i+1)
#     new.append("m"+b)
#     new.append("n"+b)
# print(new)

# 10-masala

# a=[1,2,3,4,5,9999,7,8]

# b=a.copy()
# b.sort()

# tes=a.copy()
# tes.sort(reverse=True)

# if a==b:
#     print("o'sish")
# elif a==tes:
#     print("kamayish")
# else:
#     print("tartibsiz")

# 11-masala

# a=[]

# for i in range(int(input("n: "))):
#     a.append(int(input("element: ")))
# print(a)

# count=0
# for i in a:
#     if i==0:
#         a.remove(i)
#         count+=1
# for i in range(count):
#     a.append(0)
# print(a)

# 12-masala

# a=[[1,2,3],[4,5,6],[7,8,9]]

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         if j%2!=0:
#             a[i][j]=a[i][j]**2
# print(a)

# 13-masala

# a=[10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# a[2][2].append(7000)

# print(a)





def qoshish(a, b):
    return a + b

def kopaytirish(a, b):
    return a * b

def bolish(a,b):
    return a/b
