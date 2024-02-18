from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.parameter_value import ParameterValueModel


class QueryMetadataModel(Model):
    queryResourceName: str
    queryTitle: str
    customerId: str
    adsDataCustomerId: str
    matchDataCustomerId: str
    parameterValues: dict[str, ParameterValueModel]
    startTime: str
    endTime: str
    queryText: str
    destTable: str
    userListId: str
