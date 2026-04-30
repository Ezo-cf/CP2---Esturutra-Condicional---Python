nome = input("Digite o nome do funcionário: ")

print("\nCargo:")
print("1 - Gerente")
print("2 - Analista")
print("3 - Assistente")
print("4 - Estagiário")
cargo = int(input("Escolha o cargo: "))

salario_base = float(input("Digite o salário base R$: "))
horas_extras = float(input("Digite total de horas extras: "))
faltas = int(input("Digite total de faltas: "))

resp_bonus = input("Recebeu bônus? (Sim/Não): ").lower()
recebeu_bonus = resp_bonus == 'sim'  # corrigido


def calcular_horas_extras(salario_base, horas):
    valor_hora_extra = salario_base * 0.015
    return horas * valor_hora_extra


def calcular_descontos_faltas(salario_base, faltas):
    desconto_por_falta = salario_base * 0.02
    return faltas * desconto_por_falta


def calcular_bonus(cargo, recebeu_bonus):
    if not recebeu_bonus:
        return 0

    if cargo == 1:  # Gerente
        return 1000
    elif cargo == 2:  # Analista
        return 500
    elif cargo == 3:  # Assistente
        return 300
    elif cargo == 4:  # Estagiário
        return 100
    else:
        return 0


# cálculos
total_horas_extras = calcular_horas_extras(salario_base, horas_extras)
total_descontos = calcular_descontos_faltas(salario_base, faltas)
bonus = calcular_bonus(cargo, recebeu_bonus)

salario_bruto = salario_base
acrescimos = total_horas_extras + bonus
salario_final = salario_bruto + acrescimos - total_descontos


# saída
print("\n====== RESULTADO ======")
print(f"Funcionário: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Horas extras: R$ {total_horas_extras:.2f}")
print(f"Bônus: R$ {bonus:.2f}")
print(f"Descontos: R$ {total_descontos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")