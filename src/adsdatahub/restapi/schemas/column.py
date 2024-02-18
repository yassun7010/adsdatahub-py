from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.field_type import FieldTypeModel


class ColumnModel(Model):
    columnId: str
    columnType: FieldTypeModel
