#Identify the row and col of the matrix where it contains zero 
m1 = [[7,3,4],[23,0,5],[2,0,0]]
 
col = []
row = []
for i in range(len(m1)):
    if 0 in m1[i]:
        row.append(i) 
        # print(row)
        for j in range(len(m1[i])):
            if m1[i][j] ==0:
                if (j not in col):
                    col.append(j)
                # print(col)
print(row , col)
    