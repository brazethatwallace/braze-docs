---
nav_title: 開封ピクセルとクリックトラッキング
article_title: メールの開封ピクセルとクリックトラッキング
page_order: 9
page_type: reference
description: "この参照記事では、開封ピクセルとクリックトラッキングの実装方法について説明します。"

---

# メールの開封ピクセルとクリックトラッキング {#email-open-pixel-and-click-tracking}

> [開封ピクセルトラッキング]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#update-the-placement)とクリックトラッキングは、各ユーザープロファイルごとにオンまたはオフにできます。この柔軟性により、地域のプライバシー法に準拠できます。個々のユーザープロファイルがトラッキングを望まないことを示している場合にも対応できます。

## 開封ピクセルおよびクリックトラッキングの有効化 {#turning-on-open-pixel-or-click-tracking}

[API]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)、[CSV]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)、または[クラウドデータインジェスション (CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) を通じてユーザープロファイルをインポートまたは更新する際、以下の2つのフィールドを変更できます。

- `email_open_tracking_disabled`: `true` または `false` を指定します。`false` に設定すると、このユーザーに送信される今後のすべてのメールに開封トラッキングピクセルが追加されます。
- `email_click_tracking_disabled`: `true` または `false` を指定します。`false` に設定すると、このユーザーに送信される今後のメール内のすべてのリンクにクリックトラッキングが追加されます。

参考として、この情報はユーザープロファイルの**エンゲージメント**タブにあるメールの**連絡先設定**に反映されます。

![ユーザープロファイルのエンゲージメントタブにあるメールの開封およびクリックトラッキングピクセルフィールド]({% image_buster /assets/img_archive/open_click_user_profile.png %}){: style="max-width:60%;"}

## クリックトラッキングリンクの要件 {#click-tracking-link-requirements}

Brazeのクリックトラッキングは、`http://` または `https://` URLを使用するリンクのみを書き換えます。`mailto:` や `tel:` などの他のスキームを使用するリンクは、クリックトラッキングの対象外です。

電話番号やメールアドレスのクリックをトラッキングするには、`tel:` や `mailto:` の宛先に転送する `https://` リダイレクトURLを使用してください。

### クリックトラッキングURLパターン {#click-tracking-url-patterns}

メールサービスプロバイダー (ESP) がクリックトラッキングのためにリンクを書き換えると、生成されるURLにはクリックトラッキングドメインとESP固有のパスプレフィックスが使用されます。各ESPが生成するパターン（ファイアウォールルールやセキュリティ許可リストに必要）については、[クリックおよび開封トラッキングURLパターン]({{site.baseurl}}/user_guide/channels/email/email_setup/ssl#click-and-open-tracking-url-patterns)を参照してください。