# Projeto
Projeto desenvolvido com intuito de criar um servidor 
com flask quee salvasse as informações em um banco de 
dados não relacional.

## Como Funciona?

O servidor possui apenas a rota */solicitacao* com os 
seguintes métodos:

1. **GET**: Lista todas as solicitações de cartões no sistema.

2. **POST**: Insere uma nova solicitação de cartão.

3. **DELETE**: Deleta uma solicitação.


## Rodando o projeto

Assim que realizar o download ou clonar o projeto, 
basta instalar os requirements através do comando:

```bash
$ python -m pip install -r requirements.txt
```

Após a instalação, o servidor pode ser inicializado com o comando:

```bash
$ python app.py
```

**OBS**: Você precisa ter o MongoDB instalado e rodando para o servidor 
funcionar corretamente. Em meus testes eu utilizei a versão 4.4.1

Você também pode rodar este servidor utilizando o docker-compose 
realizando os seguintes comandos:

```bash
$ docker-compose build
$ docker-compose up -d
```

Desta maneira, o servidor estará rodando em uma imagem do Docker, juntamente 
com uma imagem do MongoDB na mesma versão que utilizei, e se comunicando com 
sua máquina através da porta 5000.
