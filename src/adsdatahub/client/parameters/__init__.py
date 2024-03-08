from adsdatahub.client.parameters.primitive_parameters import PrimitivePythonParameter

# TODO: 配列の型、デフォルト値などをサポートする必要があるが、後回し。
#
# TODO: デフォルト値や NULL のサポートをするためには、 dataclass や pydantic を利用する必要がある。
#
# NOTE: ドキュメントの記載は一貫性がない。
#       1. STRING または INT64 のプリミティブ型に加えて、配列と構造体をサポートしているように見える。
#          https://developers.google.com/ads-data-hub/reference/rest/v1/FieldType?hl=ja
#
#       2. AdsDataHub のコンソールからはさらに多くのパラメータの型を扱うことができるようだ。
#          https://developers.google.com/ads-data-hub/guides/run-queries?hl=ja#parameter_types
#
PythonParameter = PrimitivePythonParameter
"""
クエリのパラメータとして使える Python の型。
"""
