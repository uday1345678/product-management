data=[6,5,3,4,7]
datae=[]
datao=[]
n=len(data)
for i in range(n):
    if(data[i]%2==0):
        datae.append(data[i])
    else:
        datao.append(data[i])
print(datae)
print(datao)

