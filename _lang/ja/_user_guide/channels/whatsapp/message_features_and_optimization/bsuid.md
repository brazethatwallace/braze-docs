---
nav_title: ユーザー名とBSUID
article_title: WhatsAppユーザー名とビジネススコープユーザーID
page_order: 7
description: "WhatsAppユーザー名とビジネススコープユーザーID（BSUID）が、Brazeにおけるユーザー識別、メッセージング、データ処理にどのように影響するかを説明します。"
page_type: reference
alias: "/whatsapp_usernames/"
channel:
  - WhatsApp
hidden: true
noindex: true
---

# WhatsAppユーザー名とビジネススコープユーザーID {#whatsapp-usernames-and-business-scoped-user-ids}

> 2026年6月、WhatsAppはユーザー名の導入を予定しています。これは、ビジネスとのメッセージングにおいてユーザーの電話番号を非表示にするオプションのプライバシー機能です。Brazeはこの変更に完全に対応する準備ができており、ほとんどのお客様にとって、キャンペーンやキャンバスに変更を加える必要はありません。

{% alert important %}
WhatsAppユーザー名とビジネススコープユーザーID（BSUID）は2026年6月にリリースされる予定であり、Brazeの更新もこのリリースに合わせて行われます。この記事に記載されているBrazeの更新は**まだリリースされていません**。
{% endalert %}

WhatsAppユーザーがユーザー名を採用すると、メッセージを送信するビジネスに電話番号が自動的に共有されなくなります。代わりに、WhatsAppはビジネスにビジネススコープユーザーID（BSUID）を提供します。これは、各ビジネスポートフォリオとユーザーのペアに固有のユニークな識別子です。

BrazeはBSUIDを自動的に処理します。ユーザー名を採用したユーザーは、引き続きBrazeワークスペースに表示され、メッセージを受信し、キャンバスをトリガーし、イベントを生成します。一部のお客様は[変更に備える](#how-to-prepare-for-the-change)必要がある場合があります。

## ビジネススコープユーザーID（BSUID） {#business-scoped-user-id-bsuid}

BSUIDは、特定のビジネスポートフォリオ内でユーザーを表すためにWhatsAppが割り当てる、一意で永続的な識別子です。電話番号を非公開にしたいユーザーのための代替電話番号と考えてください。

BSUIDには3つの主要な特性があります。

| 特性 | 説明 |
| ----- | ----- |
| 一意性 | ビジネスポートフォリオ内で同じBSUIDを共有するユーザーはいません。 |
| ビジネススコープ | 同じユーザーでも、メッセージを送信するビジネスごとに異なるBSUIDが割り当てられます。BSUIDは異なるビジネスポートフォリオ間で共有したり比較したりすることはできません。 |
| webhookで利用可能 | BSUIDは、現在ユーザーの電話番号を含んでいるすべてのwebhookペイロードに含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ビジネススコープユーザーID（BSUID）" }

## WhatsAppユーザータイプの変更 {#changes-to-whatsapp-user-types}

WhatsAppユーザーネームの開始後、WhatsAppユーザーには2つのタイプがあります。

| ユーザータイプ | WhatsApp識別方法 | Brazeが受け取る情報 |
| ----- | ----- | ----- |
| ユーザーネームを持たないユーザー | 電話番号（変更なし） | 電話番号（変更なし） |
| ユーザーネームを持つユーザー | ユーザーネーム（表示用）、BSUID（バックエンド） | BSUID、ビジネスとの既存の会話があるユーザーの電話番号 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="WhatsAppユーザータイプの変更" }

主な違いは、ユーザーネームを採用したユーザーは、以前にそのユーザーと会話したことがある場合、またはそのユーザーがWhatsApp連絡先ブックに表示されている場合にのみ、電話番号をビジネスと共有するという点です。

## BrazeにおけるBSUIDの処理 {#how-braze-will-handle-bsuids}

Brazeは、BSUIDをユーザープロファイル上の`whats_app_bsuid`というラベルの[ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)として保存します。これにより、BSUIDのみのユーザーも完全なBrazeユーザープロファイルを持ち、キャンバスへのエントリー、メッセージの受信、イベントの生成、APIを通じた更新が可能になります。

### メッセージの送信 {#send-messages}

BrazeがWhatsAppメッセージを送信する際、電話番号が利用可能であればそれを使用します。ユーザーがBSUIDのみを持っている場合（ユーザーネームの採用後に初めてメッセージを送信したユーザーなど）、Brazeは代わりにBSUIDを使用して送信します。メッセージテンプレート、キャンペーン、またはキャンバスステップの変更は不要です。

### 受信メッセージとキャンバストリガー {#inbound-messages-and-canvas-triggers}

ユーザーネームを持つユーザーからWhatsAppの受信メッセージが届いた場合、Brazeは以下の処理を行います：

1. BSUIDまたは電話番号（Webhookで利用可能な方）でユーザーを検索します。
2. 一致するユーザーが見つからない場合、BSUIDをユーザーエイリアスとして保存した新しい匿名ユーザープロファイルを作成します。
3. 受信WhatsAppメッセージで開始するように設定されたキャンバスまたはキャンペーンをトリガーします。

### ユーザープロファイル {#user-profile}

ユーザーのBSUIDは、BrazeユーザープロファイルのWhatsAppセクションで確認できます。

![ビジネススコープユーザーIDが表示されたWhatsAppセクションを含むユーザープロファイル。]({% image_buster /assets/img/whatsapp/bsuid_profile.png %}){: style="max-width:60%;"}

### 購読グループ {#subscription-groups}

購読グループの管理は、BSUIDユーザーに対しても、ユーザーエイリアスで識別される他のユーザーと同じように機能します。BSUIDユーザーの購読ステータスは、以下の方法で更新できます：

- `user_alias`を使用した[users/trackエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [ユーザー更新]({{site.baseurl}}/user_update)キャンバスステップ（自動的に動作します）
- CSVアップロード

{% alert note %}
[subscription/status/setエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)は[`user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object)をサポートしません。BSUIDのみのユーザーの購読ステータスを更新するには、[users/trackエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用してください。
{% endalert %}

### Currentsとイベントデータ {#currents-and-event-data}

すべてのWhatsApp Currentsイベント（送信、配信、既読、失敗、受信、中止、再試行）にはBSUIDフィールドが含まれます。電話番号とBSUIDの両方を持つユーザーの場合、両方のフィールドが含まれます。BSUIDのみを持つユーザーの場合、BSUIDフィールドのみが含まれます（電話番号フィールドは空になります）。

## 変更に備える方法 {#how-to-prepare-for-the-change}

ほとんどの顧客は、特別な対応は必要ありません。Brazeは自動的にBSUIDルーティング、ユーザー作成、イベントトラッキングを処理します。ただし、[WhatsApp連絡先ブックの有効化](#enable-whatsapp-contact-book)と、複数のWhatsApp Businessアカウント（WABA）を使用している場合は[ビジネスポートフォリオのリンク](#link-business-portfolios-if-you-use-multiple-wabas)をお勧めします。

### WhatsApp連絡先ブックを有効にする {#enable-whatsapp-contact-book}

連絡先ブックは、すでに会話したユーザーの電話番号を記録するMetaの機能です。ユーザーがユーザー名を採用した場合でも、連絡先ブックに表示されていれば、そのユーザーの電話番号はビジネスに引き続き表示されます。これにより、Brazeはユーザーがユーザー名を有効にした後でも、電話番号でユーザーを識別し続けることができます。

連絡先ブックを有効にするには：

1. **Meta Business Suite** > **ビジネス設定** > **ビジネス情報**に移動します。
2. 連絡先ブック機能が有効になっていることを確認します。

{% alert tip %}
連絡先ブック機能はデフォルトで有効になっていますが、Meta Businessの設定で確認することをお勧めします。連絡先ブックが無効になっている場合、ユーザー名を採用したユーザーは、以前メッセージを送信したことがある場合でも、新しいBSUIDのみのユーザーとして表示されます。
{% endalert %}

### 複数のWABAを使用している場合はビジネスポートフォリオをリンクする {#link-business-portfolios-if-you-use-multiple-wabas}

BSUIDは単一のビジネスポートフォリオにスコープされます。組織が同じBrazeワークスペース内で複数のビジネスポートフォリオからWABAを管理している場合、同じユーザーがポートフォリオごとに異なるBSUIDを持つことになります。これにより、Brazeのユーザープロファイルが重複する可能性があります。

これを防ぐには、Metaの担当者に連絡して、ビジネスがポートフォリオのリンクに適格かどうかを確認してください。詳細については、[ビジネスポートフォリオと親BSUIDのリンク](#link-business-portfolios-and-parent-bsuids)を参照してください。

すべてのWABAが同じビジネスポートフォリオ内にある場合は、特別な対応は必要ありません。

## ビジネスポートフォリオと親BSUIDのリンク {#link-business-portfolios-and-parent-bsuids}

組織が異なるビジネスポートフォリオにまたがる複数のWhatsApp Businessアカウント（WABA）を運用している場合、Metaの担当者に連絡して、それらのポートフォリオをリンクする資格があるかどうかを確認してもらうことができます。資格はMetaが判断し、マネージドビジネスに提供されます。

### リンクされたポートフォリオの動作 {#linked-portfolio-behavior}

ビジネスポートフォリオがリンクされると、WhatsAppはすべてのメッセージwebhookに通常のBSUIDとともに親BSUIDを含めます。親BSUIDはwebhookペイロードの新しい`parent_user_id`プロパティに割り当てられます。

親BSUIDは通常のBSUIDと同じプロパティを持ちますが、リンクされたポートフォリオのセット内のすべてのビジネス電話番号で共有されます。これにより、同じユーザーがメッセージを送信するWABAに関係なく、単一の一貫した識別子を持つことになり、ユーザープロファイルの重複リスクを回避できます。

親BSUIDには、国コードと英数字の識別子の間に`ENT`が含まれます。例：

```
US.ENT.11815799212886844830
```

通常のBSUIDには`ENT`は含まれません。

### Brazeが親BSUIDを使用する方法 {#how-braze-uses-parent-bsuids}

webhookに通常のBSUIDと親BSUIDの両方が含まれている場合、Brazeは親BSUIDをプライマリ識別子として使用します。これにより、リンクされたポートフォリオ内の複数のWABAにメッセージを送信するユーザーが、同じBrazeユーザープロファイルに一貫してマッチングされます。

親BSUIDが存在しない場合（例えば、ポートフォリオがリンクされていない場合やユーザーがリンクされていないWABAにメッセージを送信している場合）、Brazeは通常のBSUIDを使用します。通常のBSUIDは、すべてのケースで引き続き正常に機能します。

{% alert note %}
ビジネスポートフォリオのリンクプロセスはMetaが管理しています。開始するには、Metaの担当者にお問い合わせください。ポートフォリオがリンクされている場合でも、通常のBSUIDを使用してユーザーにメッセージを送信することは引き続き可能です。親BSUIDは追加的なものであり、置き換えではありません。
{% endalert %}

| シナリオ | Brazeが使用する識別子 |
| ----- | ----- |
| 単一のビジネスポートフォリオ | 通常のBSUID |
| 複数のリンクされたポートフォリオ | 親BSUID（優先）。親BSUIDが存在しない場合は通常のBSUIDを使用 |
| 複数のリンクされていないポートフォリオ | 通常のBSUID（ポートフォリオごとにユーザープロファイルが重複する可能性あり） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeが親BSUIDを使用する方法" }

## よくある質問 {#frequently-asked-questions}

### WhatsAppユーザーネームが導入されると、既存のキャンペーンやキャンバスは動作しなくなりますか？ {#will-my-existing-campaigns-and-canvases-break-when-whatsapp-usernames-launch}

いいえ。既存のキャンペーンやキャンバスは引き続き動作します。ユーザーネームを採用しないユーザーにはまったく影響がありません。ユーザーネームを採用し、かつ貴社との既存の会話履歴があるユーザーについては、Brazeは引き続き電話番号をプライマリ識別子として使用します。

### ユーザーネームを採用したユーザーが、すでに自社のビジネスにメッセージを送っていた場合はどうなりますか？ {#what-happens-to-a-user-who-adopts-a-username-but-has-already-messaged-my-business}

WhatsAppコンタクトブックが有効で、過去30日以内にそのユーザーとの会話（またはメッセージ送信）があった場合、webhookペイロードにはBSUIDと並んで電話番号が引き続き表示されます。Brazeはそのユーザーを既存のユーザープロファイルに照合します。重複プロファイルは作成されません。

### ユーザーネームを採用したユーザーが、自社のビジネスとの以前の会話がない場合はどうなりますか？ {#what-if-a-user-adopts-a-username-and-has-no-prior-conversation-with-my-business}

BrazeはインバウンドwebhookでユーザーのBSUIDを受信し、既存のユーザープロファイルに照合するか（以前にBSUIDを保存していた場合）、またはBSUIDをユーザーエイリアスとして保存した新しい匿名ユーザープロファイルを作成します。その後、そのユーザーはキャンバスに入ったり、アウトバウンドメッセージを受信したり、Brazeの標準的なID解決ツールを使用して他のプロファイルと識別またはマージしたりできます。

### BSUIDユーザーをセグメントでターゲットにできますか？ {#can-i-target-bsuid-users-in-segments}

BSUIDユーザーは完全なBrazeユーザープロファイルであるため、標準のオーディエンスフィルター（「WhatsAppメッセージを受信した」や購読グループのメンバーシップなど）を通じてターゲットにできます。ただし、BSUID値に基づくセグメンテーション（「BSUIDが存在する」や「BSUIDがXに等しい」など）はサポートされていません。

### BSUIDユーザーのWhatsApp料金はどのように機能しますか？ {#how-does-whatsapp-pricing-work-for-bsuid-users}

WhatsAppの会話料金は、ユーザーの国によって決まります。電話番号で識別されるユーザーの場合、Metaは電話番号の国コードから国を判定します。BSUIDで識別されるユーザーの場合、国はBSUID自体に直接エンコードされています。たとえば、`US`で始まるBSUIDは米国のユーザーを表します。

つまり、ユーザーが電話番号またはBSUIDのどちらで識別されても、料金体系は一貫しています。会話料金の計算に使用される国は、Metaが提供する識別子によって決まり、Brazeはこれを変更せずにそのまま渡します。特別な対応は不要ですが、BSUIDのみのユーザーにメッセージを送信する場合、Metaの国ベースの料金は電話番号ではなくユーザーのBSUIDにエンコードされた国に基づいていることにご注意ください。

### API呼び出しでBSUIDユーザーをどのように参照しますか？ {#how-do-i-reference-a-bsuid-user-in-api-calls}

`user_alias`パラメーターを使用し、`alias_label: "whats_app_bsuid"`と`alias_name`にユーザーのBSUID値を設定します。例：

```json
{
  "user_alias": {
    "alias_label": "whats_app_bsuid",
    "alias_name": "DDC91135R"
  }
}
```

これは`users/track`、`users/identify`、CSVアップロード、およびUser Updateキャンバスステップで使用できます。

### Currentsのデータパイプラインは影響を受けますか？ {#will-my-currents-data-pipelines-break}

WhatsAppのCurrentsイベントには、既存の電話番号フィールドとともに`bsuid`フィールドが含まれます。BSUIDのみのユーザーの場合、電話番号フィールドは空になります。下流のパイプラインで電話番号フィールドに対する厳格な要件がある場合は、nullまたは空の値を処理できることを確認してください。

### 異なるビジネスポートフォリオにまたがる複数のWABAを持っている場合、同じユーザーがBrazeで2つの異なるプロファイルとして表示されますか？ {#i-have-multiple-wabas-across-different-business-portfolios-will-the-same-user-appear-as-two-different-profiles-in-braze}

ポートフォリオがリンクされていない場合はその通りです。同じWhatsAppユーザーはビジネスポートフォリオごとに異なるBSUIDを持ち、Brazeはそれぞれに別のプロファイルを作成します。

これを解決するには、Metaの担当者に連絡してポートフォリオリンクの適格性を確認してください。リンクされると、Metaはすべてのポートフォリオで共有される親BSUIDを提供し、BrazeはこれをすべてのWABA間でユーザーを一貫して識別するために使用します。詳細については、[ビジネスポートフォリオのリンクと親BSUID](#link-business-portfolios-and-parent-bsuids)を参照してください。

### コンタクトブックを無効にできますか？ {#can-i-disable-the-contact-book}

コンタクトブックは有効のままにしておくことを強くお勧めします。コンタクトブックを無効にすると、ユーザーの過去の電話番号レコードがすべて失われます。ユーザーネームを採用したユーザーは、以前にメッセージを送ったことがある場合でも、新しいBSUIDのみのユーザーとして表示されます。

## その他のリソース {#additional-resources}

* [WhatsApp設定]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)
* [ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)
* [WhatsApp購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
* [WhatsApp Currentsイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#whatsapp-abort-events)
* [Meta: Business-scoped user IDs](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids)