def By_values(d,reverse=False):
    return dict(sorted(d.items(),key=lambda k:k[1],reverse=reverse))
  
d={1:2,2:3,3:6,0:4,7:1,9:7}  

print("Sorted by valuse in ascending order:")
print(By_values(d))

print("Sorted by valuse in dscending order:")
print(By_values(d,True))
