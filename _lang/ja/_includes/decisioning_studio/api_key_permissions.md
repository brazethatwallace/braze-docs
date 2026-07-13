| 権限 | 目的 | 必須かどうか |
| :--- | ----- | :---: |
| [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) | ユーザープロファイルのカスタム属性を更新します。また、テスト送信を使用する際に一時的なユーザープロファイルを作成します。 | &#10003; |
| [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) | テスト送信の使用中に作成された一時的なユーザープロファイルを削除します。 | テスト送信のみ |
| [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) | 選択した各セグメントからユーザーの一覧をエクスポートして、毎朝利用可能なオーディエンスのコミュニケーションを更新します。 | &#10003; |
| [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) | セグメントの代わりに `external_id` を使用してユーザーをターゲットにする場合に、識別子の一覧を取得します。Decisioning Studioは個人を特定できる情報（PII）を受け付けないため、`fields_to_export` パラメーターが非PIIフィールドのみを返すようにする必要があります。 | `external_ids` を使用している場合のみ |
| [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | Decisioning Studioの実験者向けに設定されたAPI キャンペーンを使用して、推奨される時間に推奨されるバリアントを送信します。 | &#10003; |
| [`/campaigns/list`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/#prerequisites) | アクティブなキャンペーンの一覧を取得し、実験に使用可能なメールコンテンツを抽出します。 | &#10003; |
| [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/) | 集計されたキャンペーンデータをエクスポートして、Decisioning Studioでのレポート作成、検証、トラブルシューティングを可能にします。レポート値を比較し、ベースラインのパフォーマンスを分析できます。<br><br>必須ではありませんが、この権限を推奨します。 |  |
| [`/campaigns/details`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) | 既存のキャンペーンからHTMLコンテンツ、件名、画像リソースを取得して、実験に使用します。 | &#10003; |
| [`/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) | アクティブなキャンバスの一覧を取得し、実験に使用可能なメールコンテンツを抽出します。 | &#10003; |
| [`/canvas/data_series`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/) | 集計されたキャンバスデータをエクスポートして、レポート作成と検証を行います。特にBAUがキャンバスでオーケストレーションされている場合に有用です。<br><br>必須ではありませんが、この権限を推奨します。 |  |
| [`/canvas/details`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/#prerequisites) | 既存のキャンバスからHTMLコンテンツ、件名、画像リソースを取得して、実験に使用します。 | &#10003; |
| [`/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/) | 既存の全セグメントを、Decisioning Studioの実験者向けの潜在的なターゲットオーディエンスとして取得します。 | &#10003; |
| [`/segments/data_series`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/) | オーディエンスを選択する際にDecisioning Studioに表示されるセグメントサイズ情報をエクスポートします。 | &#10003; |
| [`/segments/details`]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/#prerequisites) | オーディエンスのサイズやパフォーマンスの変化を理解するのに役立つ、エントリや終了の基準などのセグメントの詳細を取得します。 |  |
| [`/templates/email/create`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) | 実験用に、[ダイナミックなプレースホルダー]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)（Braze Liquidタグ）を含む選択済みの基本HTMLテンプレートのコピーを作成し、オリジナルへの変更を回避します。 | &#10003; |
| [`/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) | コールトゥアクションなどの実験条件が変更された場合に、Decisioning Studioで作成されたテンプレートのコピーに更新を反映します。 | &#10003; |
| [`/templates/email/info`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/#prerequisites) | BrazeインスタンスでDecisioning Studioによって作成されたテンプレートの情報を取得します。 | &#10003; |
| [`/templates/email/list`]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) | テンプレートがBrazeインスタンスに正常にコピーされたことを検証します。 | &#10003; |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Table" }