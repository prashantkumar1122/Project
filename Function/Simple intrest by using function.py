def simple_intrest():
    principle=int(input('Enter the principle : '))
    rate=int(input('Enter the rate : '))
    time=int(input('Ente rthe time : '))
    multiple=principle*rate*time
    s_i=multiple/100
    return s_i

calculate_s_i=simple_intrest()
print(calculate_s_i)
