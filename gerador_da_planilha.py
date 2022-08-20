import openpyxl


def faz_a_planilha_excel_com_os_dados_da_contagem_das_moedas(lista_com_a_quantidade_de_cada_moeda: list, lista_com_os_valores_de_cada_moeda: list, soma_total):
    nova_planilha = openpyxl.Workbook()

    aba_atual = nova_planilha.active
    aba_atual.title = "Contagem das suas moedas"

    aba_atual["A1"] = "Quantidade de moedas"

    for indice_da_linha, quantidade_da_moeda in enumerate(lista_com_a_quantidade_de_cada_moeda):
        aba_atual[f"A{indice_da_linha + 2}"] = int(quantidade_da_moeda)

    aba_atual["B1"] = "Valor individual de cada moeda"

    for indice_da_linha, valor_individual_da_moeda in enumerate(lista_com_os_valores_de_cada_moeda):
        aba_atual[f"B{indice_da_linha + 2}"] = valor_individual_da_moeda

    aba_atual["C1"] = "Valor total das suas moedas"
    aba_atual["C4"] = soma_total

    nova_planilha.save("Contagem_das_suas_moedas.xlsx")
