f=open("sample.txt")
a=f.read()
u=0
l=0
d=0

for i in range(len(a)):
    if a[i].isupper():
        u+=1
    elif a[i].islower():
        l+=1
    elif a[i].isdigit():
        d+=1      
        
print("Uppercase:",u)
print("Lowercase: ",l)
print("Digit:",d)
