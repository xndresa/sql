
<h2> # Desafio DIO - SQL: Associando Comandos e Descrições </h2>

## Descrição do Projeto

Esse é um projeto simples que foi desenvolvido para reforçar o conhecimento de comandos e palavras-chave fundamentais da linguagem SQL. O objetivo é associar um comando SQL à sua descrição correta, funcionando como um exercício de fixação para quem está começando a estudar bancos de dados relacionais.

O programa recebe como entrada um comando SQL e retorna a sua função correspondente.

## Tecnologias

O código foi implementado em **Python 3**, mas a lógica pode ser facilmente adaptada para qualquer outra linguagem de programação.

Para executar, você precisa apenas de:

  - Um editor de código (como VS Code, Sublime Text, ou PyCharm).
  - Um terminal ou prompt de comando.

## Como Usar

Siga os passos abaixo para executar o script:

1.  Crie um novo arquivo com a extensão `.py` (por exemplo, `desafio.py`).
2.  Copie e cole o código abaixo no arquivo.

<!-- end list -->

```python
comandos_sql = {
    "SELECT": "recupera dados de uma ou mais tabelas",
    "PRIMARY KEY": "identificador único para cada registro de uma tabela",
    "FOREIGN KEY": "define relacionamento entre tabelas via chave",
    "WHERE": "filtra registros com base em condições específicas"
}

entrada = input()

if entrada in comandos_sql:
    print(comandos_sql[entrada])
```

3.  Abra seu terminal, navegue até a pasta onde salvou o arquivo e execute o comando:

    ```bash
    python desafio.py
    ```

4.  O programa irá aguardar a sua entrada. Digite um dos comandos válidos e pressione `Enter`.

## Comandos e Descrições Válidas

O programa aceita e mapeia as seguintes entradas:

| Entrada | Descrição Correspondente |
| :--- | :--- |
| `SELECT` | recupera dados de uma ou mais tabelas |
| `PRIMARY KEY` | identificador único para cada registro de uma tabela |
| `FOREIGN KEY` | define relacionamento entre tabelas via chave |
| `WHERE` | filtra registros com base em condições específicas |

## Exemplo de Uso

Ao executar o programa e digitar `SELECT` no terminal, a saída será:

```
recupera dados de uma ou mais tabelas
```# sql
