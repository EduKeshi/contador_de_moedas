from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showwarning

from contador_de_moedas import retorna_uma_lista_com_todos_os_valores_das_moedas, \
    retorna_a_soma_total_dos_valores_das_moedas
from envia_emails import faz_o_corpo_do_email, manda_emais_com_os_valores_de_cada_moeda_contada_e_o_valor_total
from gerador_da_planilha import faz_a_planilha_excel_com_os_dados_da_contagem_das_moedas
from gerador_do_arquivo_de_texto import faz_o_arquivo_de_texto


def is_campo_vazio():
    if caixa_de_texto_da_moeda_de_1_real.get() == "":
        return True
    elif caixa_de_texto_da_moeda_de_50_centavos.get() == "":
        return True
    elif caixa_de_texto_da_moeda_de_25_centavos.get() == "":
        return True
    elif caixa_de_texto_da_moeda_de_10_centavos.get() == "":
        return True
    elif caixa_de_texto_da_moeda_de_5_centavos.get() == "":
        return True
    else:
        return False


def is_eamil_invalido():
    if "@" not in caixa_de_texto_do_email.get():
        return True
    elif "." not in caixa_de_texto_do_email.get():
        return True
    else:
        return False


def mostra_a_mensagem_de_campo_em_branco():
    showwarning(title="Campos em branco",
                message="Informe todas as quantidades de moedas antes de apertar o botão!")


def mostra_a_mensagem_de_email_invalido():
    showwarning(title="E-mail inválido",
                message="O e-mail digitado não é válido")


def exclui_o_conteudo_das_entradas():
    caixa_de_texto_da_moeda_de_1_real.delete("0", "end")
    caixa_de_texto_da_moeda_de_50_centavos.delete("0", "end")
    caixa_de_texto_da_moeda_de_25_centavos.delete("0", "end")
    caixa_de_texto_da_moeda_de_10_centavos.delete("0", "end")
    caixa_de_texto_da_moeda_de_5_centavos.delete("0", "end")
    caixa_de_texto_do_email.delete("0", "end")


def exclui_o_conteudo_da_combobox():
    opcoes_de_dowload.delete("0", "end")


def pega_as_quantidades_do_input_e_passa_para_a_funcao_que_chama_as_funcionalidades():
    if is_campo_vazio():
        mostra_a_mensagem_de_campo_em_branco()
        return

    lista_com_a_quantidade_de_cada_moeda = [
        caixa_de_texto_da_moeda_de_1_real.get(),
        caixa_de_texto_da_moeda_de_50_centavos.get(),
        caixa_de_texto_da_moeda_de_25_centavos.get(),
        caixa_de_texto_da_moeda_de_10_centavos.get(),
        caixa_de_texto_da_moeda_de_5_centavos.get(),
    ]

    lista_com_os_valores_de_cada_moeda = retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_cada_moeda)
    soma_total = retorna_a_soma_total_dos_valores_das_moedas(lista_com_os_valores_de_cada_moeda)

    chama_as_outras_funcoes(lista_com_a_quantidade_de_cada_moeda, lista_com_os_valores_de_cada_moeda, soma_total)


def chama_as_outras_funcoes(lista_com_a_quantidade_de_cada_moeda: list, lista_com_os_valores_de_cada_moeda: list, soma_total):
    if opcao_selecionada.get() == "Arquivo de texto (.txt)":
        faz_o_arquivo_de_texto(lista_com_a_quantidade_de_cada_moeda, lista_com_os_valores_de_cada_moeda, soma_total)

    elif opcao_selecionada.get() == "Excel (.xlsx)":
        faz_a_planilha_excel_com_os_dados_da_contagem_das_moedas(lista_com_a_quantidade_de_cada_moeda,
                                                                 lista_com_os_valores_de_cada_moeda,
                                                                 soma_total)
    else:
        envia_o_email_com_os_valores_das_moedas(lista_com_a_quantidade_de_cada_moeda,
                                                lista_com_os_valores_de_cada_moeda,
                                                soma_total)

    exclui_o_conteudo_das_entradas()
    exclui_o_conteudo_da_combobox()


def envia_o_email_com_os_valores_das_moedas(lista_com_a_quantidade_de_cada_moeda: list, lista_com_os_valores_de_cada_moeda: list, soma_total):
    if is_eamil_invalido():
        mostra_a_mensagem_de_email_invalido()
        return

    email_para_enviar = caixa_de_texto_do_email.get()

    corpo_do_email = faz_o_corpo_do_email(lista_com_a_quantidade_de_cada_moeda,
                                          lista_com_os_valores_de_cada_moeda,
                                          soma_total,
                                          email_para_enviar)
    manda_emais_com_os_valores_de_cada_moeda_contada_e_o_valor_total(email_para_enviar, corpo_do_email)


janela = Tk()
janela.title("Contador de moedas")
janela.geometry("800x600")
janela.maxsize(width=680, height=450)

lista_com_os_valores_de_moedas_existentes = ["1 real", "50 centavos", "25 centavos", "10 centavos", "5 centavos"]
lista_com_as_opcoes_de_download = ["Arquivo de texto (.txt)", "Excel (.xlsx)"]

label_de_boas_vindas = Label(janela, text="Bem vindo\nao\ncontador de moedas")
label_de_boas_vindas.grid(column=1, row=1, columnspan=2)

for indice in range(5):
    label_das_moedas = Label(janela, text=f"Qual a quantidade de moedas de {lista_com_os_valores_de_moedas_existentes[indice]}?")
    label_das_moedas.grid(column=0, row=indice + 2)

# Caixa de texto da moeda de 1 real
caixa_de_texto_da_moeda_de_1_real = Entry(janela)
caixa_de_texto_da_moeda_de_1_real.grid(column=1, row=2)

# Caixa de texto da moeda de 50 centavos
caixa_de_texto_da_moeda_de_50_centavos = Entry(janela)
caixa_de_texto_da_moeda_de_50_centavos.grid(column=1, row=3)

# Caixa de texto da moeda de 25 centavos
caixa_de_texto_da_moeda_de_25_centavos = Entry(janela)
caixa_de_texto_da_moeda_de_25_centavos.grid(column=1, row=4)

# Caixa de texto da moeda de 10 centavos
caixa_de_texto_da_moeda_de_10_centavos = Entry(janela)
caixa_de_texto_da_moeda_de_10_centavos.grid(column=1, row=5)

# Caixa de texto da moeda de 5 centavos
caixa_de_texto_da_moeda_de_5_centavos = Entry(janela)
caixa_de_texto_da_moeda_de_5_centavos.grid(column=1, row=6)

# Parte do e-mail
label_de_boas_vindas = Label(janela, text="Coloque um E-mail para que\npossamos enviar os resultados")
label_de_boas_vindas.grid(column=1, row=7, columnspan=2)

# Caixa de texto para digitar um E-mail
caixa_de_texto_do_email = Entry(janela, width=35)
caixa_de_texto_do_email.grid(column=1, row=8, columnspan=2)

# Botão para chamar a função "pega_as_quantidades_do_input_e_passa_para_a_funcao"
botao_para_enviar_a_resposta_da_moeda_de_1_real = Button(janela, text="Enviar o E-mail!", command=pega_as_quantidades_do_input_e_passa_para_a_funcao_que_chama_as_funcionalidades)
botao_para_enviar_a_resposta_da_moeda_de_1_real.grid(column=1, row=9, columnspan=2)

# Label antes da combobox
label_de_ou = Label(janela, text="ou")
label_de_ou.grid(column=1, row=11, columnspan=2)

# Label do baixe o arquivo
label_falando_para_baixar_o_arquivo = Label(janela, text="Baixe o arquivo com\nos valores")
label_falando_para_baixar_o_arquivo.grid(column=1, row=12, columnspan=2)

# Caixa de opções de download
opcao_selecionada = StringVar()
opcoes_de_dowload = ttk.Combobox(janela, values=lista_com_as_opcoes_de_download, state="normal",
                                 textvariable=opcao_selecionada)
opcoes_de_dowload.grid(column=1, row=13, columnspan=2)

# Botão para enviar a opção de download
botao_para_defenir_a_opcao_de_download = Button(janela, text="Baixar!", command=pega_as_quantidades_do_input_e_passa_para_a_funcao_que_chama_as_funcionalidades)
botao_para_defenir_a_opcao_de_download.grid(column=1, row=14, columnspan=2)

janela.mainloop()
