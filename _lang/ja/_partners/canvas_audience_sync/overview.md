---
nav_title: オーディエンス同期について
article_title: オーディエンス同期について
alias: /partners/about_audience_sync/
description: "このリファレンス記事では、Braze Audience Sync to Facebookを使用して、行動トリガーやセグメンテーションなどに基づいて広告を配信する方法について説明します。"
page_order: 0
tool:
  - Canvas

---

# オーディエンス同期について {#about-audience-sync}

> Brazeのオーディエンス同期機能は、多くのトップソーシャルテクノロジーおよび広告テクノロジーにキャンペーンのリーチを拡大するのに役立ちます。[Brazeキャンバス]({{site.baseurl}}/user_guide/messaging/canvas)を通じて、ブランドはファーストパーティのユーザーデータを広告エコシステムにダイナミックかつ安全に同期させ、マーケティングと運用の効率化を推進できます。

## 機能の利用について {#feature-availability}

Brazeをご利用のすべてのお客様は、Audience Sync to GoogleとAudience Sync to Facebookをすぐに利用できますが、アクションクレジットをご利用のお客様はすべてのAudience Syncパートナーにアクセスできます。アクションクレジットを使用していないお客様が追加のAudience Sync送信先をロック解除するには、Audience Sync Proを購入してください。詳細については、Brazeのアカウントマネージャーにお問い合わせください。

## ユースケース {#use-cases}

- 所有チャネルと有料チャネルを利用して高価値のユーザーをターゲティングし、購買やエンゲージメントの増加を図ります。
- 新規ユーザーの獲得コストとコンバージョンを最適化するために、価値の高いユーザーの類似オーディエンスを作成します。
- 他のマーケティングチャネルで反応が低いユーザーを広告でリターゲティングします。
- すでに自社ブランドの忠実な消費者であるユーザーが広告を受け取ることを防ぐための抑制オーディエンスを作成します。

## 概要 {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| 送信先 | オーディエンスメンバーのマッチにかかる時間 | レート制限 | 類似または類似行動 | ヒント |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | 最長24時間 | 1分あたり250,000リクエスト。Googleのフィードバックに基づく自動リトライで、5秒ごとにバッチ処理されます。 | はい | {::nomarkdown}<ul><li>Criteoは最大1,000件の広告オーディエンスに対応します。</li><li>最小オーディエンスサイズは500人、推奨は20,000人以上です。</li></ul>{:/} |
| [FacebookまたはInstagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | 最長24時間 | 毎時190,000件の広告アカウント | はい | {::nomarkdown}<ul><li>Facebookは最大500の広告オーディエンスに対応します。</li><li>Facebookのオーディエンスは1,000ユーザー以上にする必要があります。</li></ul>{:/} |
| [Google広告またはYouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | 6～12時間 | Googleのフィードバックに基づく自動リトライで、5秒ごとにバッチ処理されます。 | いいえ | {::nomarkdown}<ul><li><b>カスタマーマッチ:</b> モバイル広告、メールアドレス、電話番号のいずれかを使用します。</li><li>Googleオーディエンスでの広告配信の開始には、5,000人以上のユーザーが必要です。</li><li>ユーザー数が1,000人以上になるまでは、オーディエンスサイズはゼロと表示されます。</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | 48時間 | LinkedInは毎秒10件のクエリを処理し、リクエスト1件あたり100,000ユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | AI予測オーディエンス | {::nomarkdown}<ul><li>ロケーションターゲティングを考慮した場合、オーディエンスの最小サイズは300人です。</li><li>LinkedInはBrazeダッシュボードにマッチ率を表示します。</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | 24～48時間 | Pinterestは毎秒7件のクエリを処理し、リクエスト1件あたり1,900ユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | はい | Pinterestのオーディエンスには100人以上のユーザーが必要です。 |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/A | Snapchatは毎秒10件のクエリを処理し、リクエスト1件あたり100,000ユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | はい | Snapchatは最大1,000の広告オーディエンスに対応します。 |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | 最長24時間 | N/A | はい | {::nomarkdown}<ul><li>The Trade DeskのCRMオーディエンスには最小オーディエンスサイズの制限はありません。</li><li>The Trade Deskがサポートするオーディエンス数に制限はありません。</li><li>EUに設定されたリージョンのオーディエンスに同期する場合、電話番号はサポートされません。</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | 24～48時間 | TikTokは毎秒50件のクエリを処理し、リクエスト1件あたり10,000ユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | はい | {::nomarkdown}<ul><li>TikTokは最大400の広告オーディエンスに対応します。</li><li>TikTokオーディエンスでの広告配信の開始には、1,000人以上のユーザーが必要です。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="概要" }
<sup>レート制限に達すると、Brazeは13時間にわたって同期を再試行します。</sup>

## 仕組み {#how-it-works}

Audience Sync to GoogleまたはAudience Sync to Facebookを使用するには、**テクノロジーパートナー**ページでパートナーを検索して、広告アカウントを接続します。

![Facebookのテクノロジーパートナー。]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google広告のテクノロジーパートナー。]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

広告アカウントの接続後に、オーディエンス同期ステップを含むキャンバスを作成できます。

![ユーザージャーニーにオーディエンス同期ステップを追加するキャンバスコンポーネントメニュー。]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択します。

![オーディエンス同期ステップでオーディエンス同期パートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

パートナーごとに、オーディエンス同期ステップの一部として次の内容を設定する必要があります。

- 広告アカウント
- オーディエンス
- ユーザーを追加または削除するアクション
- マッチするフィールド

キャンバス内でユーザーがオーディエンス同期ステップに入るとすぐに、Brazeによりユーザーが同期されることに注意してください。

オーディエンス同期の送信先ごとに、パートナーの送信可能なフィールドに関する要件が異なる場合があります。詳細については、特定のパートナーのドキュメントを参照してください。

### Audience Sync Pro

TikTok、Pinterest、Snapchat、CriteoなどのAudience Sync Proパートナーを使用するには、**テクノロジーパートナー**ページの**Audience Sync Pro**セクションでAudience Sync Proの購入割り当てに基づいてパートナーを選択できます。

![パートナーが未選択のAudience Sync Pro。]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

最初に**Select Partners**を選択して、使用するパートナーを選択します。Audience Sync Proを購入すると、1回の購入につき3つのAudience Sync Pro送信先が割り当てられます。これは、ダッシュボードの各ワークスペース内で使用可能になります。

![Brazeに接続するパートナーを3社まで選択できるオプション。]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Audience Sync Pro送信先を選択したら、パートナータイルをクリックして、選択したパートナーの広告アカウントを接続します。

![オーディエンス同期のパートナーに選ばれたSnapchatとTikTokの例。]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Snapchatオーディエンス同期設定。「Snapchatアカウント1件の接続に成功しました」というメッセージを表示。]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

最後に、このAudience Sync Pro送信先を使用して、キャンバスでオーディエンス同期ステップを作成します。

### バッチ処理とレイテンシー {#batching-and-latency}

キャンバス内でユーザーがオーディエンス同期ステップに入ると、Brazeはユーザーをバッチ処理システムにキューイングし、パートナーAPIにディスパッチする前にユーザーの更新を集約します。バッチは以下のいずれかの条件が満たされたときに送信されます。

- **バッチがサイズ上限に達した場合。** これはパートナーによって異なります。
  - デフォルトでは最大2,000ユーザー
  - Google広告では最大10,000ユーザー
  - FacebookとTikTokでは最大2,000ユーザー
- **バッチのレイテンシータイマーが期限切れになった場合。** デフォルトは1時間ですが、パートナーごとに設定可能です。たとえば、The Trade Deskでは10分です。

大量のキャンバスではバッチがより早く満たされるため、ディスパッチが早くなる場合があります。少量のキャンバスではレイテンシータイマーが期限切れになるまで待機します。Brazeは固定のディスパッチ時間を保証しません。タイミングはバッチサイズと設定されたレイテンシーウィンドウに依存します。

Brazeはモニタリングとトラブルシューティングのために内部ログにディスパッチアクティビティを記録しますが、これらのタイムスタンプはクエリ可能なフィールドとしては公開されません。BrazeがパートナーAPIにバッチをディスパッチした後、パートナーは独自のサービスレベルアグリーメントに従ってオーディエンスの更新を処理します（通常6～48時間）。

Brazeは、個々のユーザーがマッチまたは同期されたことについてパートナーから確認を受け取りません。パートナーの応答は受信のHTTP確認であり、マッチの確認ではありません。オーディエンスが正しく構成されたことを確認するには、パートナーの広告プラットフォーム（Google広告オーディエンスマネージャーやMeta Business Managerなど）を確認してください。

### オーディエンス同期エラーメール {#audience-sync-error-emails}

エラーがパートナー連携全体に関連している場合（認可の問題など）、連携を接続したユーザーにメールが送信されます。そのユーザーがもう存在しない場合は、管理者がメールを受け取ります。

エラーがキャンバスのオーディエンス同期コンポーネントの問題（「オーディエンスが存在しない」など）に関連している場合、キャンバスを設定したユーザーにメールが送信されます。そのユーザーがもう存在しない場合は、会社の管理者にフォールバックされます。

これらのメールの受信者を設定するには、カスタマーサクセスマネージャーに連絡し、**通知設定**で受信者を追加してください。この機能は現在の動作を変更するため、Brazeのデフォルトでは誰もオプトインされません。エラーメールを見逃さないよう、すぐにこの新しい通知設定に受信者を追加する必要があります。

## データプライバシーに関する考慮事項 {#data-privacy-considerations}

{% alert important %}
本書は、法的助言を提供することを意図したものではなく、また法的助言を提供するものとして依拠することもできません。オーディエンス同期の使用には、特定の法的要件が適用されます。適用されるすべての法律を遵守して使用していることを確認するために、法律顧問の助言を求めてください。
{% endalert %}

広告トラッキングのオーディエンスを構築する際、ユーザーの嗜好に基づき、また[CCPA](https://oag.ca.gov/privacy/ccpa)に基づく「販売または共有しない」権利などのプライバシー法を遵守するために、特定のユーザーを含めたり除外したりしたい場合があります。マーケターは、キャンバスのエントリ基準の範囲内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。以下にいくつかの選択肢を挙げます。

[Braze SDKを通じてiOS IDFA]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)を収集した場合、「Ads Tracking Enabled」フィルターを使用できます。ユーザーがオプトインしたオーディエンス同期の送信先にのみユーザーを送信するには、値を`true`に選択します。

![エントリオーディエンスが「Ad Tracking Enabled is true」のキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集する場合は、キャンバスのエントリ基準にこれらをフィルターとして含める必要があります。

![エントリオーディエンスが「opted_in_marketing equals true」のキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Brazeプラットフォーム内でこれらのデータ保護法を遵守する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance)を参照してください。

## 広告ターゲティングの同意の管理 {#managing-consent-for-ad-targeting}

広告主として、ユーザーの広告トラッキングやターゲティングに対する同意を管理する責任を負います。

ユーザーに広告を配信するには、適用されるすべての法律と規制、および広告プラットフォームのポリシーと要件を遵守する必要があります。ユーザーの同意を得た場合にのみ、Brazeを使用してユーザーのターゲティングと同期を行ってください。

これらの広告プラットフォームのオーディエンスリストを最新の状態に保ち、同意を取り消したユーザーを削除するには、オーディエンス同期ステップを使用して、これらの既存のオーディエンスリストからユーザーを削除するキャンバスを設定します。