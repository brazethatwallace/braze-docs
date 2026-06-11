---
nav_title: APIメールユーザー設定センター
article_title: APIメールユーザー設定センター
page_order: 1
description: "この記事では、APIメールユーザー設定センターとそのカスタマイズ方法について説明します。"
channel:
  - email
---

# APIメールユーザー設定センター {#api-email-preference-center}

> ユーザー設定センターを設定すると、ユーザーが[メールメッセージング]({{site.baseurl}}/user_guide/channels/email/)の通知設定を一か所で編集・管理できるようになります。この記事では、APIで生成するユーザー設定センターの構築手順を説明しますが、[ドラッグ＆ドロップエディター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/dnd_preference_center/)を使用してユーザー設定センターを構築することもできます。

Brazeダッシュボードで、**オーディエンス** > **メールユーザー設定センター**に移動します。

ここで各サブスクリプショングループを管理・表示できます。作成した各サブスクリプショングループは、このユーザー設定センターリストに追加されます。複数のユーザー設定センターを作成できます。

{% alert important %}
ユーザー設定センターはBrazeメールチャネル内で使用することを目的としています。ユーザー設定センターのリンクは各ユーザーに基づいて動的に生成されるため、外部でホストすることはできません。
{% endalert %}

## APIでユーザー設定センターを作成する {#create-a-preference-center-with-api}

[ユーザー設定センターBrazeエンドポイント]({{site.baseurl}}/api/endpoints/preference_center/)を使用すると、Brazeがホストするウェブサイトであるユーザー設定センターを作成でき、ユーザーのサブスクリプション状態やサブスクリプショングループのステータスを表示できます。HTMLとCSSを使用して、開発者チームがページのスタイリングをブランドガイドラインに合わせたユーザー設定センターを構築できます。

Liquidを使用すると、サブスクリプショングループの名前と各ユーザーのステータスを取得できます。これにより、ページが読み込まれたときにBrazeがこのデータを保存・取得します。

### 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| ユーザー設定センターの有効化 | Brazeダッシュボードにユーザー設定センター機能を使用する権限があること。 |
| メール、SMS、またはWhatsAppサブスクリプショングループを持つ有効なワークスペース | 有効なユーザーとメール、SMS、またはWhatsAppサブスクリプショングループを持つ稼働中のワークスペース。 |
| 有効なユーザー | メールアドレスとexternal IDを持つユーザー。 |
| ユーザー設定センター権限を持つ生成済みAPIキー | Brazeダッシュボードで、**設定** > **APIキー**に移動し、ユーザー設定センター権限を持つAPIキーにアクセスできることを確認します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

### ステップ 1: ユーザー設定センター作成エンドポイントを使用する {#step-1-use-the-create-preference-center-endpoint}

[ユーザー設定センター作成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/)を使用して、ユーザー設定センターの構築を始めましょう。ユーザー設定センターをカスタマイズするには、ブランディングに合ったHTMLを`preference_center_page_html`フィールドと`confirmation_page_html`フィールドに含めることができます。

[ユーザー設定センターURL生成エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/)を使用すると、Brazeを通じて送信されるメール以外で、特定のユーザーのユーザー設定センターURLを取得できます。

{% alert note %}
Brazeは`data:` URLを使用するiframe内で`confirmation_page_html`をレンダリングします。ブラウザは`data:` URLを不透明なオリジンとして扱います。そのため、そのiframe内のスクリプトは追加の外部リソースを読み込むことができず、そのページから親ウィンドウのナビゲーションやフレーム間通信は失敗します。<br><br>代わりに、スクリプトを埋め込む代わりに、ホストされた調査URLなどの外部コンテンツにリンクできます。サードパーティツールを埋め込む必要があり、ベンダーが許可している場合は、ツールのホストされたHTTPS URLを`src`に指定した`<iframe>`を使用してください。
{% endalert %}

### ステップ 2: メールCampaignに含める {#step-2-include-in-your-email-campaign}

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

メールにユーザー設定センターへのリンクを配置するには、配信停止URLを挿入する方法と同様に、メール内の目的の場所に以下のLiquidタグを使用します。

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Liquidを含むHTMLの組み合わせも使用できます。たとえば、HTMLエディターまたはドラッグ＆ドロップエディターでURLとして以下を貼り付けることができます。これにより、すべてのメールサブスクリプショングループを自動的にリストする基本的なユーザー設定センターレイアウトが表示されます。[リンクエイリアス]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_aliasing/)を使用する場合は、Brazeがトラッキングパラメーターを追加できるように、Liquidタグの後に末尾のクエスチョンマーク（`?`）を追加してください。

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

ユーザー設定センターには、ユーザーがすべてのメールの配信を停止できるチェックボックスがあります。テストメッセージとして送信された場合、これらの設定は保存できないことに注意してください。

{% alert important %}
上記のLiquidタグは、CampaignまたはCanvasを起動する場合にのみ機能します。テストメールの送信では有効なリンクは生成されません。ユーザー設定センターのリンクを確認するには、テストプロファイルのみをターゲットとするCampaignでメッセージを起動してください。
{% endalert %}

#### ユーザー設定センターを編集する {#edit-a-preference-center}

[ユーザー設定センター更新エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/)を使用して、ユーザー設定センターを編集・更新できます。

#### ユーザー設定センターと詳細を確認する {#identify-preference-centers-and-details}

ユーザー設定センターを確認するには、[ユーザー設定センター詳細表示エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/)を使用して、最終更新タイムスタンプやユーザー設定センターIDなどの関連情報を返します。

## ユーザー設定センターをカスタマイズする {#customize-a-preference-center}

Brazeはユーザー設定センターからのサブスクリプション状態の更新を管理し、ユーザー設定センターを同期した状態に保ちます。ただし、以下のオプションで[サブスクリプショングループAPI]({{site.baseurl}}/api/endpoints/subscription_groups/)を使用して、独自のユーザー設定センターを作成・ホストすることもできます。

### オプション 1: 文字列クエリパラメーターを使用したリンク {#option-1-link-with-string-query-parameters}

URLの本文にクエリ文字列のフィールド値ペアを使用して、ユーザーIDとメールカテゴリをページに渡すことで、ユーザーは配信停止の選択を確認するだけで済みます。このオプションは、ユーザー識別子をハッシュ形式で保存しており、まだサブスクリプションセンターを持っていない場合に適しています。

このオプションでは、各メールカテゴリに固有の配信停止リンクが必要です:<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Liquidフィルターを使用して、送信時にユーザーのexternal IDをハッシュ化することも可能です。これにより、`user_id`がMD5ハッシュ値に変換されます。例:
{% raw %}
```liquid
{% assign my_string = ${user_id} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### オプション 2: JSON Webトークンによる認証 {#option-2-authenticate-with-json-web-token}

[JSON Webトークン](https://auth0.com/learn/json-web-tokens/)を使用して、通常はユーザー名とパスワードのログインなどの認証レイヤーの背後にあるWebサーバーの一部（アカウント設定など）にユーザーを認証します。

このアプローチでは、URLにクエリ文字列の値ペアを埋め込む必要はありません。これらはJSON Webトークンのペイロードで渡すことができます。例:

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": "offers"
}
```

## よくある質問 {#frequently-asked-questions}

### ユーザー設定センターを作成していないのに、ダッシュボードに「PreferenceCenterBrazeDefault」が表示されるのはなぜですか？ {#i-havent-created-a-preference-center-why-am-i-seeing-preferencecenterbrazedefault-on-my-dashboard}

これは、レガシーLiquid {%raw%}`${preference_center_url}`{%endraw%}が使用されている場合にユーザー設定センターをレンダリングするために使用されます。つまり、{%raw%}`${preference_center_url}`または`preference_center.${PreferenceCenterBrazeDefault}`{%endraw%}を参照するキャンバスステップやテンプレートは機能しません。これは、レガシーLiquidまたは「PreferenceCenterBrazeDefault」をメッセージの一部として含む以前に送信されたメッセージにも適用されます。

新しいメッセージで{%raw%}`${preference_center_url}`{%endraw%}を再度参照すると、「PreferenceCenterBrazeDefault」という名前のユーザー設定センターが再び作成されます。

### ユーザー設定センターは複数の言語をサポートしていますか？ {#do-preference-centers-support-multiple-languages}

いいえ。ただし、カスタムのオプトインおよびオプトアウトページのHTMLを記述する際にLiquidを活用できます。動的リンクを使用して配信停止を管理している場合、これは単一のリンクです。

たとえば、スペイン語を話すユーザーの配信停止率を追跡する場合、別々のCampaignを使用するか、Currentsに関する分析を活用する必要があります（ユーザーが配信停止した時期を確認し、そのユーザーの優先言語を確認するなど）。

別の例として、スペイン語を話すユーザーの配信停止率を追跡する場合、ユーザーの言語がスペイン語であれば配信停止URLに`?Spanish=true`のようなクエリパラメーター文字列を追加し、そうでなければ通常の配信停止リンクを使用できます:

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

その後、Currentsを通じて、どのユーザーがスペイン語を話し、その配信停止リンクに対するクリックイベントがいくつあったかを特定できます。

### 送信には配信停止リンクとメールユーザー設定センターの両方が必要ですか？ {#are-both-unsubscribe-links-and-email-preference-centers-required-for-sending}

いいえ。メールCampaignの作成時に「メール本文に配信停止リンクが含まれていません」というメッセージが表示される場合、配信停止リンクがコンテンツブロックに含まれている場合にこの警告が表示されることが想定されています。

### デフォルトのブラウザアイコンを更新するにはどうすればよいですか？ {#how-do-i-update-the-default-browser-icon}

デフォルトでは、ブラウザタブ名の横のアイコン（ファビコン）にはBrazeのロゴが使用されます。カスタムファビコンを追加するには、作成または更新の[ユーザー設定センターAPI呼び出し]({{site.baseurl}}/api/endpoints/preference_center/)で`links-tags`属性を介して設定します。Brazeはホストされたページに{% raw %}`<link rel="icon" ...>`{% endraw %}タグを挿入します。

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