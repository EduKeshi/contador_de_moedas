from pathlib import Path
from tkinter.messagebox import showinfo


def faz_o_arquivo_de_texto(lista_com_a_quantidade_de_cada_moeda: list, lista_com_os_valores_de_cada_moeda: list, soma_total):
    nome_do_arquivo = "Moedas contadas"

    texto_do_arquivo = f"""Quantidade das suas moedas:
    Moeda de 1 real: {lista_com_a_quantidade_de_cada_moeda[0]}
    Moeda de 50 centavos: {lista_com_a_quantidade_de_cada_moeda[1]}
    Moeda de 25 centavos: {lista_com_a_quantidade_de_cada_moeda[2]}
    Moeda de 10 centavos: {lista_com_a_quantidade_de_cada_moeda[3]}
    Moeda de 5 centavos: {lista_com_a_quantidade_de_cada_moeda[4]}

Valor individual de cada moedas:
    Moeda de 1 real: {lista_com_os_valores_de_cada_moeda[0]} R$
    Moeda de 50 centavos: {lista_com_os_valores_de_cada_moeda[1]} R$
    Moeda de 25 centavos: {lista_com_os_valores_de_cada_moeda[2]} R$
    Moeda de 10 centavos: {lista_com_os_valores_de_cada_moeda[3]} R$
    Moeda de 5 centavos: {lista_com_os_valores_de_cada_moeda[4]} R$

Valor total das moedas:
     {soma_total} R$
    """
    arquivo_de_texto_novo = open(f"{nome_do_arquivo}.txt", "w")
    arquivo_de_texto_novo.write(texto_do_arquivo)

    mostra_a_mensagem_de_sucesso_do_txt_gerado(nome_do_arquivo)


def mostra_a_mensagem_de_sucesso_do_txt_gerado(nome_do_arquivo: str):
    local_do_arquivo_de_texto = Path(f"{nome_do_arquivo}.txt").absolute()

    showinfo(title="Arquivo de texto gerado com sucesso",
             message=f"Seu arquivo foi gerado com sucesso.\n\nNome:\n{nome_do_arquivo}\n\nLocal:{local_do_arquivo_de_texto}")