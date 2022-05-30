f=open("sample.txt","r")
li=f.read().split()
unique_item=set(li)

for word in unique_item:
    print("frequency of word is:",word,li.count(word))
