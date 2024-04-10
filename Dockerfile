# Base da imagem Docker a ser utilizada
FROM python:3.12.2-alpine

WORKDIR /cprod

VOLUME /cprod

COPY ./app app


# copiar o arquivo de instalação dos requisitos do ambiente
COPY ./main.py /cprod/main.py
COPY ./requirements.txt .
COPY .gitignore /cprod/.gitignore
COPY docker-compose.yaml /cprod/docker-compose.yaml
COPY Dockerfile /cprod/Dockerfile
COPY README.md /cprod/README.md

#EXPOSE 80
#EXPOSE 443
EXPOSE 5441
EXPOSE 8000
#EXPOSE 1521

#RUN apt-get update && apt-get install apache2 && apt-get clean
#user user


# rodar um comando para instalar os pacotes necessários 
#RUN  /bin/sh -c python pip install -r requirements.txt

# comando a ser rodado dentro do container para rodar o servidor da api
# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
# python manage.py runserver 0.0.0.0:8000

#ENTRYPOINT [ "python","manage.py","runserver","0.0.0.0:8000"]

# Adicionar o interpretador de comandos bash
#RUN apk update && apk add bash

# Comando para o container não parar após a leitura de todas as camadas
ENTRYPOINT ["tail", "-f", "/dev/null"]