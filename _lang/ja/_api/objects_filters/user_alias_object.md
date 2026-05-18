---
nav_title: "ユーザーエイリアスオブジェクト"
article_title: APIユーザーエイリアスオブジェクト
page_order: 11
page_type: reference
description: "このリファレンス記事では、ユーザーエイリアスオブジェクトのさまざまなコンポーネントについて説明します。"

---

# ユーザーエイリアスオブジェクト {#user-alias-object}

> エイリアスは、代替のユニークなユーザー識別子として機能します。ユーザーエイリアスオブジェクトを使用することで、モバイルアプリやWebサイトにログインする前と後の両方で、特定のユーザーを追跡する分析用の一貫した識別子を設定できます。また、このオブジェクトを使用して、サードパーティベンダーが使用する識別子を会社ユーザーに追加し、外部とのデータ照合を容易にすることもできます。

ユーザーエイリアスオブジェクトは、識別子そのものを表す `alias_name` と、エイリアスのタイプを示す `alias_label` の2つの部分で構成されます。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つしか持つことができません。

このオブジェクトはすべてのエンドポイントで頻繁に使用され、他のオブジェクト内でもよく使用されます。

## オブジェクト本体 {#object-body}

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

| フィールド | データタイプ | 例 | 説明 |
|---|---|---|---|
| `alias_name` | 文字列 | `john_doe_123` | サードパーティシステムのIDなど、ユーザーのユニークな識別子です。この値は空でなく、236バイト以下である必要があります。 |
| `alias_label` | 文字列 | `crm_id` | エイリアスのタイプを定義する空でないカスタム文字列です。この値は特定のオプションに限定されません。`email_id`、`amplitude_id`、`salesforce_lead_id` など、ユースケースに合った任意の意味のあるラベルを使用できます。この値は236バイト以下である必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object body" }

### 例 {#example}

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "crm_id"
  },
  "external_id": "user_456"
}
```

この例では、`crm_id` はエイリアスがCRMシステムの識別子を表すことを示すカスタムラベルです。

### その他の例 {#additional-example}

```json
{
  "user_alias": {
    "alias_name": "a9f3c102",
    "alias_label": "amplitude_id"
  }
}
```

この例では、`amplitude_id` は使用可能なラベル値の1つです。`email_id` や `salesforce_lead_id` など、識別子スキームに合った他のカスタムラベルも使用できます。