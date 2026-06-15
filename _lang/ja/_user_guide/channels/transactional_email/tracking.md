---
nav_title: "トラッキングの設定"
article_title: "トラッキング"
page_order: 2
description: "このリファレンス記事では、トランザクションメールキャンペーンのリアルタイムトラッキングの設定方法について説明します。"
page_type: reference
tool:
  - キャンペーン
channel: email

---

# トランザクションメールの追跡 {#track-transactional-emails}

> このページでは、[トランザクションメールキャンペーン]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email/)のリアルタイムトラッキングの設定方法について説明します。エンドポイント自体の詳細については、[APIトリガー配信を使用したトランザクションメールの送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message/)を参照してください。

トランザクションメール（注文確認やパスワードリセットなど）を送信する際、それらが顧客に届いているかどうかを把握することが不可欠です。Brazeのトランザクション HTTPイベントポストバックを使用すると、すべてのトランザクションメールのステータスに関するリアルタイムのインサイトを取得できるため、問題が発生した場合に迅速に対応できます。

この機能を使用すると、以下のことが可能です。

- **メールをリアルタイムで監視する:** メッセージが送信、処理、配信されたか、または問題が発生したかを即座に確認できます。
- **プロアクティブに対応する:** メッセージを再試行したり、SMSなどの別のチャネルに切り替えたり、フォールバックシステムを使用して、コミュニケーションが確実に配信されるようにします。

## トランザクションメールのトラッキング {#tracking-your-transactional-emails}

{% multi_lang_include http_event_postback.md %}