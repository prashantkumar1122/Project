f=open("sample.txt")
a=f.read()
V=0
for i in range(len(a)):
    if a[i] in ["a","e","i","o","u","A","E","I","O","U"]:
        V+=1
print(V)   
