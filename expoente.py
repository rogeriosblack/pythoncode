base = int(input("digite o valor da base: "))
exp = int(input("Digite o valor do expoente: "))
cont = 0
produto = 1

while cont < exp:
    produto = produto * base
    cont = cont + 1

print (base, "elevado a", exp, "é igual ", produto)
    
