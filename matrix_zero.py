# m = [[1,3,4],[23,4,5],[2,0,0]]
# c= 0
# # col = []
# # row = []
# m1 = m
# for i in range(len(m)):
#     k = m[i]
#     for j in range(len(k)):
#         if k[j] == 0:
#             # col
#             for y in range(len(m1)):
#                 m1[y][j] = 0
#                 print(j)

#             # row 
#             for l in range(len(k)):
#                 # k[l] =0
#                 m1[i][l] = 0
#                 # print(i,l)
            
#             break
#             c = 1
#         if c == 1:
#             break    
            

# print(m)

def zero():
    for i in range(len(m)):
        temp = m[i]
        for j in temp:
            if j == 0:
                print(temp.index(j))

m = [[2,3,5,3],[2,9,0,1],[3,0,4,0]]

zero()