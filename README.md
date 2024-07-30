# Marketing counter

## Development

```sh
# copy env.local to .env
cp env.local .env.local
```

```sh
# local build and run the project
docker compose -f compose/local/docker-compose.yaml up --build
```

## Production

```sh
# copy env.local to .env.prod
cp env.prod .env.prod
```

```sh
# production build and run the project
docker compose -f compose/prod/docker-compose.yaml up --build -d
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
