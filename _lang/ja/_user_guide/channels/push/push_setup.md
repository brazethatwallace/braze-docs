---
nav_title: "セットアップ"
article_title: プッシュのセットアップ
page_order: 0
layout: dev_guide
guide_top_header: "プッシュのセットアップ"
guide_top_text: "プッシュトークンのライフサイクルとサブスクリプション状態を理解して、プッシュ通知を適切なユーザーに届けましょう。"

page_type: landing
description: "Brazeにおけるプッシュ通知のプッシュトークンライフサイクルとサブスクリプション状態について説明します。"

guide_featured_title: "セクション記事"
guide_featured_list:
  - name: プッシュトークンのライフサイクル
    link: /docs/user_guide/channels/push/push_setup/push_token_lifecycle
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: プッシュサブスクリプション状態
    link: /docs/user_guide/channels/push/push_setup/push_subscription_states
    image: /assets/img/braze_icons/users-01.svg
---

## 前提条件 {#prerequisites}

Brazeを使用してプッシュメッセージを作成・送信するには、開発者と連携してWebサイトまたはアプリにプッシュを統合する必要があります。詳細な手順については、各プラットフォームの統合ガイドを参照してください。

- [iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)

## プッシュプライミング {#push-priming}

ユーザーがメッセージを受け取るにはプッシュへのオプトインが必要であることを念頭に置いてください。そのため、アプリ内メッセージを使用して、プッシュ通知を送信する理由やプッシュを有効にすることでどのようなメリットがあるかを顧客に説明することをお勧めします。このプロセスは[プッシュプライミング]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)と呼ばれています。