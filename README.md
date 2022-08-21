# contador de moedas
O contador de moedas é uma interface onde você informa a quantidade das suas moedas e decide se você quer enviar um
e-mail ou baixar um arquivo.<br>

**Conteúdo que vai no e-mail e no arquivo**:
- Quantidade individual de cada moeda
- Valor de cada moeda
- soma total das moedas<br>

**Opções de download**:
- Arquivo de texto - .txt
- Planilha Excel - .xlsx

# IDE utilizada
- PyCharm

# Liguagem utilizada
- Python

# Bibliotecas utilizadas
- tkinter: Essas biblioteca foi usada para fazer a janela
- openpyxl: Essa biblioteca foi utilizada para fazer o arquivo Excel
- win32com.client: Essa biblioteca foi utilizada para fazer a integração com o Outlook
- pathlib: Essa biblioteca foi utilizada para pegar o caminho dos arquivos gerados

# Como surgiu essa ideia?
Eu precisava contar algumas moedas, nesse caso eu ia ter que contar cada moeda, multiplicar cada valor na
calculadora e depois anotar isso no papel.<br>
Então eu tive a ideia de fazer um script simples só para eu contar a quantidade das moedas e o resto esse
script ia fazer, mas depois que eu finalizei o script eu vi que ele tinha um potencial.<br>
Primeiro eu fiz a integração para ele mandar um e-mail com todos os atributos citados no primeiro tópico, depois que
eu fiz isso eu queria deixar ele mais fácil de ser usado, então pensei em fazer uma interface.<br>
Por fim eu queria mais opções além de mandar um e-mail, então fiz uma funcionalidade para baixar um arquivo com as mesmas informações que vem
no e-mail.