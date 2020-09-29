# #1
# l=[]
# a,b,c=100,150,5
# for i in range(a,b+1):
#     if i%c==0:
#         l.append(i)
# print(l)
# print(len(l))

# #2
# a=[]
# def tobin(N):
#     if N>0:
#         tobin(N//2)
#         a.append(N%2)
#     print(a)

# tobin(80)

# #3_1
# (a,b,c,d,e)=(200,511,300,501,510)

# largest=a
# if b>largest:
#   largest=b
# if c>largest:
#   largest=c
# if d>largest:
#   largest=d
# if e>largest:
#   largest=e
# print (largest)

# #3_2
# (a,b,c,d,e)=(60,15,105,150,155)
# if a>b:
#     if a>c:
#         if a>d:
#             if a>e:
#                 print(a)
#             else:
#                 print(e)
#         else:
#             if d>e:
#                 print(d)
#             else:
#                 print(e)
#     else:
#         if c>d:
#             if c>e:
#                 print(c)
#             else:
#                 print(e)
#         else:
#             if d>e:
#                 print(d)
#             else:
#                 print(e)
# else:
#     if b>c:
#         if b>d:
#             if b>e:
#                 print(b)
#             else:
#                 print(e)
#         else:
#             if d>e:
#                 print(d)
#             else:
#                 print(e)
#     else:
#         if c>d:
#             if c>e:
#                 print(c)
#             else:
#                 print(e)
#         else:
#             if d>e:
#                 print(d)
#             else:
#                 print(e)

# def DtoB(num):
#     if num >= 1:
#       DtoB(num // 2)
#     print(num % 2, end='')


# number = int(input("number: "))
# DtoB(number)