from adsdatahub.restapi.schemas._model import Model
from adsdatahub.restapi.schemas.parameter_value import ParameterValue


class QueryMetadataModel(Model):
    queryResourceName: str
    queryTitle: str
    customerId: str
    adsDataCustomerId: str
    matchDataCustomerId: str
    parameterValues: dict[str, ParameterValue]
    startTime: str
    endTime: str
    queryText: str
    destTable: str
    userListId: str
