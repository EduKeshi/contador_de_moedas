import openpyxl
from tkinter.messagebox import showinfo
from pathlib import Path


def faz_a_planilha_excel_com_os_dados_da_contagem_das_moedas(lista_com_a_quantidade_de_cada_moeda: list, lista_com_os_valores_de_cada_moeda: list, soma_total):
    nome_do_arquivo = "Contagem_das_suas_moedas"

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

    nova_planilha.save(f"{nome_do_arquivo}.xlsx")

    mostra_a_mensagem_de_sucesso_da_planilha(nome_do_arquivo)


def mostra_a_mensagem_de_sucesso_da_planilha(nome_do_arquivo):
    local_da_planilha = Path(f"{nome_do_arquivo}.xlsx").absolute()

    showinfo(title="Planilha gerada com sucesso",
             message=f"Seu arquivo foi gerado com sucesso.\n\nNome:\n{nome_do_arquivo}\n\nLocal:{local_da_planilha}")
