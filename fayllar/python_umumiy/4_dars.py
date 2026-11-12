# lst=["111","1212",'2343','999']
# natija=max(lst,key=int)

# natija=max(lst,key=lambda x: x[-1])

# # natija=max(lst,key=lambda x : sum([int(i) for i in x]))


# print(natija)

# --------------------------------------------------------------

# son=int(input("son: "))

# print("musbat") if son>0 else print("nolga teng") if son==0 else print("manfiy")


# ----------------------------------------------------------------

# lst=[i for i in range(10)]

# print(lst)

# lst=[ int(i) for i in ["22","11","221"] if int(i)!=0]

# print(lst)

# print("$- ".join(["salom","alama","asdd"]))
# lst = [ i if i in "auieo" else 0 for i in "salom"]
# print(lst)
# lst=[i.lower() if i.isupper() else i.upper() for i in input(">>> ")]

# print(lst)

# --------------------------------------- VAZIFALAR -------------------------------------------------

# 1-masala

# lst=[1,2,33,5,6,7,7]

# n=int(input("n: "))

# for i in range(len(lst)):
#     for j in range(i+1 , len(lst)):
#         if lst[i] + lst[j]== n:
#             print(f"{i}, {j}")

# # 2-masala

# lst=[1,4,6,8]

# new=[]

# for i in lst:
#     new.append(i*2)
# print(new)

# 3-masala

# lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# for index, value in enumerate(lst):
#     value=list(value)
#     value[-1]=100
#     value=tuple(value)
#     lst[index]=value
# print(lst)

# 4-masala

# lst = [(), (), ('',), (), ('a', 'b'), (), ('a', 'b', 'c'), (), ('d',)]

# # for toplam in lst.copy():
# #     if len(toplam)==0:
# #         lst.remove(toplam)
# # print(lst)

# 5-masala

# lst = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

# natija = sorted(lst, key=lambda x: float(x[1]), reverse=True )

# print(natija)

# 6-masala

# s = "python 3.0"
# lst=list(s)

# lst=tuple(lst)
# print(lst)

# 7-masala

# lst = [1, 2, 3, 4]
# a = "emp"
# new=[]

# for i in lst:
#     b=str(i)
#     b=a+b
#     new.append(b)
# print(new)

# 8-masala

# gap = "salom aziz qalaysan"
# sozlar =gap.split()

# sozlar.sort(key=len)
# print(sozlar)

# 9-masala

# lst = [12, 'salom', 4.5, 'dunyo', True]

# # # new=[]
# # # for i in lst:
# # #     if type(i)==str:
# # #         new.append(i)
# # # new.sort()

# new=sorted(i for i  in lst if type(i)==str)

# print(new)


# 10-masala

# t = (-3, 5, 0, 9, -1, 4)

# t=list(t)
# new=[i for i in t if i>0]
# print(tuple(new))

# 11-masala

# lst = ['salom', 23, 'dunyo', 5, 100, 'python']

# new_s=sorted([i  for i in lst if type(i)==str])
# new_r=sorted([i for i in lst if type(i)==int ],reverse=True)

# print(new_r)
# print(new_s)

# 12-masala

# lst = [(3, 10), (1, 20), (2, 30)]

# natija=sorted(lst, key=lambda x : int(x[0]))

# print(natija)

# 13-masala
# lst = [1, 2, 3, 4]

# for i in range(len(lst)):
#     lst[i]=lst[i]**2
# print(lst)

# 14-masala

# lst = ['salom', 'dunyo', 'python']

# for index, value in enumerate(lst):
#     lst[index]=value.title()    
# print(lst)

# 15-masala

# t = (1, 2, 3, 4, 5)
# t=list(t)

# new=sum(i for i in t)

# print(new)
























