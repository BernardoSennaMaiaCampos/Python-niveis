def calcular_valor_pagamento(litros, tipo_combustivel):
    # Preços por litro
    preco_gasolina = 5.50
    preco_alcool = 4.90

    # Determinar o preço do litro do combustível
    if tipo_combustivel == 'A':
        preco_por_litro = preco_alcool
        if litros <= 20:
            desconto = 0.03
        else:
            desconto = 0.05
    elif tipo_combustivel == 'G':
        preco_por_litro = preco_gasolina
        if litros <= 20:
            desconto = 0.04
        else:
            desconto = 0.06
    else:
        return "Tipo de combustível inválido."

    # Calcular o valor total sem desconto
    valor_total_sem_desconto = litros * preco_por_litro
    
    # Calcular o valor do desconto
    valor_desconto = valor_total_sem_desconto * desconto
    
    # Calcular o valor total a ser pago após o desconto
    valor_total_com_desconto = valor_total_sem_desconto - valor_desconto
    
    return valor_total_com_desconto

def main():
    # Solicitar ao usuário o número de litros vendidos e o tipo de combustível
    litros = float(input("Digite o número de litros vendidos: "))
    tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

    # Calcular o valor a ser pago
    valor_a_pagar = calcular_valor_pagamento(litros, tipo_combustivel)
    
    if isinstance(valor_a_pagar, str):
        print(valor_a_pagar)
    else:
        print(f"Valor a ser pago: R$ {valor_a_pagar:.2f}")

# Executar o programa
main()
