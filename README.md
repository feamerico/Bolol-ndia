# Bololândia

Projeto feito para a disciplina Projeto Integrador Transdisciplinar de Engenharia de Software II na faculdade EAD Cruzeiro do Sul Virtual - Unifran.

## Stack utilizada

**Front-end:** Bootstrap

**Back-end:** Django

## Aprendizados

Aprendi como o levantamento de requisitos e o planejamento das funcionalidades auxilia e facilita o desenvolvimento de um sistema e sobre a importância da manutenção dessa documentação.

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/feamerico/Bolol-ndia
```

Entre no diretório do projeto

```bash
  cd backend
```

Instale as dependências, preferencialmente dentro de um virtual environment

```bash
  pip install -r requirements.txt
```

Inicie o servidor

```bash
  python manage.py runserver
```

## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  python manage.py test
```

## Deploy

Link: https://bololandia.herokuapp.com/


## Roadmap

- Adicionar forma de pagamento: PIX (QR Code)

- Adicionar forma de pagamento: PIX (Cartão de crédito)

- Adicionar mensagem na tentativa de extrapolar a quantidade de estoque disponível do produto

- Adicionar página "Meu Perfil" para alterar as informações que servirão de padrão para auto preenchimento dos detalhes do pedido

- Adicionar edição de status do pedido para o superuser

## Autores

- [@feamerico](https://www.github.com/feamerico)

## Licença

[GPL](https://choosealicense.com/licenses/gpl-3.0/)
