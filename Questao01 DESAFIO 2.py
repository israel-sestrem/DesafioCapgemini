qntdNumeros = int(input("Quantos números deseja adicionar? "))
lista = []

while( ( qntdNumeros < 3 ) or ( qntdNumeros % 2 == 0 ) ):
    print("Informar pelo menos 3 e ímpar")
    qntdNumeros = int(input("Quantos números deseja adicionar? "))

for i in range(qntdNumeros):
    lista.append(int(input("Informe o número: ")))

mediana = lista[int(len(lista) / 2)]
print(f"A mediana é: {mediana}")