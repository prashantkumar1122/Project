import numpy as np 
arr=np.array(["Prashant","Kumar","course"],dtype="str")
print("original array:",arr)

multi_linesplit=np.char.splitlines(arr)
print(multi_linesplit)
