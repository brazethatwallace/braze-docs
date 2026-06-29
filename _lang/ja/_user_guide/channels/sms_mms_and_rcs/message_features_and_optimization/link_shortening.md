---
nav_title: リンク短縮
article_title: リンク短縮
page_order: 1
description: "この参照記事では、SMSメッセージでリンク短縮を有効にする方法と、よくある質問について説明しています。"
page_type: reference
alias: "/link_shortening/"
tool:
  - キャンペーン
channel:
  - SMS
  - MMS
  - RCS
---

# リンク短縮 {#link-shortening}

> このページでは、SMSおよびRCSメッセージでリンク短縮を有効にする方法、短縮リンクのテスト、短縮リンクでのカスタムドメインの使用などについて説明します。

{% alert important %}
Brazeは[統合リンク短縮]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/?sdktab=unified)を段階的にロールアウトしています。これにより、すべてのSMSおよびRCSの短縮リンクが単一のパーソナライズ済みリンク形式（例：`brz.ai/abcdefgh`）に統合されます。
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include channels/sms/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include channels/sms/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}