degraus = int(input("Informe a quantidade de degraus: "))
x = 1

for i in range(degraus-1,-1,-1):
    print(i*" " + x*"*")
    x += 1