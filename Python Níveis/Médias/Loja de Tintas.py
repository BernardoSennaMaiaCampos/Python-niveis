import math

def calcular_tinta(area):
    # Cálculo da quantidade de tinta necessária
    litros_necessarios = area / 3
    # Cálculo do número de latões necessários, arredondando para cima
    latas_necessarias = math.ceil(litros_necessarios / 18)
    # Cálculo do custo total
    custo_total = latas_necessarias * 80
    return latas_necessarias, custo_total

def main():
    # Solicitar ao usuário o tamanho da área em metros quadrados
    area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
    # Calcular a quantidade de latas e o custo total
    latas, custo = calcular_tinta(area)
    # Exibir o resultado
    print(f"Para pintar uma área de {area:.2f} metros quadrados, você precisará de {latas} latão(ões) de tinta.")
    print(f"O custo total será de R${custo:.2f}")

# Executar o programa
main()
