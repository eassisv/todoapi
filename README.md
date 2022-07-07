# TODO List Challenge

> :warning: **Essa API foi criada com o intuito de fornecer um backend para um desafio de desenvolvimento frontend, e por isso não possui configuração para execução em produção.** :warning:

> :warning: **A documentação das rotas da API ainda não está completa!** :warning:

## Rotas
* Autenticação
```
POST /accounts/signup/
  body:
    username: string
    password: string
    first_name: string
    last_name: string
    email: string
  response:
    username: string
    first_name: string
    last_name: string
    email: string

POST /accounts/signin/
  body:
    username: string
    password: string
  response:
    username: string
    first_name: string
    last_name: string
    email: string
```
* Todos
```
GET /todo-lists/
  body:
  response:
    username: string
    first_name: string
    last_name: string
    email: string
```
