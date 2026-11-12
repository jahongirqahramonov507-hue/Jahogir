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
