# To Do List API evoe

Essa API foi desenvolvida utilizando Django e Django-Rest-Framework. Com essa API é possível o usuário realizar um cadastro, logar com seus dados, e utilizar o token gerado pelo Login para
realizar operações CRUD, nas atividades salvas.

---

## Instalação

- Clone esse repositório no seu computador utilizando `https://github.com/meiraDaniel/testeEvoe` ou faça o download e a extração dos arquivos.

---

### Setup

- Dentro da pasta principal rode os comandos.

> Instale as dependências

```shell
$ pip install -r requirements.txt
```

> Rode o comando migrate, para criar o banco de dados. O arquivo com as migrations necessárias do modelo ToDo já estão criados.

```shell
$ python manage.py migrate
```

> Rode a API

```shell
$ python manage.py runserver
```

## Usabilidade

- Após inicialiazar o servidor, é possível realizar o cadastro de um novo usuário na url api/register/. Esse endpoint só permite metodos post, não sendo possível recuperar a lista de usuários.
- Com o novo usuário em mãos faça o login na url api/login, utilizando no body da requisição os dados cadastrados, como no exemplo abaixo:

> Imagens feitas utilizando o Postman

![alt text](https://github.com/meiraDaniel/apiEvoe/blob/master/imgs/Login.png?raw=true)


- Se a requisição for feita com sucesso, sera retornado como resposta um token de acesso JWT, com tempo de vida de 1 hora.
- Com esse token em mãos é possível realizar as operações CRUD, disponíveis na url api/activities passando o token no header da requisição, como no exemplo abaixo.

> Imagens feitas utilizando o Postman

![alt text](https://github.com/meiraDaniel/apiEvoe/blob/master/imgs/HeaderToken.png?raw=true)

