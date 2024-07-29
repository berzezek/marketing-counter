# Marketing counter

## Instalation

```sh
# copy env.local to .env
cp env.local .env
```

```sh
# local build and run the project
docker compose -f compose/local/docker-compose.yaml up --build
```

## Usage

```sh
# run the project
docker compose up -d
```

## Authorizations

- rest framework token authentication

### Create token

```sh
docker ps
```

```sh
docker exec -it <container_backend-web> sh
```

```sh
python manage.py shell
```

```python

```shell
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

user = User.objects.get(username='admin')

token = Token.objects.create(user=...)
print(token.key)
```

## Database

- MYSQL for production
- SQLITE for development
  
## Endpoints

- GET /api/v1/marketing-counters/

```sh
curl -X GET -H "Authorization: Token <token>" http://localhost:8000/api/v1/marketing-counters/
```

- POST /api/v1/marketing-counter-create/

```sh
curl -X POST -H "Authorization: Token <token>" -d '{"foo": "bar"}' http://localhost:8000/api/v1/marketing-counter-create/
```

## VPS

```sh
https://vm.megahost.kz/

# ip address
45.136.59.93

# login password
root: FC4B63fF4Gm8
```
