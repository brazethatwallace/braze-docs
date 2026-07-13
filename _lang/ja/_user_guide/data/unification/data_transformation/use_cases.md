---
nav_title: ユースケース
article_title: Braze データ変換のユースケース
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze データ変換のユースケースをいくつか紹介します。"
---

# データ変換のユースケース {#data-transformation-use-cases}

> Braze データ変換と外部プラットフォーム例からのwebhookの組み合わせによる、以下のようなユースケースを検討してみましょう。

## リード創出 {#generating-leads}

自社のWebサイトで、リードを創出する Typeform フォームをホストしています。新規ユーザーがこのフォームに入力すると、次のことができます。
- Brazeで新規ユーザーを作成する。
- Brazeのメールリストに追加する。
- 回答のいくつかをBrazeのカスタム属性として同期する。回答は、将来に向けてパーソナライズされたメッセージングエクスペリエンスを強化できる貴重なファーストパーティデータであるためです。

## サービスチケットを開く {#opening-service-tickets}

顧客が Zendesk などのプラットフォームでカスタマーサービスチケットを開く場合には、次のことができます。
- Zendeskチケットが作成されたときに、Brazeにカスタムイベントを書き込む。
- Zendeskに否定的なCSATレーティングが提供されたときに、イベントプロパティ付きのカスタムイベントをBrazeに書き込む。

## Brazeとの連携 {#integrating-with-braze}

Brazeは、顧客インサイトおよびアンケートのプラットフォームである [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate) と連携しています。データ変換では、複数のカスタム属性を保存する既存の連携ではなく、1つの階層化カスタム属性の下にアンケートの回答を複数保存できます。

## HubSpotの連絡先属性を同期する {#sync-hubspot-contact-attributes}

HubSpotをCRMとして、Brazeをメッセージングに使用している場合、データ変換を使用してHubSpotのwebhookペイロードをBrazeの `/users/track` 更新に変換できます。

この例では、`external_id` の有無を確認し、受信したユーザーオブジェクトをコピーして、含まれるすべてのフィールドをカスタム属性としてBrazeに送信します。

```
function toBrazeTrackPayload(userObject) {
  if (!userObject.external_id) {
    throw new Error("Braze requires an 'external_id' field.");
  }

  return {
    attributes: [userObject]
  };
}

const brazePayload = toBrazeTrackPayload(payload);
return brazePayload;
```

## 変換コードの例 {#example-transformation-code}

アンケートプラットフォームである Typeform から、アンケートの回答を受信するたびに送信される以下のサンプルペイロードを考えてみましょう。

![変換コードの例に関連するスクリーンショット。]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab 基本的な変換 %}

この例では、アンケートの回答を属性として取得し、アンケートが完了したことを示すイベントを書き込みます。

```
return {
  "attributes": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab 高度な変換 %}

基本的な変換の例をさらに発展させ、`if` ステートメントを導入して、いずれかの回答に基づいてユーザーを分類します。

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}