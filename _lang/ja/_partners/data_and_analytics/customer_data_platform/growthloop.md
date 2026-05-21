---
nav_title: GrowthLoop
article_title: GrowthLoop
description: "この参考記事では、BrazeとGrowthLoopの提携について概説しています。GrowthLoopは、データウェアハウスから顧客データを直接セグメント化してBrazeに送信できるプラットフォームです。"
alias: /partners/growthloop/
page_type: partner
search_tag: Partner

---

# GrowthLoop

> [GrowthLoop](https://growthloop.com/) は、クラウドデータウェアハウスからBrazeやその他のチャネルへ顧客データをアクティベートするマーケティングチームを支援します。クラウドデータウェアハウスからマーケティングプログラムを自動化、スケーリング、測定し、データを一元管理できます。

_この統合はGrowthLoopによって管理されています。_

## 統合について {#about-the-integration}

BrazeとGrowthLoopの統合により、データウェアハウスから直接顧客データをセグメント化してBrazeに送信できます。これにより、ユーザーはBrazeの豊富な機能セットを、信頼できる唯一の情報源とともに最適化できます。顧客セグメンテーションとアクティベーションのためのマーケティング活動を合理化し、Brazeに送信されたターゲットキャンペーンのセグメンテーション、ローンチ、テスト、結果測定にかかる時間を短縮します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| GrowthLoopのgrowthアカウントまたはenterpriseアカウント | このパートナーシップを利用するには、GrowthLoopのアカウントが必要です。 |
| Braze REST APIキー | すべての権限を持つBraze REST APIキー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)に応じて異なります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース {#use-cases}

データウェアハウスからBrazeに顧客リストを送信し、ワンクリックでメールやプッシュ通知キャンペーンのターゲット設定を行い、常に同期を維持できます。

- サインアップアクティベーションに基づくメール — サインアップフローから離脱したユーザーをアクティブユーザーに転換するためのメールを送信します。
- あらゆるユーザー行動に基づくメール — 「カートに追加」などのユーザー行動に基づいてメールを送信します。
- 解約顧客へのメール — オファー付きのメールで解約した顧客に再度アプローチします。

## 統合 {#integration}

### GrowthLoopでBraze接続を設定する {#configure-braze-connection-in-growthloop}

GrowthLoopのセグメントation Platformにサインインしたら、左サイドバーの**Destinations**タブを開き、右上の**New Destination**をクリックします。

Brazeが見つかるまでスクロールし、**Add Braze**をクリックします。

送信先への接続を設定するポップアップが表示されます。

- **Destination name**：送信先に指定される名前であり、今後アプリではこの名前で参照されます。
- **Sync frequency**：DailyまたはHourlyを選択します。これにより、GrowthLoopがオーディエンスをBrazeにエクスポートする頻度が制御されます。
- **API key**：前提条件で作成した、必要な権限を持つAPIキー。
- **API URL**：前提条件で定義されているURL。

**Create**をクリックします。これで最初のオーディエンスをBrazeにエクスポートできます。GrowthLoopでオーディエンスを作成するには、[オーディエンスの作成](https://www.growthloop.com/help-center-articles/create-an-audience)を参照してください。

### エクスポート後の作業 {#post-export}

オーディエンスがエクスポートされると、GrowthLoopは15分ごとに最新の顧客リストを生成してBrazeに送信します。

同時にGrowthLoopは、条件を満たさなくなったユーザーをオーディエンスから削除し、新たに条件を満たしたユーザーをオーディエンスに追加します。

Brazeはユーザーを照合し、ユーザーがGrowthLoopのオーディエンスに含まれていることを示すフラグを作成します。

Brazeでキャンペーンを作成するときに、そのGrowthLoopオーディエンスから顧客を選択できます。

## トラブルシューティング {#troubleshooting}

追加情報やサポートについては、GrowthLoopチーム（solutions@growthloop.com）までお問い合わせください。