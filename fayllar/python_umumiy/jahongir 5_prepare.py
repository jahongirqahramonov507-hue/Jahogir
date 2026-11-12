interval_1=[3,7]
interval_2=[4,6]
a_b=3
a_o=7
b_b=4
b_o=6
if a_b<=b_o and b_b<=a_o:
    print("mavjud")
    i=a_b
    while i<=a_o:
        if b_b<=i and i<=b_o:
            print(i,end=" ")
        i=i+1
else:
    print("yo'q")
