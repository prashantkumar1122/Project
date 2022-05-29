def roll_call(x):
    li=[1,2,3,4,5,6,7,8,9,10,22]
    
    if x in li:
        print(f"roll number {x} is present")
    else:
        print(f"roll number {x}  is Absent") 
        
n=int(input("enter the roll number:"))           
roll_call(n)
