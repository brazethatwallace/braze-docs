---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "この参考記事では、BrazeとTransifexのパートナーシップについて説明します。Transifexはローカライゼーションプラットフォームであり、翻訳を自動化することで、チームが優れたカスタマーエクスペリエンスの提供に集中できるようにします。"
page_type: partner
search_tag: Partner

---

# Transifex

> [Transifex](https://www.transifex.com/)は、言語に関係なく、ユーザー群全体で堅牢なローカライゼーションを可能にします。

_この統合はTransifexによって管理されています。_

## 統合について {#about-the-integration}

BrazeとTransifexの統合では、コネクテッドコンテンツを使用してリソース文字列コレクションを取得し、言語ベースの条件付き書式の行ではなく、関連する翻訳をメッセージに含めることができます。これにより翻訳が自動化され、チームは優れたカスタマーエクスペリエンスの提供に集中できます。

{% alert important %}
2022年4月7日をもって、TransifexはAPIバージョン2および2.5を廃止し、バージョン3に移行しました。v2およびv2.5は動作しなくなり、関連するリクエストは失敗します。<br><br>以下の統合手順はバージョン3のアップデートを反映しています。コネクテッドコンテンツの呼び出しを適宜更新してください。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Transifexアカウント | このパートナーシップを利用するには、[Transifexアカウント](https://www.transifex.com/signin/)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Transifex統合では、Transifexの[リソース翻訳API](https://developers.transifex.com/reference/get_resource-translations)を使用します。次のcURLを使用すると、アカウントに翻訳に関連付けられたコンテンツ値があるかどうかを確認できます。

まず、Transifexアカウントにある`<ORGANIZATION_NAME>`、`<PROJECT_NAME>`、`<RESOURCE_NAME>`を入力します。次に、`<LANGUAGE>`を翻訳をフィルタリングしたい言語コードに、`<TRANSIFEX_BEARER_TOKEN>`をTransifexの[ベアラートークン](https://developers.transifex.com/reference/api-authentication)に置き換えます。

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSIFEX_BEARER_TOKEN>'
```

たとえば、Transifexプロジェクトが`https://www.transifex.com/appboy-3/french2/french_translationspo/`にある場合、`project_name`は「french2」になり、`resource_name`は「french_translationspo」になります。

## コネクテッドコンテンツメッセージの例 {#connected-content-message-example}

このコード例は、Transifexリソース翻訳APIとユーザーの`language`属性を利用しています。必要に応じて文字列オブジェクトをループし、次のLiquidを使用して関連するコンテンツを取得できます: `{{strings.data[X].attributes.strings.other}}`。

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}


[16]: [success@braze.com](mailto:success@braze.com)