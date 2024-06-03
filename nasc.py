from datetime import datetime

def calcular_idade(data_nascimento):
    # Obter a data atual
    data_atual = datetime.now()

    # Converter a string de data de nascimento em um objeto datetime
    data_nascimento = datetime.strptime(data_nascimento, '%Y-%m-%d')

    # Calcular a diferença entre as datas
    diferenca = data_atual - data_nascimento

    # Calcular o número de dias, semanas e meses
    dias = diferenca.days
    semanas = dias // 7
    meses = diferenca.days // 30

    return dias, semanas, meses

# Solicitar a data de nascimento ao usuário
data_nascimento = input("Digite sua data de nascimento (no formato ano-mês-dia): ")

# Calcular idade
dias, semanas, meses = calcular_idade(data_nascimento)

# Imprimir os resultados
print(f"Desde a sua data de nascimento até hoje, se passaram:")
print(f"{dias} dias")
print(f"{semanas} semanas")
print(f"{meses} meses")
