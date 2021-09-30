# 3Bee-Apiary
In this project we provide REST apis build on top of a simple apiary model.

# Setup
```commandline
cd apiary
pip install -r requirements.txt
```

Create a `.env` file inside the `apiary` directory, containing the following env vars:
```
MYSQL_HOST=db
MYSQL_PORT=3306
MYSQL_DATABASE=db
MYSQL_USER=local
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
DJANGO_SECRET_KEY=local
DJANGO_SETTINGS_MODULE=apiary.settings.local
```

# Run dev server
```commandline
cd apiary
docker-compose up --build
```

A list of all the APIs is provided via Swagger at:
```
http://localhost:8000/api/schema/swagger-ui/
```

# Run tests
```commandline
cd apiary
docker-compose run web pytest
```