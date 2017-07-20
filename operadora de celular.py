min = int(input("Quantos minutos vc usou? ")) 

if min < 200:
    preço = 0.20
elif min >=200 and min<400:
    preço = 0.18
elif min >800:
    preço = 0.08
else:
    preço = 0.15


print (preço)
    
