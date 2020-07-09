import json

from src.voucher.models.code_model import CodeModel


def list_codes(event: dict, context):
    scan_result = CodeModel.scan()
    result = {'status': 'ok', 'payload': [dict(item) for item in scan_result]}

    response = {
        "statusCode": 200,
        "body": json.dumps(result),
    }

    return response
