---
nav_title: APIメールユーザー設定センター
article_title: APIメールユーザー設定センター
page_order: 1
description: "この記事では、APIメールユーザー設定センターとそのカスタマイズ方法について説明します。"
channel:
  - email
---

# APIメールユーザー設定センター {#api-email-preference-center}

> ユーザー設定センターを設定すると、ユーザーが[メールメッセージング]({{site.baseurl}}/user_guide/channels/email)の通知設定を一か所で編集・管理できるようになります。この記事では、APIで生成するユーザー設定センターの構築手順を説明しますが、[ドラッグ＆ドロップエディター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center)を使用してユーザー設定センターを構築することもできます。

Brazeダッシュボードで、**オーディエンス** > **メールユーザー設定センター**に移動します。

ここで各サブスクリプショングループを管理・表示できます。作成した各サブスクリプショングループは、このユーザー設定センターリストに追加されます。複数のユーザー設定センターを作成できます。

{% alert important %}
ユーザー設定センターはBrazeメールチャネル内で使用することを目的としています。ユーザー設定センターのリンクは各ユーザーに基づいて動的に生成されるため、外部でホストすることはできません。
{% endalert %}

## APIを使用してユーザー設定センターを作成する {#create-a-preference-center-with-api}

[ユーザー設定センターBrazeエンドポイント]({{site.baseurl}}/api/endpoints/preference_center)を使用すると、Brazeがホストするウェブサイトであるユーザー設定センターを作成でき、ユーザーの購読状態と購読グループのステータスを表示できます。HTMLとCSSを使用して、開発者チームはページのスタイリングがブランドガイドラインに合うようにユーザー設定センターを構築できます。

Liquidを使用すると、購読グループの名前と各ユーザーのステータスを取得できます。これにより、ページが読み込まれたときにBrazeがこのデータを保存および取得します。

### 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| ユーザー設定センターの有効化 | Brazeダッシュボードにユーザー設定センター機能を使用する権限があること。 |
| メール、SMS、またはWhatsApp購読グループを持つ有効なワークスペース | 有効なユーザーとメール、SMS、またはWhatsApp購読グループを持つ稼働中のワークスペース。 |
| 有効なユーザー | メールアドレスとexternal IDを持つユーザー。 |
| ユーザー設定センター権限を持つ生成済みAPIキー | Brazeダッシュボードで、**設定** > **APIキー**に移動し、ユーザー設定センター権限を持つAPIキーにアクセスできることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

### ステップ1:ユーザー設定センター作成エンドポイントを使用する {#step-1-use-the-create-preference-center-endpoint}

[ユーザー設定センター作成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center)を使用してユーザー設定センターの構築を始めましょう。ユーザー設定センターをカスタマイズするには、ブランディングに合ったHTMLを`preference_center_page_html`フィールドと`confirmation_page_html`フィールドに含めることができます。

[ユーザー設定センターURL生成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)を使用すると、Brazeを通じて送信されるメール以外で、特定のユーザーのユーザー設定センターURLを取得できます。

{% alert note %}
Brazeは`data:` URLを使用するiframe内で`confirmation_page_html`をレンダリングします。ブラウザは`data:` URLを不透明なオリジンとして扱います。そのため、そのiframe内のスクリプトは追加の外部リソースを読み込むことができず、そのページから親ウィンドウのナビゲーションやフレーム間の通信は失敗します。<br><br>代わりに、スクリプトを埋め込む代わりに、ホストされた調査URLなどの外部コンテンツにリンクできます。サードパーティツールを埋め込む必要があり、ベンダーが許可している場合は、ツールのホストされたHTTPS URLを指す`<iframe title="埋め込みコンテンツの説明" src="https://example.com/...">`を使用してください。
{% endalert %}

### ステップ2:メールキャンペーンに含める {#step-2-include-in-your-email-campaign}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

メールにユーザー設定センターへのリンクを配置するには、購読解除URLを挿入する方法と同様に、メール内の目的の場所に以下のLiquidタグを使用します。

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Liquidを含むHTMLの組み合わせを使用することもできます。たとえば、以下をHTMLエディターまたはドラッグ＆ドロップエディターのURLとして貼り付けることができます。これは、すべてのメール購読グループを自動的にリストする基本的なユーザー設定センターレイアウトを表示します。[リンクエイリアス]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing)を使用する場合は、BrazeがトラッキングパラメーターをAppendできるように、Liquidタグの後に末尾のクエスチョンマーク（`?`）を追加してください。

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

ユーザー設定センターには、ユーザーがすべてのメールの購読を解除できるチェックボックスがあります。

{% multi_lang_include preference_center/testing.md section="api" %}

#### ユーザー設定センターを編集する {#edit-a-preference-center}

[ユーザー設定センター更新エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center)を使用して、ユーザー設定センターを編集および更新できます。

#### ユーザー設定センターと詳細を特定する {#identify-preference-centers-and-details}

ユーザー設定センターを特定するには、[ユーザー設定センター詳細表示エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center)を使用して、最終更新タイムスタンプ、ユーザー設定センターIDなどの関連情報を返します。

## ユーザー設定センターのカスタマイズ {#customize-a-preference-center}

Brazeはユーザー設定センターからの購読ステータスの更新を管理し、ユーザー設定センターを同期された状態に保ちます。ただし、以下のオプションで[購読グループ API]({{site.baseurl}}/api/endpoints/subscription_groups)を使用して、独自のユーザー設定センターを作成しホストすることもできます。

### オプション1：文字列クエリパラメーターを使用したリンク {#option-1-link-with-string-query-parameters}

URLの本文にクエリ文字列のフィールドと値のペアを使用して、ユーザーIDとメールカテゴリーをページに渡すことで、ユーザーは購読解除の選択を確認するだけで済みます。このオプションは、ユーザー識別子をハッシュ形式で保存しており、まだ購読センターを持っていない場合に適しています。

このオプションでは、各メールカテゴリーに固有の購読解除リンクが必要です。<br>
`http://mycompany.com/query-string-form-fill?field_id=Alex&field_category=offers`

{% alert tip %}
Liquidフィルターを使用して、送信時にユーザーのexternal IDをハッシュ化することも可能です。これにより、`user_id`がMD5ハッシュ値に変換されます。例：
{% raw %}
```liquid
{% assign my_string = ${user_id} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### オプション2：JSON Webトークンによる認証 {#option-2-authenticate-with-json-web-token}

[JSON Webトークン](https://auth0.com/learn/json-web-tokens/)を使用して、通常はユーザー名とパスワードによるログインなどの認証レイヤーの背後にあるWebサーバーの一部（アカウント設定など）に対してユーザーを認証します。

このアプローチでは、URLにクエリ文字列の値ペアを埋め込む必要はありません。これらはJSON Webトークンのペイロードで渡すことができます。例：

```json
{
    "user_id": "1234567890",
    "name": "Alex Smith",
    "category": "offers"
}
```

## よくある質問 {#frequently-asked-questions}

### テスト送信でユーザー設定センターが機能しないのはなぜですか？ {#why-doesnt-my-preference-center-work-in-a-test-send}

ユーザー設定センターのリンクにはライブ送信コンテキストが必要です。テスト送信では有効なユーザー設定センターの URL が生成されず、ページが読み込まれると**設定を保存**ボタンが無効になります。これは想定された動作です。エンドツーエンドのテストを行うには、テストユーザーまたは小規模な内部セグメントに対してキャンペーンまたはキャンバスステップを開始するか、[ユーザー設定センター URL 生成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center)を使用してください。詳細については、[ユーザー設定センターのテスト](#testing-preference-centers)を参照してください。

### ユーザー設定センターを作成していないのに、ダッシュボードに「PreferenceCenterBrazeDefault」が表示されるのはなぜですか？ {#i-havent-created-a-preference-center-why-am-i-seeing-preferencecenterbrazedefault-on-my-dashboard}

これは、レガシー Liquid {%raw%}`${preference_center_url}`{%endraw%} が使用されている場合にユーザー設定センターをレンダリングするために使用されます。つまり、{%raw%}`${preference_center_url}` または `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} を参照するキャンバスステップやテンプレートは機能しません。これは、レガシー Liquid または「PreferenceCenterBrazeDefault」をメッセージの一部として含む過去に送信されたメッセージにも適用されます。

新しいメッセージで再度 {%raw%}`${preference_center_url}`{%endraw%} を参照すると、「PreferenceCenterBrazeDefault」という名前のユーザー設定センターが再び作成されます。

### ユーザー設定センターは複数の言語をサポートしていますか？ {#do-preference-centers-support-multiple-languages}

いいえ。ただし、カスタムオプトインおよびオプトアウトページの HTML を記述する際に Liquid を活用できます。ダイナミックなリンクを使用して購読解除を管理している場合、これは単一のリンクになります。

たとえば、スペイン語を話すユーザーの購読解除率を追跡する場合、別々のキャンペーンを使用するか、Currents に関する分析を活用する必要があります（ユーザーが購読解除した時点を確認し、そのユーザーの優先言語を確認するなど）。

別の例として、スペイン語を話すユーザーの購読解除率を追跡するために、ユーザーの言語がスペイン語の場合は購読解除 URL に `?Spanish=true` のようなクエリパラメータ文字列を追加し、それ以外の場合は通常の購読解除リンクを使用できます。

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

その後、Currents を通じて、どのユーザーがスペイン語を話し、その購読解除リンクに対するクリックイベントがいくつあったかを特定できます。

### 購読解除リンクとメールのユーザー設定センターの両方が送信に必要ですか？ {#are-both-unsubscribe-links-and-email-preference-centers-required-for-sending}

いいえ。メールキャンペーンの作成時に「Your Email Body does not include an unsubscribe link」というメッセージが表示される場合、購読解除リンクがコンテンツブロックに含まれている場合にこの警告が表示されることが想定されています。

### デフォルトのブラウザアイコンを更新するにはどうすればよいですか？ {#how-do-i-update-the-default-browser-icon}

デフォルトでは、ブラウザタブ名の横にあるアイコン（ファビコン）には Braze のロゴが使用されます。カスタムファビコンを追加するには、[ユーザー設定センター API コール]({{site.baseurl}}/api/endpoints/preference_center)の作成または更新で `links-tags` 属性を設定します。Braze はホストされたページに {% raw %}`<link rel="icon" ...>`{% endraw %} タグを挿入します。

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}