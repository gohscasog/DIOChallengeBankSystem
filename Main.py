header = """
(c) LixoWarez Ltda.
NOBANK v1.0

Conta: 69420-0
Senha: ******
"""
title = " NoBank Digital "
menu = """
4. Consultar Saldo
3. Depositar
2. Sacar
1. Extrato
0. Sair"""
command = -1
screenWidth = 30
DAILY_DRAW_LIM = 3
DRAW_AMOUNT_LIM = 500.0
draws = 0
balance = 0.0
statement = "SALDO\t\tCREDITO\t\tDEBITO\n"

print(header)
print("$".center(screenWidth, "$"))
print(title.center(screenWidth, "$"))
print("$".center(screenWidth, "$"))

while command:
    print(menu)

    command = int(input("> "))
    balanceMsg = f"Saldo: R${balance:.2f}"

    print()

    if command == 4:
        print(balanceMsg)
    elif command == 3:
        print(balanceMsg)
        temp = float(input("\nDigite o valor a depositar\n> "))
        if temp > 0.0:
            balance += temp
            statement += f"{balance:.2f}\t\t+R${temp:.2f}\n"
        else: print("\nValor nulo ou inválido")
    elif command == 2:
        print(balanceMsg)
        if draws < DAILY_DRAW_LIM: 
            temp = float(input("\nDigite o valor a sacar\n> "))
            if temp > 500.0: print("\nValor acima do limite de saque")
            elif balance < temp: print("\nSaldo insuficiente")
            elif temp > 0.0: 
                balance -= temp
                draws += 1
                statement += f"{balance:.2f}\t\t\t\t-R${temp:.2f}\n"
            else: print("\nValor nulo ou inválido")
        else: print("\nLimite diário de saques atingido")
    elif command == 1: print(statement)
    elif command == 0: print("Até mais!\n")
    else: print("Operação inválida")