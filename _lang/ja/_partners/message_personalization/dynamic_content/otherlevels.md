---
nav_title: OtherLevels
article_title: OtherLevels
alias: /partners/otherlevels/
description: "この記事では、OtherLevels Experience PlatformとBrazeの統合について説明します。"
page_type: partner
search_tag: OtherLevels

---

# OtherLevels

> [OtherLevels](https://www.otherlevels.com/) Experience Platformは、GenAIを活用して、従来のコンテンツをオンブランドのパーソナライズされた動画やリッチメディア体験に大規模に変換することで、スポーツブランド、パブリッシャー、オペレーターが顧客とつながる方法を変革します。

*この統合はOtherLevelsによって維持されています。*

## 概要 {#overview}

BrazeとOtherLevelsの統合により、OtherLevels Experience PlatformへのAPIコールを通じてカスタムGenAI動画を作成し、[Braze Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)を通じてこれらの動画をiOSプッシュ動画としてユーザーに送信できます。

OtherLevelsのAIを活用した体験で、ユーザーにより良いエクスペリエンスを提供しましょう。既存のコンテンツやサードパーティコンテンツを拡張性の高い動画やリッチメディアに変換し、すでに異なる方法でコンテンツを消費し、文脈に応じたパーソナライズされた体験に強く反応するオーディエンスに届けましょう。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| OtherLevelsアカウント | このパートナーシップを利用するには、OtherLevelsアカウントが必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

この統合では、Brazeからユーザーにメッセージを送信する前に、動画生成プロセスの一部としてOtherLevels Experience Platform APIを呼び出す必要があります。このドキュメントではcURLの例を提供していますが、APIコールを自動化するためにPostmanのようなAPIクライアントの使用を推奨します。

## ユースケース {#use-cases}

OtherLevels Experience Platformで作成したGenAI動画を使用して、以下を実現できます。
- スポーツオーナーやリーグ、ファンエンゲージメント、スポーツブック、iGaming、宝くじ向けに、より良い体験を創出する。
- テキストベースのコンテンツをリッチメディアや動画に変換し、人間的で魅力的な体験を創出することで、カスタマーマーケティングを強化する。
- 既存のBraze統合を再構築するのではなく拡張することで、獲得からリテンションまでの成果を向上させる。

## OtherLevels Experience Platformの統合 {#integrating-the-otherlevels-experience-platform}

### ステップ1：OtherLevels Experience Platform APIを呼び出して動画を生成する {#step-1}

統合の最初のステップでは、OtherLevels Experience Platform APIを呼び出して新しい動画を生成します。動画の生成は即時ではないことに注意してください。動画の長さや複雑さによっては、コンテンツの生成に最大30分かかる場合があります。メッセージングのスケジュールとAPIコールを適切に計画し、動画を生成するためのAPIコールがBrazeメッセージの送信予定時刻より十分前に行われるようにしてください。

{% alert important %}
以下のリクエストはcURLを使用しています。APIリクエストをより効率的に管理するには、PostmanのようなAPIクライアントの使用を推奨します。
{% endalert %}

APIコールの構成方法については、以下の例を参照してください。動画仕様のカスタマイズやAPIコールの構造についての詳細は、[GenAI動画のカスタマイズ](#customizing-the-genai-video)を参照してください。

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

以下を置き換えてください。

| プレースホルダー | 説明 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY` | OtherLevelsプロジェクトキーは、OtherLevelsアカウントのプロビジョニング時に提供されます。 |
| `BACKGROUND_IMAGE_URL` | 動画の背景用のHTTPS URL。 |
| `INSERT_TITLE` | 動画のタイトル。これは内部参照用であり、動画には表示されません。 |
| `TALENT_TEMPLATE` | タレントテンプレートID。OtherLevelsは、アカウントのプロビジョニング中にお客様と協力してタレント（アバター）を作成します。使用可能な1つまたは複数のタレントIDが提供されます。 |
| `TALENT_MODEL` | タレントモデルID。OtherLevelsは、アカウントのプロビジョニング中にお客様と協力してタレント（アバター）を作成します。使用可能な1つまたは複数のタレントモデルが提供されます。 |
| `INSERT_SCRIPT` | 動画の中でタレントに話させたい正確なスクリプト。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1：OtherLevels Experience Platform APIを呼び出して動画を生成する" }

APIレスポンスの一部として、OtherLevelsはAPIコールが成功したことを示すJSONペイロードを返します。JSONには、生成された動画を識別するための一意の`recipe_id`が含まれます。`recipe_id`は次のステップで必要になります。

以下はAPIからのレスポンスの例です。

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### ステップ2：`recipe_id`をカスタム属性として設定する {#step-2-setting-the-recipe_id-as-a-custom-attribute}

[ステップ1](#step-1)で受け取った`recipe_id`を、動画を送信したいユーザーのBrazeカスタム属性として設定します。

ユースケースによっては、大規模なオーディエンス向けに1本の動画を生成した場合、同じ`recipe_id`を複数のユーザーに設定できます。あるいは、それぞれ異なるユーザーをターゲットにした複数のユニークな動画を生成した場合は、各ユーザーにカスタム`recipe_id`をBrazeカスタム属性として設定する必要があります。

{% alert important %}
以下のリクエストはcURLを使用しています。APIリクエストをより効率的に管理するには、PostmanのようなAPIクライアントの使用を推奨します。
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

以下を置き換えてください。

| プレースホルダー | 説明 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT` | 現在のBrazeインスタンスのBraze RESTエンドポイントURL。詳細については、[REST APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys)を参照してください。 |
| `BRAZE_API_KEY` | `users.track`権限を持つBraze REST APIキー。 |
| `USER_ID` | この動画を受信するユーザーID。使用できる識別子の例については、[/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を参照してください。 |
| `RECIPE_ID` | [ステップ1](#step-1)でOtherLevels APIレスポンスから受け取った`recipe_id`。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ2：recipe_idをカスタム属性として設定する" }

### ステップ3：Braze Connected Contentで送信する {#step-3-sending-through-braze-connected-content}

GenAI動画をiOSプッシュメッセージとしてユーザーに送信するには、以下の手順に従います。

1. Braze iOSプッシュ通知キャンペーンを作成します。
2. キャンペーンの作成中に、**アセット**セクションに移動し、以下のConnected Content構文を**URLから追加**フィールドに貼り付けます。

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

次に、`OTHERLEVELS_PROJECT_KEY`をOtherLevelsが提供するプロジェクトキーに置き換えます。

{: start="3"}
3. **URLファイル形式**のドロップダウンで、**MP4**を選択します。
4. キャンペーンの残りの部分（メッセージ内容、送信スケジュール、ターゲットオーディエンスなど）を、希望する設定に基づいて構成します。

![Connected Contentのアセットフィールドの例。]({% image_buster /assets/img/otherlevels/1.png %})

## GenAI動画のカスタマイズ {#customizing-the-genai-video}

### 動画サイズと属性 {#video-size-and-attributes}

動画の背景は、`bg_image`キー内で指定できます。

| パラメーター | 説明 |
|-------------------------|----------------------------|
| `url` | 背景画像のHTTPS URL。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="動画サイズと属性" }

動画背景のサイズは、`resize_image`キー内で指定できます。背景画像は、ここで設定したものと同じサイズにすることを推奨します。

| パラメーター | 説明 |
|-------------------------|----------------------------|
| `width` | 背景画像の幅。縦向きと横向きの両方のオプションがあります。 |
| `height` | 背景画像の高さ。縦向きと横向きの両方のオプションがあります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="動画サイズと属性" }

動画オーバーレイオプションは、`image_video_overlay`キー内で指定できます。

| パラメーター | 説明 |
|-------------------------|----------------------------|
| `width` | オーバーレイの幅。縦向きと横向きの両方のオプションがあります。 |
| `height` | オーバーレイの高さ。縦向きと横向きの両方のオプションがあります。 |
| `color` | RGBで指定されたオーバーレイの色と透明度。 |
| `y_pos` | 中心からのY軸オフセット。 |
| `x_pos` | 中心からのX軸オフセット。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="動画サイズと属性" }

### タレントとスクリプト {#talent-and-script}

プロビジョニングの一環として、OtherLevelsはお客様と協力して、動画で使用する1つまたは複数のタレント（アバターと呼ばれることもあります）を生成します。ユースケースやブランドに応じて、既存のブランドアンバサダーの形で作成することも、ユニークなクリエーションとして作成することもできます。

これらが作成されると、APIで使用可能な`TALENT_TEMPLATE`と`TALENT_MODEL`のIDが提供されます。

入力スクリプトを処理するために使用される音声モデルは、人間が読むような自然なスクリプトを提供した場合に最も効果的に機能します。ほとんどの場合、手動でスクリプトを誘導するための追加の句読点は必要ありません。ただし、実際のオーディエンスに送信する前に、すべてのスクリプトをテストすることを推奨します。タレントがスクリプトを読む速度は、`talking_talent_speed`キー内で指定できます。

| パラメーター | 説明 |
|-------------------------|----------------------------|
| `speed` | タレントがスクリプトを読む速度を指定します。例：`1.5`。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="タレントとスクリプト" }

## その他の考慮事項 {#additional-considerations}

- iOSプッシュ通知プラットフォームのみが動画メディアをネイティブでサポートしています。Androidプッシュ通知は動画をネイティブでサポートしていないため、この統合はiOSオーディエンスにのみ使用できます。
- iOSデバイスで動画プッシュ通知を受信する場合、ユーザーは動画を読み込んで再生するためにプッシュ通知を長押しする必要があります。これはiOSプラットフォームの標準的な動作であり、カスタマイズすることはできません。