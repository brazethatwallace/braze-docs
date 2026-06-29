---
nav_title: KakaoTalkクリックトラッキング
article_title: KakaoTalkクリックトラッキング
page_order: 3
description: "このページでは、KakaoTalkメッセージでクリックトラッキングを有効にする方法、短縮リンクのテスト、トラッキングリンクでのカスタムドメインの使用などについて説明します。"
page_type: reference
alias: /kakaotalk_click_tracking/
channel:
 - KakaoTalk
---

# KakaoTalkクリックトラッキング {#kakaotalk-click-tracking}

> このページでは、KakaoTalkメッセージでクリックトラッキングを有効にする方法、短縮リンクのテスト、トラッキングリンクでのカスタムドメインの使用などについて説明します。

KakaoTalkクリックトラッキングを有効にすると、BrazeはURLを自動的に短縮し、トラッキングメカニズムを追加して、クリックをリアルタイムで記録します。このデータにより、クリック行動に基づくユーザーのセグメンテーションや、特定のクリックに応じたメッセージのトリガーなど、よりターゲットを絞ったセグメンテーションおよびリターゲティング戦略を構築できます。

KakaoTalkクリックトラッキングは、テキスト、画像、リストアイテムメッセージで使用できます。ボタン内のリンクや画像のクリック時アクションをサポートしています。また、Liquidやカスタムドメインを使用してURLをパーソナライズすることもできます。

## 仕組み {#how-it-works}

KakaoTalkクリックトラッキングの設定は、メッセージ作成画面の**Link options**セクションで管理できます。有効にすると、URLはデフォルトのBrazeドメイン（`https://brz.ai`）またはサブスクリプショングループに指定されたカスタムドメインを使用して短縮され、ユーザーごとにパーソナライズされます。

`http://` または `https://` で始まるURLはすべて短縮されます。1つのメッセージに最大25個のURLを含めることができます。Liquidパーソナライゼーション（ユーザーレベルのトラッキングやUTMパラメーターなど）を含む短縮URLは、2か月間有効です。

## クリックトラッキングの設定 {#set-up-click-tracking}

### テキストメッセージ {#text-messages}

テキストメッセージのクリックトラッキングを設定するには：

1. **Text**メッセージを作成し、テキストフィールドまたはボタンにURLを追加します。
2. メッセージ作成画面の**Link options**セクションで、**Click Tracking**がチェックされていることを確認します。クリックトラッキングは、すべての新しいメッセージでデフォルトで有効になっています。

![Link optionsセクションでClick TrackingがチェックされているKakaoTalkテキストメッセージ作成画面。]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

### 画像メッセージ {#image-messages}

画像メッセージのクリックトラッキングを設定するには：

1. **Image**メッセージを作成し、クリック時の動作をURLを開くように設定します。
2. URLフィールドにURLを入力します。
3. メッセージ作成画面の**Link options**セクションで、**Click Tracking**がチェックされていることを確認します。

### リストアイテムメッセージ {#list-item-messages}

リストアイテムメッセージのクリックトラッキングを設定するには：

1. **List item**メッセージを作成し、任意のアイテムの**Website URL**フィールドにURLを追加します。
2. メッセージ作成画面の**Link options**セクションで、**Click Tracking**がチェックされていることを確認します。

## カスタムドメイン {#custom-domains}

KakaoTalkクリックトラッキングでは、独自のドメインを使用して短縮URLの外観をパーソナライズし、一貫したブランドイメージを表現できます。詳細については、[カスタムドメイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/custom_domains)を参照してください。

## URL内のLiquidパーソナライゼーション {#liquid-personalization-in-urls}

Brazeメッセージ作成画面内で直接URLを動的に構築できるため、URLにダイナミックUTMパラメーターを追加したり、ユーザーにユニークなリンクを送信したりできます（放棄カートへの誘導や、再入荷した特定の製品への誘導など）。

URLは、サポートされているLiquidパーソナライゼーションタグを使用して動的に生成できます。

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

以下の例に示すように、カスタム定義のLiquid変数を短縮することもできます。

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

BrazeはLiquidによってレンダリングされたURL（APIトリガープロパティに含まれるURLを含む）を短縮します。たとえば、{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %}が有効なURLを表す場合、BrazeはKakaoTalkメッセージを送信する前にそのURLを短縮してトラッキングします。

## テスト {#testing}

CampaignまたはCanvasを起動する前に、まずメッセージをプレビューしてテストすることがベストプラクティスです。これを行うには、**Test**タブに移動して、コンテンツテストグループまたは個々のユーザーにKakaoTalkメッセージをプレビューして送信します。

プレビューは、関連するパーソナライゼーションと短縮URLで更新されます。

{% alert important %}
アクティブなCanvas内で下書きが作成された場合、短縮URLは生成されません。実際の短縮URLは、Canvasの下書きがアクティブになったときに生成されます。
{% endalert %}

## レポート {#reporting}

KakaoTalkパフォーマンステーブルには、バリアントごとのクリックイベント数と関連するクリック率を示す**Total Clicks**列が含まれています。KakaoTalk指標の詳細については、[KakaoTalkレポート]({{site.baseurl}}/kakaotalk_reporting)を参照してください。

クリックデータは分析ダッシュボードに自動的にレポートされます。

## ユーザーのリターゲティング {#retarget-users}

KakaoTalkメッセージ内のURLをクリックしたユーザーを、以下のセグメンテーションフィルターとトリガーを使用してリターゲティングできます。

- アクションベースのトリガー
    - Interact with Campaign
    - Interact with Step

- セグメンテーションフィルター
    - Clicked/Opened Campaign
    - Clicked/Opened Campaign or Canvas with Tag
    - Clicked/Opened Step

## よくある質問 {#frequently-asked-questions}

### テスト送信で受け取るリンクは実際のURLですか？ {#are-the-links-i-receive-when-test-sending-real-urls}

はい、テスト送信時に実際のURLが生成されます。ただし、起動されたCampaignで送信される正確なURLは、テスト送信で送信されたものとは異なる場合があります。

### URLが短縮される前にUTMパラメーターを追加できますか？ {#can-i-add-utm-parameters-to-a-url-before-it-is-shortened}

はい、静的パラメーターとダイナミックパラメーターの両方を追加できます。

### 短縮URLはどのくらいの期間有効ですか？ {#how-long-do-shortened-urls-remain-valid}

パーソナライズされたURLは、URL登録時から2か月間有効です。

### URLを短縮するためにBraze SDKをインストールする必要がありますか？ {#does-the-braze-sdk-need-to-be-installed-in-order-to-shorten-urls}

いいえ、クリックトラッキングはSDK統合なしで機能します。

### URLをクリックした個々のユーザーを特定できますか？ {#do-i-know-which-individual-users-are-clicking-on-a-url}

はい。クリックトラッキングが有効になっている場合、[KakaoTalkリターゲティングフィルター](#retargeting-users)を使用して、URLをクリックしたユーザーをリターゲティングできます。

### クリックトラッキングはディープリンクやユニバーサルリンクで機能しますか？ {#does-click-tracking-work-with-deep-links-or-universal-links}

クリックトラッキングはWeb URLに適用されます。ディープリンクについては、KakaoTalkのボタンのクリック時アクションタイプとしてディープリンクを直接設定できます。これらはURL短縮やクリックトラッキングを経由しません。BranchやAppsFlyerなどのプロバイダーのユニバーサルリンクを使用する場合、それらは短縮できますが、発生する可能性のある問題（アトリビューションの破損やリダイレクトの失敗など）についてBrazeはトラブルシューティングできません。