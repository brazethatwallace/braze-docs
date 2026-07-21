{% alert note %}
RCSメッセージの場合、リンク短縮およびURLレベルのクリックトラッキングはメッセージ本文内のURLに対してサポートされていますが、推奨アクション内のURLに対してはサポートされていません。推奨アクションのURLに対するクリックはRCSクリックイベントとして記録されますが、CurrentsおよびSnowflakeでは`URL`フィールドと`SHORT_URL`フィールドはnullになります。
{% endalert %}