menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input('Qual o valor do deposito: '))

        if valor > 0:
            saldo += valor 
            extrato += f"deposito: {valor: .2f}\n"

        else:
            print("Não é possível realizar a operação.")
    
    elif opcao == "s":
        valor = float(input("Qual o valor de saque: "))

        excedeu_saldo  = saldo < valor

        excedeu_limite = limite < valor

        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo o suficiente.")

        elif excedeu_limite:
            print("Você excedeu o limite de 500 reais.")

        elif excedeu_saques:
            print("Você excedeu o limite de 3 saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: {valor: .2f}\n"
            numero_saques += 1
        
        else:
            print("Valor inválido.")

    elif opcao == "e":
        print("---------- EXTRATO --------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------")
    
    elif opcao == "q":
        break
    
    else:
        print("Não foi possível realizar alguma operação, selecione uma opção ofertada.")
        

        
        
        
