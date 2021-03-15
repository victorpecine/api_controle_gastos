# API para controle de gastos financeiros

Esta API foi desenvolvida em **Python 3.9.2**, **Django 3.1.7** e **Django Rest Framework 3.12.2**.

O banco de dados utilizado foi criado no **MySQL**.

## Parte I
- [x] Modelos do banco de dados
- [x] Serializers para conversão Python/Json e Json/Python em
- [x] Views para visualização em localhost:8000/ no formato Json
- [x] URLs para acesso no localhost:8000/
- [x] Criação de usuário admin para realizar operações CRUD

* Todo gasto tem quem paga (usuário)
* Todo gasto é realizado em um estabelecimento
* Cada estabelecimento possui apenas uma categoria
* Uma categoria pode pertencer a vários estabelecimentos
* Todo gasto tem uma forma de pagamento

![Diagrama relacional do BD](https://www.imagemhost.com.br/images/2021/03/15/diagrama_relacional_bd.png)

## Parte II
- [ ] URL para visualização dos estabelecimentos agrupados por categoria
- [ ] Visualização de soma por **categoria**, **estabelecimento** e **forma de pagamento**  no MySQL
- [ ] Visualização de soma por **categoria**, **estabelecimento** e **forma de pagamento**  no localhost:8000/admin
