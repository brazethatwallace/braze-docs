---
nav_title: Zoom登録の自動化
article_title: Zoom登録の自動化
page_order: 1
page_type: tutorial
description: "この記事では、メール、プッシュ、アプリ内メッセージキャンペーンでZoomの参加者登録を自動化する方法について説明します。"
channel:
  - email
  - push
  - in-app messages

---

# Zoom登録の自動化 {#automate-zoom-registration}

> ウェビナーは、ここ数年でBrazeの顧客がホストする一般的な手段となっています。Zoomウェビナーをホストする場合、ユーザーはZoomのランディングページで情報を入力してサインアップする必要があります。

推奨されるユーザーフローは以下のとおりです。
1. Zoomでウェビナーをスケジュールし、`webinarId`を生成します。
2. Brazeを使用して、メール、プッシュ、アプリ内メッセージチャネルを通じてZoomウェビナーを宣伝します。
3. これらのコミュニケーションにコールトゥアクションボタンを含め、ユーザーを自動的にウェビナーに追加します。

これは、[Zoom API](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate)を使用して、メール、プッシュ、またはアプリ内メッセージ内のボタンクリックでユーザーをウェビナーに自動的に追加することで実現できます。以下のエンドポイントを使用し、APIリクエスト内のウェビナーIDを置き換えてください。

POST: `/meetings/{webinarId}/registrants`

詳細については、Zoomの[ウェビナー登録者追加エンドポイント](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate)を参照してください。<br><br>

{% tabs %}
{% tab メール %}

メッセージ本文にコールトゥアクションボタンを含むメールキャンペーンを作成します。ユーザーがボタンをクリックすると、ウェビナーのランディングページにリダイレクトされます（リダイレクトリンクに適切なパラメーターを含めます）。

URL内のパラメーターを使用してユーザーデータを渡し、ページが読み込まれたときにAPIコールを実行してユーザーをウェビナーに追加します。

![Liquidテンプレートを使用して名、姓、メールアドレス、市区町村を含むメールメッセージ。]({% image_buster /assets/img/zoom/zoom1.png %})

ユーザーは、Brazeプロファイルに既に存在する詳細情報でウェビナーに登録されます。

{% endtab %}
{% tab プッシュ %}

1. プッシュキャンペーンを作成します<br><br>

	ボタンのクリック時の動作を、ウェビナーのランディングページへのリンクに設定します。<br>

	![ボタンがクリックされたときにウェビナーにリンクする設定。]({% image_buster /assets/img/zoom/zoom2.png %})<br><br>

	プッシュのボタンクリックでサインアップしたユーザー向けのランディングページのシンプルな例です。ユーザーにサインアップ内容を知らせ、登録を確認します。<br>

	![Brazeからサインアップした後に表示されるウェビナー確認ランディングページ。]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. アプリ内メッセージまたはボタンクリックによってトリガーされるWebhookキャンペーンを作成します。<br><br>
 	Brazeプロファイルの既存のユーザーデータを使用して、ユーザーをウェビナーに登録します。<br>

	![特定のキャンペーンのボタンをクリックしたユーザーに送信されるアクションベースのキャンペーン。]({% image_buster /assets/img/zoom/zoom6.png %})<br><br>

	ZoomエンドポイントへのWebhookコールの例。<br>
	{% raw %}
	```http
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. ユーザーは、Brazeプロファイルに既に存在する詳細情報でウェビナーに登録されます。

{% endtab %}
{% tab アプリ内メッセージ %}

1. アプリ内メッセージキャンペーンを作成します<br><br>

	ボタンのクリック時の動作を、ウェビナーのランディングページへのリンクに設定します。<br>

	![ボタンがクリックされたときにウェビナーにリンクする設定。]({% image_buster /assets/img/zoom/zoom3.png %})<br><br>

	アプリ内メッセージのボタンクリックでサインアップしたユーザー向けのランディングページのシンプルな例です。ユーザーにサインアップ内容を知らせ、登録を確認します。<br>

	![Brazeからサインアップした後に表示されるウェビナー確認ランディングページ。]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. アプリ内メッセージまたはボタンクリックによってトリガーされるWebhookキャンペーンを作成します。<br><br>
	Brazeプロファイルの既存のユーザーデータを使用して、ユーザーをウェビナーに登録します。<br>

	![特定のキャンペーンのボタンをクリックしたユーザーに送信されるアクションベースのキャンペーン。]({% image_buster /assets/img/zoom/zoom5.png %})<br><br>

	ZoomエンドポイントへのWebhookコールの例。<br>
	{% raw %}
	```http
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. ユーザーは、Brazeプロファイルに既に存在する詳細情報でウェビナーに登録されます。

{% endtab %}
{% endtabs %}