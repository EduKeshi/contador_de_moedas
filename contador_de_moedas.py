def pergunta_quantas_moedas_de_cada_valor_tem():
    lista_com_os_valores_de_moedas_existentes = ["1 real", "50 centavos", "25 centavos", "10 centavos", "5 centavos"]
    lista_com_a_quantidade_de_moedas = []

    for valor_da_moeda in lista_com_os_valores_de_moedas_existentes:
        quantidade_de_moedas = input(f"\nQuantas moedas de {valor_da_moeda} tem?: ")

        lista_com_a_quantidade_de_moedas.append(int(quantidade_de_moedas))

    return lista_com_a_quantidade_de_moedas


def retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_moedas: list):
    lista_com_os_valores_totais_de_cada_moeda = [
        int(lista_com_a_quantidade_de_moedas[0]) * 1,
        int(lista_com_a_quantidade_de_moedas[1]) * 0.50,
        int(lista_com_a_quantidade_de_moedas[2]) * 0.25,
        int(lista_com_a_quantidade_de_moedas[3]) * 0.10,
        round(int(lista_com_a_quantidade_de_moedas[4]) * 0.05, 2)
    ]

    return lista_com_os_valores_totais_de_cada_moeda


def retorna_a_soma_total_dos_valores_das_moedas(lista_com_os_valores_totais_de_cada_moeda: list):
    return round(sum(lista_com_os_valores_totais_de_cada_moeda), 2)
