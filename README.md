# COVID-19 Dashboard

Este projeto tem como próposito disponibilizar uma ferramenta de simples acesso aos dados de COVID-19 no Brasil. A opção pela ferramenta de visualização de dados [Metabase](https://www.metabase.com/start/) se dá pelo fato da simplicidade em formular "perguntas" em função do banco de dados.

## Requisitos
* Python3
* psycopg2
* PostgreSQL

## Como Usar

Criar table no bando de dados
```
$ sudo -i -u postgres psql
postgres=# CREATE DATABASE br_covid;
postgres=# GRANT ALL PRIVILEGES ON DATABASE br_covid TO postgres;
```

Rodar O ETL Script e informar a senha do Banco de Dados:
```bash
$ python3 etl.py
>> PostgreSQL Password: 
...
```
Pronto, os dados serão incluídos no bancos de dados.

## Configurando o Metabase

Baixe última versão do [Metabase](https://www.metabase.com/start/).

Execute a aplicação:

```bash
$ java -jar metabase.jar
```

Ao iniciar, configure o banco de dados em `Settings>Admin>databases`.

## Simples Exemplo Dashboard

![](images/exemplo.png)