---
nav_title: "マルチプラットフォームプッシュメッセージ"
article_title: "マルチプラットフォームメッセージ"
alias: "/multiple_platform_push/"
description: "この記事では、複数のプラットフォームを選択してプッシュCampaignまたはCanvasを作成する際に知っておくべきことについて説明します。"
page_order: 4
---

# マルチプラットフォームプッシュメッセージ {#multiple-platform-push-messages}

> この記事では、1つのコンポーザーから複数のプラットフォームとデバイスをターゲットにするプッシュCampaignまたはCanvasを作成する際に知っておくべきことについて説明します。

BrazeでプッシュCampaignまたはCanvasを作成する際、複数のプラットフォームとデバイスを選択して、単一の編集エクスペリエンスですべてのプラットフォーム向けに1つのメッセージを作成できます。

## ユースケース {#use-cases}

この編集エクスペリエンスは、以下のユースケースに最適です。

- 複数のデバイスタイプ（iOSとAndroidの両方など）に送信する必要があるモバイルプッシュCampaignおよびCanvasメッセージステップ。
- 複数のプラットフォームを迅速かつ正確にターゲットにする必要がある時間的制約のあるプッシュ通知で、プラットフォーム間でコンテンツが同じ場合（ニュース速報やライブゲームの更新など）。

## マルチプラットフォームプッシュCampaignまたはCanvasの作成 {#creating-a-multiple-platform-push-campaign-or-canvas}

複数のプラットフォームとデバイスをターゲットにするCampaignを作成するには：

1. Campaignを作成するか、Canvasに[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)を追加します。
2. **プッシュ通知**を選択します。
3. 希望するプラットフォーム（モバイル、Web、Kindle）とモバイルデバイス（iOS、Android）を選択します。複数のデバイスを選択した場合、Campaignで多変量テストは利用できません。

### Campaignのプラットフォーム選択 {#selecting-platforms-for-a-campaign}
![モバイル、Web、Kindleなどの複数のプラットフォームと、iOSやAndroidなどの複数のデバイスを選択するオプション。]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Canvasステップのプラットフォーム選択 {#selecting-platforms-for-a-canvas-step}
![プッシュメッセージステップでモバイル、Web、Kindleなどの複数のプラットフォームと、iOSやAndroidなどの複数のデバイスを選択するオプション。]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. **確認**を選択します。**確認**を選択した後は、選択したプラットフォームやデバイスを変更できません。
5. CampaignまたはCanvasの設定を続けます。

## マルチプラットフォーム多変量テストの実行 {#running-a-multi-platform-multivariate-test}

多変量テストはマルチプラットフォームCampaignでサポートされています。単一プラットフォームのCampaignと同様に、バリアント名の横にあるプラスアイコンを選択するだけです。多変量テストの作成については[ガイドをお読みください]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/)。また、[BrazeAI<sup>TM</sup>バリアント選択]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection/)を活用して、エンゲージメントを自動化し最大化することをお勧めします。

![簡単なマルチプラットフォーム多変量テスト]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## 知っておくべきこと {#things-to-know}

### 統合メッセージング {#unified-messaging}
**作成**タブでは、選択したすべてのプラットフォームとデバイスに対して、1つのタイトル、メッセージ、およびクリック時の動作を指定できます。

プレビューペインには、各プラットフォームでメッセージがどのように表示されるかの概要が表示されます。文字数制限に達する可能性がある箇所を把握するのに役立ちますが、Campaignを送信する前に必ず実際のデバイスでメッセージをテストしてください。

![iOS、Android、Webの3つのプッシュタイプに対して、1つのタイトル、メッセージ、クリック時の動作フィールドを持つ単一編集ビュー。]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### 個別のアセット {#separate-assets}
**アセット**セクションでは、各プラットフォームに表示する画像を選択またはアップロードします。デバイスによって画像や文字数の仕様が異なることに注意してください。詳しくは[プッシュメッセージと画像のフォーマット]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)を参照してください。

![プッシュアイコン画像、iOS通知画像、Android通知画像、Web通知画像のフィールドを持つ単一編集ビューのアセットセクション。]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### 通知タイプ {#notification-type}

通知タイプはデフォルトで「標準プッシュ」に設定されており、変更できません。Push Storiesやインライン画像（Android）など、別のプッシュを作成する場合は、デバイスタイプごとに個別のCampaignを作成してください。

### デバイス固有の設定 {#device-specific-settings}

エディターでプラットフォーム固有の設定を編集できます。これには、[プッシュアクションボタン]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/)、通知チャネルとグループ、TTL、表示優先度、サウンドなどの設定が含まれます。

デバイス固有の設定の詳細については、以下の記事コレクションを参照してください。

- [iOSオプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/)
- [Androidオプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/)

### Push Stories

Push Storiesは、AndroidとiOSでのみマルチプラットフォームで利用できます。送信先のプラットフォームとしてWebまたはKindleを選択した場合、このオプションは利用できません。