---
nav_title: 12月
page_order: 0
noindex: true
page_type: update
description: "この記事には2021年12月のリリースノートが含まれています。"
alias: "/help/release_notes/2022/january/"
---
# 2021年12月 {#december-2021}

## セグメントごとのユーザーエクスポートエンドポイントの更新 {#update-to-export-users-by-segment-endpoint}

2021年12月より、[セグメントごとのユーザーエクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)に以下の変更が適用されます。

1. このAPIリクエストの`fields_to_export`フィールドは必須となります。すべてのフィールドをデフォルトにするオプションは削除されます。
2. `custom_events`、`purchases`、`campaigns_received`、`canvases_received`のフィールドには、過去90日間のデータのみが含まれます。

## Currentsメッセージエンゲージメントイベントの新しいプロパティ {#new-properties-for-currents-message-engagement-events}

一部の[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)に新しいプロパティが追加されました。この更新は、以下のCurrentsメッセージエンゲージメントイベントと、それらを使用するすべてのパートナーに適用されます。

- `LINK_ID`、`LINK_ALIAS`を以下に追加：
  - メールクリック（すべての送信先）
- `USER_AGENT`を以下に追加：
  - メール開封
  - メールクリック
  - スパムとしてマーク
- `MACHINE_OPEN`を以下に追加：
  - メール開封

## 新しいLiquidパーソナライゼーションタグ {#new-liquid-personalization-tag}

以下のLiquidタグを使用して、デバイスでフォアグラウンドプッシュが有効になっているユーザーへのターゲット設定をサポートするようになりました。

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

詳細については、[サポートされるパーソナライゼーションタグ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)を参照してください。

## Webhookについて {#about-webhooks}

Webhookは強力で柔軟なツールですが、少しわかりにくいかもしれません。Webhookとは何か、Brazeでどのように使用できるかについて知りたい場合は、[Webhookについて]({{site.baseurl}}/about_webhooks/)の新しい記事をご覧ください。

## Amazon Personalize

Amazon Personalizeは、Amazonの機械学習によるレコメンデーションシステムを終日利用できるようなものです。20年以上にわたるレコメンデーションの経験に基づき、Amazon Personalizeは、リアルタイムでパーソナライズされた商品やコンテンツのレコメンデーション、およびターゲットを絞ったマーケティングプロモーションを提供することで、カスタマーエンゲージメントを向上させます。

さらに詳しく知りたい方は、[Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize/)の新しい記事をご覧いただき、Amazon Personalizeが提供するユースケース、扱うデータ、サービスの設定方法、Brazeとの統合方法についてご確認ください。

## 新しいBrazeパートナーシップ {#new-braze-partnerships}

### Yotpo - eコマース {#yotpo-ecommerce}

[Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/)とBrazeの統合により、Braze内のメールやその他の通信チャネルで、製品の星評価、トップレビュー、視覚的なユーザー生成コンテンツを動的に取得して表示できます。また、顧客レベルのロイヤルティデータをメールやその他のコミュニケーション手段に組み込むことで、よりパーソナライズされたインタラクションを実現し、売上とロイヤルティを高めることができます。

### Zeotap - 顧客データプラットフォーム {#zeotap-customer-data-platform}

[Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/)とBrazeの統合により、Zeotapの顧客セグメントを同期してZeotapのユーザーデータをBrazeのユーザーアカウントにマッピングすることで、キャンペーンの規模とリーチを拡張できます。このデータに基づいてアクションを起こし、ユーザーにパーソナライズされたターゲット体験を提供することができます。