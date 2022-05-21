a={'mango':'Aam','cat':'Billi','dog':'Kutta','apple':'Save'}

print('Your options is :',a.keys())

b=input('Enter any word which meaning you want:')

#print('your searchrd meaning is :',a[b])

print('your searchrd meaning is :',a.get(b))    # GET FUNCTION NOT SHOWS ANY ERROR
