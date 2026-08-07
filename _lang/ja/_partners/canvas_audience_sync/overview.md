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

すべてのBraze顧客は、Google および Facebook へのオーディエンス同期にすぐにアクセスできますが、アクションクレジットを利用している顧客はすべてのオーディエンス同期パートナーにアクセスできます。アクションクレジットを利用していない顧客が追加のオーディエンス同期送信先を利用するには、Audience Sync Pro を購入してください。詳細については、Brazeアカウントマネージャーにお問い合わせください。

## ユースケース {#use-cases}

- 自社チャネルと有料チャネルを使用して高価値ユーザーをターゲティングし、追加購入やエンゲージメントを促進します。
- 高価値ユーザーの類似オーディエンスを作成し、新規ユーザー獲得コストとコンバージョンを最適化します。
- 他のマーケティングチャネルへの反応が低いユーザーに広告でリターゲティングします。
- すでにブランドのロイヤル消費者であるユーザーに広告が配信されないよう、抑制オーディエンスを作成します。

## 概要 {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| 送信先 | オーディエンスメンバーのマッチにかかる時間 | レート制限 | 類似オーディエンスまたはアクタライク | ヒント |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | 最大24時間 | 1分あたり250,000リクエスト。5秒ごとにバッチ処理され、自動リトライあり。 | あり | {::nomarkdown}<ul><li>Criteoは最大1,000の広告オーディエンスをサポートしています。</li><li>最小オーディエンスサイズは500で、推奨は20,000以上です。</li></ul>{:/} |
| [FacebookまたはInstagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | 最大24時間 | 1時間あたり190,000広告アカウント | あり | {::nomarkdown}<ul><li>Facebookは最大500の広告オーディエンスをサポートしています。</li><li>Facebookではオーディエンスに最低1,000ユーザーが必要です。</li></ul>{:/} |
| [Google 広告またはYouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | 6〜12時間 | Googleのフィードバックに基づき、5秒ごとにバッチ処理され、自動リトライあり | なし | {::nomarkdown}<ul><li><b>カスタマーマッチ：</b>モバイル広告、またはメールアドレスか電話番号を使用します。</li><li>Google オーディエンスでは広告配信を開始するために最低5,000ユーザーが必要です。</li><li>オーディエンスサイズは、最低1,000ユーザーに達するまでゼロと表示されます。</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | 48時間 | LinkedInは1秒あたり10クエリ、1リクエストあたり100,000ユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | AI予測オーディエンス | {::nomarkdown}<ul><li>最小オーディエンスサイズは、ロケーションターゲティングを考慮して300メンバーです。</li><li>LinkedInはBrazeダッシュボードにマッチ率を表示します。</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | 24〜48時間 | Pinterestは1秒あたり7クエリ、1リクエストあたり1,900ユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | あり | Pinterestオーディエンスには最低100ユーザーが必要です。 |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/A | Snapchatは1秒あたり10クエリ、1リクエストあたり100,000ユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | あり | Snapchatは最大1,000の広告オーディエンスをサポートしています。 |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | 最大24時間 | N/A | あり | {::nomarkdown}<ul><li>The Trade DeskのCRMオーディエンスには最小オーディエンスサイズの制限はありません。</li><li>The Trade Deskがサポートするオーディエンス数に制限はありません。</li><li>EUに設定されたリージョンのオーディエンスに同期する場合、電話番号はサポートされません。</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | 24〜48時間 | TikTokは1秒あたり50クエリ、1リクエストあたり10,000ユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | あり | {::nomarkdown}<ul><li>TikTokは最大400の広告オーディエンスをサポートしています。</li><li>TikTokオーディエンスでは広告配信を開始するために最低1,000ユーザーが必要です。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="概要" }
<sup>レート制限に達した場合、Brazeは13時間にわたって同期をリトライします。</sup>

## 仕組み {#how-it-works}

Google または Facebook へのオーディエンス同期を使用するには、**テクノロジーパートナー**ページでパートナーを検索して広告アカウントを接続します。

![Facebookテクノロジーパートナー。]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google 広告テクノロジーパートナー。]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

広告アカウントを接続したら、オーディエンス同期ステップを含むキャンバスを作成できます。

![ユーザージャーニーにオーディエンス同期ステップを追加するためのキャンバスコンポーネントメニュー。]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択します。

![オーディエンス同期ステップでオーディエンス同期パートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

各パートナーについて、オーディエンス同期ステップの一部として以下を設定する必要があります。

- 広告アカウント
- オーディエンス
- ユーザーを追加または削除するアクション
- マッチングするフィールド

Brazeは、ユーザーがキャンバス内のオーディエンス同期ステップに入るとすぐに同期を行います。

各オーディエンス同期の送信先について、Brazeが送信できるフィールドに関してパートナーごとに異なる要件がある場合があります。詳細については、各パートナーのドキュメントを参照してください。

### Audience Sync Pro

TikTok、Pinterest、Snapchat、Criteoなどの Audience Sync Pro パートナーを使用するには、**テクノロジーパートナー**ページの **Audience Sync Pro** セクションで、Audience Sync Pro の購入割り当てに基づいてパートナーを選択できます。

![パートナーがまだ選択されていない Audience Sync Pro。]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

まず、使用するパートナーを選択します。Audience Sync Pro を購入するたびに、3つの Audience Sync Pro 送信先が割り当てられ、ダッシュボード内の各ワークスペースで利用できます。

![Brazeに接続する最大3つのパートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Audience Sync Pro の送信先を選択したら、パートナータイルをクリックして、選択したパートナーの広告アカウントを接続します。

![オーディエンス同期のパートナーとして Snapchat と TikTok が選択された例。]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![「Snapchatアカウント1件の接続に成功しました」というメッセージが表示された Snapchat オーディエンス同期設定。]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

最後に、この Audience Sync Pro 送信先を使用してキャンバスでオーディエンス同期ステップを作成します。

### バッチ処理とレイテンシー {#batching-and-latency}

ユーザーがキャンバスのオーディエンス同期ステップに入ると、Brazeはユーザーをバッチ処理システムにキューイングし、パートナーAPIに送信する前にユーザーの更新を集約します。バッチは以下のいずれかが発生した場合に送信されます。

- **バッチがサイズ上限に達した場合。** これはパートナーによって異なります。
  - デフォルトでは最大2,000ユーザーをサポート
  - Google 広告は最大10,000ユーザーをサポート
  - Facebook と TikTok は最大2,000ユーザーをサポート
- **バッチのレイテンシータイマーが期限切れになった場合。** デフォルトは1時間ですが、パートナーごとに設定可能です。たとえば、The Trade Desk は10分を使用します。

大量のキャンバスでは、バッチがより早く満たされるため、より早く送信される場合があります。少量のキャンバスでは、レイテンシータイマーが期限切れになるまで待機します。Brazeは固定の送信時間を保証しません。タイミングはバッチサイズと設定されたレイテンシーウィンドウに依存します。

Brazeは監視とトラブルシューティングのために内部ログに送信アクティビティを記録しますが、これらのタイムスタンプはクエリ可能なフィールドとしては公開されません。Brazeがパートナー APIにバッチを送信した後、パートナーは独自のサービスレベルアグリーメントに従ってオーディエンスの更新を処理します（通常6〜48時間）。

Brazeは、個々のユーザーがマッチングまたは同期されたことについてパートナーからの確認を受け取りません。パートナーの応答は受信のHTTP確認応答であり、マッチングの確認ではありません。オーディエンスが正しく作成されたことを確認するには、パートナーの広告プラットフォーム（Google 広告のオーディエンスマネージャーや Meta Business Manager など）を確認してください。

### オーディエンス同期のエラーメール {#audience-sync-error-emails}

エラーがパートナー連携全体に関連する場合（認証の問題など）、連携を接続したユーザーにメールが送信されます。そのユーザーが存在しなくなった場合は、管理者がメールを受信します。

エラーがキャンバスのオーディエンス同期コンポーネントに関連する問題（「オーディエンスが存在しません」など）の場合、キャンバスを設定したユーザーにメールが送信されます。そのユーザーが存在しなくなった場合は、会社の管理者にフォールバックされます。

これらのメールの受信者を設定するには、カスタマーサクセスマネージャーに連絡して、**通知設定**で受信者を追加してください。この設定は、連携エラーとオーディエンス同期コンポーネントエラーの両方をカバーします。追加した受信者は、エラーに関連付けられたユーザーに加えてこれらのメールを受信します。

## データプライバシーに関する考慮事項 {#data-privacy-considerations}

{% alert important %}
このドキュメントは、法的助言を提供することを意図しておらず、法的助言として依拠することはできません。オーディエンス同期の使用には、特定の法的要件が適用されます。適用されるすべての法律に準拠して使用していることを確認するために、法律顧問の助言を求めてください。
{% endalert %}

広告トラッキング用のオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりすることや、[CCPA](https://oag.ca.gov/privacy/ccpa)に基づく「販売または共有の拒否」権などのプライバシー法に準拠することが必要になる場合があります。マーケターは、キャンバスのエントリ条件内でユーザーの適格性に関連するフィルターを実装する必要があります。以下のオプションが役立ちます。

[Braze SDKを通じてiOS IDFAを収集]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection)している場合、「広告トラッキング有効」フィルターを使用できます。値を`true`に設定すると、オプトインしたユーザーのみをオーディエンス同期の送信先に送信できます。

![エントリオーディエンスが「広告トラッキング有効がtrue」に設定されたキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合は、キャンバスのエントリ条件にフィルターとしてこれらを含める必要があります。

![エントリオーディエンスが「opted_in_marketingがtrueと等しい」に設定されたキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Brazeプラットフォーム内でこれらのデータ保護法に準拠する方法の詳細については、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance)を参照してください。

## 広告ターゲティングに関する同意の管理 {#managing-consent-for-ad-targeting}

広告主として、ユーザーの広告トラッキングまたはターゲティングに関する同意を管理する責任があります。

ユーザーに広告を配信するには、適用されるすべての法律および規制、ならびに広告プラットフォームのポリシーと要件を遵守する必要があります。同意を取得したユーザーのターゲティングと同期にのみBrazeを使用してください。

これらの広告プラットフォームのオーディエンスリストを最新の状態に保ち、同意を取り消したユーザーを削除するには、Audience Syncステップを使用して既存のオーディエンスリストからユーザーを削除するキャンバスを設定してください。