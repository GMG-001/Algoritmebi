# #3_1
(a,b,c,d,e)=(200,5,300,500,510)

largest=a
if (a<b) and (b>c) and (b>d) and (b>e):
    largest=b
elif (c>a) and (c>b) and (c>d) and (c>e):
    largest=c
elif (d>a) and (d>b) and (c<d) and (d>e):
    largest=d
elif (e>a) and (e>b) and (e>c) and (e>d):
    largest=e
print(largest)

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