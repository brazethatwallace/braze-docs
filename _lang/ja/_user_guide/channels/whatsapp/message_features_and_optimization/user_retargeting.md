---
nav_title: ユーザーリターゲティング
article_title: ユーザーリターゲティング
page_order: 5
description: "このリファレンス記事では、ユーザーのWhatsAppインタラクションによってメッセージをリターゲティングする方法について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# ユーザーリターゲティング {#user-retargeting}

> ユーザーのサブスクリプション状態の変更に加えて、Brazeはユーザープロファイルとのインタラクションも記録し、メッセージのフィルタリングやトリガーに活用します。<br><br>これらのフィルターとトリガーにより、WhatsAppメッセージを受信したユーザーや、特定のWhatsApp キャンペーンまたはキャンバスステップからWhatsAppメッセージを受信したユーザーをフィルタリングできます。

## リターゲティングオプション {#retargeting-options}

{% alert note %}
ユーザーリターゲティングでオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりすることや、CCPAの「販売または共有の拒否」権利などのプライバシー法に準拠することが必要になる場合があります。マーケターは、キャンバスやキャンペーンのエントリ条件内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。
{% endalert %}

### WhatsAppでユーザーをフィルタリングする {#filter-users-by-whatsapp}

ユーザーは、最後にWhatsAppを受信した日時や、特定のWhatsApp キャンペーンからWhatsAppを受信したかどうかでフィルタリングできます。フィルターは、キャンペーンビルダーのターゲットユーザーステップで設定できます。

#### 最後にWhatsAppを受信した日時でフィルタリング {#filter-by-last-received-whatsapp}

![2025年4月22日にWhatsAppメッセージを最後に受信したことでフィルタリング。]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

#### WhatsApp キャンペーンからの受信メッセージでフィルタリング {#filter-by-received-messages-from-whatsapp-campaign}

特定のWhatsApp キャンペーンからメッセージを受信したユーザーをフィルタリングします。このフィルターでは、WhatsApp キャンペーンからメッセージを受信していないユーザーを除外するオプションもあります。

{% alert note %}
WhatsAppメッセージが配信、開封、またはクリックされると、Brazeはインタラクションを記録したプロファイルと同じ電話番号を共有するすべてのプロファイルのデータを更新します。そのため、メッセージを受信、開封、またはクリックした人と電話番号を共有しているユーザーは、直接送信されていなくても「受信済み」フィルターに一致する場合があります。
{% endalert %}

![WhatsApp キャンペーンの受信でフィルタリング。]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### エンゲージメントでフィルタリング {#filter-by-engagement}

WhatsApp キャンペーンまたはキャンバスステップを既読した、またはしていないユーザーをリターゲティングします。

#### 特定のWhatsApp キャンペーンを開封/既読したユーザーをリターゲティング {#retarget-users-who-have-openedread-a-specific-whatsapp-campaign}

1. **Clicked/Opened Campaign** フィルターを使用してセグメントを作成します。
2. **read WhatsApp message** を選択します。
3. 目的のキャンペーンを選択します。

![WhatsAppメッセージを既読したことでフィルタリング。]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

#### 特定のキャンバスステップを開封/既読したユーザーをリターゲティング {#retarget-users-who-have-openedread-a-specific-canvas-step}

1. **Clicked/Opened Step** フィルターを使用してセグメントを作成します。
2. **read WhatsApp message** を選択します。
3. 目的のキャンバスとキャンバスステップを選択します。

![WhatsAppステップの既読でフィルタリング。]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

#### キャンペーンまたはキャンバスアトリビューションでフィルタリング {#filter-by-campaign-or-canvas-attribution}

特定のWhatsApp キャンペーンまたはキャンバスコンポーネント、タグに対して開封/既読したユーザーをフィルタリングします。

![特定のWhatsAppメッセージの開封でフィルタリング。]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}