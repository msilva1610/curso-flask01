# Comandos do docker

### docker run para rodar e baixar a imagem do postgres
``` 
docker run --name pglocal -d -p 5432:5423 -e='POSTGRES_PASSWORD=secret' postgres
```

# Comandos postgres

### Comando para entrar no postgres
```
docker exec -it pglocal psql -U postgres 
```

### Criando uma base de dados no postgres
```
create database statusok_curso;
```

### Conectando a base de dados
``` 
\c statusok_curso
```

### Verificar todas as tabelas
```
\dt
```

# Comandos pipenv

```
pipenv shell
pipenv install flask==1.1.1
```

### Verificar dependências
```
pipenv graph
```

### Instalar o sqlalchemy
```
pipenv install flask-sqlalchemy
```

### Instalar o driver do postgres para o python
```
pipenv install psycopg2-binary
```

### 