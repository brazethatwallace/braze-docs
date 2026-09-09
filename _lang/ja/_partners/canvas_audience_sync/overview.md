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

## 機能の利用可能性 {#feature-availability}

すべてのBrazeの顧客は、Google およびFacebookへのオーディエンス同期にすぐにアクセスできますが、アクションクレジットを利用している顧客はすべてのオーディエンス同期パートナーにアクセスできます。アクションクレジットを利用していない顧客が追加のオーディエンス同期の送信先を利用するには、Audience Sync Proを購入してください。詳細については、Brazeアカウントマネージャーにお問い合わせください。

## ユースケース {#use-cases}

- 自社チャネルおよび有料チャネルを使用して高価値ユーザーをターゲティングし、追加の購入やエンゲージメントを促進する。
- 高価値ユーザーの類似オーディエンスを作成し、新規ユーザー獲得コストを最適化してコンバージョンを向上させる。
- 他のマーケティングチャネルへの反応が低いユーザーに広告でリターゲティングする。
- すでにブランドのロイヤル消費者であるユーザーに広告が配信されないよう、抑制オーディエンスを作成する。

## 概要 {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| 送信先 | オーディエンスメンバーのマッチングにかかる時間 | レート制限 | 類似オーディエンス | ヒント |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | 最大24時間 | 1分あたり250,000リクエスト。5秒ごとにバッチ処理され、自動リトライあり。 | あり | {::nomarkdown}<ul><li>Criteoは最大1,000の広告オーディエンスをサポートしています。</li><li>最小オーディエンスサイズは500で、推奨は20,000以上です。</li></ul>{:/} |
| [FacebookまたはInstagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | 最大24時間 | 1時間あたり190,000広告アカウント | あり | {::nomarkdown}<ul><li>Facebookは最大500の広告オーディエンスをサポートしています。</li><li>Facebookではオーディエンスに最低1,000人のユーザーが必要です。</li></ul>{:/} |
| [Google 広告またはYouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | 6〜12時間 | Googleのフィードバックに基づき、5秒ごとにバッチ処理され、自動リトライあり | なし | {::nomarkdown}<ul><li><b>カスタマーマッチ：</b>モバイル広告、またはメールアドレスもしくは電話番号を使用します。</li><li>Google オーディエンスでは広告の配信を開始するために最低5,000人のユーザーが必要です。</li><li>オーディエンスサイズは、ユーザーが最低1,000人に達するまでゼロと表示されます。</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | 最大48時間 | Brazeは1リクエストあたり最大2,000人のユーザーをバッチ処理し、最大約13時間の自動リトライを行います。 | AI予測オーディエンス | {::nomarkdown}<ul><li>最小オーディエンスサイズは300メンバーで、ロケーションターゲティングが考慮されます。</li><li>LinkedInのマッチ率はBrazeダッシュボードに表示されます。</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | 24〜48時間 | Pinterestは1秒あたり7クエリ、1リクエストあたり1,900人のユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | あり | Pinterestオーディエンスには最低100人のユーザーが必要です。 |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/A | Snapchatは1秒あたり10クエリ、1リクエストあたり100,000人のユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | あり | Snapchatは最大1,000の広告オーディエンスをサポートしています。 |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | 最大24時間 | N/A | あり | {::nomarkdown}<ul><li>The Trade DeskのCRMオーディエンスには最小オーディエンスサイズの制限はありません。</li><li>The Trade Deskがサポートするオーディエンス数に制限はありません。</li><li>EUに設定されたリージョンのオーディエンスに同期する場合、電話番号はサポートされません。</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | 24〜48時間 | TikTokは1秒あたり50クエリ、1リクエストあたり10,000人のユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | あり | {::nomarkdown}<ul><li>TikTokは最大400の広告オーディエンスをサポートしています。</li><li>TikTokオーディエンスでは広告の配信を開始するために最低1,000人のユーザーが必要です。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="概要" }
<sup>レート制限に達した場合、Brazeは13時間にわたって同期のリトライを行います。</sup>

## 仕組み {#how-it-works}

Google または Facebook に対してオーディエンス同期を使用するには、**テクノロジーパートナー**ページでパートナーを検索して広告アカウントを接続します。

![Facebookテクノロジーパートナー。]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google 広告テクノロジーパートナー。]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

広告アカウントを接続したら、オーディエンス同期ステップを含むキャンバスを作成できます。

![ユーザージャーニーにオーディエンス同期ステップを追加するためのキャンバスコンポーネントメニュー。]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択します。

![オーディエンス同期ステップでオーディエンス同期パートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

各パートナーについて、オーディエンス同期ステップの一部として以下を設定する必要があります。

- 広告アカウント
- オーディエンス
- ユーザーの追加または削除のアクション
- マッチするフィールド

Brazeは、ユーザーがキャンバス内のオーディエンス同期ステップに入るとすぐに同期を実行します。

オーディエンス同期の送信先ごとに、Brazeが送信できるフィールドについてパートナーの要件が異なる場合があります。詳細については、各パートナーのドキュメントを参照してください。

### Audience Sync Pro

Criteo、LinkedIn、Pinterest、Snapchat、TikTokなどのAudience Sync Proパートナーを使用するには、**テクノロジーパートナー**ページの**Audience Sync Pro**セクションで、Audience Sync Proの購入割り当てに基づいてパートナーを選択できます。

![パートナーがまだ選択されていないAudience Sync Pro。]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

まず、使用するパートナーを選択します。Audience Sync Proを購入するたびに、3つのAudience Sync Pro送信先が割り当てられ、ダッシュボード内の各ワークスペースで利用できます。

![Brazeに接続する最大3つのパートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Audience Sync Proの送信先を選択したら、パートナータイルをクリックして選択したパートナーの広告アカウントを接続します。

![オーディエンス同期のパートナーとしてSnapchatとTikTokが選択されている例。]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![「Snapchatアカウントを1つ正常に接続しました」というメッセージが表示されたSnapchatオーディエンス同期設定。]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

最後に、このAudience Sync Proの送信先を使用して、キャンバスでオーディエンス同期ステップを作成します。

### バッチ処理とレイテンシ {#batching-and-latency}

ユーザーがキャンバスのオーディエンス同期ステップに入ると、Brazeはユーザーをバッチ処理システムにキューイングし、パートナーAPIにディスパッチする前にユーザーの更新を集約します。バッチは以下のいずれかが発生した時に送信されます。

- **バッチがサイズの上限に達した場合。**これはパートナーによって異なります。
  - デフォルトは最大2,000ユーザーをサポートします
  - Google 広告は最大10,000ユーザーをサポートします
  - FacebookとTikTokは最大2,000ユーザーをサポートします
- **バッチのレイテンシタイマーが期限切れになった場合。**デフォルトは1時間ですが、パートナーごとに設定可能です。例えば、The Trade Deskは10分を使用します。

大量のキャンバスはバッチがより速く埋まるため、より早くディスパッチされる場合があります。少量のキャンバスはレイテンシタイマーが期限切れになるまで待機します。Brazeは固定のディスパッチ時間を保証しません。タイミングはバッチサイズと設定されたレイテンシウィンドウによって異なります。

Brazeはモニタリングとトラブルシューティングのために内部ログにディスパッチアクティビティを記録しますが、これらのタイムスタンプはクエリ可能なフィールドとして公開されていません。BrazeがパートナーAPIにバッチをディスパッチした後、パートナーは独自のサービスレベル契約に従ってオーディエンスの更新を処理します（通常6〜48時間）。

Brazeは、個々のユーザーがマッチまたは同期されたというパートナーからの確認を受け取りません。パートナーのレスポンスは受信のHTTP確認応答であり、マッチの確認ではありません。オーディエンスが正常に作成されたことを確認するには、パートナーの広告プラットフォーム（Google 広告オーディエンスマネージャーやMeta Business Managerなど）を確認してください。

### オーディエンス同期のエラーメール {#audience-sync-error-emails}

エラーがパートナー連携全体に関連する場合（認証の問題など）、連携を接続したユーザーにメールが送信されます。そのユーザーが存在しなくなった場合は、管理者がメールを受け取ります。

エラーがキャンバス内のオーディエンス同期コンポーネントの問題に関連する場合（「オーディエンスが存在しません」など）、キャンバスを設定したユーザーにメールが送信されます。そのユーザーが存在しなくなった場合は、会社の管理者にフォールバックされます。

これらのメールの受信者を設定するには、カスタマーサクセスマネージャーに連絡して**通知設定**に受信者を追加してください。この設定は、連携エラーとオーディエンス同期コンポーネントエラーの両方を対象としています。追加された受信者は、エラーに関連付けられたユーザーに加えてこれらのメールを受信します。

## データプライバシーに関する考慮事項 {#data-privacy-considerations}

{% alert important %}
このドキュメントは、法的助言を提供することを意図したものではなく、また法的助言として依拠することもできません。オーディエンス同期の使用には、特定の法的要件が適用されます。適用されるすべての法律に準拠して使用していることを確認するために、法律顧問の助言を求めてください。
{% endalert %}

広告トラッキング用のオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりすることや、[CCPA](https://oag.ca.gov/privacy/ccpa)に基づく「販売または共有の拒否」権などのプライバシー法に準拠することが必要になる場合があります。マーケターは、キャンバスのエントリ条件内でユーザーの適格性に関連するフィルターを実装する必要があります。以下のオプションが役立ちます。

[Braze SDKを通じてiOS IDFAを収集]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations)している場合、「広告トラッキング有効」フィルターを使用できます。値を`true`に設定して、オプトインしたユーザーのみをオーディエンス同期の送信先に送信します。

![エントリオーディエンスが「広告トラッキング有効がtrue」のキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、キャンバスのエントリ条件にフィルターとして含める必要があります。

![エントリオーディエンスが「opted_in_marketingがtrueに等しい」のキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Brazeプラットフォーム内でこれらのデータ保護法に準拠する方法の詳細については、[データ保護技術支援]({{site.baseurl}}/dp-technical-assistance)を参照してください。

## 広告ターゲティングに関する同意の管理 {#managing-consent-for-ad-targeting}

広告主として、ユーザーの広告トラッキングまたはターゲティングに関する同意を管理する責任があります。

ユーザーに広告を配信するには、適用されるすべての法律と規制、および広告プラットフォームのポリシーと要件を遵守する必要があります。同意を取得したユーザーに対してのみ、Brazeを使用してターゲティングと同期を行ってください。

これらの広告プラットフォームのオーディエンスリストを最新の状態に保ち、同意を撤回したユーザーを削除するには、Audience Sync ステップを使用して既存のオーディエンスリストからユーザーを削除するキャンバスを設定してください。