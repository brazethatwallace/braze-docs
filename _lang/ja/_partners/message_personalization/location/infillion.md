---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "この参考記事では、BrazeとInfillionのパートナーシップについて説明しています。Infillionでは位置情報を活用してマーケティングの関連性を高めることができます。"
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/)を利用すると、位置情報を活用してマーケティングの関連性を高めることができます。同社の位置情報SDKは、ジオフェンシングソフトウェアやビーコンと組み合わせることで、関連性が高く、パーソナライズされた、近接を意識したモバイル体験を提供します。

ビーコンやジオフェンスサポートをBrazeのターゲティングやメッセージング機能と組み合わせることで、ユーザーの物理的なアクションについて詳しく知ることができ、それに応じてメッセージを送ることができます。このパートナー連携により、次のようなさまざまなユースケースが可能になります。

- **マーケティング：**文脈に応じた関連性のあるメッセージを送信し、体験型の消費者ジャーニーを構築します。
- **競合分析：**消費者の傾向やパターンを理解するために、競合ロケーション周辺にトリガーを設定します。
- **オーディエンスインサイト：**ユーザーの訪問行動を理解し、それらの学習に基づいてさらにセグメント化します。

{% alert note %}
この統合は、Infillionのビーコンとinfillionのジオフェンスソリューションで同様に機能します。
{% endalert %}

## 前提条件 {#prerequisites}

| 必要条件| 説明|
| ---| ---|
| [Infillionマネージャーアカウント](https://manager.gimbal.com/login/users/sign_in) | このパートナーシップを利用するには、Infillionのマネージャーアカウントが必要です。 |
|[Infillion Location SDK](https://docs.gimbal.com/index.html) | Infillion Location SDKは、近接ビーコンとジオフェンスを使用したマクロおよびミクロの位置情報ベースのモバイル体験を提供し、アプリユーザーとのコミュニケーション効果を高めます。SDKを実装し、ジオフェンス（またはビーコン）を設定しておく必要があります。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## SDK統合 {#sdk-integration}

BrazeとInfillionを統合するには、Infillion Location SDKを実装し、Infillionマネージャーアカウントを作成する必要があります。Android、FireOS、iOS向けの以下の統合では、ユーザーが入る新しい場所ごとに固有のカスタムイベントが作成されます。これらのイベントをキャンペーンやキャンバスでのトリガーやリターゲティングに使用できます。

50以上の場所を作成することが予想される場合は、汎用的な`Places Entered`カスタムイベントを作成し、イベントプロパティとして場所名を追加することをお勧めします。

1. [Infillionドキュメント](https://docs.gimbal.com/)の手順に従って、AndroidおよびiOS向けの[Infillion SDK](https://manager.gimbal.com/sdk_downloads)をアプリに統合します。
2. Infillionの[place REST API](https://docs.gimbal.com/rest.html)を使って、ユーザーの`places`を取得します。
3. Braze [REST APIキー](https://manager.gimbal.com/apps)を入力して、InfillionアカウントをBrazeにリンクします。
4. Braze SDKで[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/)を設定します。Infillionは[AndroidおよびFireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/beacon_integration/#gimbal-beacons)と[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/beacon_integration/#gimbal-beacons)でBrazeと統合できます。
5. これらのイベントのプロパティ（場所名、滞留時間）をログに記録します。
6. これらのプロパティとイベントを使用して、Brazeでキャンペーンやキャンバスをトリガーします。