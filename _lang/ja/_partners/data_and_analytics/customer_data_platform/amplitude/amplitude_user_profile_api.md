---
nav_title: Amplitudeとコネクテッドコンテンツ
article_title: Amplitudeとコネクテッドコンテンツ
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "AmplitudeのUser Profile APIは、Amplitudeユーザープロファイルを提供します。これには、ユーザープロパティ、計算されたユーザープロパティ、ユーザーを含むコホートのコホート IDのリスト、およびおすすめが含まれます。"
search_tag: Partner

---

# Amplitudeとコネクテッドコンテンツ {#amplitude-and-connected-content}

> AmplitudeのUser Profile APIは、Amplitudeユーザープロファイルを提供します。これには、ユーザープロパティ、計算されたユーザープロパティ、ユーザーを含むコホートのコホート IDのリスト、およびおすすめが含まれます。以下に、コネクテッドコンテンツで使用できる一般的なAmplitude APIエンドポイントを示します。

## エンドポイントパラメーター {#endpoint-parameters}

以下の表は、User Profile APIの呼び出しで使用できるパラメーターを示しています。

| パラメーター | 必須 | 説明 |
| --------- | -------- | ----------- |
| `user_id` | オプション | クエリ対象のユーザー ID（外部データベース ID）。`device_id` が設定されていない場合は必須です。 |
| `device_id` | オプション | クエリ対象のデバイス ID（匿名 ID）。`user_id` が設定されていない場合は必須です。 |
| `get_recs` | オプション<br>(デフォルトは false) | このユーザーのおすすめ結果を返します。 |
| `rec_id` | オプション | 取得するおすすめ。`get_recs` が true の場合は必須です。複数のおすすめを取得するには、`rec_ids` をカンマで区切って指定します。 |
| `rec_type` | オプション | デフォルトの実験的コントロール設定を上書きします。`rec_type=model` はモデル化されたおすすめを返し、`rec_type=random` はランダムなおすすめを返します。将来的にはその他のオプションが導入される可能性があります。 |
| `get_amp_props` | オプション<br>(デフォルトは false) | このユーザーの、計算を含まないユーザープロパティの完全なセットを返します。 |
| `get_cohort_ids` | オプション<br>(デフォルトは false) | このユーザーが所属し、追跡するよう設定されているすべてのコホート IDのリストを返します。デフォルトでは、どのコホートについてもユーザーのコホートメンバーシップは追跡されません。 |
| `get_computations` | オプション<br>(デフォルトは false) | このユーザーに対して有効になっているすべての計算のリストを返します。 |
| `comp_id` | オプション | このユーザーで有効になっている可能性のある単一の計算を返します。存在しない場合は null 値を返します。`get_computations` が true の場合、この値を含むすべての値がフェッチされます（アーカイブまたは削除されていない限り）。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

以下の表は、Amplitudeの応答で最もよく見られるパラメーターを示しています。

| 応答パラメーター | 説明 |
| ------------------ | ----------- |
| `rec_id` | リクエストされたおすすめ ID。 |
| `child_rec_id` | Amplitudeがモデルパフォーマンス向上のための内部実験の一部としてバックエンドで使用する可能性がある、より詳細なおすすめ ID。ほとんどの場合、これは `rec_id` と同じです。 |
| `items` | このユーザーへのおすすめリスト。 |
| `is_control` | このユーザーがコントロールグループに属している場合は true。 |
| `recommendation_source` | このおすすめの生成に使用されたモデルの名前。 |
| `last_updated` | このおすすめが最後に生成され、同期されたときのタイムスタンプ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

## 一般的なAmplitudeエンドポイント {#common-amplitude-endpoints}

### おすすめを取得する {#get-a-recommendation}

#### エンドポイント {#endpoint}
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### レスポンス例 {#example-response}
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### 複数のおすすめを取得する {#get-multiple-recommendations}

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### レスポンス例
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### ユーザープロパティを取得する {#get-user-properties}

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### レスポンス例
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### コホート IDを取得する {#get-cohort-ids}

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### レスポンス例
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### 単一の計算を取得する {#get-a-single-computation}

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### レスポンス例
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### すべての計算を取得する {#get-all-computations}

#### エンドポイント
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### レスポンス例
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

