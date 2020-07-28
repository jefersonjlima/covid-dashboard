# COVID-19 Dashboard

Este projeto tem como proposito disponibilizar uma ferramenta de simples acesso aos dados de COVID-19 no Brasil. A opção pela ferramenta de visualização de dados [Metabase](https://www.metabase.com/start/) se dá pelo fato da simplicidade em formular "questões" em função do banco de dados.

## Requisitos
* Python3
    * requests
    * psycopg2
* PostgreSQL

## Como Usar

Criar table no bando de dados
```
$ sudo -i -u postgres psql
postgres=# CREATE DATABASE br_covid;
postgres=# GRANT ALL PRIVILEGES ON DATABASE br_covid TO metabase;
```

Rodar O ETL Script e informar a senha do Banco de Dados:
```bash
$ python3 etl.py
>> PostgreSQL Password: 
...
```
Pronto, os dados serão incluídos no banco de dados.

## Configurando o Metabase

Baixe última versão do [Metabase](https://www.metabase.com/start/).

Execute a aplicação:

```bash
$ java -jar metabase.jar
```

Ao iniciar, configure o banco de dados em `Settings>Admin>databases`.

## Exemplo Dashboard

![](images/exemplo.png)

[Click aqui](http://149.28.110.217:3000/public/dashboard/13b79964-6711-436e-9fe1-e3c4de76c9b0#theme=night) para o acessar o `dashboard`.

## Contribuições

Veja as intruções para contribuir com o projeto em CONTRIBUTING.md.


## Social

* <sub><sub>[![Discord](https://img.shields.io/discord/708027279854534656?logo=discord&logoColor=white)](https://discord.gg/e8EQFT)</sub></sub>

## Responsáveis
* João Tavares - [@TavaresJoao](https://github.com/TavaresJoao)
* Victor Alberti Costa - [@victorUTF](https://github.com/victorUTF)
* Vitor Oliveira Dos Santos[@vitor-o-s](https://gitlab.com/vitor-o-s)
* Jeferson Lima - [@jeferson.lima](https://gitlab.com/jeferson.lima)

## Referências

* [Brasil.IO - Dados abertos para um Brasil mais ligado](https://github.com/turicas/brasil.io)
* [Metabase](https://www.metabase.com/start/)