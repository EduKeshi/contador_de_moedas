from tkinter import *


from contador_de_moedas import pergunta_quantas_moedas_de_cada_valor_tem, \
    retorna_uma_lista_com_todos_os_valores_das_moedas, retorna_a_soma_total_dos_valores_das_moedas
from envia_emails import pergunta_para_qal_email_o_usuario_quer_enviar, faz_o_corpo_do_email, \
    manda_emais_com_os_valores_de_cada_moeda_contada_e_o_valor_total


# Parte das moedas
def pega_as_quantidades_do_input_e_passa_para_a_funcao():
    lista_com_a_quantidade_de_cada_moeda = [
        caixa_de_texto_da_moeda_de_1_real.get(),
        caixa_de_texto_da_moeda_de_50_centavos.get(),
        caixa_de_texto_da_moeda_de_25_centavos.get(),
        caixa_de_texto_da_moeda_de_10_centavos.get(),
        caixa_de_texto_da_moeda_de_5_centavos.get(),
    ]

    lista_com_os_valores_de_cada_moeda = retorna_uma_lista_com_todos_os_valores_das_moedas(lista_com_a_quantidade_de_cada_moeda)
    soma_total = retorna_a_soma_total_dos_valores_das_moedas(lista_com_os_valores_de_cada_moeda)

    return lista_com_os_valores_de_cada_moeda, soma_total


# Parte do e-mail
# email_para_enviar = pergunta_para_qal_email_o_usuario_quer_enviar()
# corpo_do_email = faz_o_corpo_do_email(quantidade_de_moedas_de_cada_valor, lista_com_os_valores_de_cada_moeda,
# soma_total, email_para_enviar)
# manda_emais_com_os_valores_de_cada_moeda_contada_e_o_valor_total(email_para_enviar, corpo_do_email)

janela = Tk()
janela.title("Contador de moedas")
janela.geometry("800x600")

lista_com_os_valores_de_moedas_existentes = ["1 real", "50 centavos", "25 centavos", "10 centavos", "5 centavos"]

for i in range(10):
    label_de_orientacao_das_colunas = Label(janela, text=f"| Coluna {i} |")
    label_de_orientacao_das_colunas.grid(column=i, row=0)


label_de_boas_vindas = Label(janela, text="Bem vindo ao contador de moedas")
label_de_boas_vindas.grid(column=4, row=1, columnspan=3)


for indice in range(5):
    label_das_moedas = Label(janela, text=f"Qual a quantidade de moedas de {lista_com_os_valores_de_moedas_existentes[indice]}?")
    label_das_moedas.grid(column=0, row=indice + 2, columnspan=3)

# Caixa de texto da moeda de 1 real
caixa_de_texto_da_moeda_de_1_real = Entry(janela)
caixa_de_texto_da_moeda_de_1_real.grid(column=3, row=2, columnspan=2)

# Caixa de texto da moeda de 50 centavos
caixa_de_texto_da_moeda_de_50_centavos = Entry(janela)
caixa_de_texto_da_moeda_de_50_centavos.grid(column=3, row=3, columnspan=2)

# Caixa de texto da moeda de 25 centavos
caixa_de_texto_da_moeda_de_25_centavos = Entry(janela)
caixa_de_texto_da_moeda_de_25_centavos.grid(column=3, row=4, columnspan=2)

# Caixa de texto da moeda de 10 centavos
caixa_de_texto_da_moeda_de_10_centavos = Entry(janela)
caixa_de_texto_da_moeda_de_10_centavos.grid(column=3, row=5, columnspan=2)

# Caixa de texto da moeda de 5 centavos
caixa_de_texto_da_moeda_de_5_centavos = Entry(janela)
caixa_de_texto_da_moeda_de_5_centavos.grid(column=3, row=6, columnspan=2)

# Botão para chamar a função
botao_para_enviar_a_resposta_da_moeda_de_1_real = Button(janela, text="Confirmar", command=pega_as_quantidades_do_input_e_passa_para_a_funcao)
botao_para_enviar_a_resposta_da_moeda_de_1_real.grid(column=5, row=4, columnspan=1, rowspan=2)

janela.mainloop()
