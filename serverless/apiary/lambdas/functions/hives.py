import os

import boto3

from lambdas import responses

dynamodb = boto3.resource("dynamodb")


def get(event, context):
    table = dynamodb.Table(os.environ["HIVE_TABLE"])

    try:
        hive_id = int(event["pathParameters"]["id"])
    except KeyError:
        return responses.HTTP_400_BAD_REQUEST({"detail": "`id` path param is missing"})

    result = table.get_item(Key={"id": hive_id})

    if "Item" not in result:
        return responses.HTTP_404_NOT_FOUND(
            {"detail": "Hive with ID {} not found!".format(hive_id)}
        )

    return responses.HTTP_200_OK(result["Item"])


def list(event, context):
    table = dynamodb.Table(os.environ["HIVE_TABLE"])

    try:
        next_ = int(event["queryStringParameters"]["next"])
        result = table.scan(ExclusiveStartKey={"id": next_})
    except KeyError:
        result = table.scan()

    last_evaluated_key = result.get("LastEvaluatedKey", None)

    return responses.HTTP_200_OK({"items": result["Items"], "next": last_evaluated_key})
