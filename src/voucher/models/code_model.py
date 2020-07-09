from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, ListAttribute


class CodeModel(Model):
    class Meta:
        table_name = 'code-table'
        region = 'us-east-1'

    value = UnicodeAttribute(hash_key=True, null=False)
    brand_id = UnicodeAttribute(null=True)

    def __iter__(self):
        for name, attr in self.get_attributes().items():
            if isinstance(attr, ListAttribute):
                yield name, [a for a in getattr(self, name)]
            else:
                yield name, attr.serialize(getattr(self, name))