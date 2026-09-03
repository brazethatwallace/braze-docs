---
nav_title: データ
article_title: Braze データプラットフォーム
page_order: 3
description: "Braze データプラットフォームについて、データの統一、有効化、配信の方法を含めて説明します。"
---

# Braze データプラットフォーム {#braze-data-platform}

> Braze データプラットフォームについて、データの統一、有効化、配信の方法を含めて説明します。

Braze データプラットフォーム (BDP) は、包括的でコンポーザブルなデータ機能とパートナー連携のセットであり、顧客向けにパーソナライズされたエクスペリエンスを作成できるようにします。Brazeでは、データを3つのデータ関連ジョブの観点で考えています：[統一]({{site.baseurl}}/user_guide/data/unification)、[有効化]({{site.baseurl}}/user_guide/data/activation)、[配信]({{site.baseurl}}/user_guide/data/distribution)です。

Braze データプラットフォームの機能を組み合わせて使用することで、データを活用して、顧客のリアルタイムの行動に応じた意味のあるターゲットメッセージを作成できます。

## 仕組み {#how-it-works}

### データの統合 {#unify-your-data}

ユーザーデータはさまざまなエントリポイントからBrazeに流入します。[API]({{site.baseurl}}/api/home)や[SDK]({{site.baseurl}}/developer_guide/sdk_integration)を使用して、あらゆるソースからファーストパーティデータを収集・統合できます。また、[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)などの組み込みインジェスションツールを使用して、データウェアハウスやファイルストレージソリューションからBrazeへの直接統合を構築したり、[Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation)を使用してBrazeへのデータ転送用Webhook連携を構築・管理したりすることもできます。

### データの活用 {#activate-your-data}

データをクリーンアップ、整理し、使用に向けて準備します。ユーザープロファイルやセグメントを活用して、顧客の行動や嗜好をリアルタイムで把握します。ターゲットメッセージを作成する際には[レポート指標用語集]({{site.baseurl}}/user_guide/analytics/metrics_glossary)を参照し、[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)を使用して商品データやコンテンツデータでメッセージを充実させましょう。パーソナライズされた体験に対する顧客の反応を把握できます。

### データの配信 {#distribute-your-data}

データをストリーミングおよび[エクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data)して外部システムに送り、次のステップのインサイトや意思決定に活用します。[Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents)を使用してBrazeのイベントデータをデータウェアハウスにストリーミングし、ビジネスインテリジェンスツールを強化できます。また、[テクノロジーパートナー連携]({{site.baseurl}}/partners/data_and_analytics)によってデータ活用の幅をさらに広げることもできます。

## データインフラ {#data-infrastructure}

Brazeのデータインフラには、レイテンシー（データがサーバーとユーザーの間を移動するのにかかる時間）を最小限に抑える[データセンター]({{site.baseurl}}/user_guide/data/infrastructure/data_centers)が含まれています。この地理的な分散により、当社のサービスの信頼性と拡張性が確保されています。また、機密データを保護し、Brazeで共有される個人を特定できる情報（PII）を最小限に抑えるために、[フィールドレベルの暗号化]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption)も提供しています。使用量と請求の詳細については、[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points)を参照してください。

## 基本原則 {#core-principles}

データは、パーソナライズされた体験の創出、顧客行動の理解、メッセージング戦略の最適化を可能にすることで、カスタマーエンゲージメント戦略の強化に重要な役割を果たします。Brazeでは、3つの基本原則を念頭に置いてすべてのデータ機能を構築しています。

{% details データをより効果的に活用する %}
- **柔軟でコンポーネントベース:** 包括的な目標は、データをより効果的かつ完全に活用できるようにすることです。コンポーザブルアーキテクチャで構築されているため、不要なミドルウェアなしに、データをより有効に活用するために必要なテクノロジーを活用できます。
- **パートナー連携:** Brazeは、リアルタイムの双方向データ共有を簡素化する、業界最高クラスのエコシステムテクノロジーとの連携（およびAPIの提供）を優先しています。
- **ストリーム処理アーキテクチャ:** Brazeに取り込まれたあらゆるデータポイントに基づいて、セグメンテーション、オーケストレーション、パーソナライゼーションのためのアクションをトリガーできます。
{% enddetails %}

{% details データのアジリティを高めてパフォーマンスを向上させる %}
- **柔軟なオーディエンス構築:** 技術チームへの依存を減らし、パーソナライズされたカスタマーエンゲージメントを大規模に作成・配信できます。
- **スピードとパフォーマンス:** エンゲージメントデータとインサイトはリアルタイムで提供されるため、反復的で効果的なカスタマーエンゲージメントや、より広範なビジネスの意思決定を支援します。
{% enddetails %}

{% details データの安全性、保護、コンプライアンスを確保する %}
- **業界をリードするセキュリティプラクティス:** SOC 2 Type 2やISO 27001を含む定期的な第三者監査を実施し、最高水準の業界基準に準拠しています。潜在的な脆弱性に事前に対処するための公開バグバウンティプログラムを維持しており、データの保護に取り組む専任のセキュリティチームがあります。
- **業界コンプライアンス:** GDPRやCCPAを含むデータ保護規制への準拠を促進するツールを提供しています。
- **データプライバシー:** エンドユーザーの同意の管理、リクエストの処理、消費者の権利の行使が可能です。
{% enddetails %}