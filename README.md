executar

PS> docker build . -t naldfranc/cprod:1.0

PS> docker run --network=bridge -d -p 8000:8000 -p 5441:5441 -v .:/CPROD --name cprod naldfranc/cprod:1.0
PS> docker run --network=host -d -p 8000:8000 -p 5441:5441 -v .:/CPROD --name cprod naldfranc/cprod:1.0

PS> docker-compose -up

Abrir um terminal dentro do docker iniciado


...
Criar o ambiente virtual

```
python -m venv ./venv
```
Para ativar o ambiente virtual
```
# source venv/bin/activate
c:\> venv/Scripts/Activate.ps1
```

#Instalar os pacotes um a um
python -m pip install fastapi psycopg2 uvicorn pydantic sqlalchemy

#se der erro use abaixo
pip install --upgrade pip

#Instalar os pacotes pelo arquivo requiriments.txt
pip install -r requirements.txt


#Caso ainda não exista o arquivo requeriments.txt, cria-lo com  as dependências do projeto
pip freeze > requirements.txt
#recria-lo a cada pacote instalado

## Rodando a API Produtos utilizando o framework FastAPI
#Para executar o servidor FastAPI

uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```


dentro da pasta lanacmento-> models.py
...
class Producao(models.Model):
    producao_id = models.AutoField(primary_key=True, db_column="td01_producao_id")
    leitura = models.CharField(max_length=24, db_column="td01_leitura")
    cod_produto = models.CharField(max_length=15, db_column="td01_cod_produto")
    descricao = models.CharField(max_length=30, db_column="td01_descricao")
    status = models.IntegerField(db_column="td01_status")
    id = models.CharField(max_length=6, db_column="td01_id")
    dt = models.DateTimeField(db_column="td01_dt")
    hr = models.TimeField( db_column="td01_hr")
    serie = models.CharField(max_length=6,db_column="td01_serie")
    re = models.CharField(max_length=6, db_column="td01_re")
    local = models.CharField(max_length=4, db_column="td01_local")
    os = models.IntegerField(db_column="td01_os")
class Meta:
        # Definindo o nome da tabela no banco de dados
        db_table = 'td01_producao'

def __str__(self):
        return self.name
dentro da pasta lanacmento-> models.py
...
class Producao(models.Model):
    producao_id = models.AutoField(primary_key=True, db_column="td01_producao_id")
    leitura = models.CharField(max_length=24, db_column="td01_leitura")
    cod_produto = models.CharField(max_length=15, db_column="td01_cod_produto")
    descricao = models.CharField(max_length=30, db_column="td01_descricao")
    status = models.IntegerField(db_column="td01_status")
    id = models.CharField(max_length=6, db_column="td01_id")
    dt = models.DateTimeField(db_column="td01_dt")
    hr = models.TimeField( db_column="td01_hr")
    serie = models.CharField(max_length=6,db_column="td01_serie")
    re = models.CharField(max_length=6, db_column="td01_re")
    local = models.CharField(max_length=4, db_column="td01_local")
    os = models.IntegerField(db_column="td01_os")
class Meta:
        # Definindo o nome da tabela no banco de dados
        db_table = 'td01_producao'

def __str__(self):
        return self.name
dentro da pasta lanacmento-> models.py
...
class Producao(models.Model):
    producao_id = models.AutoField(primary_key=True, db_column="td01_producao_id")
    leitura = models.CharField(max_length=24, db_column="td01_leitura")
    cod_produto = models.CharField(max_length=15, db_column="td01_cod_produto")
    descricao = models.CharField(max_length=30, db_column="td01_descricao")
    status = models.IntegerField(db_column="td01_status")
    id = models.CharField(max_length=6, db_column="td01_id")
    dt = models.DateTimeField(db_column="td01_dt")
    hr = models.TimeField( db_column="td01_hr")
    serie = models.CharField(max_length=6,db_column="td01_serie")
    re = models.CharField(max_length=6, db_column="td01_re")
    local = models.CharField(max_length=4, db_column="td01_local")
    os = models.IntegerField(db_column="td01_os")
class Meta:
        # Definindo o nome da tabela no banco de dados
        db_table = 'td01_producao'

def __str__(self):
        return self.name
