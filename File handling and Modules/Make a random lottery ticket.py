import random as rd 
lottery_li=[]
print("Creating 100 lottey tickets:")

for i in range(0,100):
    lt=rd.randrange(1000000000,9999999999)
    lottery_li.append(lt)
    
print("Lucky Two lottery tickets are winners:")
print(rd.sample(lottery_li,2))
