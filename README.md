# Utilizando a API Psycopg2 em uma aplicação

Neste repositório contém uma aplicação em python, que foi desenvolvida para fins de estudo, com o intuito de fazer uma conexão com um banco de dados PostgreSQL, utilizando o drive de conexão Psycopg2.

Esta aplicação foi feita atendendo os requisitos da atividade avaliativa da matéria de Banco de Dados 2 do curso de Ciência da Computação – UNIFEI.

#### Dupla:
**Flavio Mota Gomes -- 2018005379**

**Rafael Antunes Vieira -- 2018000980**

## Descrição dos arquivos

#### ATENÇÃO: Esta aplicação foi desenvolvida utilizando o padrão MVC ( MODEL, VIEW, CONTROLLER) !!!

- ### view.py
   Contém toda a parte da interface qda aplicação. Responsável pela entrada e saida de dados entre o usuário e o programa.
   
- ### controle.py
   Contém a parte da aplicação que tem a função de controlar as ações que o programa vai fazer, dependendo da opção selecionada no menu exibido pela view.py.
   
- ### model.py
   Responsável por receber os dados, preparar a query e executa-lá no banco de dados PostgreSQL, através do drive de conexão Psycopg2. Neste arquivo a parte de preparação da query e a parte de conexão do banco estão juntas no mesmo arquivo.
   
- ### modelM.py
   Este arquivo é parecido com o (model.py), mas não contêm a parte de conexão com o banco. Neste caso, o código escrito nesse arquivo, prepara a query e chama outro arquivo (config.py) que será responsavel por fazer a conexão com o banco. Essa separação foi feita para fins de estudo.
   
- ### config.py
  Responsavel por receber a query e os dados enviados do modelM para fazer a coneção no banco de dados, utilizando o driver de conexão Psycopg2.
  
- ### northwind.backup
  Backup do banco de dados utilizado para a conexão com a aplicação. 
  
  
 
