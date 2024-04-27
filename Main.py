# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<< FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

def PrintDRM(drm):
    print(drm)

def Login(clients):
    while True:
        acc = input("Account Number: ")
        pwd = input("Password: ")   

        if clients.get(acc) and pwd == clients[acc]["password"]:
            return acc
        else:
            print("\nAcesso inválido\n")

def PrintTitle(width = 30):
    print()
    print("$".center(width, "$"))
    print(TITLE.center(width, "$"))
    print("$".center(width, "$"))

def PrintCredentials(clients, account):
    print("Conta: {acc}\tName: {name}"
        .format(
            acc = account, 
            name = clients[account]["name"]
        ))

def PrintBalance(balance):
    print(f"Saldo: R${balance:.2f}")

def Deposit(clients, account):
    PrintBalance(clients[account]["balance"])
    temp = float(input("\nDigite o valor a depositar\n> "))
    if temp > 0.0:
        clients[account]["balance"] += temp
        clients[account]["statement"] += f'{clients[account]["balance"]:.2f}\t\t+R${temp:.2f}\n'
    else: print("\nValor nulo ou inválido")

def Withdraw(clients, account):
    PrintBalance(clients[account]["balance"])
    if clients[account]["draws"] < DAILY_DRAW_LIM:
        temp = float(input("\nDigite o valor a sacar\n> "))
        if temp > DRAW_AMOUNT_LIM: 
            print("\nValor acima do limite de saque")
        elif clients[account]["balance"] < temp: 
            print("\nSaldo insuficiente")
        elif temp > 0.0: 
            clients[account]["balance"] -= temp
            clients[account]["draws"] += 1
            clients[account]["statement"] += f'{clients[account]["balance"]:.2f}\t\t\t\t-R${temp:.2f}\n'
        else: print("\nValor nulo ou inválido")
    else: print("\nLimite diário de saques atingido")

def PrintStatement(clients, account):
    print(STATEMENT_HEADERS, end = "")
    print(clients[account]["statement"])


# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<< CONSTANTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

SCREEN_WIDTH = 30
DAILY_DRAW_LIM = 3
DRAW_AMOUNT_LIM = 500.0
DRM = """
(c) LixoWarez Ltda.
NOBANK v2.0
"""
TITLE = " NoBank Digital "
MENU = """
4. Consultar Saldo
3. Depositar
2. Sacar
1. Extrato
0. Sair"""
STATEMENT_HEADERS = "SALDO\t\tCREDITO\t\tDEBITO\n"


# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<< VARIABLES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

clients = {"account" : dict.fromkeys([
    "password", 
    "name", 
    "balance", 
    "draws",
    "statement"
])}

# TEST CASE
clients["0"] = {
    "password" : "123", 
    "name" : "test", 
    "balance" : 100.0, 
    "draws" : 1,
    "statement" : ""
}

# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<<< PROGRAM >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

PrintDRM(DRM)

while True:
    command = -1
    account = Login(clients)

    PrintTitle(SCREEN_WIDTH)
    print()
    PrintCredentials(clients, account)

    while command:
        print(MENU)

        command = int(input("> "))

        print()

        if command == 4: PrintBalance(clients[account]["balance"])
        elif command == 3: Deposit(clients, account)
        elif command == 2: Withdraw(clients, account)
        elif command == 1: PrintStatement(clients, account)
        elif command == 0: print("Até mais!\n")
        else: print("Operação inválida")