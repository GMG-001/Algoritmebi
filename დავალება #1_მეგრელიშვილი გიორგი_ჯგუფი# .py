# #3_1
# (a,b,c,d,e)=(20,5,300,500,510)

# if (a>b) and (a>c) and (a>d) and (a>e):
#     largest=a
# elif (a<b) and (b>c) and (b>d) and (b>e):
#     largest=b
# elif (c>a) and (c>b) and (c>d) and (c>e):
#     largest=c
# elif (d>a) and (d>b) and (c<d) and (d>e):
#     largest=d
# else:
#     largest=e
# print(largest)

#3_2
(a,b,c,d,e)=(60,55,105,50,155)
if a>b:
    if a>c:
        if a>d:
            if a>e:
                print(a)
            else:
                print(e)
        else:
            if d>e:
                print(d)
            else:
                print(e)
    else:
        if c>d:
            if c>e:
                print(c)
        else:
            print(e)
else:
    if b>c:
        print(b)
    else:
        print(c)

# # 2 
# a=[]
# g=int(input('ricxvi '))
# for i in range(g):
#     b=i%2
#     a.append(b)
#     print(a)