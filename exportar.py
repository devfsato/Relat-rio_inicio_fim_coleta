import pyodbc as p ##Módulo de Acesso SQL
import pandas as pd
from datetime import datetime, timedelta

##Conexão com o Banco de Dados
cnxn = p.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                      # IP ou nome do servidor.
                      r"SERVER=.\FSATO;"
                      # Porta
                      "PORT=1433;"
                      # Banco que será utilizado.
                      "DATABASE=CADASTRO;"
                      # Nome de usuário.
                      f"UID={'homologacao'};"
                      # Senha.
                      f"PWD={'homo@teste'}")

data1 = (datetime.now() - timedelta(days=1))
data1format = data1.strftime("%d%m%Y")

data2 = datetime.now()
data2format = data2.strftime("%d%m%Y")

pd.read_sql('SELECT * FROM PESSOA',cnxn).to_excel('{}_{}.xlsx'.format(data1format,data2format))