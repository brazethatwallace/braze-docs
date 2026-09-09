---
nav_title: "マルチプラットフォームプッシュメッセージ"
article_title: "マルチプラットフォームメッセージ"
alias: "/multiple_platform_push/"
description: "この記事では、複数のプラットフォームを選択してプッシュキャンペーンまたはキャンバスを作成する際に知っておくべきことについて説明します。"
page_order: 4
---

# マルチプラットフォームプッシュメッセージ {#multiple-platform-push-messages}

> この記事では、1つのコンポーザーから複数のプラットフォームとデバイスをターゲットにするプッシュキャンペーンまたはキャンバスを作成する際に知っておくべきことについて説明します。

Brazeでプッシュキャンペーンまたはキャンバスを作成する際、複数のプラットフォームとデバイスを選択して、単一の編集エクスペリエンスですべてのプラットフォーム向けに1つのメッセージを作成できます。

## ユースケース {#use-cases}

この編集エクスペリエンスは、以下のユースケースに最適です。

- 複数のデバイスタイプ（iOSとAndroidの両方など）に送信する必要があるモバイルプッシュキャンペーンおよびキャンバスのメッセージステップ。
- 複数のプラットフォームを迅速かつ正確にターゲットにする必要がある緊急性の高いプッシュ通知で、プラットフォーム間でコンテンツが同一の場合（速報ニュースやライブゲームの更新など）。

## マルチプラットフォームのプッシュキャンペーンまたはキャンバスの作成 {#creating-a-multiple-platform-push-campaign-or-canvas}

複数のプラットフォームとデバイスをターゲットとするキャンペーンを作成するには、以下の手順に従います。

1. キャンペーンを作成するか、キャンバスに[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step)を追加します。
2. **プッシュ通知**を選択します。
3. 目的のプラットフォーム（モバイル、Web、Kindle）とモバイルデバイス（iOS、Android）を選択します。複数のデバイスを選択した場合、キャンペーンで多変量テストは利用できません。

### キャンペーンのプラットフォーム選択 {#selecting-platforms-for-a-campaign}
![プッシュキャンペーンで複数のプラットフォーム（モバイル、Web、Kindle）と複数のデバイス（iOS、Android）を選択するオプション。]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### キャンバスステップのプラットフォーム選択 {#selecting-platforms-for-a-canvas-step}
![プッシュメッセージステップで複数のプラットフォーム（モバイル、Web、Kindle）と複数のデバイス（iOS、Android）を選択するオプション。]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. **確認**を選択します。**確認**を選択すると、選択したプラットフォームやデバイスを変更することはできません。
5. キャンペーンまたはキャンバスの設定を続行します。

## マルチプラットフォームの多変量テストを実行する {#running-a-multi-platform-multivariate-test}

多変量テストはマルチプラットフォームキャンペーンでサポートされています。単一プラットフォームのキャンペーンと同様に、バリアント名の横にあるプラスアイコンを選択します。設定手順については、[多変量テストとA/Bテストを作成する]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests)を参照してください。

バリアントを自動的に最適化するには、[BrazeAI<sup>TM</sup>でA/Bテストを最適化する]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)を参照してください。

![マルチプラットフォームの多変量テストを簡単に実施]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## 知っておくべきこと {#things-to-know}

### 統一メッセージング {#unified-messaging}
**作成**タブでは、選択したすべてのプラットフォームとデバイスに対して、1つのタイトル、メッセージ、クリック時の動作を指定できます。

プレビューペインには、各プラットフォームでメッセージがどのように表示されるかの概要が表示されます。文字数制限に達する可能性がある箇所を把握するのに役立ちますが、キャンペーンを送信する前に必ず実際のデバイスでメッセージをテストしてください。

![iOS、Android、Webの3つのプッシュタイプに対して、1つのタイトル、メッセージ、クリック時の動作フィールドを持つ単一編集ビュー。]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### 個別のアセット {#separate-assets}
**アセット**セクションでは、各プラットフォームに表示する画像を選択またはアップロードします。デバイスごとに画像やテキストの仕様が異なることに留意してください。詳しくは[プッシュメッセージと画像のフォーマット]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)を参照してください。

![プッシュアイコン画像、iOS通知画像、Android通知画像、Web通知画像のフィールドを持つ単一編集ビューのアセットセクション。]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### 通知タイプ {#notification-type}

通知タイプはデフォルトで「標準プッシュ」に設定されており、変更できません。Push Storiesやインライン画像（Android）など、別のプッシュを作成する場合は、デバイスタイプごとに個別のキャンペーンを作成してください。

### デバイス固有の設定 {#device-specific-settings}

エディターでプラットフォーム固有の設定を編集できます。これには、[プッシュアクションボタン]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons)、通知チャネルとグループ、TTL、表示優先度、サウンドなどの設定が含まれます。

デバイス固有の設定の詳細については、以下の記事コレクションを参照してください。

- [iOSオプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Androidオプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Push Storiesは、AndroidとiOSでのみマルチプラットフォームで利用できます。送信先のプラットフォームとしてWebまたはKindleを選択した場合、このオプションは利用できません。