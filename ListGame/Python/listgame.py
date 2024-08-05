num=int(input())

def factorisation(numb):
    count=0
    lim=round(numb ** 0.5)
    
    while numb%2==0:
        count +=1
        numb=numb/2
    lim=round(numb ** 0.5)


    i = 3
    while i<=lim :     
        if numb%i==0:
            count +=1
            numb= numb/i
        else:
            i+=2
            lim=round(numb ** 0.5)

            
    if numb !=1:
        count +=1


    return count

print(factorisation(num))