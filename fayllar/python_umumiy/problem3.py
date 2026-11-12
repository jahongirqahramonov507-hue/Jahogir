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
