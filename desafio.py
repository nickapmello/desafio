def input_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, digite um número válido.")

def depositar(saldo, extrato):
    valor = input_float("Informe o valor do depósito: ")
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite):
    print(f"Seu limite de saque atual é: R$ {limite:.2f}")
    valor = input_float("Informe o valor do saque: ")
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o seu limite de R$ {limite:.2f}.")
    elif valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques

def mostrar_extrato(extrato, saldo):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def alterar_limite(limite):
    novo_limite = input_float("Informe o novo limite de saque: ")
    if novo_limite > 0:
        limite = novo_limite
        print(f"Limite de saque atualizado para: R$ {limite:.2f}")
    else:
        print("Operação falhou! O valor do limite deve ser positivo.")
    return limite

def main():
    saldo = 0
    limite = 500  # Limite inicial
    extrato = ""
    numero_saques = 0

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [l] Alterar Limite de Saque
    [q] Sair

    Seu limite atual de saque é: R$ {limite:.2f}
    => """

    while True:
        print(menu.format(limite=limite))
        opcao = input()
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, limite)
        elif opcao == "e":
            mostrar_extrato(extrato, saldo)
        elif opcao == "l":
            limite = alterar_limite(limite)
        elif opcao == "q":
            print("Obrigado por usar nosso banco. Até mais!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
