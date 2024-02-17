from ads_data_hub.restapi.schemas._model import Model
from ads_data_hub.restapi.schemas.field_type import FieldTypeModel


class ColumnModel(Model):
    columnId: str
    columnType: FieldTypeModel
