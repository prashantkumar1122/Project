import numpy as np 
x=np.array(["Prashant","Kumar","elephantinforest","c++"],dtype=np.str)
print("original array")
print(x)

remove_space=np.char.strip(x)
print("\nRemoving the leading and trailing white spaces:",remove_space)
