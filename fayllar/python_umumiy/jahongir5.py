#a)shart on = oxirgi nuqta, bn= boshlang'ich nuqta
interval_1=(5,10)
interval_2=(1,12)
interval_3=(6,8)
interval_4=(7,15)
interval_5=(4,9)
a_b, a_t = 5, 10      # interval 1
b_b, b_t = 1, 12      # interval 2
c_b, c_t = 6, 8       # interval 3
d_b, d_t = 7, 15      # interval 4
e_b, e_t = 4, 9         # interval 5
if a_t >= b_b and a_b <= b_t:
    if a_b > b_b:
        bn = a_b
    else:
        bn=b_b
    if a_t>b_t:
        on=b_t
    else:
        on=a_t
else:
    print("Umumiy nuqtalar yo'q")
    exit()

# 3-interval (c) bilan solishtirish
if on >= c_b and bn <= c_t:
    if bn > c_b:
        bn = bn
    else:
        bn = c_b
    if on > c_t:
        on = c_t
    else:
        on = on
else:
    print("Umumiy nuqtalar yo'q")
    exit()

# 4-interval (d) bilan solishtirish
if on >= d_b and bn <= d_t:
    if bn > d_b:
        bn = bn
    else:
        bn = d_b
    if on > d_t:
        on = d_t
    else:
        on = on
else:
    print("Umumiy nuqtalar yo'q")
    exit()

# 5-interval bilan solishtirish
if bn <= e_t and on >= e_b:
    if bn > e_b:
        bn =  bn
    else:
        bn = e_b
    if on > e_t:
        on = e_t
    else:
        on = on
else:
    print("umumiy interval yo'q")
    exit()
print("umumiy interval>>> (",bn,",",on,")")
