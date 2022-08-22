from tkinter.messagebox import showwarning


def mostra_a_mensagem_de_campo_em_branco():
    showwarning(title="Campos em branco",
                message="Informe todas as quantidades de moedas antes de apertar o botão!")


def mostra_a_mensagem_de_letra_ao_inves_de_numero():
    showwarning(title="Letras no lugar de números",
                message="Todos os campos devem ser números!")


def mostra_a_mensagem_de_email_sem_arroba():
    showwarning(title="E-mail inválido",
                message="O e-mail digitado não tem @")


def mostra_a_mensagem_de_email_sem_ponto():
    showwarning(title="E-mial inválido",
                message="O e-mail digitado não possui . (ponto)")
