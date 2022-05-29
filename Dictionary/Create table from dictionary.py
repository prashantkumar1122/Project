d={"Prashant":[70,80,90,68,59],"Sanika":[70,80,90,68,59],"Vaishnavi":[70,80,90,68,59],"tapish":[70,80,90,68,59],"Abhishek":[70,80,90,68,59]}

for row in zip(*([k]+(v) for k,v in sorted(d.items()))):
    print(*row,sep="\t")
