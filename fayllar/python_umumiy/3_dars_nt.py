# a=[True, "salom",5,5.6]
# new=[]
# for i in a:
#     new.append(type(i))
# print(new)

# 2-masala
# a=[7,8,1,3,4,6,7,5]
# new=[]
# for i in range(len(a)):
#     if i %2==0:
#         a[i]=a[i]**2
#     else :
#         a[i]=a[i]**3
# print(a)

# 3-masala
# a=[]

# for i in range(int(input("n: "))):
#     a.append(int(input("element: ")))
# print(a)
# nol=a.count(0)
# for i in a.copy():
#     if i==0:
#         a.remove(0)
# print(a)
# for i in range(nol):
#     a.append(0)
# print(a)

#  4 - masala

# a=[]

# for i in range(int(input("n: "))):
#     a.append(int(input("element: ")))
# print(a)
# a.sort()
# print(a[1])

# 5-masala

# a=[1,3,4,5,2,4,2,2,24,4,4,4,4,5]
# new=[]

# for i in a:
#     if i not in new:
#         new.append(i)
# print(new)

# 6-masala

# a=[4,5,2,4,2,2,24,4,4,4,4,5]

# b=""

# for i in  a:
#     b+=str(i)

# print(int(b))

# 7-masala

# a=[4,5,2,4,2,2,24,4,4,4,4,5]
# b=[1,23,44,4,44,55,6,6]

# orta=((sum(a))/len(a)+(sum(b))/len(b))/2

# print(orta)

# 8-masala

# a=[]

# for i in range(int(input("n: "))):
#     a.append(input("element: "))
# print(a)

# for i in a: 
#     if i==i[::-1]:
#         print(f"{i} -> palidrom")
#     else:
#         print(f"{i} -> palindrom emas")

# 9-masala

# a=[]
# n=(int(input("n: ")))
# i=0
# while i<n:
#     element=input("element: ")
#     if len(element)>=2:
#         a.append(element)
#         i=i+1
#     else:
#         print("2+ ber")
        
# print(a)
# count=0
# for i in a:
#     if i[0]==i[-1]:
#         count+=1
# print(count)

# 10-masala


# a=[]

# for i in range(int(input("n: "))):
#     a.append(int(input("element: ")))
# print(a)

# for i in a:
#     if i%2==0:
#         a.remove(i)

# print(a)

# 11-masala

# a=[1,2,3,4,5,6,7,8,7,9]
# b=[1,23,3,4,5,89,7,6,5]

# new=[]

# for i in a.copy():
#     if i not in new:
#         if i in b:
#             new.append(i)
# for i in b.copy():
#     if i not in new:
#         if i in a:
#             new.append(i)
# print(new)

# 12-masala



# a=[]

# for i in range(int(input("n: "))):
#     a.append(int(input("element: ")))
# print(a)

# tartibli=a.copy()
# tartibli.sort()

# tes_tar=a.copy()
# tes_tar.sort(reverse=True)

# if tartibli==a:
#     print("o'sish")
# elif tes_tar==a:
#     print("kamayish")
# else:
#     print ("tartibsiz")

# 13-masala


# a = [[1,2,3], [23,4,5], [24,45], [2]]
# katta = []

# for i in range(len(a)):
#     if len(a[i]) >= 2:
#         if katta == []:
#             katta = a[i]
#         elif sum(a[i]) > sum(katta):
#             katta = a[i]

# print(katta) 

# 14-masala


# a=[]

# for i in range(int(input("n: "))):
#     a.append(int(input("element: ")))
# print(a)

# b=""

# for i in  a:
#     b+=str(i)

# b=str(int(b)+1)
# natija=[]
# for raqam in b:
#     natija.append(int(raqam))
# print(natija)





    




