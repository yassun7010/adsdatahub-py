from typing import TypeAlias

CustomerId: TypeAlias = str
"""
クエリを実行する顧客のID。基本的には数値の文字列だが、"global" という文字列が変えることもある。

ex. "1234567890", "global"
"""

ResourceId: TypeAlias = str
"""
クエリのリソースID。

ex. "00d30ae989fa487d9a96e15afc244770"
"""
