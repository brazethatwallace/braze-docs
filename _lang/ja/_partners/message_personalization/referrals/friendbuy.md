---
nav_title: Friendbuy
article_title: Friendbuy
description: "FriendbuyとBrazeを統合する方法を学びます。"
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> [Friendbuy](https://www.friendbuy.com/)とBrazeの統合を活用して、メールやSMSの機能を拡張し、紹介やロイヤルティプログラムのコミュニケーションを簡単に自動化できます。Brazeでは、Friendbuy経由で収集されたすべてのオプトイン電話番号の顧客プロファイルが生成されます。

_この統合はFriendbuyによって管理されています。_

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Friendbuyアカウント | このパートナーシップを活用するには、[Friendbuyアカウント](https://retailer.friendbuy.io/)が必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。これは、Brazeダッシュボードの**設定** > **API キー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。これはBrazeインスタンスのURLに応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Friendbuyの統合 {#integrating-friendbuy}

[Friendbuy](https://retailer.friendbuy.io/)で**Developer Center** > **Integrations**に移動し、Braze統合カードで**Add integration**を選択します。

![FriendbuyのBraze統合カード。]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

フォームにRESTエンドポイントとAPIキーを入力し、**Install Integration**を選択します。

![Friendbuy統合フォーム。]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

[Friendbuyアカウント](https://retailer.friendbuy.io/)に戻り、ページを更新します。統合が成功すると、以下のようなメッセージが表示されます。

![統合がインストールされた状態]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### カスタム属性 {#custom-attributes}

| カスタム属性名 | 定義 | データタイプ |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status** | 紹介者は*Advocate*、被紹介者は*Referred Friend*に分類されます。 | 文字列 |
| **Friendbuy Customer Name** | 顧客が紹介ウィジェットから情報を送信する際に入力した名前 | 文字列 |
| **Friendbuy Referral Link** | Advocateに対して生成されるパーソナル紹介リンク（PURL）。例: https://fbuy.io/EzcW | 文字列 |
| **Friendbuy Date of Last Share** | 任意の共有チャネルを通じてAdvocateが最後にFriendと共有した日時。Advocateがまだ共有していない場合、このプロパティは表示されません。 | 時刻 |
| **Friendbuy キャンペーン ID** | Advocateのために生成されたパーソナル紹介リンクに関連するキャンペーン ID | 文字列 |
| **Friendbuy キャンペーン Name** | Advocateのために生成されたパーソナル紹介リンクに関連するキャンペーン名 | 文字列 |
| **Friendbuy Coupon Code** | 顧客に配布された最新の紹介クーポンコード。注: 表示されるコードは1つだけです。 | 文字列 |
| **Friendbuy Coupon Value** | 顧客に配布された最新のクーポンコードの通貨価値。 | 数値 |
| **Friendbuy Coupon Status** | 顧客に配布された最新のクーポンコードのステータス。注: ステータスは「distributed」または「redeemed」です。 | 文字列 |
| **Friendbuy Coupon Currency** | 顧客に配布された最新のクーポンコードに関連する通貨コード（USD、CADなど）またはパーセント（%）。 | 文字列 |
| **Friendbuy Coupon キャンペーン ID** | 顧客のために生成されたクーポンコードに関連するキャンペーン ID。 | 文字列 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="カスタム属性" }

## デフォルトの動作 {#default-behavior}

顧客データをBrazeに送信する前に、顧客は紹介ウィジェットで以下の1つ以上のチェックボックスをオンにしてオプトインする必要があります。

![紹介ウィジェット]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
Friendbuyは国際標準規格（E.164）を使用して実在する電話番号を検証します。`555-555-5555` のような無効な番号はBrazeに送信されません。
{% endalert %}

### チェックボックスの動作 {#checkbox-behavior}

| 選択されたチェックボックス | 動作 |
|-------------------|-----------------------------------------------------------------|
| メールのみ | 顧客のメールアドレスのみがBrazeに送信されます。 |
| 電話のみ | 顧客の電話番号のみがBrazeに送信されます。 |
| どちらも選択しない | 顧客データはBrazeに送信されません。 |
| 両方 | 顧客のメールアドレスと電話番号がBrazeに送信されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Checkbox behavior" }