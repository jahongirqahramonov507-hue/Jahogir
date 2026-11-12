# import vazifa_3

# print(vazifa_3.qoshish(4, 6))       # 10
# print(vazifa_3.kopaytirish(4, 6))
# print(vazifa_3.bolish(30,10))   

# def 
#     ko'p qatorli 
#     Ko'p martali 
#     nomi bor 
#     return ishlatsa bo'ladi 
#     ()

# lambda 
#     bir qatorli 
#     bir martali 
#     nomi yo'q 
#     return ishlatilmiydi 
#     ()()


# natija = (lambda: 5+5)()
# natija = (lambda a,b: a*b)("salom",5)
# natija = (lambda x: [soz for soz in x if soz==soz[::-1]])(["salom", "dunyo", 'kiyik'])

# natija =(lambda x: [soz for soz in x if soz==soz[::-1]])(["amma", "qara","non"])

# natija=(lambda x: print("juft") if x%2==0 else print("toq"))(2)



# natija = list(filter(lambda x: x%2==0, [1,12,34,9,0,3,2]))
# natija = list(filter(lambda x: x, [0,1,12,34,9,0,3,2]))
# natija = list(filter(lambda x: x in "aueio", "salom bolalar"))
# natija = list(filter(lambda x: x>7, [78, 5, 14, 0, 23, 3]))
# print(natija)


# natija = list(map(lambda x: x*2, [2,3,4,1]))
# natija = list(map(lambda x: int(x), input().split()))
# natija = list(map(lambda x: x%2==0, [2,1,3,4,5]))
# natija = "".join(list(map(lambda x: x.lower(), "assaLOM")))
# print(natija)





# natija = list(filter(lambda x: x>100 , [123,12,2,3,12113,3,32]))

# natija = list(filter( lambda x: x in "1234567890", "salom1 ustoz2 kechirasiz34q12345"))

# natija =list(filter ( lambda x: x%5==0, int(input())))



# natija = list(map(lambda x: x**2,[1,2,3,4,5,6,6]))
# natija =list (map(lambda x: x%2==0,[1,2,3,4,4,5,5,5,5,433,2,2,11]))
# print(natija)


# ----------------------------------------- MODULE -------------------------------------

# from vazifa_3 import * 
# print(bolish(30,15))
# print(qoshish(21,2923))
# print(kopaytirish(13,10))

# ---------------------------------------------- VAZIFA ---------------------------------
# 1-masala
# oylar = {
#     1: "yanvar",
#     2: "fevral",
#     3: "mart",
#     4: "aprel",
#     5: "may",
#     6: "iyun",
#     7: "iyul",
#     8: "avgust",
#     9: "sentabr",
#     10: "oktabr",
#     11: "noyabr",
#     12: "dekabr"
# }
# def format_date(date:str)->str:
    
#     date=date.split(".")
#     kun=int(date[0])
#     oy=int(date[1])
    

#     return  (f"{kun}-{oylar[oy]} {date[2]}-yil")

# print(format_date("01.12.2025"))

# 2-masala

# def get_top_user(data: list[tuple[str, int]]) -> str:

#     if data==[]:
#         return ""
#     else :
#         natija=max(data, key=lambda x: x[1])

#         return natija[0] 

# data = [
    # ("x",0),
    #     ("y",0)
    # ("user1", 50),
    # ("user2", 60),
    # ("user1", 40),
    # ("user3", 30)
# ]
# print(get_top_user(data))

# 3-masala

# def calculate_class_averages(scores: dict) -> dict: 
#     new={}
    
#     for sinf, ballar in scores.items():
#         if ballar==[]:
#             new[sinf] = 0
#             continue
#         meani=sum(ballar)/len(ballar)
#         butun_m=int(meani)
#         if meani-butun_m>0.5:
#             butun_m+=1

#         if sinf not in new:
#             new[sinf]=butun_m
        
            
            

#     return new

        

    

# scores = {"Class B": [96, 76, 98], "Class C": [60, 90],"class G":[]} 
# print(calculate_class_averages(scores)) 
# Output: {'Class B': 90, 'Class C': 75}



# 4-masala
# def max_movies_to_watch(movies: list) -> tuple:
#     new=[]
#     kinolar=sorted(movies, key=lambda x: x[1])
#     oxirgi_tugash=0

#     for i in range(len(kinolar)):
#         if  kinolar[i][0]>=oxirgi_tugash:
#             new.append(kinolar[i])
#             oxirgi_tugash=kinolar[i][1]
#     new.insert(0,len(new))


    
    
#     return new
        
	
    		

# movies = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)] 
# print(max_movies_to_watch(movies)) 
# # Output: (3, [(1, 4), (5, 7), (8, 9)])














