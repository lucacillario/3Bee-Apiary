import os

import boto3

from lambdas import responses

dynamodb = boto3.resource("dynamodb")


def get(event, context):
    table = dynamodb.Table(os.environ["DEVICE_TABLE"])

    try:
        device_serial = event["pathParameters"]["serial"]
    except KeyError:
        return responses.HTTP_400_BAD_REQUEST({"detail": "`serial` path param is missing"})

    result = table.get_item(Key={"serial": device_serial})

    if "Item" not in result:
        return responses.HTTP_404_NOT_FOUND(
            {"detail": "Device with serial {} not found!".format(device_serial)}
        )

    return responses.HTTP_200_OK(result["Item"])


def list(event, context):
    table = dynamodb.Table(os.environ["DEVICE_TABLE"])

    try:
        next_ = event["queryStringParameters"]["next"]
        result = table.scan(ExclusiveStartKey={"serial": next_})
    except KeyError:
        result = table.scan()

    last_evaluated_key = result.get("LastEvaluatedKey", None)

    return responses.HTTP_200_OK({"items": result["Items"], "next": last_evaluated_key})
