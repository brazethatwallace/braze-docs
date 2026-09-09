---
nav_title: サブスクリプショングループ
article_title: サブスクリプショングループ
page_order: 1
description: "この記事では、LINEメッセージの購読グループについて説明します。"
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# LINE購読グループ {#line-subscription-groups}

> LINEユーザーには、購読中と購読解除の2つの購読状態があります。各購読グループはそれぞれのLINEチャネルに接続されます。購読グループのクロスチャネルの概要については、[購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)を参照してください。

| 状態 | 定義 |
| --- | --- |
| 購読中 | ユーザーがLINEアプリ内からLINEチャネルをフォローしました。連携ステップの完了後にユーザーがフォローすると、自動的に購読中になります。 |
| 購読解除 | ユーザーがLINEアプリ内からLINEチャネルをフォローしなかった、またはユーザーが明示的にLINEチャネルのフォローを解除しました。<br><br> LINE購読グループから購読解除したユーザーは、その購読グループに属する送信チャネルからのLINEメッセージを受信しなくなります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE購読グループ" }

## ユーザーのLINE購読グループの設定 {#set-a-users-line-subscription-group}

LINEがユーザーの購読ステータスをホストします。Brazeはフォローおよびフォロー解除イベントを処理して、購読ステータスを更新します。

{% alert important %}
LINE購読グループはワークスペース間で移動できません。購読グループをアーカイブした後に別のワークスペースでLINEチャネルを再統合すると、Brazeはターゲットワークスペースに新しい購読グループを作成します。元の購読グループは最初のワークスペースに残ります。
{% endalert %}

## アーカイブの動作 {#archive-behavior}

- **標準アーカイブ:** LINE購読グループをアーカイブし、そのチャネルを別のワークスペースに再統合しない場合は、後で購読グループのアーカイブを解除できます。
- **永久アーカイブ:** 購読グループをアーカイブした後にLINEチャネルを別のワークスペースに再統合すると、元の購読グループは永久にアーカイブされ、ダッシュボードからアーカイブを解除することはできません。

チャネルの再統合手順については、[LINE設定]({{site.baseurl}}/user_guide/channels/line/line_setup#re-integrate-a-line-channel-in-another-workspace)を参照してください。