x = int(input("Informe um valor para a diferença: "))
qntdNumeros = int(input("Informe a quantidade de números que deseja adicionar: "))
lista = []
pares = []

for i in range(qntdNumeros):
    lista.append(int(input("Informe um valor: ")))

for i in range(len(lista)):
    for j in range(len(lista)):
        if ( lista[i] - lista[j] == x ):
            pares.append([lista[i],lista[j]])

print(f"Quantidade de pares inteiros com diferença informada: {len(pares)}")
for i in range(len(pares)):
    print(pares[i])
