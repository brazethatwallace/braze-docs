---
nav_title: Storyly
article_title: Storyly
description: "このリファレンス記事では、Braze と Storyly のパートナーシップについて説明します。Storyly は、アプリオーナーがセグメントをターゲットにし、より多くのファーストパーティデータを Braze にフィードできるようにする軽量 SDK です。"
alias: /partners/storyly/
page_type: partner
search_tag: Partner

---

# Storyly

> [Storyly](https://www.storyly.io/) は、アプリやWeb サイトにストーリーをもたらす軽量 SDK です。直感的なデザインスタジオ、洞察に満ちた分析、シームレスな接続性を備えた Storyly は、オーディエンス体験を豊かにする強力なツールです。

_この統合は Storyly によって管理されています。_

## 統合について {#about-the-integration}

Braze と Storyly の統合により、Brazeのセグメントを Storyly プラットフォームでオーディエンスとして使用できます。この統合により、次のことが可能になります。
- 特定のストーリーでセグメントをターゲットにする
- ユーザー属性を使ってストーリーコンテンツをパーソナライズする

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Storyly アカウント | このパートナーシップを活用するには、Storyly アカウントが必要です。 |
| Storyly SDK | [Storyly SDK](https://integration.storyly.io/) をインストールする必要があります。 |
| Braze REST API キー | 以下の権限を持つ Braze REST API キー。<br><br> `users.export.ids`<br> `users.export.segments`<br> `segments.list`<br> `segments.details` <br><br> これは、Braze ダッシュボードの**設定** > **API キー**から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイント URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスの Braze URL に依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース {#use-cases}

Braze と Storyly の統合により、アプリオーナーはBrazeのすべてのセグメントにストーリーを表示し、ユーザー属性でストーリーをパーソナライズできます。

一般的なユースケースには以下のようなものがあります。

__Storyly でBraze セグメントをターゲットにする__<br>統合が完了したら、Braze セグメントに基づいて Storyly オーディエンスを作成できます。これは、デモグラフィックセグメントまたは行動セグメントです。例えば、特定の場所に住んでいるユーザー、アプリで特定のアクションを起こしたユーザー、特定の商品に興味があるユーザーを特定のストーリーでターゲットにすることで、コンバージョンを高めることができます。<br>
__ユーザー属性でパーソナライズされたストーリー__<br>Brazeのユーザー属性はStorylyでも使用でき、ダイナミックなストーリーを生成できます。これには、ユーザーの名前、買い物かごに入っている製品、お気に入りの製品などを含めることができ、ユーザーに独自のパーソナライズされたストーリーを提供できます。パーソナライゼーションは、ストーリーのコンバージョン率とストーリー全体のエンゲージメント率を高めるのに役立ちます。

## データエクスポートの統合 {#data-export-integration}

Braze と Storyly の統合については、以下の動画で説明されています。

{% multi_lang_include video.html id="3-OEqQs48Zw" source="youtube" %}

Storyly の統合がカスタムパラメーターを保持していることを確認してください。これらのパラメーターは、Brazeの `external id` ユーザープロパティに対応します。カスタムパラメーターの実装については、[iOS](https://integration.storyly.io/ios/personalization-customaudience.html)、[Android](https://integration.storyly.io/android/personalization-customaudience.html)、[React Native](https://integration.storyly.io/react-native/personalization-customaudience.html)、[Flutter](https://integration.storyly.io/flutter/personalization-customaudience.html)、[Web](https://integration.storyly.io/web/personalization-customaudience.html) の各ページで説明されています。

詳細については、[Storyly](https://docs.storyly.io/page/connect-your-braze-audiences-with-storyly) のドキュメントも参照してください。

### ステップ 1: Storyly ダッシュボードで統合を設定する {#step-1-set-the-integration-on-storyly-dashboard}

統合は **Storyly Dashboard > Settings > Integrations > Connect with Braze** で作成します。ここでは、Braze REST API キーと Braze REST エンドポイントが必要です。

### ステップ 2: セグメントを取得する {#step-2-get-your-segments}

次に、Braze セグメントを使用して Storyly オーディエンスを作成できます。これは、**Storyly Dashboard > Settings > Audiences > New Audience > Create Audience with Braze** で作成できます。

ここには2つの同期オプションがあります。特定のキャンペーンストーリーには **One-time sync** を、長期的なストーリーには **Daily Sync** を選択してください。