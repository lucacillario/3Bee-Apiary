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

# Serverless
In the `serverless` directory you can find the code used
to deploy some basic REST APIs using the [Serverless Framework](https://www.serverless.com/).

These APIs are deployed to `AWS Lambda` and interact with `DynamoDB`.

## How to deploy
```commandline
cd serverless/apiary/
serverless deploy
```
If the deployment succeed, in order to get some results from the APIs, 
remember to add some data in the DynamoDB tables.

## Deployed endpoints
- `/lambdas/devices/{serial}`: given a device serial number, returns the device info.
- `/lambdas/devices`: returns a paginated list of devices.
- `/lambdas/hives/{id}`: given an hive ID, returns the hive info.
- `/lambdas/hives`: returns a paginated list of hives.