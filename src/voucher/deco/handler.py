import json


def deco(event: dict, context):

    response = {
        "statusCode": 200,
        "body": json.dumps(event),
    }

    return response
