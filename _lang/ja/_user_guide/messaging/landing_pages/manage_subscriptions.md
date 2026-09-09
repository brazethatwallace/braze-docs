---
nav_title: 購読管理ブロック
article_title: 購読管理ブロック
description: "この記事では、Brazeランディングページに購読管理フォームブロックを追加・設定して、消費者がメール、SMS、またはWhatsApp購読グループにオプトインおよび管理できるようにする方法について説明します。"
page_order: 5
---

# 購読管理ブロック {#manage-subscriptions-block}

> ランディングページに**購読管理**ブロックを追加して、ユーザーがメール、SMS、またはWhatsApp購読グループを表示、オプトイン、更新できるようにします。

**購読管理**ブロックは、2つの主要なユースケースをサポートしています。

- **[既存の購読を管理する](#update-existing-subscriptions):** ランディングページの[Liquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)をメール、SMS、WhatsApp、またはその他のチャネルメッセージで共有します。識別済みのユーザーがページを開くと、ブロックは各購読グループのチェックボックスに現在の購読状態を自動的に事前入力するため、ユーザーは設定を確認して更新できます。
- **[新しいオプトインを取得する](#capture-new-subscribers):** リードジェネレーションランディングページに**メールキャプチャ**または**電話番号キャプチャ**ブロックと一緒にこのブロックを追加して、新しい訪問者がフォームを送信する際に参加する購読グループを選択できるようにします。

{% alert important %}
各**購読管理**ブロックは1つのチャネル用です：[メール]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups)、[SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states)、または[WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states)。複数のチャネルを収集するには、チャネルごとにブロックを追加してください。RCSの同意については、代わりに[電話番号キャプチャ]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)ブロックを使用してください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| メール、SMS、またはWhatsApp購読グループ | ブロックに追加するチャネルに対応する、少なくとも1つの[メール購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups)、[SMS購読グループ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states)、または[WhatsApp購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states)が必要です。メールグループはダッシュボードまたは[購読グループエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups)から作成できます。SMSグループは[SMS設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#enable-subscription-groups)時にプロビジョニングされます。WhatsAppグループはワークスペースに[WhatsAppを統合]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)する際に作成されます。 |
| ランディングページの権限 | ランディングページの作成および編集に必要な同じ[権限]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ1: 購読管理ブロックを追加する {#step-1-add-the-manage-subscriptions-block}

ドラッグ＆ドロップランディングページエディターで、**ビルド**セクションに移動し、**フォームブロック**を選択します。**購読管理**をページ上の行にドラッグします。列の幅に自動的に調整されます。

ブロックは、購読グループを追加するまで空の状態です。複数のチャネルのグループを表示するには、チャネルごとに**購読管理**ブロックを追加します。

## ステップ2: チャネルと購読グループを選択する {#step-2-select-the-channel-and-subscription-groups}

**購読を管理**ブロックを選択した状態で、右側の**ブロックのプロパティ**パネルで**+ 購読グループを追加**を選択します。**購読グループを追加**モーダルが開きます。

1. **チャネルを選択**で、**メール**、**SMS**、または**WhatsApp**を選択します。各ブロックは1つのチャネルをサポートしています。あるチャネルにすでにページ上の**購読を管理**ブロックが設定されている場合、そのチャネルカードは無効化され、**追加済み**と表示されます。
2. **購読グループを選択**で、含めるグループを選択します。リストの見出しはチャネルに対応しています（**メール購読グループ**、**SMS購読グループ**、または**WhatsApp購読グループ**）。
3. **選択したものを追加**を選択します。

各購読グループは、ランディングページ上で個別に選択可能なチェックボックスとして表示されます。

**SMS**を選択し、ワークスペースにまだSMS購読グループがない場合、モーダルには**SMSの購読グループはまだありません**と表示されます。[SMS購読グループの設定]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#sms-subscription-states)を完了してから、ブロックに戻ってください。

**WhatsApp**を選択し、ワークスペースにまだWhatsApp購読グループがない場合、モーダルには**WhatsAppの購読グループはまだありません**と表示されます。[WhatsApp購読グループの設定]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups#whatsapp-subscription-states)を完了してから、ブロックに戻ってください。

{% alert note %}
**購読を管理**ブロックには、明示的に追加したグループのみが表示されます。購読グループをブロックに追加しても、訪問者が自動的にそのグループに購読登録されるわけではありません。訪問者がそのグループのチェックボックスを選択し、フォームを送信する必要があります。
{% endalert %}

## ステップ3：ブロック設定を構成する {#step-3-configure-the-block-settings}

**ブロックプロパティ**パネルを使用して、ブロックの動作と表示を調整します。

### 購読グループ {#subscription-groups}

- **グループの並べ替え：**購読グループのハンドルをドラッグして、ブロック内に表示される順序を変更します。
- **グループの追加または削除：****+ 購読グループを追加**を選択してグループを追加するか、グループの横にある削除アイコンを選択してブロックからグループを削除します。

### 説明文を含める {#include-descriptions}

**説明文を含める**をオンにすると、各購読グループの説明文が名前の横に表示され、訪問者がオプトインする内容についてより詳しいコンテキストを確認できます。メールグループは購読管理で説明文を含めることができます。このブロック内のSMSおよびWhatsAppグループでは説明文は表示されません。

### 「すべてを購読する」チェックボックス {#subscribe-to-all-checkbox}

**「すべてを購読する」チェックボックス**設定をオンにすると、ブロックに追加のチェックボックスが表示されます。訪問者がこれを選択すると、ブロック内のすべての購読グループのチェックボックスが選択されます。これは、リストされたすべてのグループに素早くオプトインするのに便利です。

## 既存の購読を更新する {#update-existing-subscriptions}

既存のユーザーがメール、SMS、またはWhatsAppの購読を確認・更新できるようにするには、ランディングページの[Liquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)を使用して、メール、SMS、WhatsApp、キャンバスステップ、またはその他のメッセージでページを共有します。ユーザーがそのリンクからページを開くと、Brazeはユーザーを識別し、**購読の管理**ブロック内の各購読グループのチェックボックスを現在の購読状態に合わせて自動的に事前入力します。これは[メールのユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)と同様の動作です。

ユーザーはチェックボックスを選択またはクリアして購読を更新し、フォームを送信して変更を保存できます。

{% alert note %}
**購読の管理**ブロックでユーザーの現在の購読状態を事前入力する機能はデフォルトで含まれており、[ランディングページProティア]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers)は必要ありません。これは、ランディングページProが必要な他のフォームフィールドの[Liquidベースの事前入力]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields)とは異なります。
{% endalert %}

## 新しい購読者の獲得 {#capture-new-subscribers}

新しい購読者を収集するには、**Manage Subscriptions**ブロックとそのチャネルのキャプチャフィールドを組み合わせます。

- **メール：**[メールキャプチャ]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)ブロックを追加して、訪問者のメールアドレスとメール購読グループの選択を取得します。
- **SMSまたはWhatsApp：**[電話番号キャプチャ]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)ブロックを追加して、訪問者の電話番号とSMSまたはWhatsApp購読グループの選択を取得します。

訪問者が識別されていない場合（たとえば、ランディングページのLiquidタグなしでアクセスした場合）、チェックボックスは未選択の状態で表示されます。フォームを送信すると、選択した購読グループに購読登録されます。

## 知っておくべきこと {#things-to-know}

- **チャネルごとに1つのブロック:** ページ上の各チャネルに1つの**購読の管理**ブロックを追加できます（メール用に1つ、SMS用に1つ、WhatsApp用に1つ）。
- **RCS:** このブロックにはRCS購読グループは表示されません。RCSの同意を収集するには、[電話番号キャプチャ]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)ブロックを使用してください。
- **確認エクスペリエンス:** **購読の管理**を含むフォームブロックがあるランディングページでは、送信後に確認エクスペリエンスが必要です。[確認ページを作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional)し、**送信**ボタンからリンクしてください。
- **エディターブロックリファレンス:** ランディングページのすべてのブロックとそのプロパティの完全なリファレンスについては、[エディターブロック（ランディングページ）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)を参照してください。