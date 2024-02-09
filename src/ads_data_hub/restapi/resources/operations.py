class OperationsResource:
    """このリソースは、ネットワーク API 呼び出しの結果である長時間実行オペレーションを表します。"""

    def cancel(self, name: str):
        """
        長時間実行オペレーションの非同期キャンセルを開始します。
        サーバーは操作のキャンセルに全力を尽くしますが、成功は保証されません。
        このメソッドがサーバーでサポートされていない場合は、google.rpc.Code.UNIMPLEMENTED を返します。
        クライアントは Operations.GetOperation などのメソッドを使用して、キャンセルが成功したか、あるいはキャンセルしたにもかかわらずオペレーションが完了したかを確認できます。
        キャンセルが成功するとそのオペレーションは削除されず、google.rpc.Status.code が 1 の Operation.error 値を持つオペレーションになります。
        これは Code.CANCELLED に相当します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/cancel?hl=ja
        """
        raise NotImplementedError()

    def delete(self, name: str):
        """
        長時間実行オペレーションを削除します。
        このメソッドは、クライアントがそのオペレーション結果に関心がなくなったことを表しています。
        このメソッドではオペレーションはキャンセルされません。
        このメソッドがサーバーでサポートされていない場合は、google.rpc.Code.UNIMPLEMENTED を返します。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/delete?hl=ja
        """
        raise NotImplementedError()

    def get(self, name: str):
        """
        長時間実行オペレーションの最新の状態を取得します。
        クライアントはこのメソッドを使用して、API サービスで推奨される間隔でオペレーションの結果をポーリングできます。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/get?hl=ja
        """
        raise NotImplementedError()

    def list(self, name: str):
        """
        リクエストで指定されたフィルタに一致するオペレーションをリストします。
        このメソッドがサーバーでサポートされていない場合は、UNIMPLEMENTED を返します。

        注: name バインディングを使用すると、users/*/operations などの異なるリソース名スキームを使用するために、API サービスがバインディングをオーバーライドできます。
        バインディングをオーバーライドするときに、API サービスは "/v1/{name=users/*}/operations" のようなバインディングをサービス構成に追加する場合があります。
        下位互換性を維持するため、デフォルトの名前にはオペレーションのコレクション ID が含まれています。
        ただし、オーバーライドを行うユーザーは、名前のバインディングが親リソースであり、オペレーション コレクション ID がないことを確認する必要があります。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/list?hl=ja
        """
        raise NotImplementedError()

    def wait(self, name: str):
        """
        指定した長時間実行オペレーションが完了するか、指定したタイムアウトに達するまで待機し、最新の状態を返します。
        オペレーションがすでに完了している場合は、すぐに最新の状態が返されます。
        指定されたタイムアウトがデフォルトの HTTP/RPC タイムアウトを上回る場合は、HTTP/RPC タイムアウトが使用されます。
        サーバーがこのメソッドをサポートしていない場合は、google.rpc.Code.UNIMPLEMENTED を返します。
        このメソッドはベスト エフォートに基づきます。
        指定されたタイムアウト（直前を含む）の前に最新の状態を返すことがあります。
        つまり、すぐにレスポンスがあったとしても、オペレーションが完了したことを保証するものではありません。

        Reference: https://developers.google.com/ads-data-hub/reference/rest/v1/operations/wait?hl=ja
        """
        raise NotImplementedError()
