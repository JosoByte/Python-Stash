nlista=22
lista1=[]
lista2=[]
for i in range(0,nlista,1):
    lista2.append(i)
for i in range(0,nlista,1):
    lista1.append(lista2)
for i in range(0,len(lista1),1):
    for j in range(0,len(lista1[i]),1):
        if j!=nlista-1:
            print(lista1[i][j], end='')
        else:
            print(lista1[i][j])
