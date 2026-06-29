---
nav_title: APIのユースケース
article_title: APIのユースケース
description: "このリファレンス記事は、熟練した開発者であっても、最小限の開発者リソースしか持たないマーケターであっても、Braze REST APIのパワーを活用してさまざまなタスクを達成し、カスタマーエンゲージメント戦略を強化する方法を理解するのに役立つように設計されています。"
page_type: reference
page_order: 4.8
---

# APIのユースケース {#api-use-cases}

> [Braze REST API]({{site.baseurl}}/api/basics)は、カスタマーエンゲージメント戦略の管理と最適化を支援するために設計された幅広いエンドポイントを提供します。この記事では、カタログ、メールリストとアドレス、エクスポート、メッセージ、ユーザー設定センター、SMS、サブスクリプショングループ、テンプレート、ユーザーデータなど、各エンドポイントコレクションのユースケースをいくつか紹介します。<br><br>各セクションでは、ステップバイステップのガイド、コードサンプル、期待される結果とともにシナリオを紹介します。この記事を読み終わる頃には、カスタマーエンゲージメント活動を強化するためのBraze REST APIの使い方をより深く理解できるようになります。

## カタログの複数のアイテムを削除する {#deleting-multiple-items-in-a-catalog}

キッチン用品を専門とする小売ブランドKitchenerieは、新年を迎えて新商品を発表しました。Brazeダッシュボードでは、Kitchenerieの食器コレクション用に「Dishware」というカタログが設定されています。今年は以下の製品を食器コレクションから削除することになりました。

* Plain Bisque
* Pearl Porcelain
* Pink Shimmer

これらの製品をカタログから削除するには、Kitchenerieは[`/catalogs/{catalog_name}/items` エンドポイント]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk)を使用してアイテムIDを渡すことができます。

リクエストの例を以下に示します。

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/dishware/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "plainbisque"},
    {"id": "pearlporcelain"},
    {"id": "pinkshimmer"}
  ]
}'
```

このペイロードを送信すると、レスポンスにより、BrazeがKitchenerieの食器カタログから3つのコレクションを正常に削除したことが確認されます。

```json
{
  "message": "success"
}
```

## Brazeのスパムリストからメールを削除する {#removing-emails-from-the-braze-spam-list}

ストリーミングサービス会社のMovieCanonでは、開発者チームが定期的にメールリストを監査し、メールキャンペーンに登録しているユーザーを特定して維持する役割を担っています。この監査の一環として、MovieCanonは以下のメールリストをスパムリストから削除したいと考えています。

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

このタスクを達成するには、開発者チームは`/email/spam/remove` エンドポイントを使用するための`email.spam.remove` 権限を持つAPIキーが必要です。このエンドポイントは、Brazeのスパムリストと MovieCanonのメールプロバイダーが管理するスパムリストからメールアドレスを削除します。

このリクエストを送信するには、文字列のメールアドレスか、修正するメールアドレスを最大50件まで含む配列のいずれかを含めます。削除するメールのリストが50件以下であるため、MovieCanonは以下のリクエストボディでこのタスクを達成できます。

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

このペイロードを正常に送信すると、レスポンスにより、BrazeがMovieCanonのスパムリストからメールを削除したことが確認されます。

```json
{
  "message": "success"
}
```

## すべてのCanvasesを監査する {#auditing-all-canvases}

Siege Valley Healthは、数千人の患者を抱える10の稼働中の病院と研究センターからなる病院システムです。同社のマーケティングチームは、過去3年間にBrazeを使用してインフルエンザ予防接種の予約を促すために患者に送信したCanvasesを比較したいと考えています。Siege Valley Healthのマーケティングチームは、Canvasesのリストと分析サマリーの両方を素早く効率的に確認する方法も求めています。

Brazeダッシュボードでフィルタリングするのではなく、エンドポイントの組み合わせを使ってSiege Valley Healthがこの2つのタスクをどのように達成できるかを見てみましょう。

Canvasesを監査する最初のタスクとして、[`/canvas/list` エンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases)を使用して、名前とタグを含むCanvasesのリストをエクスポートします。リクエストの例を以下に示します。

{% details Siege Valley Healthのマーケティングチームが受け取るレスポンスは以下のとおりです。 %}
```json
{
  "canvases" : [
  	{
  		"id": "canvas_identifier_1",
  		"last_edited": "2020-07-10T23:59:59",
  		"name": "PatientReminder_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "2020"
      }
  	},
  	{
  		"id": "canvas_identifier_2",
  		"last_edited": "2020-07-30T23:59:59",
  		"name": "PatientReminder2_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "reminder", "2020"
      }
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```
{% enddetails %}

次に、Siege Valley HealthのCanvasesリストから最初のCanvasの分析サマリーを確認するタスクに移りましょう。そのためには、以下のリクエストパラメーターで[`/canvas/data_summary` エンドポイント]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary)を使用します。

* `canvas_id`: "canvas_identifier_2"
* `ending_at`: 2023-07-10T23:59:59
* `starting_at`: 2020-07-10T23:59:59

リクエストの例を以下に示します。

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## 今後スケジュールされているCampaignsとCanvasesを確認する {#checking-upcoming-scheduled-campaigns-and-canvases}

衣料品や美容製品をオンラインと店舗で販売する小売ブランドFlash & Threadにとって、最も忙しい時期が間もなく訪れます。同社のマーケティングチームは、2024年3月31日午後12時までに、Brazeダッシュボードから今後のCampaignsとCanvasesを確認したいと考えています。これは[`/messages/scheduled_broadcasts` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled)を使用して実現できます。

リクエストの例を以下に示します。

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

このエンドポイントは、今後のCampaignsとCanvasesのリストを返します。ここから、マーケティングチームはレスポンス内のCampaignsとCanvasesの`name` フィールドを参照することで、メッセージのリストを確認できます。

## 古いユーザー設定センターを表示する {#viewing-an-older-preference-center}

PoliterWeeklyはデジタル雑誌で、購読者にはメールで連絡を取ることができます。マーケティングチームは、購読者のユーザージャーニーをより深く理解するため、PoliterWeeklyのユーザー設定センターの詳細を確認し、いつ作成され、最後に更新されたかを調べたいと考えています。

[`/preference_center/v1/{preferenceCenterExternalID}` エンドポイント]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center)を使用すると、マーケティングチームはパスパラメーターとしてユーザー設定センターの外部IDを挿入するだけで済みます。以下のようになります。

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details PoliterWeeklyのマーケティングチームが受け取るレスポンスは以下のとおりです。 %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Braze updated your preferences successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

このレスポンスから、マーケティングチームはユーザー設定センターが最新の更新の3年前に作成されたことがわかります。この情報を踏まえて、マーケティングチームは新しいユーザー設定センターを作成して立ち上げることができます。

{% enddetails %}

## 無効な電話番号を削除する {#removing-invalid-phone-numbers}

CashBlastrの主な目標は、迅速な送金と受取りの方法を簡素化することです。金融サービス会社として、CashBlastrは顧客の電話番号リストを最新かつ正確な状態に保ちたいと考えています。開発者チームは、マーケティングチームのSMSメッセージがCashBlastrの適切な顧客に届くように、「無効」とマークされた以下の電話番号リストを削除するよう指示されています。

- 12223135467
- 12183095514
- 14235662245
- 14324567892

[`/sms/invalid_phone_numbers/remove` エンドポイント]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers)でリクエストを送信するには、電話番号は[e.164形式](https://en.wikipedia.org/wiki/E.164)の文字列の配列にする必要があり、リクエストごとに最大50件の電話番号を指定できます。リストが50件を超えないため、CashBlastrの開発者チームが送信するリクエストボディの例を以下に示します。

```http
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

このペイロードを送信すると、レスポンスにより、BrazeがCashBlastrの無効な電話番号をBrazeの無効リストから削除したことが確認されます。

```json
{
  "message": "success"
}
```

## ユーザーのサブスクリプショングループのステータスを表示する {#viewing-a-users-subscription-group-status}

SandwichEmperorは米国のクイックサービスレストランチェーンであり、マーケティングチームはランダムに選んだユーザーリストのSMS用サブスクリプショングループのステータスを確認したいと考えています。[`/subscription/status/get` エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)を使用すると、SandwichEmperorは以下のリクエスト例で個々のユーザーに対してこのタスクを実行できます。

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

このエンドポイントは、ユーザーのメールに関するサブスクリプショングループのステータスも一覧表示します。複数のユーザーのサブスクリプショングループのステータスを確認する際にも使用できます。

## メールメッセージング用のHTMLテンプレートを確認する {#checking-an-html-template-for-email-messaging}

WorkFriendsは、異なる業界の労働者間のつながりを構築するソーシャルネットワークであり、マーケティングチームがユーザーにメールキャンペーンを送信する役割を担っています。これらのキャンペーンには、地域イベントのリマインダー、毎週のニュースレター、プロフィール活動のハイライトなどが含まれることがよくあります。

このシナリオでは、WorkFriendsはこれまでレガシーブランディングで単一のHTMLテンプレートを使用してきました。ブランドアイデンティティの統一を図るため、WorkFriendsは新しいテンプレートに移行する前に、このHTMLテンプレートに活用できる有用な情報があるかどうかを確認したいと考えています。

{% details WorkFriendsチームが受け取るレスポンスは以下のとおりです。 %}

```json
{
  "email_template_id": "WorkFriends_Email_Template_ID",
  "template_name": "Promo template",
  "description": "Promo template",
  "subject": "WorkFriends Weekly Newsletter",
  "preheader": "Another week, another WorkFriends update",
  "body": "<!DOCTYPE html><html><head><title>WorkFriends Weekly Newsletter</title><style>body {font-family: Arial, sans-serif; color: #333;}.container {padding: 20px;}.header {background-color: #f2f2f2; padding: 10px; text-align: center;}.content {margin-top: 20px;}.footer {margin-top: 20px; font-size: 12px; text-align: center; color: #777;}</style></head><body><div class=\"container\"><div class=\"header\"><h2>WorkFriends Weekly Newsletter</h2></div><div class=\"content\"><p>Hello WorkFriends,</p><p>Welcome to another edition of our weekly newsletter. We've got some exciting updates and promos for you this week!</p><!-- Add more content here --><p>Don't forget to check out our latest promos and updates. Stay connected, stay informed!</p></div><div class=\"footer\"><p>Thank you for being a part of WorkFriends.</p><p>Unsubscribe | Update Preferences</p></div></div></body></html>",
  "tags": "promo",
  "created_at": "2020-07-10 13:00:00.000",
  "updated_at": "2024-02-04 17:00:00.000"
}
```

{% enddetails %}

このテンプレート情報を確認した後、WorkFriendsは[`/templates/email/update` エンドポイント]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template)を使用して、APIを通じてメールテンプレートを更新することもできます。Brazeダッシュボードのメールテンプレートにはこれらの編集内容が反映されます。