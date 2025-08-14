lista_maiores = []
while True:
    nome = input('digite seu nome! (ou "sair" para encerrar): ')
    if nome.lower() == 'sair':
        break

    idade = int(input('digite sua idade!'))

    if idade >= 19:
        print('Pode entrar!')
        lista_maiores.append({"nome": nome, "idade": idade})

    elif idade < 19:
        print('Entrada não autorizada!')
print("\n--- Pessoas autorizadas (maiores de 19 anos) ---")
for pessoa in lista_maiores:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']} anos")

print(f"\nTotal de pessoas autorizadas: {len(lista_maiores)}")
