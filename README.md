# 3Bee-Apiary
In this project we provide REST apis build on top of a simple apiary model.

# Setup
```commandline
cd apiary
pip install -r requirements.txt
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