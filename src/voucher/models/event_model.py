from dataclasses import dataclass

from marshmallow import Schema, fields, post_load, EXCLUDE


@dataclass
class HttpApiEvent:
    raw_path: str
    body: str


class EventSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    raw_path = fields.Str(data_key='rawPath')
    body = fields.Str(data_key='body')

    @post_load
    def make_event(self, data, **kwargs):
        return HttpApiEvent(**data)
