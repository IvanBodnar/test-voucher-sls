from functools import wraps

from src.voucher.models.event_model import EventSchema


def process_inputs(func):
    @wraps(func)
    def wrapper(event: dict, *args, **kwargs):
        schema = EventSchema()
        http_api_event = schema.load(event)
        result = func(http_api_event, *args, **kwargs)
        return result
    return wrapper
