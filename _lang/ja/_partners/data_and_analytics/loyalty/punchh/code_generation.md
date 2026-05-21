---
nav_title: 動的コード生成
article_title: Punchh 動的コード生成
page_order: 2
description: "このリファレンス記事では、BrazeにおけるPunchh動的コード生成の使い方を説明します。"
page_type: partner
search_tag: Partner
---

# Punchhによる動的コード生成 {#dynamic-code-generation-with-punchh}

> クーポンコードとは、一人のユーザーが使用できるユニークなコードです（1回使用でも複数回使用でも可）。Punchhフレームワークはクーポンコードを生成し、モバイルアプリ内やPOSシステムで処理できます。

_この統合はPunchhによって管理されています。_

## 統合について {#about-the-integration}

PunchhクーポンフレームワークとBrazeを使用すると、以下のシナリオを実現できます。

- ゲストがメール内のクーポン生成リンクをクリックしたときにクーポンコードを生成する：クーポンコードは動的に生成され、Webページに表示されます。
- ゲストがメールを開封したときにクーポンコードを生成する：クーポンコードは動的に生成され、メール内に画像として表示されます。

## 動的クーポンコード生成の統合 {#integrating-dynamic-coupon-code-generation}

### ステップ1：クーポンキャンペーンを作成する {#step-1-create-a-coupon-campaign}

1. Punchhクーポンキャンペーンを使用して、以下の画像のように動的生成クーポンキャンペーンを作成します。
2. Punchhクーポンフレームワークは、動的クーポン生成を可能にするために以下のパラメーターを生成します。
    - 動的クーポン生成トークン：暗号化のためにシステムが生成するセキュリティトークンです。
    - 動的クーポン生成URL：このURLは、ビジネスの要件に応じてリンクまたは画像としてメールに埋め込まれます。

![Punchhでクーポンキャンペーンを作成するためのフォーム。]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### ステップ2：署名を生成しURLを構築する {#step-2-generate-signature-and-construct-url}

JWT.IOライブラリーは、JSONウェブトークンをデコード、検証、生成します。これは、2つの当事者間でクレームを安全に表現するための、オープンで業界標準のRFC 7519方式です。

次の`ClaimType`名を使用して、ゲストとクーポンの一意性を確保できます。

- `campaign_id`：システム生成のPunchh Campaign IDを表します。
- `email`：ユーザーのメールアドレスを表します。
- `first_name`：ユーザーの名を取得します。
- `last_name`：ユーザーの姓を取得します。

Punchhの動的クーポンコードAPIを使用するには、JWTトークンを構築する必要があります。Brazeダッシュボードで使用したいチャネルのメッセージ本文に、以下のLiquidテンプレートを追加してください。

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


以下を置き換えてください。

| プレースホルダー | 説明 |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | 動的クーポン生成トークン。 |
| `CAMPAIGN_ID` | キャンペーン ID。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Generate signature and construct URL" }

### ステップ3：クーポンコードをメッセージ本文に追加する {#step-3-append-coupon-code-to-message-body}

#### Punchh Webページへのリンク {#linking-to-punchh-web-page}

PunchhがホストするWebページにリンクするには、[先ほど作成した](#step-1-create-a-coupon-campaign-in-punchh)動的生成URLに`{% raw %}{{jwt}}{% endraw %}`を追加します。リンクは以下のようになります。

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

ユーザーがクーポンURLをクリックすると、PunchhがホストするWebページにリダイレクトされ、生成されたクーポンが表示されます。

![ユーザーがクーポンコードの生成に成功した後の確認メッセージの例。]({% image_buster /assets/img/punchh/punchh7.png %})

#### JSON経由でコードをプレーンテキストとして抽出する {#extracting-code-via-json-as-plain-text}

JSON応答を返すには、[先ほど作成した](#step-1-create-a-coupon-campaign-in-punchh)動的生成URLに`{% raw %}{{jwt}}{% endraw %}`を追加し、URL文字列のトークンの後に`.json`を追加します。リンクは以下のようになります。

{% raw %}
`````````liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

その後、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)を活用して、コードをプレーンテキストとして任意のメッセージ本文に挿入できます。例：

{% raw %}
`````````liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
```
{% endraw %}

#### メールコンテンツ内の画像にリンクする {#linking-an-image-inside-email-content}

クーポンコードを画像内にリンクするには：

1. [先ほど作成した](#step-1-create-a-coupon-campaign-in-punchh)動的生成URLに`{% raw %}{{jwt}}{% endraw %}`を追加します。
2. URL文字列のトークンの後に`.png`を追加します。
3. リンクをHTML{% raw %}`<img>`{% endraw %}タグに埋め込みます。

{% tabs local %}
{% tab 入力例 %}
{% raw %}
`````````liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
```
{% endraw %}
{% endtab %}

{% tab 出力例 %}
![クーポンコード画像タグのレンダリング出力。]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## エラーメッセージ {#error-messages}

| エラーコード | エラーメッセージ | 説明 |
| --- | --- | --- |
| `coupon_code_expired` | This promo code has expired | 設定された有効期限日を過ぎた後にコードが使用されています。 |
| `coupon_code_success` | Congratulations, Promo Code Applied Successfully. | コードが正常に使用されました。 |
| `coupon_code_error` | Please enter a valid promo code | 使用されたコードが無効です。 |
| `coupon_code_type_error` | Incorrect coupon type. This coupon can only be redeemed at `%{coupon_type}`. | POSで使用するはずのコードがモバイルアプリで使用された場合、このエラーが発生します。 |
| `usage_exceeded` | The usage for this coupon code's campaign is full. Please try next time. | コードの使用数が、使用を許可されたユーザー数を超えています。例えば、ダッシュボード設定で3,000人のユーザーによるコード使用を許可しており、ユーザー数が3,000人を超えた場合、このエラーが発生します。 |
| `usage_exceeded_by_guest` | This promo code has already been processed. | ユーザーによるコードの使用回数が、許可された回数を超えています。例えば、ダッシュボード設定で1つのコードをユーザーが3回使用できるようにしている場合、それ以上使用するとこのエラーが発生します。 |
| `already_used_by_other_guest` | This promo code has already been used by some other guest. | 別のユーザーがすでにこのコードを使用しています。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Error messages" }