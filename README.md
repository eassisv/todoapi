# TODO List API

### Essa API foi criada com o objetivo fornecer um backend para desafios de frontend

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