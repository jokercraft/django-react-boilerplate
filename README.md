# django-react-boilerplate
A minimalist boilerplate for Django with React.

### Setup

Create a .env file that stores database and redis configurations like below:

```
POSTGRES_DB=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
REDIS_HOST=redis
```

### Then build containers:

```
$ docker-compose build --no-cache
```

Now you are ready to start the development.


### Dev Environment

```
$ docker-compose up -d
$ cd frontend && npm run dev
```

### Prod Environment

```
$ docker-compose up -d
$ cd frontend && npm run build
```