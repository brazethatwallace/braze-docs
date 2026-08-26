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

すべてのBraze顧客は、Google および Facebook へのオーディエンス同期にすぐにアクセスできます。アクションクレジットをご利用の顧客は、すべてのオーディエンス同期パートナーにアクセスできます。アクションクレジットをご利用でない顧客が追加のオーディエンス同期の送信先を利用するには、Audience Sync Pro を購入してください。詳細については、Brazeアカウントマネージャーにお問い合わせください。

## ユースケース {#use-cases}

- 自社チャネルと有料チャネルを使用して高価値ユーザーをターゲティングし、追加の購入やエンゲージメントを促進します。
- 高価値ユーザーの類似オーディエンスを作成し、新規ユーザー獲得のコストとコンバージョンを最適化します。
- 他のマーケティングチャネルへの反応が低いユーザーに対して、広告でリターゲティングします。
- 抑制オーディエンスを作成し、すでにブランドのロイヤルな消費者であるユーザーに広告が配信されないようにします。

## 概要 {#overview}

<style>
table td {
    word-break: break-word;
}
</style>

| 送信先 | オーディエンスメンバーのマッチにかかる時間 | レート制限 | 類似オーディエンスまたはアクタライク | ヒント |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync) | 最大24時間 | 1分あたり250,000リクエスト。5秒ごとにバッチ処理され、自動リトライが行われます。 | はい | {::nomarkdown}<ul><li>Criteoは最大1,000件の広告オーディエンスをサポートしています。</li><li>最小オーディエンスサイズは500で、推奨は20,000以上です。</li></ul>{:/} |
| [FacebookまたはInstagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync) | 最大24時間 | 1時間あたり190,000広告アカウント | はい | {::nomarkdown}<ul><li>Facebookは最大500件の広告オーディエンスをサポートしています。</li><li>Facebookのオーディエンスには最低1,000人のユーザーが必要です。</li></ul>{:/} |
| [Google 広告またはYouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) | 6〜12時間 | Googleのフィードバックに基づいて、5秒ごとにバッチ処理され自動リトライが行われます | いいえ | {::nomarkdown}<ul><li><b>カスタマーマッチ：</b>モバイル広告ID、またはメールアドレスか電話番号を使用します。</li><li>Google オーディエンスでは広告配信を開始するために最低5,000人のユーザーが必要です。</li><li>オーディエンスサイズは、最低1,000人のユーザーに達するまでゼロと表示されます。</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync) | 48時間 | LinkedInは1秒あたり10件のクエリと1リクエストあたり100,000人のユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | AI予測オーディエンス | {::nomarkdown}<ul><li>最小オーディエンスサイズは、位置情報ターゲティングを考慮して300メンバーです。</li><li>LinkedInのマッチ率はBrazeダッシュボードに表示されます。</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync) | 24〜48時間 | Pinterestは1秒あたり7件のクエリと1リクエストあたり1,900人のユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | はい | Pinterestのオーディエンスには最低100人のユーザーが必要です。 |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync) | N/A | Snapchatは1秒あたり10件のクエリと1リクエストあたり100,000人のユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | はい | Snapchatは最大1,000件の広告オーディエンスをサポートしています。 |
| [The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync) | 最大24時間 | N/A | はい | {::nomarkdown}<ul><li>The Trade DeskのCRMオーディエンスには最小オーディエンスサイズの制限はありません。</li><li>The Trade Deskがサポートするオーディエンス数に制限はありません。</li><li>地域がEUに設定されたオーディエンスに同期する場合、電話番号はサポートされません。</li></ul>{:/} |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync) | 24〜48時間 | TikTokは1秒あたり50件のクエリと1リクエストあたり10,000人のユーザーを処理します。Brazeは5秒ごとにユーザーをバッチ処理します。 | はい | {::nomarkdown}<ul><li>TikTokは最大400件の広告オーディエンスをサポートしています。</li><li>TikTokのオーディエンスでは広告配信を開始するために最低1,000人のユーザーが必要です。</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="概要" }
<sup>レート制限に達した場合、Brazeは13時間にわたって同期のリトライを行います。</sup>

## 仕組み {#how-it-works}

GoogleやFacebookへのAudience Syncを使用するには、**テクノロジーパートナー**ページでパートナーを検索して広告アカウントを接続します。

![Facebookテクノロジーパートナー。]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Google Adsテクノロジーパートナー。]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

広告アカウントを接続した後、Audience Syncステップを含むキャンバスを作成できます。

![ユーザージャーニーにAudience Syncステップを追加するためのキャンバスコンポーネントメニュー。]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

次に、オーディエンスを同期するパートナーを選択します。

![Audience SyncステップでAudience Syncパートナーを選択するオプション。]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

各パートナーについて、Audience Syncステップの一部として以下を設定する必要があります。

- 広告アカウント
- オーディエンス
- ユーザーを追加または削除するアクション
- マッチするフィールド

Brazeは、ユーザーがキャンバス内のAudience Syncステップに入るとすぐに同期することに注意してください。

各Audience Sync送信先について、Brazeが送信できるフィールドの要件はパートナーごとに異なる場合があります。詳細については、各パートナーのドキュメントを参照してください。

### Audience Sync Pro

TikTok、Pinterest、Snapchat、CriteoなどのAudience Sync Proパートナーを使用するには、**テクノロジーパートナー**ページの**Audience Sync Pro**セクションで、Audience Sync Proの購入割り当てに基づいてパートナーを選択できます。

![まだパートナーが選択されていないAudience Sync Pro。]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

まず、使用するパートナーを選択します。Audience Sync Proを購入するたびに、3つのAudience Sync Pro送信先が割り当てられ、ダッシュボード内の各ワークスペースで利用できます。

![Brazeに接続するパートナーを最大3つ選択するオプション。]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Audience Sync Proの送信先を選択した後、パートナータイルをクリックして、選択したパートナーの広告アカウントを接続します。

![Audience SyncのパートナーとしてSnapchatとTikTokが選択されている例。]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![「Snapchatアカウント1件の接続に成功しました」というメッセージが表示されたSnapchat Audience Sync設定。]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

最後に、このAudience Sync Pro送信先を使用してキャンバスでAudience Syncステップを作成します。

### バッチ処理とレイテンシー {#batching-and-latency}

ユーザーがキャンバスのAudience Syncステップに入ると、BrazeはパートナーAPIにディスパッチする前にユーザー更新を集約するバッチ処理システムにキューイングします。バッチは以下のいずれかが発生したときに送信されます。

- **バッチがサイズ制限に達した場合。**これはパートナーによって異なります。
  - デフォルトでは最大2,000ユーザーをサポートします
  - Google Adsは最大10,000ユーザーをサポートします
  - FacebookとTikTokは最大2,000ユーザーをサポートします
- **バッチレイテンシータイマーが期限切れになった場合。**デフォルトは1時間ですが、パートナーごとに設定可能です。例えば、The Trade Deskは10分を使用します。

大量のキャンバスはバッチがより早く満たされるため、より早くディスパッチされる場合があります。少量のキャンバスはレイテンシータイマーが期限切れになるまで待機します。Brazeは固定のディスパッチ時間を保証しません。タイミングはバッチサイズと設定されたレイテンシーウィンドウに依存します。

Brazeは監視とトラブルシューティングのために内部ログにディスパッチアクティビティを記録しますが、これらのタイムスタンプはクエリ可能なフィールドとしては公開されません。BrazeがパートナーAPIにバッチをディスパッチした後、パートナーは独自のサービスレベルアグリーメントに従ってオーディエンスの更新を処理します（通常6〜48時間）。

Brazeは、個々のユーザーがマッチまたは同期されたことについてパートナーからの確認を受け取りません。パートナーの応答は受信のHTTP確認応答であり、マッチの確認ではありません。オーディエンスが追加されたことを確認するには、パートナーの広告プラットフォーム（Google Ads Audience ManagerやMeta Business Managerなど）を確認してください。

### Audience Syncエラーメール {#audience-sync-error-emails}

エラーがパートナー連携全体に関連する場合（認証の問題など）、連携を接続したユーザーにメールが送信されます。そのユーザーが存在しなくなった場合、管理者がメールを受信します。

エラーがキャンバスのAudience Syncコンポーネントの問題に関連する場合（「オーディエンスが存在しません」など）、キャンバスを設定したユーザーにメールが送信されます。そのユーザーが存在しなくなった場合、会社の管理者にフォールバックされます。

これらのメールの受信者を設定するには、カスタマーサクセスマネージャーに連絡して**通知設定**で受信者を追加してください。この設定は、連携エラーとAudience Syncコンポーネントエラーの両方をカバーします。追加した受信者は、エラーに関連付けられたユーザーに加えてこれらのメールを受信します。

## データプライバシーに関する考慮事項 {#data-privacy-considerations}

{% alert important %}
このドキュメントは、法的アドバイスを提供することを目的としたものではなく、法的アドバイスとして依拠することはできません。オーディエンス同期の使用は、特定の法的要件に従います。適用されるすべての法律を遵守して使用するために、法律顧問の助言を求めてください。
{% endalert %}

広告トラッキング用のオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めるか除外し、[CCPA](https://oag.ca.gov/privacy/ccpa) における「販売または共有の拒否」権などのプライバシー法に準拠することが必要な場合があります。マーケターは、キャンバスのエントリ条件内でユーザーの適格性に関する適切なフィルターを実装する必要があります。以下のオプションが役立ちます。

[Braze SDKを通じてiOS IDFAを]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations)収集している場合、「広告トラッキング有効」フィルターを使用できます。値として`true`を選択すると、オプトインしたユーザーのみをオーディエンス同期の送信先に送信できます。

![エントリオーディエンスが「広告トラッキング有効がtrue」に設定されたキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

`opt-ins`、`opt-outs`、`Do Not Sell Or Share`、またはその他の関連するカスタム属性を収集している場合、キャンバスのエントリ条件内にフィルターとしてこれらを含める必要があります。

![エントリオーディエンスが「opted_in_marketingがtrue」に設定されたキャンバス。]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Brazeプラットフォーム内でこれらのデータ保護法に準拠する方法について詳しくは、[データ保護テクニカルアシスタンス]({{site.baseurl}}/dp-technical-assistance)を参照してください。

## 広告ターゲティングに関する同意の管理 {#managing-consent-for-ad-targeting}

広告主として、ユーザーの広告トラッキングまたはターゲティングに関する同意を管理する責任があります。

ユーザーに広告を配信するには、適用されるすべての法律および規制、ならびに広告プラットフォームのポリシーおよび要件に準拠する必要があります。同意を得たユーザーのターゲティングおよび同期にのみBrazeを使用してください。

これらの広告プラットフォームのオーディエンスリストを最新の状態に保ち、同意を撤回したユーザーを削除するには、Audience Syncステップを使用して既存のオーディエンスリストからユーザーを削除するキャンバスを設定してください。