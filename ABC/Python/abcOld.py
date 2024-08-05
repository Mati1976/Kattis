import sys
i=0
temp=0

for line in sys.stdin:
    data = line.split()
    if (i == 0) :
        A = int(data[0])
        B = int(data[1])
        C = int(data[2])
    else:
        L = data[0]
    i += 1

if A>B:
    temp = A
    A = B
    B = temp
if B>C:
    temp = B
    B = C
    C = temp
if A>B:
    temp = A
    A = B
    B = temp
    
match L:
    case 'ABC':
        print(A,B,C)
    case 'ACB':
        print(A,C,B)
    case 'BAC':
        print(B,A,C)
    case 'BCA':
        print(B,C,A)
    case 'CAB':
        print(C,A,B)
    case 'CBA':
        print(C,B,A)
    
    
