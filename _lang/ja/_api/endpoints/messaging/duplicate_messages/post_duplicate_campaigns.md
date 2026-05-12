---
nav_title: "POST: Campaignの複製"
article_title: "POST: Campaignの複製"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "この記事では、Campaignの複製エンドポイントについて詳しく説明します。"

---
{% api %}
# APIを使用してCampaignを複製する {#duplicate-campaigns-using-the-api}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> このエンドポイントを使用して、Campaignを複製します。このAPIエンドポイントは、[BrazeダッシュボードでCampaignを複製する][1]のと同様です。

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`campaigns.duplicate` 権限を持つAPIキーを生成する必要があります。

## レート制限 {#rate-limit}

このエンドポイントは、1分あたり100回のAPI呼び出しに制限されています。

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
  "tag_names": (optional, string) The tags of the resulting campaign,
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | 必須 | 文字列 | [Campaign識別子]({{site.baseurl}}/api/identifier_types/)を参照してください。 |
| `name` | 必須 | 文字列 | 作成されるCampaignの名前。 |
| `description` | オプション | 文字列 | 作成されるCampaignの説明フィールド。 |
| `tag_names` | オプション | 文字列 | 作成されるCampaignのタグ。既存のタグである必要があります。リクエストに新しいタグを追加すると、元のCampaignにあったタグが上書きされます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## 応答 {#response}

このエンドポイントは `202` ステータスコードを返し、Campaignの作成は非同期で行われます。[セキュリティイベントのダウンロード][2]を使用して、Campaignがいつ複製されたか、どのAPIキーによって複製されたかの記録を確認できます。


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report

{% endapi %}