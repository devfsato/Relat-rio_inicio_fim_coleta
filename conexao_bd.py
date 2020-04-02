import pyodbc

conn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};"
                      # IP ou nome do servidor.
                      r"SERVER=.\FSATO;"
                      # Porta
                      "PORT=1433;"
                      # Banco que será utilizado.
                      "DATABASE=CADASTRO;"
                      # Nome de usuário.
                      f"UID={'homologacao'};"
                      # Senha.
                      f"PWD={'homo@teste'}"
                      )

cursor = conn.cursor()


def listar():
    sql = """
    SELECT * FROM PESSOA
    """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
