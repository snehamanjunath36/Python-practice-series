def pascal(num):
    ans = [[1]]
    for i in range(2,num+1):
        temp = [0] + ans[-1] +[0]
        res =[]
        for j in range(len(ans[-1])+1):
            res.append(temp[j]+temp[j+1])
        ans.append(res)
    print(ans)
    
num = int(input('enter the triangle length'))
pascal(num)