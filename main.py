comando = input() # Recebe a entrada do usuário

if comando == "SELECT":
    print("recupera dados de uma ou mais tabelas")
elif comando == "PRIMARY KEY":
    print("identificador único para cada registro de uma tabela")
elif comando == "FOREIGN KEY":
    print("define relacionamento entre tabelas via chave")
elif comando == "WHERE":
    print("filtra registros com base em condições específicas")

comandos_sql = {
    "SELECT": "recupera dados de uma ou mais tabelas",
    "PRIMARY KEY": "identificador único para cada registro de uma tabela",
    "FOREIGN KEY": "define relacionamento entre tabelas via chave",
    "WHERE": "filtra registros com base em condições específicas"
}

entrada = input() # Recebe a entrada do usuário

if entrada in comandos_sql:
    print(comandos_sql[entrada])