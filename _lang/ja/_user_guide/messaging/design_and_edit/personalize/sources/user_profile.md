---
nav_title: ユーザープロファイル
article_title: ユーザープロファイル
page_order: 0
description: "標準属性項目、カスタム属性、イベントプロパティなど、ユーザープロファイルデータを使用してメッセージをパーソナライズする方法を説明します。"
---

# ユーザープロファイル {#user-profile}

> 標準属性項目、カスタム属性、イベントプロパティなど、各ユーザーのプロファイルに保存されたデータを使用してメッセージをパーソナライズできます。Brazeでは、メッセージコンテンツに直接挿入できる[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)タグを通じてこのデータを利用できます。

## 標準属性項目 {#standard-attributes}

{% raw %}
標準属性項目は、Brazeが自動的に追跡する定義済みのプロファイルフィールドで、`{{${first_name}}}`、`{{${email_address}}}`、`{{${city}}}`などがあります。これらの属性は一貫した命名規則に従っているため、追加の設定なしにどのメッセージでも参照できます。

たとえば、ユーザーの名でメッセージを始めるには次のようにします。

```liquid
Hi {{${first_name} | default: 'there'}}, check out our latest picks for you!
```
{% endraw %}

標準属性項目タグの完全なリストについては、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を参照してください。

## カスタム属性 {#custom-attributes}

{% raw %}
カスタム属性は、ロイヤルティティア、お気に入りカテゴリ、アカウントタイプなど、ワークスペース固有のプロファイルフィールドです。`{{custom_attribute.${attribute_name}}}`タグを使用して参照します。

たとえば、ユーザーの会員ティアに基づいてメッセージをパーソナライズするには次のようにします。

```liquid
{% if custom_attribute.${membership_tier} == 'gold' %}
  As a Gold member, you get early access to our new collection.
{% else %}
  Upgrade your membership for early access to new collections.
{% endif %}
```
{% endraw %}

カスタム属性の作成と管理の詳細については、[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)を参照してください。

## イベントプロパティ {#event-properties}

{% raw %}
CampaignまたはCanvasがカスタムイベントや購入によってトリガーされると、そのイベントのプロパティをパーソナライゼーションに使用できます。`{{event_properties.${property_name}}}`を使用して参照します。

たとえば、カスタムイベント`completed_purchase`に`product_name`プロパティが含まれている場合は次のようにします。

```liquid
Thanks for purchasing {{event_properties.${product_name}}}! Your order is on its way.
```
{% endraw %}

イベントプロパティは、アクションベースのCampaignおよびアクションベースのCanvasの最初のステップで使用できます。詳細については、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)を参照してください。

## APIトリガープロパティ {#api-trigger-properties}

{% raw %}
APIを通じてトリガーされるCampaignやCanvasesでは、トリガープロパティオブジェクトを使用して追加データを渡すことができます。これらの値は`{{api_trigger_properties.${property_name}}}`で参照します。

たとえば、次のようにします。

```liquid
Your verification code is {{api_trigger_properties.${verification_code}}}.
```
{% endraw %}

詳細については、[APIトリガープロパティオブジェクト]({{site.baseurl}}/api/objects_filters/trigger_properties_object)を参照してください。

## デバイス属性 {#device-attributes}

{% raw %}
ユーザーが最後に使用したデバイスの属性も参照できます。たとえば、`{{most_recently_used_device.${model}}}`はデバイスのモデル名を返し、`{{most_recently_used_device.${os}}}`はオペレーティングシステムを返します。
{% endraw %}

デバイス属性タグの完全なリストについては、[サポートされているパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information)を参照してください。

## デフォルト値の設定 {#setting-default-values}

特定のユーザーのプロファイルフィールドが空の場合、Brazeはデフォルトで空の文字列をレンダリングします。不完全に見えるメッセージを防ぐには、`default` Liquidフィルターを使用してフォールバック値を設定します。

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}},
```
{% endraw %}

詳細については、[デフォルト値の設定]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values)を参照してください。