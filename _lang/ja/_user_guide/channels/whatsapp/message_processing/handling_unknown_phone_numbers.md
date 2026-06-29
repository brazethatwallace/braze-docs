---
nav_title: "不明な電話番号の処理"
article_title: "不明な電話番号の処理"
description: "このリファレンス記事では、WhatsAppユーザーの不明な電話番号をBrazeがどのように処理するかについて説明しています。"
page_type: reference
channel:
  - WhatsApp
page_order: 50
---

# 不明な電話番号の処理 {#handle-unknown-phone-numbers}

> WhatsAppをBrazeで稼働させた後、不明なユーザーからメッセージを受信することがあります。以下のステップでは、未確認のユーザーと電話番号がどのように処理されるかを説明します。

## 不明な番号に対するオプトイン/アウトおよびカスタムキーワードワークフロー {#opt-inout-and-custom-keyword-workflow-for-unknown-numbers}

Brazeはまず、一致する番号を持つユーザーを検索します。見つからない場合、Brazeは以下の2つの方法のいずれかで不明な番号を自動的に処理します。

1. **[オプトインCanvas]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)を持つトリガーワードが設定されている場合:**
- Brazeは匿名プロファイルを作成します
- 以下の詳細でプロファイルにユーザーエイリアスを割り当てます:
  - ユーザーが提供した電話番号を値とする`alias_name`
  - `phone`を値とする`alias_label`
- システムが電話属性を設定します
- Canvas内で設定されたロジックに基づいて、ユーザーは対応するサブスクリプショングループに購読されます<br><br>
2. **オプトインCanvasが設定されていない場合:**
- Brazeは匿名プロファイルを作成します
- 以下の詳細でプロファイルにユーザーエイリアスを割り当てます:
  - ユーザーが提供した電話番号を値とする`alias_name`
  - `phone`を値とする`alias_label`
- システムが電話属性を設定します
- ユーザーのサブスクリプションステータスは、すべてのWhatsAppサブスクリプショングループに対してデフォルトで`unsubscribed`になります<br><br>