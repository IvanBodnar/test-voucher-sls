import json

from src.voucher.models.code_model import CodeModel


def create(event: dict, context):
    new_code_data = json.loads(event.get('body'))
    result = {'status': 'ok', 'payload': new_code_data}
    try:
        CodeModel(**new_code_data).save()
    except Exception as e:
        result = {'status': 'error', 'payload': str(e)}

    response = {
        "statusCode": 200,
        "body": json.dumps(result),
    }

    return response
