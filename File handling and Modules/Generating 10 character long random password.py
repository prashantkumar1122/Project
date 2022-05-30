import random as rd 
import string as st 

randomlist=st.ascii_letters+st.digits+st.punctuation
password=rd.sample(randomlist,6)
password+=rd.sample(st.ascii_uppercase,2)
password+=rd.choice(st.digits)
password+=rd.choice(st.punctuation)
password_list=list(password)
shu=rd.shuffle(password_list)

print("your password is:")
print("".join(password_list))
