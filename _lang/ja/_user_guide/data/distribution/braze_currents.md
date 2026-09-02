---
page_order: 1
nav_title: Currents
article_title: Currents

layout: dev_guide

page_type: landing
description: "Braze Currentsの設定方法、データパートナー、配信セマンティクス、エンゲージメントデータエクスポートのイベント用語集について説明します。"
tool: currents
search_rank: 9
guide_top_header: "Braze Currents"
guide_top_text: "エンゲージメント戦略の影響を理解することは、ユーザーとのコミュニケーションの改善と最適化を進めるうえで非常に重要です。この貴重なエンゲージメントデータを他のオペレーションと緊密に統合し、データサイエンスへの投資効果を最大化するために、Brazeプラットフォームでは連携を通じて幅広いイベントデータを追跡し、分析、リターゲティング、およびお客様のシステム内でのその他のユースケースに活用できます。<br> <br>Currentsツールは、エンゲージメントイベントのリアルタイムデータストリームであり、Brazeプラットフォームからの最も堅牢かつ詳細なエクスポートです。Avroファイルタイプのデータを多くの<a href='/docs/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners'>データパートナー</a> の1つに提供し、Brazeが生成するユニークで価値のあるデータを活用して、他の最高クラスのプラットフォームでビジネスインテリジェンス（BI）および分析の取り組みを強化できます。"

guide_featured_title: "セクションの記事"
guide_featured_list:
  - name: Currentsを設定する
    link: /docs/user_guide/data/distribution/braze_currents/setting_up_currents
    image: /assets/img/braze_icons/building-01.svg
  - name: Currentsイベント用語集
    link: /docs/user_guide/data/distribution/braze_currents/event_glossary
    image: /assets/img/braze_icons/data.svg
  - name: ユースケース
    link: /docs/user_guide/data/distribution/braze_currents/use_cases
    image: /assets/img/braze_icons/expand-05.svg
  - name: FAQ
    link: /docs/user_guide/data/distribution/braze_currents/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

## Currentsの機能 {#currents-capabilities}

Currentsでは、以下のことが可能です：
* Brazeイベントデータをデータウェアハウスまたは[分析パートナー]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/available_partners)にストリーミングして、詳細な分析を行います。
* Brazeイベントデータを継続的にストリーミングして、ビジネスインテリジェンスツールや機械学習アルゴリズムなどに活用します。
* [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium)、[セグメント]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment)、または[mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents)を使用して、Brazeイベントデータをさまざまな他のシステムにルーティングします。

Currentsでアクセスできるイベントデータを活用すれば、さらに多くのことが可能です。[BrazeもCurrentsを使用しています]({{site.baseurl}}/user_guide/data/distribution/braze_currents/use_cases/how_braze_uses_currents)！

## Currentsデータ配信モデル {#currents-data-distribution-model}

Currentsは、コネクターの作成やオプションのイベントトラッキングを制御するためにエンタイトルメントプールを使用します。

- **Engagement Eventsエンタイトルメント**は、標準のCurrentsコネクターを作成するたびに必要です。
- **Customer Behavior Eventsエンタイトルメント**は、コネクターで**Track Customer Behavior and User Events**を有効にする場合に必要です。
- **User Profiles and Attributesエンタイトルメント**は、コネクターで**Track user profiles and attributes**を有効にする場合に必要です。

テスト用のCurrentsコネクターは個別のテスト制限を使用し、標準コネクターのエンタイトルメントを消費しません。

いずれかのエンタイトルメント上限に達した場合は、[Currentsの設定のトラブルシューティング]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#troubleshooting)および[Currents FAQ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/faq)を参照するか、アカウントマネージャーにお問い合わせください。

## Currentsへのアクセス方法 {#how-to-access-currents}

Currentsコネクターは、多くのプロおよびエンタープライズレベルのパッケージに含まれています。Currentsの利用にご興味がある場合は、アカウントマネージャーにお問い合わせください。アカウントマネージャーとBrazeのデータスペシャリストが、[Currentsの設定と連携]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)をサポートいたします。

<br><br>