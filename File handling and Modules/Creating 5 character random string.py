import random as rd
import string
letters=string.ascii_letters 

print("The five char random string is: ")
sr=""

for i in range(5):
    st=rd.choice(letters)
    sr+=st 
print(sr) 
