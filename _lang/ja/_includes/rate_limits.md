<!---DEFAULT RATE LIMIT-->

{% if include.endpoint == "default" %}
[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、このエンドポイントにはBrazeのデフォルトのレート制限（1時間あたり250,000リクエスト）が適用されます。

<!---PUT /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "update dashboard user" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/scim/v2/Users/` GET、DELETE、およびPOSTエンドポイントと共有されます。

<!---GET /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "look up dashboard user" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/scim/v2/Users/` PUT、GET、DELETE、およびPOSTエンドポイントと共有されます。

<!---DELETE /scim/v2/Users/YOUR_ID_HERE--->
{% elsif include.endpoint == "delete dashboard user" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/scim/v2/Users/` PUT、GET、およびPOSTエンドポイントと共有されます。

<!---POST /scim/v2/Users--->
{% elsif include.endpoint == "create dashboard user" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/scim/v2/Users/` PUT、GET、およびDELETEエンドポイントと共有されます。

<!---GET /scim/v2/Users--->
{% elsif include.endpoint == "look up dashboard user email" %}
このエンドポイントには、1日あたり1会社あたり5,000リクエストのレート制限があります。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/scim/v2/Users/` PUT、GET、DELETE、およびPOSTエンドポイントと共有されます。

<!---/users/external_id/rename-->
<!---/users/external_id/remove-->

{% elsif include.endpoint == "external id migration" %}
[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、このエンドポイントには1分あたり1,000リクエストのレート制限が適用されます。

<!---/users/track-->

{% elsif include.endpoint == "users track" %}
このエンドポイントのレート制限は、ご契約内容によって異なります。料金体系にデータポイントが含まれている顧客の場合、Brazeは3秒あたり3,000リクエストのバースト制限を適用します。その他すべての顧客の場合、制限はご契約条件に基づいて設定されます。お客様のアカウントの現在の制限は、ダッシュボードの**設定** > **APIと識別子** > **API使用状況ダッシュボード**で確認できます。

各`/users/track`リクエストには、`attributes`、`events`、`purchases`を合わせて最大75個のオブジェクトを含めることができます。各オブジェクトは1人のユーザーを更新できます。単一のユーザープロファイルを複数のオブジェクトで更新することも可能です。

Monthly Active Users CY 24-25、Universal MAU、Web MAU、またはMobile MAUを購入された顧客には、追加のレート制限が適用されます。詳細については、[Monthly Active Users CY 24-25の制限]({{site.baseurl}}/api/endpoints/user_data/post_user_track#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau)を参照してください。

{% details レガシーレート制限 %}
レガシーレート制限が適用される顧客の場合、各`/users/track`リクエストには最大75個の属性オブジェクト、75個のイベントオブジェクト、75個の購入オブジェクトを含めることができます。各オブジェクトは1人のユーザーを更新でき、1リクエストあたり最大225個のオブジェクトを組み合わせることができます。単一のユーザープロファイルを複数のオブジェクトで更新することも可能です。
{% enddetails %}

詳細については、[APIレート制限]({{site.baseurl}}/api/api_limits)を参照してください。制限の引き上げが必要な場合は、カスタマーサクセスマネージャーにお問い合わせください。

<!---/users/export/ids-->

{% elsif include.endpoint == "users export ids" %}
2024年8月22日以降にBrazeにオンボーディングした場合、このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、1分あたり250リクエストのレート制限が適用されます。

以下の要件を満たすことで、このエンドポイントのレート制限を1秒あたり40リクエストまで引き上げることもできます。

- ワークスペースにデフォルトのレート制限（1分あたり250リクエスト）が有効になっていること。既存のレート制限の解除についてサポートが必要な場合は、担当のBrazeアカウントマネージャーにお問い合わせください。
- リクエストに、受け取りたいすべてのフィールドを列挙する`fields_to_export`パラメーターが含まれていること。

{% alert important %}
`fields_to_export`パラメーターに`canvases_received`または`campaigns_received`を含めると、リクエストは高速なレート制限の対象外となります。これらをリクエストに含めるのは、具体的なユースケースがある場合に限ることを推奨します。
{% endalert %}

<!---/users/delete-->

{% elsif include.endpoint == "users delete" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/users/alias/new`、`/users/identify`、`/users/merge`、および`/users/alias/update`エンドポイントと共有されます。

<!---/users/alias/new-->

{% elsif include.endpoint == "users alias new" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/users/delete`、`/users/identify`、`/users/merge`、および`/users/alias/update`エンドポイントと共有されます。

<!---/users/alias/update-->

{% elsif include.endpoint == "users alias update" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/identify`、および`/users/merge`エンドポイントと共有されます。

<!---/users/identify-->

{% elsif include.endpoint == "users identify" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/merge`、および`/users/alias/update`エンドポイントと共有されます。

<!---/users/merge-->

{% elsif include.endpoint == "users merge" %}
このエンドポイントには、1分あたり20,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/users/delete`、`/users/alias/new`、`/users/identify`、および`/users/alias/update`エンドポイントと共有されます。

<!---/custom_attributes-->

{% elsif include.endpoint == "custom_attributes" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/events`、`/events/list`、および`/purchases/product_list`エンドポイントと共有されます。

<!---/events-->

{% elsif include.endpoint == "events" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/custom_attributes`、`/events/list`、および`/purchases/product_list`エンドポイントと共有されます。

<!---/events/list-->

{% elsif include.endpoint == "events list" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/custom_attributes`、`/events`、および`/purchases/product_list`エンドポイントと共有されます。

<!---/purchases/product_list-->

{% elsif include.endpoint == "purchases product list" %}
このエンドポイントには、1時間あたり1,000リクエストの共有レート制限が適用されます。このレート制限は、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/custom_attributes`、`/events`、および`/events/list`エンドポイントと共有されます。

<!---/messages/send-->
<!---/campaigns/trigger/send-->
<!---/canvas/trigger/send-->

{% elsif include.endpoint == "send endpoints" %}
リクエストでConnected Audienceフィルターを使用する場合、このエンドポイントには1分あたり250リクエストのレート制限が適用されます。それ以外の場合、`external_id`を指定すると、[APIレート制限]({{site.baseurl}}/api/api_limits#requests-with-shared-rate-limits)に記載されているエンドポイント間で共有される1時間あたり250,000リクエストのデフォルトのレート制限が適用されます。

Brazeのエンドポイントは[APIリクエストのバッチ処理]({{site.baseurl}}/api/api_limits#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の`external_ids`
- リクエスト内で[Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)オブジェクトとして定義された、任意のサイズのオーディエンスセグメント

<!---/transactional/v1/campaigns/{campaign_id}/send -->

{% elsif include.endpoint == "transactional email" %}
`/transactional/v1/campaigns/{campaign_id}/send`エンドポイントは有料のエンドポイントであり、単位は時間あたりです（例：パッケージに応じて1時間あたり50,000）。エンドポイントごとの個別のレート制限は存在しません。割り当てられた容量を超えて送信することは可能ですが、SLAの対象となるのは割り当てられた容量のみです。このエンドポイントへのリクエストは[全体の外部APIレート制限]({{site.baseurl}}/api/api_limits)にカウントされます。その制限（例：全エンドポイントで1時間あたり250,000リクエスト）を超えると、Brazeは429を返し、リクエストはスロットリングされます。トランザクション量のカウントは毎時リセットされるため、1時間後には新たな割り当てが利用可能になります。SLAの対象範囲内では、メールの99.9%が1分以内に送信されます。

<!---POST /preference_center/v1 and PUT /preference_center/v1/{preferenceCenterExternalID}-->
{% elsif include.endpoint == "post or put preference center" %}
このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、1ワークスペースあたり1分あたり10リクエストのレート制限があります。

<!---GET /preference_center/v1-->
{% elsif include.endpoint == "get preference center" %}
このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、1ワークスペースあたり1分あたり1,000リクエストのレート制限があります。

<!---/sends/id/create-->

{% elsif include.endpoint == "sends id create" %}
このエンドポイントを使用すると、特定のワークスペースに対して1日あたり最大100個のカスタム送信識別子を作成できます。作成する各`send_id`と`campaign_id`の組み合わせは、1日の制限にカウントされます。有効なリクエストに対するレスポンスヘッダーには、現在のレート制限ステータスが含まれます。詳細については、[APIレート制限]({{site.baseurl}}/api/api_limits)を参照してください。

<!---/subscription/status/set-->
{% elsif include.endpoint == "subscription status set" %}
このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、`/subscription/status/set`と`/v2/subscription/status/set`エンドポイント間で共有される1分あたり5,000リクエストのレート制限があります。

<!-- Add this phrase back ", as documented in [API rate limits]({{site.baseurl}}/api/api_limits)" to CDI endpoints for GA -->

<!---GET /cdi/integrations--->
{% elsif include.endpoint == "cdi list integrations" %}
このエンドポイントには、1分あたり50リクエストのレート制限があります。

<!---POST /cdi/integrations/{integration_id}/sync--->
{% elsif include.endpoint == "cdi job sync" %}
このエンドポイントには、1分あたり20リクエストのレート制限があります。

<!---POST /cdi/integrations/{integration_id}/job_sync_status--->
{% elsif include.endpoint == "cdi job sync status" %}
このエンドポイントには、1分あたり100リクエストのレート制限があります。

<!---/media_library/create, /media_library/replace_file--->
{% elsif include.endpoint == "media_library" %}
このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、1時間あたり100リクエストのレート制限があります。

{% endif %}

<!---Additional if statement for Messaging endpoints-->

{% if include.category == "message endpoints" %}

Brazeのエンドポイントは[APIリクエストのバッチ処理]({{site.baseurl}}/api/api_limits#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の`external_ids`
- `segment_id`で指定される、Brazeダッシュボードで作成された任意のサイズのセグメント
- リクエスト内で[Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)オブジェクトとして定義された、任意のサイズのオーディエンスセグメント

{% endif %}

{% if include.category == "send messages endpoints" %}

Brazeのエンドポイントは[APIリクエストのバッチ処理]({{site.baseurl}}/api/api_limits#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- それぞれに個別のメッセージパラメーターを持つ、最大50個の特定の`external_ids`
- リクエスト内で[Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)オブジェクトとして定義された、任意のサイズのオーディエンスセグメント

{% endif %}

<!---Additional if statement for Translation endpoints-->

{% if include.endpoint == "translation endpoints" %}

このエンドポイントには、1分あたり250,000リクエストのレート制限があります。

{% endif %}

<!---Additional if statement for /messages/send endpoint-->

{% if include.category == "message send endpoint" %}

Brazeのエンドポイントは[APIリクエストのバッチ処理]({{site.baseurl}}/api/api_limits#batching-api-requests)をサポートしています。メッセージングエンドポイントへの単一のリクエストは、次のいずれかに到達できます。

- 最大50個の特定の`external_ids`
- `segment_id`で指定される、Brazeダッシュボードで作成された任意のサイズのセグメント
- リクエスト内で[Connected Audience]({{site.baseurl}}/api/objects_filters/connected_audience)オブジェクトとして定義された、任意のサイズのオーディエンスセグメント

{% endif %}

{% if include.endpoint == "asynchronous catalog item" %}

このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、すべての非同期カタログアイテムエンドポイント間で1分あたり16,000リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "synchronous catalog item" %}

このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、すべての同期カタログアイテムエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "synchronous catalog" %}

このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、すべての同期カタログエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "asynchronous catalog fields" or include.endpoint == "asynchronous catalog selections" %}

このエンドポイントには、[APIレート制限]({{site.baseurl}}/api/api_limits)に記載されているように、すべての非同期カタログフィールドおよびセレクションエンドポイント間で1分あたり50リクエストの共有レート制限があります。

{% endif %}

{% if include.endpoint == "export campaign analytics" %}

このエンドポイントには、1分あたり50,000リクエストのレート制限があります。

{% endif %}