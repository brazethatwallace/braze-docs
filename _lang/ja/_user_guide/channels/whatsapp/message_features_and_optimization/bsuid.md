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

BSUIDは、WhatsAppが特定のビジネスポートフォリオ内のユーザーを表すために割り当てる、ユニークで永続的な識別子です。電話番号を非公開にすることを選択したユーザーのための代替電話番号と考えてください。

BSUIDには3つの主要な特性があります。

| 特性 | 説明 |
| ----- | ----- |
| ユニーク | ビジネスポートフォリオ内で同じBSUIDを共有するユーザーはいません。 |
| ビジネススコープ | 同じユーザーでも、メッセージを送信するビジネスごとに異なるBSUIDを持ちます。BSUIDは異なるビジネスポートフォリオ間で共有または比較することはできません。 |
| webhookで利用可能 | BSUIDは、現在ユーザーの電話番号を含むすべてのwebhookペイロードに含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ビジネススコープユーザーID（BSUID）" }

## WhatsAppユーザータイプの変更 {#changes-to-whatsapp-user-types}

WhatsAppユーザー名のリリース後、WhatsAppユーザーには2つのタイプが存在します。

| ユーザータイプ | WhatsApp識別 | Brazeが受信する情報 |
| ----- | ----- | ----- |
| ユーザー名なしのユーザー | 電話番号（変更なし） | 電話番号（変更なし） |
| ユーザー名ありのユーザー | ユーザー名（表示）、BSUID（バックエンド） | BSUID、ビジネスとの既存の会話があるユーザーの電話番号 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="WhatsAppユーザータイプの変更" }

主な違いは、ユーザー名を採用したユーザーは、以前に会話したことがある場合、またはWhatsApp連絡先帳に表示されている場合にのみ、ビジネスに電話番号を共有するという点です。

## BrazeによるBSUIDの処理方法 {#how-braze-will-handle-bsuids}

Brazeは、BSUIDをユーザープロファイル上の`whats_app_bsuid`というラベルの[ユーザーエイリアス]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases)として保存します。これにより、BSUIDのみのユーザーも完全なBrazeユーザープロファイルを持ち、キャンバスに入場し、メッセージを受信し、イベントを生成し、APIを通じて更新できます。

### メッセージの送信 {#send-messages}

BrazeがWhatsAppメッセージを送信する際、電話番号が利用可能であればそれを使用します。ユーザーがBSUIDのみを持っている場合（ユーザー名を採用した後に初めてメッセージを送信したユーザーなど）、BrazeはBSUIDを使用して送信します。メッセージテンプレート、キャンペーン、またはキャンバスステップに変更を加える必要はありません。

### 受信メッセージとキャンバストリガー {#inbound-messages-and-canvas-triggers}

ユーザー名を持つユーザーがWhatsAppの受信メッセージを送信すると、Brazeは以下を行います。

1. BSUIDまたは電話番号（webhookで利用可能な方）でユーザーを検索します。
2. 一致するユーザーが見つからない場合、BSUIDをユーザーエイリアスとして保存した新しい匿名ユーザープロファイルを作成します。
3. 受信WhatsAppメッセージで開始するように設定されたキャンバスまたはキャンペーンをトリガーします。

### ユーザープロファイル {#user-profile}

ユーザーのBSUIDは、BrazeユーザープロファイルのWhatsAppセクションで確認できます。

![ビジネススコープユーザーIDを含むWhatsAppセクションがあるユーザープロファイル。]({% image_buster /assets/img/whatsapp/bsuid_profile.png %}){: style="max-width:60%;"}

### サブスクリプショングループ {#subscription-groups}

サブスクリプショングループの管理は、ユーザーエイリアスで識別されるユーザーと同様に、BSUIDユーザーに対しても同じように機能します。BSUIDユーザーのサブスクリプションステータスは、以下の方法で更新できます。

- `user_alias`を使用した[users/trackエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [ユーザーの更新]({{site.baseurl}}/user_update)キャンバスステップ（自動的に機能します）
- CSVアップロード

{% alert note %}
[subscription/status/setエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status)は[`user_alias`]({{site.baseurl}}/api/objects_filters/user_alias_object)をサポートしません。BSUIDのみのユーザーのサブスクリプション状態を更新するには、[users/trackエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用してください。
{% endalert %}

### Currentsとイベントデータ {#currents-and-event-data}

すべてのWhatsApp Currentsイベント（送信、配信、既読、失敗、受信、中止、リトライ）にはBSUIDフィールドが含まれます。電話番号とBSUIDの両方を持つユーザーの場合、両方のフィールドが含まれます。BSUIDのみを持つユーザーの場合、BSUIDフィールドのみが含まれます（電話番号フィールドは空です）。

## 変更に備える方法 {#how-to-prepare-for-the-change}

ほとんどのお客様にとって、アクションは不要です。BrazeはBSUIDルーティング、ユーザー作成、イベントトラッキングを自動的に処理します。ただし、[WhatsApp連絡先帳の有効化](#enable-whatsapp-contact-book)と、複数のWhatsApp Business アカウント（WABA）を使用している場合は[ビジネスポートフォリオのリンク](#link-business-portfolios-if-you-use-multiple-wabas)をお勧めします。

### WhatsApp連絡先帳の有効化 {#enable-whatsapp-contact-book}

連絡先帳は、すでに会話したユーザーの電話番号を記録するMetaの機能です。ユーザーがユーザー名を採用した場合でも、連絡先帳に表示されていれば、そのユーザーの電話番号はビジネスに引き続き表示されます。これにより、Brazeはユーザー名を有効にした後でも、電話番号でユーザーを識別し続けることができます。

連絡先帳を有効にするには：

1. **Meta Business Suite** > **ビジネス設定** > **ビジネス情報**に移動します。
2. 連絡先帳機能が有効になっていることを確認します。

{% alert tip %}
連絡先帳機能はデフォルトで有効になっていますが、Metaのビジネス設定で確認することをお勧めします。連絡先帳が無効になっている場合、ユーザー名を採用したユーザーは、以前にメッセージを送信したことがあっても、新しいBSUIDのみのユーザーとして表示されます。
{% endalert %}

### 複数のWABAを使用している場合はビジネスポートフォリオをリンクする {#link-business-portfolios-if-you-use-multiple-wabas}

BSUIDは単一のビジネスポートフォリオにスコープされます。組織が同じBrazeワークスペース内で複数のビジネスポートフォリオからWABAを管理している場合、同じユーザーがポートフォリオごとに異なるBSUIDを持つことになります。これにより、Brazeユーザープロファイルが重複する可能性があります。

これを防ぐには、Metaの担当者に連絡して、ビジネスがポートフォリオのリンクの対象かどうかを確認してください。詳細については、[ビジネスポートフォリオのリンクと親BSUID](#link-business-portfolios-and-parent-bsuids)を参照してください。

すべてのWABAが同じビジネスポートフォリオ内にある場合、アクションは不要です。

## ビジネスポートフォリオのリンクと親BSUID {#link-business-portfolios-and-parent-bsuids}

組織が異なるビジネスポートフォリオにまたがる複数のWhatsApp Business アカウント（WABA）を運用している場合、Metaの担当者に連絡して、それらのポートフォリオをリンクする資格があるかどうかを確認できます。資格はMetaによって決定され、マネージドビジネスに提供されます。

### リンクされたポートフォリオの動作 {#linked-portfolio-behavior}

ビジネスポートフォリオがリンクされると、WhatsAppはすべてのメッセージwebhookに通常のBSUIDとともに親BSUIDを含めます。親BSUIDは、webhookペイロードの新しい`parent_user_id`プロパティに割り当てられます。

親BSUIDは通常のBSUIDと同じプロパティを持ちますが、リンクされたポートフォリオセット内のすべてのビジネス電話番号間で共有されます。これにより、同じユーザーがメッセージを送信するWABAに関係なく、単一の一貫した識別子を持つことになり、ユーザープロファイルの重複リスクを回避できます。

親BSUIDには、国コードと英数字識別子の間に`ENT`が含まれます。例：

```
US.ENT.11815799212886844830
```

通常のBSUIDには`ENT`は含まれません。

### Brazeによる親BSUIDの使用方法 {#how-braze-uses-parent-bsuids}

webhookに通常のBSUIDと親BSUIDの両方が含まれている場合、Brazeは親BSUIDをプライマリ識別子として使用します。これにより、リンクされたポートフォリオ内の複数のWABAにメッセージを送信するユーザーが、同じBrazeユーザープロファイルに一貫してマッチングされます。

親BSUIDが存在しない場合（例えば、ポートフォリオがリンクされていない場合や、ユーザーがリンクされていないWABAにメッセージを送信している場合）、Brazeは通常のBSUIDを使用します。通常のBSUIDは、すべてのケースで引き続き正常に機能します。

{% alert note %}
ビジネスポートフォリオのリンクプロセスはMetaが管理しています。開始するには、Metaの担当者に連絡してください。ポートフォリオがリンクされている場合でも、通常のBSUIDを使用してユーザーにメッセージを送信できます。親BSUIDは追加的なものであり、置き換えではありません。
{% endalert %}

| シナリオ | Brazeが使用する識別子 |
| ----- | ----- |
| 単一のビジネスポートフォリオ | 通常のBSUID |
| 複数のリンクされたポートフォリオ | 親BSUID（優先）。親BSUIDが存在しない場合は、通常のBSUIDを使用 |
| 複数のリンクされていないポートフォリオ | 通常のBSUID（ポートフォリオごとにユーザープロファイルが重複する可能性あり） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Brazeによる親BSUIDの使用方法" }

## よくある質問 {#frequently-asked-questions}

### WhatsAppユーザー名のリリース時に、既存のキャンペーンやキャンバスは動作しなくなりますか？ {#will-my-existing-campaigns-and-canvases-break-when-whatsapp-usernames-launch}

いいえ。既存のキャンペーンやキャンバスは引き続き動作します。ユーザー名を採用しないユーザーには一切影響がありません。ユーザー名を採用し、ビジネスとの既存の会話履歴があるユーザーについては、Brazeは引き続き電話番号をプライマリ識別子として使用します。

### ユーザー名を採用したが、すでにビジネスにメッセージを送信したことがあるユーザーはどうなりますか？ {#what-happens-to-a-user-who-adopts-a-username-but-has-already-messaged-my-business}

WhatsApp連絡先帳が有効で、過去30日以内にそのユーザーと会話した（またはメッセージを送信した）場合、電話番号はBSUIDとともにwebhookペイロードに引き続き表示されます。Brazeはそのユーザーを既存のユーザープロファイルにマッチングします。重複プロファイルは作成されません。

### ユーザー名を採用したが、ビジネスとの以前の会話がないユーザーはどうなりますか？ {#what-if-a-user-adopts-a-username-and-has-no-prior-conversation-with-my-business}

Brazeは受信webhookでユーザーのBSUIDを受信し、既存のユーザープロファイルにマッチング（以前にBSUIDを保存していた場合）するか、BSUIDをユーザーエイリアスとして保存した新しい匿名ユーザープロファイルを作成します。そのユーザーはキャンバスに入場し、アウトバウンドメッセージを受信し、Brazeの標準的なID解決ツールを使用して他のプロファイルと識別またはマージできます。

### BSUIDユーザーをセグメントでターゲットにできますか？ {#can-i-target-bsuid-users-in-segments}

BSUIDユーザーは完全なBrazeユーザープロファイルであるため、標準的なオーディエンスフィルター（「WhatsAppメッセージを受信した」やサブスクリプショングループのメンバーシップなど）を通じてターゲットにできます。ただし、BSUID値に基づく特定のセグメンテーション（「BSUIDが存在する」や「BSUIDがXに等しい」など）はサポートされていません。

### BSUIDユーザーのWhatsApp料金はどのように機能しますか？ {#how-does-whatsapp-pricing-work-for-bsuid-users}

WhatsAppの会話料金はユーザーの国によって決定されます。電話番号で識別されるユーザーの場合、Metaは電話番号の国コードから国を導出します。BSUIDで識別されるユーザーの場合、国はBSUID自体に直接エンコードされています。例えば、`US`で始まるBSUIDは米国のユーザーを表します。

これは、ユーザーが電話番号またはBSUIDのどちらで識別されても、料金の動作が一貫していることを意味します。会話レートの計算に使用される国はMetaが提供する識別子によって決定され、Brazeはこれを変更せずにそのまま渡します。特別な対応は不要ですが、BSUIDのみのユーザーにメッセージを送信する場合、Metaの国ベースの料金は電話番号ではなく、ユーザーのBSUIDにエンコードされた国に基づくことに注意してください。

### API呼び出しでBSUIDユーザーを参照するにはどうすればよいですか？ {#how-do-i-reference-a-bsuid-user-in-api-calls}

`user_alias`パラメーターを使用し、`alias_label: "whats_app_bsuid"`と`alias_name`にユーザーのBSUID値を設定します。例：

```json
{
  "user_alias": {
    "alias_label": "whats_app_bsuid",
    "alias_name": "DDC91135R"
  }
}
```

これは`users/track`、`users/identify`、CSVアップロード、およびユーザーの更新キャンバスステップで機能します。

### Currentsデータパイプラインは動作しなくなりますか？ {#will-my-currents-data-pipelines-break}

WhatsAppのCurrentsイベントには、既存の電話番号フィールドとともに`bsuid`フィールドが含まれます。BSUIDのみを持つユーザーの場合、電話番号フィールドは空です。ダウンストリームパイプラインが電話番号フィールドに厳密な要件を持っている場合、nullまたは空の値を処理できることを確認してください。

### 異なるビジネスポートフォリオにまたがる複数のWABAを持っています。同じユーザーがBrazeで2つの異なるプロファイルとして表示されますか？ {#i-have-multiple-wabas-across-different-business-portfolios-will-the-same-user-appear-as-two-different-profiles-in-braze}

リンクされたポートフォリオがない場合、はい。同じWhatsAppユーザーはビジネスポートフォリオごとに異なるBSUIDを持ち、Brazeはそれぞれに対して別々のプロファイルを作成します。

これを解決するには、Metaの担当者に連絡してポートフォリオリンクの資格を確認してください。リンクされると、Metaはすべてのポートフォリオ間で共有される親BSUIDを提供し、Brazeはこれを使用してWABA間でユーザーを一貫して識別します。詳細については、[ビジネスポートフォリオのリンクと親BSUID](#link-business-portfolios-and-parent-bsuids)を参照してください。

### 連絡先帳を無効にできますか？ {#can-i-disable-the-contact-book}

連絡先帳を有効のままにしておくことを強くお勧めします。連絡先帳が無効になると、ユーザーの過去の電話番号記録がすべて失われます。ユーザー名を採用したユーザーは、以前にメッセージを送信したことがあっても、新しいBSUIDのみのユーザーとして表示されます。

## その他のリソース {#additional-resources}

* [WhatsAppセットアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)
* [ユーザーエイリアス]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases)
* [WhatsAppサブスクリプショングループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)
* [WhatsApp Currentsイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events#whatsapp)
* [Meta: ビジネススコープユーザーID](https://developers.facebook.com/documentation/business-messaging/whatsapp/business-scoped-user-ids)