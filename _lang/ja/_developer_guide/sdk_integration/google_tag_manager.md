---
nav_title: Google Tag Manager
article_title: Google Tag Managerと Braze SDK
platform:
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "ランタイム初期化、遅延初期化、Google Tag Manager などの方法を使用して Braze SDKを初期化する方法について説明します。"

---

# Google Tag Managerと Braze SDK {#google-tag-manager-with-the-braze-sdk}

> [Google Tag Manager（GTM）](https://developers.google.com/tag-platform/tag-manager)をBraze SDKと連携することで、コード変更やアプリの新バージョンリリースを必要とせずに、Brazeのイベントトラッキングやユーザー属性の更新をリモートでコントロールできます。

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/google_tag_manager.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## トラブルシューティング {#troubleshooting}

Brazeが初期化されない場合やイベントが期待どおりに表示されない場合は、GTMコンテナが公開されていること、トリガーとタグの発火順序がSDKの[ライフサイクルおよび初期化戦略]({{site.baseurl}}/developer_guide/sdk_integration/)と一致していること、テストデバイスがBrazeエンドポイントをブロックしていないことを確認してください。

初期化の失敗については、Brazeタグまたはカスタムタグプロバイダーが期待される `actionType` とパラメーターを受信しているかを確認してください（このページのAndroid、Swift、Webの各タブを参照）。GTMから発火されたイベントを検証する際に詳細なログを取得するには、各タブからリンクされているプラットフォーム統合ガイドの説明に従って、プラットフォームのSDKデバッグログを有効にしてください。