print("enter the value in formula:")
print("result=b^2-4*a*c")

b=int(input("enter a the number:"))
a=int(input("enter b the number:"))
c=int(input("enter c the number:"))
result=(b**2)-(4*a*c) 

if result>0:
    print("Two solutins discriminate value is:",result)
    
elif result==0:
    print("One solutin discriminate value is:",result)
    
elif result<0:        
    print(" No real solutions Disciminate value is:",result)
