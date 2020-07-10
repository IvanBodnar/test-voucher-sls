import json

from src.voucher.common.decorators import process_inputs


@process_inputs
def deco(event, context):
    print('---EVENT---', type(event))

    response = {
        "statusCode": 200,
        "body": "",
    }

    return response
