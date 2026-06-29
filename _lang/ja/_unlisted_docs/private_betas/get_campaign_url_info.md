---
nav_title: "GET: Campaignのリンクエイリアス一覧"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "この記事では、リンクエイリアス一覧のBrazeエンドポイントについて詳しく説明します。"
---
{% api %}
# Campaignのリンクエイリアス一覧 {#list-link-alias-for-campaign}
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> このエンドポイントを使用して、特定のCampaignメッセージバリアントに設定されたリンクエイリアスを一覧表示します。

{% apiref postman %}  {% endapiref %}

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `campaign_id` | 必須 | 文字列 | [Campaign API識別子]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier)を参照してください。|
| `message_variation_id ` | 必須 | 文字列 | メッセージバリアントAPI識別子。これはCampaignの詳細ページの**API Identifier**セクションで確認できます。 |
| `includes_link_id` | オプション | 文字列 | 特定のリンク識別子（Brazeによって割り当てられたもの）または`null`。これは結果を特定の`link_id`でフィルタリングするために使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## リクエスト例 {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## 応答 {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### トラブルシューティング {#troubleshooting}

以下の表は、返される可能性のあるエラーと、それに関連するトラブルシューティング手順を示しています。

| エラー | トラブルシューティング |
| --- | --- |
| `Missing/Invalid Campaign ID` | Campaign API IDはAPI識別子である必要があります。これは[Campaigns一覧エクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)を使用するか、ダッシュボードにログインして確認できます。 |
| `Missing/Invalid Message Variant ID` | メッセージバリアントAPI IDはAPI識別子である必要があります。これは[Campaign詳細エクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)を使用するか、ダッシュボードにログインして確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}