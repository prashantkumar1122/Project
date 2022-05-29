def convert_upper(x):
    v=""
    for i in range(len(x)):
        if ord(x[i])>=97 and ord(x[i])<=122:
            v+=x[i].upper()
    print(v)
n=input("Enter the word in lowercase : ")
convert_upper(n)
