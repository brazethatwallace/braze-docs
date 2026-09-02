---
nav_title: Zeotap Symphony
description: "このリファレンス記事では、BrazeとZeotapのパートナーシップについて説明します。Zeotapは、アイデンティティ解決、インサイト、データ強化を提供する次世代顧客データプラットフォームです。"
page_type: partner
search_tag: Partner
page_order: 2
---

# Zeotap Symphony

BrazeとZeotap Symphonyの統合により、リアルタイムのオーケストレーションを作成し、メールやプッシュ通知のキャンペーンを実行できます。

- Zeotapを通じて姓と名を送信し、それに基づいてユーザーはBrazeからパーソナライズされたメールを送信できます。
- Zeotapを通じてカスタムイベントまたは購入イベントをリアルタイムで送信し、それに基づいてユーザーはBraze内でキャンペーントリガーを作成して顧客をターゲットにできます。

{% alert note %}
メールマーケティングキャンペーンを作成するには、生のメールをZeotap Catalogueの`Email Raw`にマッピングしてZeotapに登録します。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| クライアント名 | Brazeアカウントのクライアント名です。Brazeコンソールに移動して確認できます。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| インスタンス | Brazeインスタンスは、Brazeオンボーディングマネージャーから入手するか、[API概要ページ]({{site.baseurl}}/api/basics#endpoints)で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

このセクションでは、Brazeと統合できる2つの方法について説明します。

### 方法1 {#method-1}
この方法では、次の作業を行う必要があります。
1. Webサイトやアプリに Braze SDKを統合します。
2. Symphonyを介してBrazeをZeotapと統合します。

- `User traits`は、**Data To Send**タブの各Brazeフィールドにマッピングする必要があります。`Event`と`Purchase`の属性をマッピングすると、Braze内でイベントが重複します。
- Braze SDKの設定時に構成した`User ID`に`External ID`をマッピングします。

統合が正常に設定されると、Symphonyを通じてBrazeに送信されるカスタム属性に基づいて、メールやプッシュ通知のキャンペーンを作成できます。

### 方法2 {#method-2}
この方法では、Symphonyを介してBrazeとZeotapを統合できます。

- この方法では、アプリ内メッセージ、Content Cards、プッシュ通知などのBraze UI機能はサポートされません。
- Zeotapでは、Zeotap Catalogueで利用可能な`hashed email`を`External ID`にマッピングすることを推奨しています。

統合が正常に設定されると、Symphonyを通じてBrazeに送信されたカスタム属性に基づいてのみ、メールキャンペーンを作成できるようになります。

## Brazeへのデータフローとサポートされる識別子 {#data-flow-to-braze-and-supported-identifiers}

データは、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用してZeotapからBrazeに流れます。データの流れをまとめると以下のようになります。

1. Zeotapはユーザープロファイル属性、カスタム属性、カスタムイベント、購入フィールドを送信します。
2. 関連するすべてのZeotap Catalogueフィールドを、**Data To Send**タブのBrazeフィールドにマッピングします。
3. そのデータはBrazeにアップロードされます。

各属性の詳細は、「[Data To Send](#data-to-send-tab)」セクションで確認できます。

## 送信先の設定 {#destination-setup}

Symphonyでユーザーにフィルターを適用した後、またはユーザーの条件を追加した後は、**Send to Destinations**でBrazeのユーザーをアクティブ化できます。新しいウィンドウが開き、送信先を設定できます。**Available Destinations**リストにある既存の送信先を使用するか、新規の送信先を作成できます。

### 新しい送信先を追加する {#add-new-destination}
新しい送信先を追加するには、次のステップを実行します。
1. **Add New Destination**を選択します。
2. **Braze**を検索します。
3. **Client Name**、**API Key**、および**Instance**を追加し、送信先を保存します。

送信先が作成され、**Available Destinations**で利用できるようになります。

### ワークフローレベルの入力を追加する {#add-workflow-level-inputs}
送信先を作成したら、次にこのセクションで説明するようにワークフローレベルの入力を追加する必要があります。
1. 検索機能を使って、利用可能な送信先のリストから送信先を選択します。
2. **Client Name**、**API Key**、および**Instance**フィールドは、送信先作成時に入力した値に基づいて自動的に入力されます。
3. このワークフローノードに対して作成する**オーディエンス名**を入力します。これは**カスタム属性**としてBrazeに送信されます。
4. **Data To Send**タブでカタログから送信先へのマッピングを完了します。マッピングの実行方法の詳細については、このセクションで確認できます。

### Data To Sendタブ {#data-to-send-tab}
**Data To Send**タブでは、Zeotap CatalogueのフィールドをBrazeに送信できるBrazeフィールドにマッピングできます。マッピングは以下のいずれかの方法で行うことができます。
- **静的マッピング** - Zeotapにより関連するBrazeフィールドに自動的にマッピングされるフィールドがあります（メール、電話番号、名、姓など）。<br>
- **ドロップダウン選択** - Zeotapに取り込まれた関連フィールドを、ドロップダウンメニューに示されているBrazeフィールドにマッピングします。<br>![言語、市区町村、誕生日など、Zeotapに設定されたさまざまなユーザー特性。]({% image_buster /assets/img/zeotap/zeotap7.png %}){: style="max-width:70%;"}<br>
- **カスタムデータ入力** - 関連するZeotapフィールドにマッピングされたカスタムデータを追加し、Brazeに送信します。<br>![Zeotapのユーザー特性として「loyalty_points」を選択。]({% image_buster /assets/img/zeotap/zeotap8.png %}){: style="max-width:70%;"}

## サポートされている属性 {#supported-attributes}
このセクションでは、すべてのBrazeフィールドの詳細を確認できます。

| Brazeフィールド | マッピングタイプ | 説明 |
| --- | --- | --- |
| External ID | ドロップダウン選択 | これは、デバイスやプラットフォームを超えてユーザーを追跡するためにBrazeが定義した永続的な`User ID`です。`User ID`を`External ID`にマッピングすることを推奨します。そうしないと、Zeotapはユーザーエイリアスとしてメールを送信する可能性があります。<br><br>Zeotapでは、Zeotap Catalogueで利用可能な`hashed email`を`External ID`にマッピングすることを推奨しています。|
| メール | 静的マッピング | これは、Zeotap Catalogueの`Email Raw`にマッピングされます。 |
| 電話 | 静的マッピング | これは、Zeotap Catalogueの`Mobile Raw`にマッピングされます。<br><br>• Brazeは`E.164`フォーマットの電話番号を受け付けます。Zeotapは変換を実行しません。このため、電話番号を所定の形式で取り込む必要があります。詳細については、「[ユーザーの電話番号]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers)」を参照してください。 |
| 名 | 静的マッピング | これは、Zeotap Catalogueの`First Name`にマッピングされます。 |
| 姓 | 静的マッピング | これは、Zeotap Catalogueの`Last Name`にマッピングされます。 |
| 性別 | 静的マッピング | これは、Zeotap Catalogueの`Gender`にマッピングされます。 |
| カスタムイベント名 | 静的マッピング | これは、Zeotap Catalogueの`Event Name`にマッピングされます。<br><br>Brazeでカスタムイベントをキャプチャするには、カスタムイベント名とカスタムイベントタイムスタンプの両方をマッピングする必要があります。どちらかがマッピングされていないと、カスタムイベントは処理できません。詳細については、「[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object)」を参照してください。 |
| カスタムイベントタイムスタンプ | 静的マッピング | これは、Zeotap Catalogueの`Event Timestamp`にマッピングされます。<br><br>Brazeでカスタムイベントをキャプチャするには、カスタムイベント名とカスタムイベントタイムスタンプの両方をマッピングする必要があります。どちらかがマッピングされていないと、カスタムイベントは処理できません。詳細については、「[イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object#what-is-an-event-object)」を参照してください。 |
| メール購読 | ドロップダウン選択 | `Email Marketing Preference`フィールドを登録してそれにマッピングします。<br><br>Zeotapは次の3つの値を送信します。<br>• `opted_in` - ユーザーがメールマーケティング設定を明示的に登録していることを示します。<br>• `unsubscribed` - ユーザーがメールメッセージを明示的にオプトアウトしたことを示します。<br>• `subscribed` - ユーザーがオプトインもオプトアウトもしていないことを示します。 |
| プッシュ購読 | ドロップダウン選択 | `Push Marketing Preference`フィールドを登録してそれにマッピングします。<br><br>Zeotapは次の3つの値を送信します。<br>• `opted_in` - ユーザーがプッシュマーケティング設定を明示的に登録していることを示します。<br>• `unsubscribed` - ユーザーがプッシュメッセージを明示的にオプトアウトしたことを示します。<br>• `subscribed` - ユーザーがオプトインもオプトアウトもしていないことを示します。 |
| メール開封トラッキングの有効化 | ドロップダウン選択 | 該当する`Marketing Preference`フィールドをマッピングします。<br><br>trueに設定すると、今後このユーザーに送信されるすべてのメールに開封トラッキングピクセルが追加されるようになります。 |
| メールクリックトラッキングの有効化 | ドロップダウン選択 | 該当する`Marketing Preference`フィールドをマッピングします。<br><br>trueに設定すると、今後このユーザーに送信されるすべてのメール内のすべてのリンクのクリックトラッキングが有効になります。 |
| プロダクトID | ドロップダウン選択 | • 購入アクションの識別子`(Product Name/Product Category)`。詳細については、「[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)」を参照してください。<br>• 関連する属性をZeotap Catalogueに登録してそれにマッピングします。<br><br>Brazeで購入イベントをキャプチャするには、`Product ID`、`Currency`、および`Price`を必ずマッピングする必要があります。この3つのいずれかが欠落している場合、購入イベントは成立しません。詳細については、「[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object)」を参照してください。 |
| 通貨 | ドロップダウン選択 | • 購入アクションの通貨属性。<br>• サポートされているフォーマットは`ISO 4217 Alphabetic Currency Code`です。<br>• 正しい形式の通貨データをZeotap Catalogueに登録してそれにマッピングします。<br><br>Brazeで購入イベントをキャプチャするには、`Product ID`、`Currency`、および`Price`を必ずマッピングする必要があります。この3つのいずれかが欠落している場合、購入イベントは成立しません。 |
| 価格 | ドロップダウン選択 | • 購入アクションの価格属性。<br>• 関連する属性をZeotap Catalogueに登録してそれにマッピングします。<br><br>Brazeで購入イベントをキャプチャするには、`Product ID`、`Currency`、および`Price`を必ずマッピングする必要があります。この3つのいずれかが欠落している場合、購入イベントは成立しません。 |
| 数量 | ドロップダウン選択 | • 購入アクションの数量属性。<br>• 関連する属性をZeotap Catalogueに登録してそれにマッピングします。 |
| 国 | ドロップダウン選択 | 登録する`Country` Catalogueフィールドにマッピングします。 |
| 市区町村 | ドロップダウン選択 | 登録する`City` Catalogueフィールドにマッピングします。 |
| 言語 | ドロップダウン選択 | • 使用可能なフォーマットは`ISO-639-1`標準（例：en）です。<br>• 正しい形式の言語を登録してそれにマッピングします。 |
| 生年月日 | ドロップダウン選択 | 登録する`Date of Birth`フィールドにマッピングします。 |
| カスタム属性 | カスタムデータ入力 | 任意のユーザー属性をカスタムデータ入力にマッピングし、それをBrazeに送信します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="サポートされている属性" }

## Brazeコンソールでデータを確認する {#viewing-data-on-braze-console}

送信する関連属性をマッピングし、ワークフローでパブリッシュすると、定義された基準に基づいてBrazeにイベントが流れ始めます。BrazeコンソールでメールIDまたはexternal IDで検索できます。

![Zeotapの属性とイベントが受信されたBrazeユーザープロファイルビュー。]({% image_buster /assets/img/zeotap/zeotap6.jpg %})

各種属性は、Braze内のユーザーダッシュボードのさまざまなセクションに表示されます。
- **Profile**タブにはユーザー属性が含まれます。
- **カスタム属性**タブには、ユーザーが定義したカスタム属性が含まれます。
- **Custom Events**タブには、ユーザーが定義したカスタムイベントが表示されます。
- **Purchases**タブには、ユーザーが一定期間内に行った購入が表示されます。

## キャンペーンの作成 {#campaign-creation}

ユーザーはBraze内でキャンペーンを作成し、リアルタイムまたはスケジュールされた時間に基づいてユーザーをアクティブ化できます。キャンペーンは、ユーザーが実行したアクション（カスタムイベント、購入）またはユーザー属性に基づいてトリガーできます。