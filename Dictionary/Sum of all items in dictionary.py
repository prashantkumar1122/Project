def returnSum(Dict):
 
    list = []
    for i in Dict:
        list.append(Dict[i])
    final = sum(list)
 
    return final
 
dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))
