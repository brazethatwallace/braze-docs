---
nav_title: ユーザー管理
article_title: LINE ユーザー管理
page_order: 0
description: "この記事では、LINE ユーザー ID とその設定方法について説明します。"
page_type: reference
channel:
 - LINE
alias: /line/user_management/
---

# LINE ユーザー管理 {#line-user-management}

> LINE ユーザー ID は、`native_line_id` というユーザープロファイル属性に保存され、LINE チャネルでユーザーにメッセージを送信するために使用されます。この記事では、`native_line_id` 属性の設定方法と確認方法について説明します。

顧客のユーザーデータは [Braze ユーザープロファイル]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)で表されます。ユーザープロファイルには、名やメールアドレスなど、会社のユーザーに関する情報と属性が保存されます。

Brazeを通じて LINE メッセージを送信する場合、Brazeは `native_line_id` 属性を使用して、メッセージの送信先ユーザーを特定します。LINE がBrazeに Webhook イベント（ユーザーがチャネルをフォローした場合やメッセージに返信した場合など）を送信すると、`native_line_id` を使用して対応するユーザープロファイルが検索されます。

{% alert note %}
LINE ユーザー ID は LINE プロバイダーごとに異なります。特定のユーザーは、フォローしているプロバイダーごとに異なる LINE ユーザー ID を持ちます。ユーザーは（メールアドレスや電話番号とは異なり）自分の LINE ID を知らない可能性が高く、フォローしているブランドごとに ID が変わるためです。
{% endalert %}

## `native_line_id` 属性の設定 {#setting-the-nativelineid-attribute}

ユーザープロファイルに `native_line_id` が設定されるシナリオはいくつかあり、以下に概要を示します。

| シナリオ | `native_line_id` を持つユーザープロファイルが存在するか | 結果 |
| --- | --- | --- |
| ユーザーが LINE チャネルをフォローする | いいえ | 匿名ユーザープロファイルが作成されます（マージが必要になります）:<br> - `native_line_id` にユーザーの LINE ID が設定される<br>- `line_id` ユーザーエイリアスにユーザーの LINE ID が設定される<br>- ユーザーがチャネルのBrazeサブスクリプショングループに登録される |
| ユーザーが LINE チャネルをフォローする | はい | `native_line_id` を持つすべてのユーザープロファイル:<br>- チャネルのBrazeサブスクリプショングループに登録される |
| 会社が `native_line_id` 列を含むユーザー CSV をアップロードする | いいえ | 指定された `external_id` またはユーザーエイリアスに対応するユーザープロファイルが存在しない場合:<br>- `native_line_id` に指定された値が設定される<br>- CSV で指定されたその他すべての属性がユーザープロファイルに設定される |
| 会社が `native_line_id` 列を含むユーザー CSV をアップロードする | はい | 指定された `external_id` またはユーザーエイリアスに対応するユーザープロファイルが存在する場合:<br>- `native_line_id` に指定された値が設定される<br>- CSV で指定されたその他すべての属性がユーザープロファイルに設定される<br>- 複数のプロファイルが同じ `native_line_id` を持つ |
| 会社が `/users/track` エンドポイントを使用して `native_line_id` 属性を指定する | いいえ | 指定されたユーザー（[`external_id`、`user_alias`、`braze_id`、または `email` で指定]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens)）に対応するユーザープロファイルが存在しない場合:<br>- `native_line_id` に指定された値が設定される<br>- リクエストで指定されたその他すべての属性がユーザープロファイルに設定される |
| 会社が `/users/track` エンドポイントを使用して `native_line_id` 属性を指定する | はい | 指定されたユーザー（[`external_id`、`user_alias`、`braze_id`、または `email` で指定]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens)）に対応するユーザープロファイルが存在する場合:<br>- `native_line_id` に指定された値が設定される<br>- リクエストで指定されたその他すべての属性がユーザープロファイルに設定される<br>- 複数のプロファイルが同じ `native_line_id` を持つ |
| 会社がBrazeにサブスクリプションステータス同期ツールの実行をリクエストする | いいえ | LINE から返されたユーザー LINE ID に対応するユーザープロファイルがBrazeに存在しない場合、匿名ユーザープロファイルが作成されます:<br>- `native_line_id` にユーザーの LINE ID が設定される<br>- `line_id` ユーザーエイリアスにユーザーの LINE ID が設定される<br>- ユーザーがチャネルのBrazeサブスクリプショングループに登録される<br><br>同じ LINE ID を持つユーザーが後から作成された場合、重複ユーザーが発生しますが、両方とも正しい LINE サブスクリプションステータスを持ちます。このような場合、ユーザーマージによってユーザー群を整理できます。 |
| 会社がBrazeにサブスクリプションステータス同期ツールの実行をリクエストする | はい | LINE から返されたユーザー LINE ID に対応するユーザープロファイルがBrazeに存在する場合:<br>- ユーザーがチャネルのBrazeサブスクリプショングループに登録される |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Setting the nativelineid attribute" }

## `native_line_id` の確認 {#finding-the-nativelineid}

Brazeダッシュボードでユーザープロファイルを表示する際、**Engagement** タブ > **Contact Settings** セクション > **LINE** セクションに移動すると、`native_line_id` 属性が設定されているかどうかを確認できます。

`native_line_id` が設定されている場合、**LINE User ID** の下に表示されます。設定されていない場合は表示されません。

![Engagement タブの LINE 連絡先設定。]({% image_buster /assets/img/line/line_contact_settings.png %}){: style="max-width:50%;"}