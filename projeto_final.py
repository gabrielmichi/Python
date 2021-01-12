import pandas as pd
import requests
import json
import pyodbc
import logging
from datetime import datetime, timezone
import dateutil.parser

#Log Erros
date_log = datetime.now().strftime("%d%m%Y")
#print(date_log)

logging.basicConfig(filename="c:/python/Logs/log-BI-"+ date_log +".log", level=logging.DEBUG,filemode='a',
                    format='%(asctime)s: %(levelname)s: %(lineno)s: %(message)s')
logger = logging.getLogger(__name__)

def retornar_conexao_sql():
    server = "database.windows.net"
    database = "databasepowerbi"dff['data_criacao'] = pd.to_datetime(dff['data_criacao'])
        dff['data'] = dff['data_criacao'].dt.date
        dff['dataprimeiraresposta'] = pd.to_datetime(dff['dataprimeiraresposta'])
        dff['dataultimasituacao'] = pd.to_datetime(dff['dataultimasituacao']).dt.date
        dff['dataencerramento'] = pd.to_datetime(dff['dataencerramento']).dt.date
        n_dicionario = dff.to_dict('records')

        for dicionario in n_dicionario:
            coluna = ', '.join(str(x).replace('/', '_') for x in dicionario.keys())
            valor = ', '.join("'" + str(x).replace('NaT', '') + "'" for x in dicionario.values())
            sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('RealTimeChamados', coluna, valor)
            cursor.execute(sql)
            cursor.commit()
#print(sql)

cursor = retornar_conexao_sql()
#all_chamados_dezoito()


i = timestamp_formatada()
response = requests.get("https://link/chaveAPI/10?lastsituation_upper={}?situacao=0,1,2,3,5,6,7,8,9".format(i))

chamados = response.json()
dados_full = json.dumps(chamados['data'], ensure_ascii=False)
data_df = pd.read_json(dados_full)
dff = pd.DataFrame(data=data_df,
                           columns=['protocolo', 'tempotrabalho', 'data_criacao', 'dataprimeiraresposta', 'dataencerramento',
                                    'dataultimasituacao', 'descsituacao', 'categoria', 'status', 'nomeorganizacao', 'atendente'])
dff['data_criacao'] = pd.to_datetime(dff['data_criacao'], dayfirst=True)
dff['data'] = dff['data_criacao'].dt.date
dff['dataprimeiraresposta'] = pd.to_datetime(dff['dataprimeiraresposta'], dayfirst = True).dt.date
dff['dataultimasituacao'] = pd.to_datetime(dff['dataultimasituacao'], dayfirst = True).dt.date
#print(dff['dataultimasituacao'])
dff['dataencerramento'] = pd.to_datetime(dff['dataencerramento'], dayfirst = True).dt.date
dados_formatados = dff.to_dict('records')


try:
    for dicionario in dados_formatados:
        coluna = ', '.join(str(x).replace('/', '_') for x in dicionario.keys())
        valor = ', '.join("'" + str(x).replace('NaT','') + "'" for x in dicionario.values())
        #sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('RealTimeChamados', coluna, valor)
        sql = 'MERGE RealTimeChamados WITH (SERIALIZABLE) AS T '\
        'USING (VALUES( %s )) '\
        'AS U( %s ) '\
            'ON U.PROTOCOLO = T.PROTOCOLO '\
        'WHEN MATCHED THEN '\
            'UPDATE SET T.tempotrabalho=U.tempotrabalho, T.dataencerramento=U.dataencerramento, ' \
              'T.dataultimasituacao=U.dataultimasituacao, '\
            'T.descsituacao=U.descsituacao, T.status=U.status, T.atendente=U.atendente '\
        'WHEN NOT MATCHED THEN '\
            "INSERT ( %s ) VALUES ( %s );" % (valor, coluna, coluna, valor)
        #print(sql)
        cursor.execute(sql)
        cursor.commit()
except Exception as e:
        logging.warning({e})
        #print({e})
        raise

cursor.close()


#Todos os Chamados
#while True:
    #all_chamados_dezoito()
