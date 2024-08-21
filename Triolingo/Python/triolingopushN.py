import sys
sys.set_int_max_str_digits(0)
def MM(a,b):

    c = []
    for i in range(0,len(a)):
        temp=[]
        for j in range(0,len(b[0])):
            s = 0
            for k in range(0,len(a[0])):
                s += (a[i][k] %(1000000007)) * (b[k][j] %(1000000007)) %(1000000007)
            temp.append(s)
        c.append(temp)

    return c


def powerMat(m, y):
    res = [[1, 0], [0, 1]]

    while (y > 0):
        if ((y % 2) == 1):
            res = MM(res, m)
        y = y // 2
        if y != 0 :
            m = MM(m,m)
    return res


FibMat = [[0, 1], [1, 1]]
InpVect =[[1],[2]]

indic = int(input())

tot= 0


if indic < 3:
    print (InpVect[indic-1][0])
else:
    OutVect =MM(powerMat(FibMat, indic-2) , InpVect)
    tot = (OutVect[0][0] + OutVect[1][0]-1) %(1000000007)

    print(tot)

