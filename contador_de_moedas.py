def retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_moedas: list):
    lista_com_os_valores_totais_de_cada_moeda = [
        int(lista_com_a_quantidade_de_moedas[0]) * 1,
        round(int(lista_com_a_quantidade_de_moedas[1]) * 0.50, 2),
        round(int(lista_com_a_quantidade_de_moedas[2]) * 0.25, 2),
        round(int(lista_com_a_quantidade_de_moedas[3]) * 0.10, 2),
        round(int(lista_com_a_quantidade_de_moedas[4]) * 0.05, 2)
    ]

    return lista_com_os_valores_totais_de_cada_moeda


def retorna_a_soma_total_dos_valores_das_moedas(lista_com_os_valores_totais_de_cada_moeda: list):
    return round(sum(lista_com_os_valores_totais_de_cada_moeda), 2)
