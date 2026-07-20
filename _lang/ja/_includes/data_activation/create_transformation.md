Brazeダッシュボードで、**データ設定** > **データ変換**に移動します。

**変換を作成**を選択して変換に名前を付け、編集エクスペリエンスを選択します。

![編集エクスペリエンスとして「テンプレートを使用」または「ゼロから作成」を選択するオプションが表示された変換の詳細。]({% image_buster /assets/img/data_transformation/data_transformation10.png %}){: style="max-width:80%;"}

**テンプレートを使用**を選択すると、データ変換のユースケースを含むテンプレートライブラリーを参照できます。または、**ゼロから作成**を選択してデフォルトのコードテンプレートを読み込みます。

ゼロから作成する場合は、変換の送信先を選択します。テンプレートライブラリーからコードテンプレートを挿入することもできます。

{% details 送信先の詳細 %}
* **POST: Track users:** ソースプラットフォームからのWebhookを、属性、イベント、購入などのユーザープロファイル更新に変換します。
* **PUT: Update multiple catalog items:** ソースプラットフォームからのWebhookをカタログアイテムの更新に変換します。
* **DELETE: Delete multiple catalog items:** ソースプラットフォームからのWebhookをカタログアイテムの削除に変換します。
* **PATCH: Edit multiple catalog items:** ソースプラットフォームからのWebhookをカタログアイテムの編集に変換します。
* **POST: Send messages immediately via API Only:** ソースプラットフォームからのWebhookを変換し、指定したユーザーに即座にメッセージを送信します。
{% enddetails %}

{% alert note %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="additional templates or destinations" %}
{% endalert %}

変換を作成すると、変換の詳細ビューが表示されます。ここでは、**Webhookの詳細**の下にこの変換に対して受信した最新のWebhookが表示され、**変換コード**の下に変換コードを記述するスペースが表示されます。

{% if include.location == "typeform" %}

![Webhookの詳細と変換コードの例。]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

{% endif %}

次のステップで使用する**Webhook URL**をコピーします。