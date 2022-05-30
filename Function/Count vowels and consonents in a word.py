def count(x):
    Vow=0
    Con=0
    for i in range(len(x)):
          if x[i] in ['a','e','i','o','u','A','E','I','O','U']:
              Vow+=1
          else:
              Con+=1
    print(f"The Vowels in word :{Vow} \n The consonents in word :{Con}")
n=input("enter the word: ")
count(n)              
