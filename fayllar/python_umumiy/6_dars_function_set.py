# n=int (input("nechta mahsulot kiritasiz: "))
# m=int(input("necchtasini ko'rsatay:  "))

# products=[]

# for i in range (n):
#     name=input("nomi: ")
#     price=int(input("narxi: "))

#     products.append({"name": name, "price": price})

# natija=sorted(products, key=lambda x : x["price"], reverse=True)
# # print(products)
# print(natija[:m])

# 2-masala
# while True:
#     a=int(input("a: "))
#     b=int(input("b: "))

#     if (a/b)>=2:
#         break
#     else:    
#         print("a soni b sonidan kamida 2 baravar katta bo'lishi shart!")
# natija=[]
# i=0
# while a>=b:
#     natija.append(str(a))
    
#     a=a/2
#     i+=1
# print(i-1)
# print("->".join(natija))

# 3-masala


# def Cashmachine(user1_harakat, user2_harakat):
#     user1, user2 = 3, 3

    
#     for i in range(len(user1_harakat)):
#         if user1_harakat[i] == "share":
#             user1 -= 1
#             user2 += 3

#         if user2_harakat[i] == "share":
#             user2 -= 1
#             user1 += 3

#     return user1, user2


# lst = input("user1: ").split()
# lst2 = input("user2: ").split()

# natija = Cashmachine(lst, lst2)
# print(natija)

    

