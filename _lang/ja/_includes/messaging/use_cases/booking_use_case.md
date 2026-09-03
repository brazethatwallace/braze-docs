# ユースケース: 予約リマインダーメールシステム {#use-case-booking-reminder-email-system}

> Brazeは、プログラムで高度に制御できるように設計された包括的なカスタマーエンゲージメントプラットフォームです。このユースケースでは、予約システムなど、製品とマーケティングが交わるユースケースに適用できるBrazeの機能をいくつかご紹介します。

このユースケースでは、Brazeの機能を使用して予約リマインダーメールメッセージングサービスを構築する方法を説明します。このサービスを使用すると、ユーザーは予定を予約でき、次回の予定のリマインダーメッセージが送信されます。このユースケースではメールメッセージを使用しますが、ユーザープロファイルを一度更新するだけで、任意のチャネルまたは複数のチャネルでメッセージを送信できます。

このサービスを作成するその他の利点は次のとおりです。
- 送信されたメッセージは完全にトラッキングされ、レポートに含まれます。
- 技術的な知識を持たない会社ユーザーでもメッセージのコンテンツを更新できます。
- メッセージは、キャンペーンの設定に基づくユーザープロファイルのオプトインおよびオプトアウトステータスに従います。
- 予約データとメッセージのインタラクションデータの両方を使用して、ユーザーをセグメンテーションし、追加のメッセージングのターゲットにできます。例えば、最初のリマインダーメッセージを開封しなかったユーザーに対して、予約前に追加のリマインダーを送信してリターゲティングすることができます。

このユースケースを実現するには、次のステップに従ってください。
1. [次の予約データをBrazeユーザープロファイルに書き込む](#step-1)
2. [予約リマインダーメッセージを設定して起動する](#step-2)
3. [更新された予約とキャンセルを処理する](#step-3)

## ステップ 1: 次の予約データをBrazeユーザープロファイルに書き込む {#step-1}

予約が行われるたびに、Brazeの[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントを使用して、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)をユーザープロファイルに書き込みます。階層化カスタム属性には、リマインダーメッセージの送信とパーソナライズに必要な情報がすべて含まれていることを確認してください。このユースケースでは、階層化カスタム属性に「trips」という名前を付けます。

### 予約の追加 {#add-booking}

ユーザーが予約を作成する場合、オブジェクトの配列に次の構造を使用して、`/users/track`エンドポイント経由でデータをBrazeに送信します。

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": [
               {"trip_id":"1","name":"London Trip","start_date"{$time:"2025-11-11"}},
               {"trip_id":"2","name":"Sydney Trip","start_date"{$time:"2025-11-11"}}
           ]
       }
   ]
}
```
{% endraw %}

階層化カスタム属性「trips」は、ユーザープロファイルに次のように表示されます。

![ロンドン旅行とシドニー旅行の2つの階層化カスタム属性。]({% image_buster /assets/img/use_cases/2_nested_attributes.png %}){: style="max-width:70%;"}

### 予約の更新 {#update-booking}
ユーザーが予約を更新する場合、オブジェクトの配列に次の構造を使用して、`/users/track`エンドポイント経由でデータをBrazeに送信します。

{% raw %}
```json
{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$update:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value":"1",
                       "$new_object":{"trip_id":"1","name":"London Trip","start_date":{"$time":"2025-11-11"}}
                   }
               ]
           }
       }
 ]
}
```
{% endraw %}

### 予約の削除 {#remove-booking}

{% tabs %}
{% tab /users/track endpoint %}
#### `/users/track`エンドポイント経由でデータを送信する {#send-data-through-the-userstrack-endpoint}
ユーザーが予約を削除する場合、オブジェクトの配列に次の構造を使用して、`/users/track`エンドポイント経由でデータをBrazeに送信します。

{% raw %}
```json

{
 "attributes": [
       {
           "external_id": "test-user",
           "_merge_objects": true,
           "trips": {
               "$remove:":[
                   {
                       "$identifier_key":"trip_id",
                       "$identifier_value": "1"
                   }
               ]
           }
       }
   ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}
#### SDKを通じて階層化属性をユーザープロファイルに書き込む {#write-nested-attributes-to-user-profiles-through-the-sdk}

アプリ、Webサイト、またはその両方で予約を収集し、そのデータをユーザープロファイルに直接書き込む場合は、Braze SDKを使用してこのデータを送信できます。以下はWeb SDKを使用した例です。

{% raw %}
```json
const json = [{
  "id": 1,
  "name": "London Trip",
  "start_date": {"$time”: “2025-05-08”}
}, {
  "id": 1,
  "name": "Sydney Trip",
  "start_date": {"$time”: “2025-11-11”}
}];
braze.getUser().setCustomUserAttribute("trips", json);
```
{% endraw %}
{% endtab %}
{% endtabs %}

Brazeはユーザープロファイルの階層化カスタム属性から指定された予約を削除し、残りの予約を表示します。

![ロンドン旅行の階層化カスタム属性。]({% image_buster /assets/img/use_cases/1_nested_attribute.png %}){: style="max-width:70%;"}

## ステップ 2: 予約リマインダーメッセージを設定して起動する {#step-2}

### ステップ 2a: ターゲットオーディエンスを作成する {#step-2a-create-a-target-audience}

複数条件のセグメンテーションを使用して、リマインダーを受信するターゲットオーディエンスを作成します。例えば、予約日の2日前にリマインダーを送信する場合は、次のように選択します。

- 開始日まで**1日超**かつ
- 開始日まで**2日以内**

![開始日が1日以上かつ2日未満という条件を持つ、階層化カスタム属性「trips」。]({% image_buster /assets/img/use_cases/custom_nested_attribute.png %})

### ステップ 2b: メッセージを作成する {#step-2b-create-your-message}

[カスタムHTMLを使用したメールの作成]({{site.baseurl}}/user_guide/channels/email/html_editor)のステップに従って、リマインダーメールメッセージを作成します。この例のように、Liquidを使用して、作成したカスタム顧客属性（「trips」）のデータでメッセージをパーソナライズします。

{% raw %}
```liquid
{% assign dates = {{custom_attribute.${trips}}} %}
{% assign today = "now" | date: "%s" %}
{% assign two_days = today | plus: 172800 | date: "%F" %}
You have the following booked in 2 days! Check the information below:
{% for date in dates %}
{% if date.start_date == two_days %}
{{date.trip_id}}
{{date.name}}
{% endif %}
{% endfor %}
```
{% endraw %}

### ステップ 2c: キャンペーンを起動する {#step-2c-launch-your-campaign}

リマインダーメールメッセージのキャンペーンを起動します。Brazeが「trips」カスタム属性を受信するたびに、該当する予約オブジェクトに含まれるデータに基づいてメッセージをスケジュールします。

## ステップ 3: 更新された予約とキャンセルを処理する {#step-3}

リマインダーメッセージの送信を開始したら、予約が更新またはキャンセルされたときに送信する確認メッセージを設定できます。

### ステップ 3a: 更新データを送信する {#step-3a-send-updated-data}

{% tabs %}
{% tab /users/track %}

#### `/users/track`エンドポイント経由でデータを送信する
ユーザーが予約を更新またはキャンセルしたときにカスタムイベントを送信するには、Brazeの[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントを使用します。このイベントでは、変更を確認するために必要なデータをイベントプロパティに含めます。

このユースケースでは、ユーザーがシドニー旅行の日付を更新したとします。イベントは次のようになります。

{% raw %}
```json
{
  "events": [
    {
      "external_id": "user_id",
      "name": "trip_updated",
      "time": "2025-03-07T08:19:23+01:00",
      "properties": {
        "id": 2,
        "name": "Sydney Trip",
        "old_time": "2025-11-12"
        "new_time": "2026-01-21"
      }
    }
  ]
}
```
{% endraw %}
{% endtab %}
{% tab SDK %}

#### SDK経由でユーザープロファイルに階層化属性を書き込む

SDK経由でカスタムイベントをユーザープロファイルに送信します。例えば、Web SDKを使用している場合は、次のように送信できます。

{% raw %}
```json
braze.logCustomEvent("trip_updated", {
  id: 2,
  name: "Sydney Trip",
  old_time: "2025-11-12",
  new_time: "2026-01-21"
});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### ステップ 3b: 更新を確認するメッセージを作成する {#step-3b-create-a-message-to-confirm-the-update}

[アクションベースのキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)を作成して、更新された予約の確認をユーザーに送信します。[Liquidを使用してイベントプロパティをテンプレート化]({{site.baseurl}}/user_guide/data/activation/events/custom_events)し、予約の名前、以前の時刻、新しい時刻（キャンセルの場合は名前のみ）をメッセージ自体に反映できます。

例えば、次のようなメッセージを作成できます。

{% raw %}
```liquid
Hi {{${first_name}}}, you have successfully updated the date of your trip, {{event_properties.${name}}}, from {{event_properties.${old_time}}} to {{event_properties.${new_time}}}
```
{% endraw %}

### ステップ 3c: 更新を反映するようにユーザープロファイルを変更する {#step-3c-modify-the-user-profile-to-reflect-the-update}

最後に、最新のデータに基づいてステップ1および2の予約リマインダーを送信するために、階層化カスタム属性を更新して予約の変更またはキャンセルを反映します。

#### 予約の更新 {#updated-booking}

このユースケースのユーザーがシドニー旅行を更新した場合、`/users/track`エンドポイントを使用して、次のようなコールで日付を変更します。

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "trips": {
	  "$update": [
	    {
            "$identifier_key": "id",
            "$identifier_value": 2,
            "$new_object": {
              "start_date": "2026-01-21"
            }
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

#### 予約のキャンセル {#cancelled-booking}

このユースケースのユーザーがシドニー旅行をキャンセルした場合、`/users/track`エンドポイントに次のコールを送信します。

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "trips": {
	  "$remove": [
	   {
            "$identifier_key": "id",
            "$identifier_value": 2
          }
         ]
      }
    }
  ]
}
```
{% endraw %}

これらのコールが送信されてユーザープロファイルが更新されると、予約リマインダーメッセージにユーザーの予約日に関する最新のデータが反映されます。