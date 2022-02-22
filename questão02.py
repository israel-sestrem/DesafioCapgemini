nome = input("Informe seu nome: ")
senha = input("Informe sua senha: ")

tamanho = False
digito = False
minusculo = False
maiusculo = False
especial = False

for i in range(len(senha)):
    if ( len(senha) >= 6 ):
        tamanho = True

    if ( senha[i].isdigit() ):
        digito = True
    
    if ( senha[i].islower() ):
        minusculo = True
    
    if ( senha[i].isupper() ):
        maiusculo = True

    if ( not(senha[i].isalpha()) and not(senha[i].isdigit()) ):
        especial = True

if ( not(tamanho) ):
    print("A senha deve conter no mínimo 6 caracteres")
elif ( not(digito) ):
    print("Considere adicionar algum número na senha")
elif ( not(minusculo) ):
    print("Considere adicionar alguma letra minúscula na senha")
elif ( not(maiusculo) ):
    print("Considere adicionar alguma letra maiúscula na senha")
elif ( not(especial) ):
    print("Considere adicionar algum caractere especial na senha")
else:
    print("Sua senha está forte e segura!")