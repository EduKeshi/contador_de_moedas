from contador_de_moedas import retorna_uma_lista_com_todos_os_valores_das_moedas, retorna_a_soma_total_dos_valores_das_moedas


def test_quando_a_quantidade_de_moedas_de_um_real_for_dez_deve_retornar_10():
    lista_com_a_quantidade_de_moedas = [10, 0, 0, 0, 0]
    lista_com_os_valores_de_cada_moeda = retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_moedas)

    assert lista_com_os_valores_de_cada_moeda[0] == 10


def test_quando_a_quantidade_de_moedas_de_cinquenta_centavos_for_dez_deve_retornar_5():
    lista_com_a_quantidade_de_moedas = [0, 10, 0, 0, 0]
    lista_com_os_valores_de_cada_moeda = retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_moedas)

    assert lista_com_os_valores_de_cada_moeda[1] == 5


def test_quando_a_quantidade_de_moedas_de_vinte_e_cinco_centavos_for_dez_deve_retornar_2_virgula_5():
    lista_com_a_quantidade_de_moedas = [0, 0, 10, 0, 0]
    lista_com_os_valores_de_cada_moeda = retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_moedas)

    assert lista_com_os_valores_de_cada_moeda[2] == 2.5


def test_quando_a_quantidade_de_moedas_de_dez_centavos_for_dez_deve_retornar_um():
    lista_com_a_quantidade_de_moedas = [0, 0, 0, 10, 0]
    lista_com_os_valores_de_cada_moeda = retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_moedas)

    assert lista_com_os_valores_de_cada_moeda[3] == 1


def test_quando_a_quantidade_de_moedas_de_cinco_centavos_for_dez_deve_retornar_zero_virgula_cinco():
    lista_com_a_quantidade_de_moedas = [0, 0, 0, 0, 10]
    lista_com_os_valores_de_cada_moeda = retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_moedas)

    assert lista_com_os_valores_de_cada_moeda[4] == 0.5


def test_a_soma_de_todos_os_valores_deve_dar_19():
    lista_com_os_valores_de_cada_moeda = [10, 5.0, 2.5, 1.0, 0.5]
    soma_total = retorna_a_soma_total_dos_valores_das_moedas(lista_com_os_valores_de_cada_moeda)

    assert soma_total == 19.0
