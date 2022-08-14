import win32com.client as win32


def faz_o_corpo_do_email(lista_com_a_quantidade_de_moedas: list, valor_individual_das_medas: list, valor_total, email_para_enviar):
    primeiro_nome_da_pessoa = email_para_enviar.split(".")

    corpo_do_email = f"""
    <h2>Senhor(a) {primeiro_nome_da_pessoa[0]}</h2>
    
    <h3>Aqui está a quantidade, valor individual e valor total de suas moedas</h3>
    
    <h3>Quantidade de cada moeda</h3>
    Moedas de 1 real: {lista_com_a_quantidade_de_moedas[0]}<br> 
    Moedas de 50 centavos: {lista_com_a_quantidade_de_moedas[1]}<br> 
    Moedas de 25 centavos: {lista_com_a_quantidade_de_moedas[2]}<br>
    Moedas de 10 centavos: {lista_com_a_quantidade_de_moedas[3]}<br> 
    Moedas de 5 centavos: {lista_com_a_quantidade_de_moedas[4]}<br>
    
    <h3>Valor individual de cada moeda</h3>
    Moedas de 1 real: {valor_individual_das_medas[0]}R$<br> 
    Moedas de 50 centavos: {valor_individual_das_medas[1]}R$<br> 
    Moedas de 25 centavos: {valor_individual_das_medas[2]}R$<br>
    Moedas de 10 centavos: {valor_individual_das_medas[3]}R$<br> 
    Moedas de 5 centavos: {valor_individual_das_medas[4]}R$<br>
    
    <h3>Valor total das moedas</h3>
    {round(valor_total, 2)}R$<br><br>
    
    Att;<br>
    Eduardo Keshichian<br>
    Software engineer apprentice at <a href='https://www.zup.com.br/'>Zup IT Services</a>
    """

    return corpo_do_email


def manda_emais_com_os_valores_de_cada_moeda_contada_e_o_valor_total(email_para_enviar: str, corpo_do_email: str):
    conexao_com_o_outlook = win32.Dispatch("outlook.application")

    email = conexao_com_o_outlook.CreateItem(0)

    email.To = email_para_enviar
    email.Subject = "Conatgem das suas moedas"
    email.HTMLBody = corpo_do_email

    email.Send()
