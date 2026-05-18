---
nav_title: サブスクリプショングループ
article_title: サブスクリプショングループ
page_order: 1
description: "この記事では、LINEメッセージのサブスクリプショングループについて説明します。"
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# LINEサブスクリプショングループ {#line-subscription-groups}

> LINEユーザーには、購読中と購読解除の2つのサブスクリプション状態があります。LINEではワークスペースごとに最大100のサブスクリプショングループを持つことができ、各サブスクリプショングループはそれぞれのLINEチャネルに接続されます。

| 状態 | 定義 |
| --- | --- |
| 購読中 | ユーザーがLINEアプリ内からLINEチャネルをフォローしました。連携ステップの完了後にユーザーがフォローすると、自動的に購読中になります。 |
| 購読解除 | ユーザーがLINEアプリ内からLINEチャネルをフォローしなかった、またはユーザーが明示的にLINEチャネルのフォローを解除しました。<br><br> LINEサブスクリプショングループから購読解除したユーザーは、そのサブスクリプショングループに属する送信チャネルからのLINEメッセージを受信しなくなります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINEサブスクリプショングループ" }

## ユーザーのLINEサブスクリプショングループの設定 {#setting-a-users-line-subscription-group}

LINEがユーザーのサブスクリプションステータスをホストしています。Brazeはフォローおよびフォロー解除イベントを処理し、サブスクリプションステータスを更新します。