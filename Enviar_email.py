import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import sys
import logging
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.text import MIMEText

date_log = datetime.now().strftime("%d%m%Y")
logging.basicConfig(filename="c:/python/Logs/log-BI-"+ date_log +".log", level=logging.DEBUG,filemode='a',
                    format='%(asctime)s: %(levelname)s: %(lineno)s: %(message)s')
logger = logging.getLogger(__name__)

def retornar_conexao_sql():
    server = ""
    database = ""
    username = ""
    password = ""
    #DRIVER Server
    #string_conexao = 'Driver={ODBC Driver 11 for SQL Server};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server=' + server + ';Database=' + database + ';UID=' + username + ';PWD=' + password
    try:
        conexao = pyodbc.connect(string_conexao)
    except Exception as e:
        logging.warning({e})
        #print({e})
    return conexao

cursor = retornar_conexao_sql()
result = pd.read_sql_query("select PROTOCOLO,atendente,data_criacao,dataultimasituacao,DATEDIFF(day, dataultimasituacao, GETDATE()) as quantidade from RealTimeChamados WHERE DESCSITUACAO <> 'Finalizado' and descsituacao <> 'Cancelado' and DATEDIFF(day, dataultimasituacao, GETDATE()) > 6", cursor)

result.rename(columns={'PROTOCOLO': 'Chamado', 'atendente': 'Responsável','dataultimasituacao': 'Última_Resposta',  'quantidade': 'Quantidade_Dias'}, inplace=True)

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

# username ou email para logar no servidor
username = 'username@gmail.com'
password = 'password'

#e-mail
from_addr = 'email@provedor.com.br'
to_addrs = ['email@provedor.com.br']

html = """\
<html>
  <head></head>
  <body>
    {0}
  </body>
</html>
""".format(result.to_html(index=False))

message = MIMEText(html, 'html')

#message = MIMEText(result).to_string()
message['subject'] = 'Chamados Próximos do Vencimento'
#message['from'] = from_addr
#message['to'] = ', '.join(to_addrs)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()