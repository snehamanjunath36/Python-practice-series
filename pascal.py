# def printPascal(n):
#     res=[[]]
#     for i in range(0,n):
#         temp=[]
#         if i==0:
#             temp.append(1)
#             res.append(temp)
#         else:
#             for j in range(0,len(res[i])):
#                 sum=0
#                 if j==0:
#                     temp.append(res[i][j])
#                 else:
#                     temp.append((res[i][j-1]+res[i][j]))
#             temp.append(1)
#             res.append(temp)
#     return(res)
# print(printPascal(6))


def pascal():
    pas = []
    for i in range(0,num+1):
        if i == 0:
            pas.append([1])
        else:
            temp =[]
            sum = 0
            for j in range(i):
                if j == 0:
                    temp.append(1)
                elif j == i-1:
                    temp.append(1)
                else:
                    sum = temp[j-1] + temp[j]
                    temp.append(sum)

                pas.append(temp)

            
    return pas
num = int(input("Enter pascal triangle length"))
print(pascal())