# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<<< OBJECTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

class Info:
    account : str
    password : str
    name : str
    balance : float
    draws : int
    statement : str
    
    def __init__(self, account : str, password : str, name : str, balance : float, draws : int, statement : str):
        self.account = account
        self.password = password
        self.name = name
        self.balance = balance
        self.draws = draws
        self.statement = statement

class Bank:
    DAILY_DRAW_LIM = 3
    DRAW_AMOUNT_LIM = 500.0
    clients : dict = dict.fromkeys("account", Info)

    def __init__(self, name : str):
        self.TITLE = f" {name} "

    def AddClient(self, client):
        self.clients.update({client.account : client})

    def DelClient(self, client : Info):
        self.clients.pop(client.account)

class ATM:
    SCREEN_WIDTH = 30
    MENU = """    4. Consultar Saldo
    3. Depositar
    2. Sacar
    1. Extrato
    0. Sair"""
    ADMIN_MENU = """
    7. Listar clientes
    6. Adicionar cliente
    5. Remover cliente"""
    STATEMENT_HEADERS = "SALDO\t\tCREDITO\t\tDEBITO\n"
    CLIENTS_HEADERS = "CONTA\t\tTITULAR\n"
    holder : Info

    def __init__(self, bank : Bank):
        self.bank = bank
    
    def Login(self):
        while True:
            acc = input("Account Number: ")
            pwd = input("Password: ")
            usr = self.bank.clients.get(acc)

            if usr and pwd == usr.password:
                self.holder = usr
                break
            else:
                print("\nAcesso inválido\n")

    def Deposit(self):
        self.PrintBalance()

        temp = float(input("\nDigite o valor a depositar\n> "))

        if temp > 0.0:
            self.holder.balance += temp
            self.holder.statement += f'{self.holder.balance:.2f}\t\t+R${temp:.2f}\n'
        else: print("\nValor nulo ou inválido")

    def Withdraw(self):
        self.PrintBalance()

        if self.holder.draws < self.bank.DAILY_DRAW_LIM:
            temp = float(input("\nDigite o valor a sacar\n> "))
            
            if temp > self.bank.DRAW_AMOUNT_LIM: 
                print("\nValor acima do limite de saque")
            elif self.holder.balance < temp: 
                print("\nSaldo insuficiente")
            elif temp > 0.0: 
                self.holder.balance -= temp
                self.holder.draws += 1
                self.holder.statement += f'{self.holder.balance:.2f}\t\t\t\t-R${temp:.2f}\n'
            else: print("\nValor nulo ou inválido")
        else: print("\nLimite diário de saques atingido")

    def PrintTitle(self, width = SCREEN_WIDTH):
        print()
        print("$".center(width, "$"))
        print(self.bank.TITLE.center(width, "$"))
        print("$".center(width, "$"))

    def PrintCredentials(self):
        print("Conta: {acc}\tName: {name}"
            .format(
                acc = self.holder.account, 
                name = self.holder.name
            ))

    def PrintBalance(self):
        print(f"Saldo: R${self.holder.balance:.2f}")

    def PrintStatement(self):
        print(self.STATEMENT_HEADERS, end = "")
        print(self.holder.statement)
    
    def PrintClients(self):
        print(self.CLIENTS_HEADERS, end = "")

        for client in self.bank.clients:
            print(f"{client.account}\t{client.name}")

# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<< FUNCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

def PrintDRM(drm):
    print(drm)

# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<< CONSTANTS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

DRM = """
(c) LixoWarez Ltda.
NOBANK v2.0
"""
BANK = Bank("NoBank Digital")
ATM_ = ATM(BANK)

# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<< VARIABLES >>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

command : int

# ================================================================
# <<<<<<<<<<<<<<<<<<<<<<<<< PROGRAM >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ================================================================

PrintDRM(DRM)

while True:
    command = -1
    
    # TEST CASE
    BANK.AddClient(Info("0", "123", "admin", 100.0, 1, ""))

    ATM_.Login()
    ATM_.PrintTitle()
    print()
    ATM_.PrintCredentials()

    while command:
        if ATM_.holder.account == "0":
            print(ATM_.ADMIN_MENU)

        print(ATM_.MENU)

        command = int(input("> "))
        print()

        if ATM_.holder.account == "0":
            if command == 7: 
                print("Em desenvolvimento...")
                # TODO: ATM_.PrintClients()
            elif command == 6: 
                print("Em desenvolvimento...")
                # TODO: BANK.AddClient()
            elif command == 5: 
                print("Em desenvolvimento...")
                # TODO: BANK.DelClient()
        else:
            if command == 4: ATM_.PrintBalance()
            elif command == 3: ATM_.Deposit()
            elif command == 2: ATM_.Withdraw()
            elif command == 1: ATM_.PrintStatement()
            elif command == 0: print("Até mais!\n")
            else: print("Operação inválida")