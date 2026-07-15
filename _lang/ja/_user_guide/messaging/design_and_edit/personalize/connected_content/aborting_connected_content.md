---
nav_title: コネクテッドコンテンツの中止
article_title: コネクテッドコンテンツの中止
page_order: 2
description: "この参照記事では、コネクテッドコンテンツのメッセージ中止に関するベストプラクティスについて説明します。"
---

# コネクテッドコンテンツの中止 {#aborting-connected-content}

> Liquidテンプレートを使用する場合、条件ロジックによってメッセージを中止するオプションがあります。このページでは、その際のベストプラクティスについて説明します。

以下の例では、条件 `connected.recommendations.size < 5` と `connected.foo.bar == nil` が、メッセージを中止する状況を指定しています。

{% raw %}
```
{% connected_content https://example.com/webservice.json :save connected %}
   {% if connected.recommendations.size < 5 or connected.foo.bar == nil %}
     {% abort_message() %}
   {% endif %}
```
{% endraw %}

## 中止理由の指定 {#specify-an-abort-reason}

中止理由を指定することもできます。中止理由は[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)に保存されます。この中止理由は文字列である必要があり、Liquidを含めることはできません。

{% raw %}
`{% abort_message('Could not get enough recommendations') %}`
{% endraw %}

{% alert important %}
Brazeは、中止されたメッセージをBrazeアカウントやCurrentsの送信数にカウントしません。
{% endalert %}

{% multi_lang_include connected_content/abort_and_retry_logic.md %}