---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "このリファレンス記事では、BrazeとPassKitのパートナーシップについて説明します。このパートナーシップにより、Apple ウォレットとGoogle Payのパスをカスタマーエクスペリエンスに統合してモバイルリーチを拡大できます。"
page_type: partner
search_tag: Partner

---

# PassKit

> PassKitは、Apple ウォレットとGoogle Payのパスをカスタマーエクスペリエンスに統合することで、モバイルリーチの拡大を支援します。デジタルクーポン、ロイヤルティカード、会員カード、チケットなどの作成、管理、配布、パフォーマンス分析を簡単に行うことができ、顧客は他のアプリを必要としません。

_この統合はPassKitによって管理されています。_

## 統合について {#about-the-integration}

BrazeとPassKitの統合により、Apple ウォレットとGoogle Payのカスタムパスを即時に配信して、オンラインキャンペーンのエンゲージメントを高め、測定できます。その後、利用状況を分析し、リアルタイムに調整することで、位置情報に基づくメッセージやパーソナライズされたダイナミックな更新を顧客のモバイルウォレットに送信し、店舗内のトラフィックを増加させることができます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| PassKitアカウント | PassKitアカウントとPassKitアカウントマネージャーが必要です。 |
| `userDefinedID` | PassKitとBrazeの間でユーザーへのカスタムイベントやカスタム属性を適切に更新するには、Brazeのexternal IDを`userDefinedID`として設定する必要があります。この`userDefinedID`は、PassKitのエンドポイントにAPIコールを行う際に使用されます。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics/#endpoints)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

顧客のモバイルウォレットエクスペリエンスをさらに充実させるために、PassKitダッシュボードから、Brazeの[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint)を通じてBrazeにデータを渡すことができます。

PassKitから共有するデータの例を以下に示します。
- **パス作成**: 顧客がパスリンクをクリックして、パスが最初に表示される時点。
- **パスインストール**: 顧客がパスを追加し、自分のウォレットアプリに保存する時点。
- **パス更新**: パスが更新される時点。
- **パス削除**: 顧客がウォレットアプリからパスを削除する時点。

データがBrazeに渡されると、オーディエンスを構築し、Liquidでコンテンツをパーソナライズし、これらのアクションが実行された後にキャンペーンやキャンバスをトリガーすることができます。

## PassKitをBrazeに接続する {#connect-passkit-to-braze}

PassKitからデータを渡すには、Brazeのexternal IDをPassKitの`externalId`として設定していることを確認します。

1. PassKitパスプロジェクトまたはプログラムの**Settings**の**Integrations**で、**Braze**タブの**Connect**をクリックします。<br>![PassKitプラットフォームのBraze統合タイル。]({% image_buster /assets/img/passkit/passkit5.png %}){: style="max-width:80%"}<br><br>
2. Braze APIキーとエンドポイントURLを入力し、コネクターの名前を入力します。<br><br>
3. **Enable Integration**をトグルし、Brazeでメッセージをトリガーまたはパーソナライズしたいイベントを選択します。<br>![APIキー、エンドポイントURL、統合名、有効化設定、メンバーシップ設定、およびパス設定を受け入れるために展開されているPassKit Braze統合タイル。]({% image_buster /assets/img/passkit/passkit4.png %}){: style="max-width:70%"}

## SmartPassリンクを使用してパスを作成する {#create-pass-using-a-smartpass-link}

Brazeでは、SmartPassリンクを設定して、顧客がAndroidまたはiOSにパスをインストールするための一意のURLを生成できます。そのためには、Brazeのコンテンツブロックから呼び出せる暗号化されたSmartPassデータペイロードを定義する必要があります。この[コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks)は、今後のパスやクーポンに再利用できます。以下は統合の際に使用されます。

- **PassKit URL**: PassKit URLは、PassKitプログラムの一意のURLです。<br>各プログラムには固有のURLがあり、PassKitプログラムまたはプロジェクトの**Distribution**タブで確認できます。（例: https://pub1.pskt.io/c/ww0jir）<br><br>
- **PassKitシークレット**: URLとともに、このプログラムのPassKit Keyを手元に用意しておく必要があります。<br>これはPassKit URLと同じページで確認できます。<br><br>
- **プログラム（またはプロジェクト）ID**: SmartPass URLを作成するには、PassKitプログラムIDが必要です。<br>プロジェクトやプログラムの**Settings**タブで確認できます。

暗号化されたSmartPassリンクの作成に関する詳細は、こちらの[PassKitの記事](https://help.passkit.com/en/articles/3742778-hashed-smartpass-links)を参照してください。

### ステップ1: パスデータペイロードを定義する {#passkit-integrations}

まず、クーポンまたはメンバーのペイロードを定義する必要があります。

ペイロードにはさまざまなコンポーネントを含めることができますが、ここでは2つの重要なコンポーネントを示します。

| コンポーネント | 必須 | タイプ | 説明 |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | 必須 | 文字列 | Brazeのexternal IDとして設定され、PassKitからBrazeへのコールバックが機能するために重要です。これにより、会社ユーザーは1つのキャンペーンで複数のオファーのクーポンを持つことができます。一意であることは必須ではありません。 |
| `members.member.externalId` | オプション | 文字列 | Brazeのexternal IDとして設定します。external IDを使用してメンバーシップパスを更新できます。このフィールドを設定することで、メンバーシッププログラム内でユーザーが一意になります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Step 1: Define your pass data payload #passkit-integrations" }

使用可能なすべてのフィールドとそのタイプ、役立つ説明については、[PassKit GitHubのドキュメント](https://github.com/PassKit/smart-pass-link-from-csv-generator)を参照してください。

#### ペイロードの例 {#example-payload}
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### ステップ2: 未定義のペイロード変数を作成し、エンコードする {#step-2-create-and-encode-an-undefined-payload-variable}

Brazeダッシュボード内の**コンテンツ** > **コンテンツブロック**に移動して、新しいコンテンツブロックを作成し、名前を付けます。

**Create Content Block**を選択して開始します。

次に、**コンテンツブロックのLiquidタグ**を定義します。このコンテンツブロックを保存したら、メッセージを作成するときにこのLiquidタグを参照できます。この例では、Liquidタグを{% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %}として割り当てています。

このコンテンツブロック内部では、ペイロードを直接含めず、{% raw %}`{{passData}}`{% endraw %}変数で参照します。コンテンツブロックに追加する最初のコードスニペットは、{% raw %}`{{passData}}`{% endraw %}変数のBase64エンコードをキャプチャします。
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### ステップ3: SHA1 HMACハッシュを使用して暗号化署名を作成する {#step-3-create-your-encryption-signature-using-a-sha1-hmac-hash}

次に、プロジェクトのURLとペイロードの[SHA1 HMAC](https://en.wikipedia.org/wiki/HMAC)ハッシュを使って暗号化署名を作成します。

コンテンツブロックに追加する2つ目のコードスニペットは、ハッシュに使用するURLをキャプチャします。
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

次に、このハッシュと`Project Secret`を使用して署名を生成する必要があります。これは、3つ目のコードスニペットを含めることで可能になります。
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

最後に、5番目のコードスニペットを使って、完全なURLに署名を追加します。
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### ステップ4: URLを出力する {#step-4-print-your-url}

最後に、最終的なURLを呼び出して、メッセージ内にSmartPass URLが出力されるようにします。
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

この時点で、次のようなコンテンツブロックが作成されています。

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

この例では、これらのインストールのソースをBrazeとこのキャンペーンまで追跡するために、UTMパラメーターが追加されています。

{% alert tip %}
ページを離れる前に、コンテンツブロックを必ず保存してください。
{% endalert %}

### ステップ5: すべてをまとめる {#step-5-putting-it-all-together}

このコンテンツブロックが作成されたら、今後再利用できます。

コンテンツブロックの例では、2つの変数が未定義のままになっていることにお気づきでしょう。<br>
{% raw %}`{{passData}}`{% endraw %} - [ステップ1](#passkit-integrations)で定義したJSONパスデータのペイロード<br>
{% raw %}`{{projectUrl}}`{% endraw %} - PassKitプロジェクトのDistributionタブにあるプロジェクトまたはプログラムのURL。

これは意図的な決定であり、コンテンツブロックの再利用性をサポートします。これらの変数は参照されるだけで、コンテンツブロック内で作成されるわけではないので、コンテンツブロックを作り直すことなく変更できます。

たとえば、紹介オファーを変更して、ロイヤルティプログラムに初回ポイントを追加したり、セカンダリメンバーカードやクーポンを作成したりすることがあります。これらのシナリオではPassKitの`projectURLs`またはパスペイロードが異なる可能性があり、Brazeでキャンペーンごとに定義します。

#### メッセージ本文を作成する {#composing-the-message-body}

この2つの変数をメッセージ本文にキャプチャしてから、コンテンツブロックを呼び出します。
[ステップ1](#passkit-integrations)のミニファイ化されたJSONペイロードをキャプチャします。

**プロジェクトURLを割り当てる**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**JSONをキャプチャする**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**先ほど作成したコンテンツブロックを参照する**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

メッセージ本文は次のようになります。
![キャプチャされたJSONおよびコンテンツブロック参照を含むコンテンツブロックメッセージ作成画面の画像。]({% image_buster /assets/img/passkit/passkit1.png %}){: style="max-width:70%"}

サンプルの出力URLは以下の通りです。
![ランダムに生成された文字と数字からなる長い文字列を含む出力URL。]({% image_buster /assets/img/passkit/passkit2.png %}){: style="max-width:70%"}

出力URLは長くなります。その理由は、パスデータがすべて含まれており、データの完全性とURL変更による改ざんを防ぐために、クラス最高のセキュリティが組み込まれているからです。SMSを使用してこのURLを配布する場合は、[bit.ly](https://dev.bitly.com/v4/#operation/createFullBitlink)のようなリンク短縮プロセスで実行することをお勧めします。これは、bit.lyエンドポイントへのコネクテッドコンテンツ呼び出しを使用して行うことができます。

## PassKit Webhookを使用してパスを更新する {#update-pass-using-the-passkit-webhook}

Brazeでは、Webhookのキャンペーンやキャンバス内のWebhookを設定して、ユーザーの行動に基づいて既存のパスを更新することができます。有用なPassKitエンドポイントについては、次のリンクを参照してください。
- [メンバープロジェクト](https://docs.passkit.io/protocols/member/)
- [クーポンプロジェクト](https://docs.passkit.io/protocols/coupon/)
- [フライトプロジェクト](https://docs.passkit.io/protocols/boarding/)

### ペイロードパラメーター {#payload-parameters}

始める前に、PassKitへのWebhookの作成と更新に含めることができる一般的なJSONペイロードパラメーターを以下に示します。

| データ | タイプ | 説明 |
| ---- | ---- | ----------- |
| `externalId` | 文字列 | 一意の顧客識別子（メンバーシップ番号など）を使用する既存のシステムとの互換性を得るために、パスレコードに一意のIDを追加できます。このエンドポイントを使用して、パスIDではなく`userDefinedId`と`campaignName`でパスデータを取得できます。この値はキャンペーン内で一意でなければならず、設定後は変更できません。<br><br>Braze統合では、Brazeのexternal ID {% raw %}`{{${user_id}}}`{% endraw %}を使用することをお勧めします。 |
| `campaignId`（クーポン）<br><br> `programId`（メンバーシップ） | 文字列 | PassKitで作成したキャンペーンまたはプログラムテンプレートのIDです。これを確認するには、PassKitパスプロジェクトの**Settings**タブに移動します。 |
| `expiryDate` | IO8601日時 | パスの有効期限です。有効期限を過ぎると、パスは自動的に無効になります（`isVoided`を参照）。この値はテンプレートとキャンペーン終了日の値を上書きします。 |
| `status` | 文字列 | `REDEEMED`や`UNREDEEMED`など、クーポンの現在のステータスです。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Payload parameters" }

### ステップ1: BrazeのWebhookテンプレートを作成する {#step-1-create-your-braze-webhook-template}

今後のキャンペーンやキャンバスで使用するPassKit Webhookテンプレートを作成するには、Brazeダッシュボードの**テンプレートとメディア**セクションに移動します。単発のPassKit Webhookのキャンペーンを作成する場合、または既存のテンプレートを使用する場合は、新しいキャンペーンを作成する際にBrazeで**Webhook**を選択します。

PassKit Webhookテンプレートを選択すると、以下のように表示されます。
- **Webhook URL**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **リクエスト本文**: Raw Text

#### リクエストヘッダーとメソッド {#request-headers-and-method}

PassKitの認証には、Base64でエンコードされたPassKit APIキーを含む`HTTP Header`が必要です。以下はすでにキーと値のペアとしてテンプレートに含まれていますが、**Settings**タブでは、`<PASSKIT_LONG_LIVED_TOKEN>`をPassKitトークンに置き換える必要があります。トークンを取得するには、PassKitプロジェクト/プログラムに移動し、**Settings > Integrations > Long Lived Token**に移動します。

{% raw %}
- **HTTPメソッド**: PUT
- **リクエストヘッダー**:
  - **Authorization**: Bearer `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Type**: application/json
{% endraw %}

#### リクエスト本文 {#request-body}

Webhookをセットアップするには、リクエスト本文に新しいイベントの詳細を記入し、ユースケースに必要なペイロードパラメーターを含めます。

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### ステップ2: リクエストをプレビューする {#step-2-preview-your-request}

入力したテキストがBrazeタグに該当する場合、自動的にハイライト表示されます。

**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、Webhookをテストするために自分でカスタマイズします。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>更新されたWebhookテンプレートは、新しい[Webhookのキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を作成するときに、**保存済み Webhook テンプレート**リストで見つけることができます。
{% endalert %}

## コネクテッドコンテンツからパスの詳細を取得する {#retrieve-pass-details-via-connected-content}

パスの作成と更新に加え、ユーザーのパスメタデータをBrazeの[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)から取得し、パーソナライズされたパスの詳細をメッセージングキャンペーンに組み込むこともできます。

**PassKitコネクテッドコンテンツ呼び出し**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}}
```
{% endraw %}

**Liquidの応答の例**

{% tabs local %}
{% tab passes redemptionDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab passes status %}
```
UNREDEEMED
```
{% endtab %}
{% endtabs %}