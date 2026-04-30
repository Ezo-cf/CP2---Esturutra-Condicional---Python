nm = str(input("Olá! Digite seu nome: "))

idd = int(input(f"Perfeito, {nm}! Agora, digite sua idade: "))

def pode_aprovar(idade, renda, valor):
    if idade < 18:
        return False
    if valor > 20 * renda:
        return False
    return True

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 5 / 100
    elif parcelas <= 12:
        return 8 / 100
    else:
        return 10 / 100

def calcular_parcela(valor, taxa, parcelas):
    return valor * (taxa * (1 + taxa) * parcelas) / ((1 + taxa) * parcelas - 1)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

if idd < 18:
    print(f"Sinto muito, {nm}... tendo {idd} anos não lhe é permitido realizar quaisquer empréstimos. Tente novamente no futuro!")
else:
    renda_me = float(input(f"{nm}, por gentileza, digite sua renda mensal (em formato 1234): "))
    valor_max = 20 * renda_me
    valor_digitado = float(input(f"Tendo uma renda mensal de R$ {renda_me:.2f}, digite o valor do empréstimo que você gostaria de realizar: "))

    if not pode_aprovar(idd, renda_me, valor_digitado):
        print(f"Sinto muito, {nm}... tendo uma renda mensal de apenas R$ {renda_me:.2f}, seu empréstimo de R$ {valor_digitado:.2f} não pôde ser aprovado.")
    else:
        pcl = int(input(f"Digite o número de parcelas (3 a 24) para seu empréstimo de R$ {valor_digitado:.2f}: "))

        if pcl < 3 or pcl > 24:
            print("Número de parcelas inválido. Deve ser entre 3 e 24.")
        else:
            taxa = definir_taxa(pcl)
            parcela = calcular_parcela(valor_digitado, taxa, pcl)
            total = calcular_total(parcela, pcl)
            juros = calcular_juros(total, valor_digitado)

            print(f"\nEmpréstimo APROVADO!")
            print(f"Nome do cliente: {nm}")
            print(f"Valor financiado: R$ {valor_digitado:.2f}")
            print(f"Taxa de juros aplicada: {taxa * 100:.0f}% ao mês")
            print(f"Valor da parcela: R$ {parcela:.2f}")
            print(f"Valor total pago: R$ {total:.2f}")
            print(f"Total de juros pagos: R$ {juros:.2f}")