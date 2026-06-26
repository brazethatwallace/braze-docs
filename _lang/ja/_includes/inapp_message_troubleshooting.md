### 表示のトラブルシューティング {#troubleshooting-in-app-message-display}

アプリがアプリ内メッセージのリクエストと受信に成功しているにもかかわらず表示されない場合、デバイス側のロジックが表示を妨げている可能性があります。

1. トリガーイベントは想定どおりに発生していますか？テストするには、メッセージを別のアクション（セッション開始など）でトリガーするように設定し、表示されるかどうかを確認してください。
{% if include.sdk == "iOS" %}
2. トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift#overriding-the-default-rate-limit)（デフォルトは30秒）に基づいてレート制限されます。
{% elsif include.sdk == "Android" %}
2. トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=android#overriding-the-default-rate-limit)（デフォルトは30秒）に基づいてレート制限されます。
{% elsif include.sdk == "Web" %}
2. トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web#overriding-the-default-rate-limit)（デフォルトは30秒）に基づいてレート制限されます。
{% endif %}
3. 画像のダウンロードに失敗すると、画像付きのアプリ内メッセージが表示されなくなります。デバイスのログを確認して、ダウンロードの失敗がないか確認してください。画像を一時的に削除して、メッセージが表示されるかどうか試してみてください。
{% case include.sdk %}
  {% when "iOS" %}
4. アプリ内メッセージ処理をカスタマイズするためにデリゲートを設定している場合は、そのデリゲートが表示を抑制していないことを確認してください。[カスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift)を参照してください。
  {% when "Android" %}
4. アプリ内メッセージ処理をカスタマイズするためにデリゲートを設定している場合は、そのデリゲートが表示を抑制していないことを確認してください。[カスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)を参照してください。
  {% when "Web" %}
4. [`braze.subscribeToInAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)を介してカスタムのアプリ内メッセージ処理を行っている場合は、コールバックが表示を抑制していないことを確認してください。[カスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=web)を参照してください。
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
5. デバイスの向きがアプリ内メッセージの設定と一致しない場合、メッセージは表示されません。
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. ネットワーク状況によっては、表示前に画像のダウンロードが完了しない場合があります。低速な接続やパフォーマンスの低いデバイスでは、追加の時間を確保するか、アセットサイズを最適化してください。
{% endcase %}

{% if include.sdk == "iOS" %}
### インプレッションとクリックが記録されない {#impressions-and-clicks-arent-being-logged}

メッセージ表示またはクリックアクションを手動で処理するようにアプリ内メッセージデリゲートを設定している場合は、アプリ内メッセージの[クリック](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:))と[インプレッション](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:))を手動で記録する必要があります。
{% elsif include.sdk == "Android" %}
### インプレッションとクリックが記録されない

メッセージ表示またはクリックアクションを手動で処理するようにアプリ内メッセージデリゲートを設定している場合は、アプリ内メッセージのクリックとインプレッションを手動で記録する必要があります。
{% endif %}