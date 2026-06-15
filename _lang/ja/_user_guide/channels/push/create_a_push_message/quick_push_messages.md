---
nav_title: "クイックプッシュメッセージ"
article_title: "クイックプッシュメッセージ"
alias: "/quick_push/"
description: "この記事では、クイックプッシュ編集エクスペリエンスを使用してプッシュキャンペーンまたはキャンバスを作成する際に知っておくべきことについて説明します。"
page_order: 4
---

# クイックプッシュメッセージ {#quick-push-messages}

> この記事では、クイックプッシュ編集エクスペリエンスを使用して、1つのコンポーザーから複数のプラットフォームとデバイスをターゲットにしたプッシュキャンペーンまたはキャンバスを作成する際に知っておくべきことについて説明します。

Brazeでプッシュキャンペーンまたはキャンバスを作成する際、複数のプラットフォームとデバイスを選択して、クイックプッシュと呼ばれる単一の編集エクスペリエンスですべてのプラットフォーム向けに1つのメッセージを作成できます。

## ユースケース {#use-cases}

この編集エクスペリエンスは、以下のユースケースに最適です。

- 複数のデバイスタイプ（iOSとAndroidの両方など）に送信する必要があるモバイルプッシュキャンペーンおよびキャンバスのメッセージステップ。
- 複数のプラットフォームに迅速かつ正確にターゲットする必要がある時間的制約のあるプッシュ通知で、プラットフォーム間でコンテンツが同じ場合（ニュース速報やライブゲームの更新など）。

## クイックプッシュキャンペーンまたはキャンバスの作成 {#creating-a-quick-push-campaign-or-canvas}

複数のプラットフォームとデバイスをターゲットにしたキャンペーンを作成するには：

1. キャンペーンを作成するか、キャンバスに[メッセージステップ]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/)を追加します。
2. **Push notification**を選択します。
3. 希望するプラットフォーム（Mobile、Web、Kindle）とモバイルデバイス（iOS、Android）を選択します。複数のデバイスを選択した場合、キャンペーンで多変量テストは利用できません。

### キャンペーンのプラットフォーム選択 {#selecting-platforms-for-a-campaign}
![モバイル、Web、Kindleなどの複数のプラットフォームと、iOSやAndroidなどの複数のデバイスを選択するプッシュキャンペーンのオプション。]({% image_buster /assets/img_archive/quick_push_1.png %})

### キャンバスステップのプラットフォーム選択 {#selecting-platforms-for-a-canvas-step}
![モバイル、Web、Kindleなどの複数のプラットフォームと、iOSやAndroidなどの複数のデバイスを選択するプッシュメッセージステップのオプション。]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. **Confirm**を選択します。**Confirm**を選択した後は、選択したプラットフォームやデバイスを変更できません。
5. キャンペーンまたはキャンバスの設定を続けます。

コンポーザーの見た目が通常とは少し異なります。何が異なるかについては、以下をお読みください。

### 異なる点 {#whats-different}

**Compose**タブでは、選択したすべてのプラットフォームとデバイスに対して、1つのタイトル、メッセージ、およびクリック時の動作を指定できます。

プレビューペインには、各プラットフォームでメッセージがどのように表示されるかの概要が表示されます。文字数制限に達する可能性がある箇所を把握するのに役立ちますが、キャンペーンを送信する前に必ず実際のデバイスでメッセージをテストしてください。

![iOS、Android、Webの3つのプッシュタイプに対して、1つのタイトル、メッセージ、およびクリック時の動作フィールドを持つ単一の編集ビュー。]({% image_buster /assets/img_archive/quick_push_2.png %})

**Assets**セクションでは、各プラットフォームに表示する画像を選択またはアップロードします。デバイスによって画像や文字数の仕様が異なることに注意してください。詳しくは[プッシュメッセージと画像のフォーマット]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)を参照してください。

![プッシュアイコン画像、iOS通知画像、Android通知画像、Web通知画像のフィールドを持つ単一編集ビューのアセットセクション。]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

その後、通常通りプッシュキャンペーンの設定を完了します。詳しくは[プッシュキャンペーンの作成]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/)を参照してください。

## 知っておくべきこと {#things-to-know}

### 通知タイプ {#notification-type}

通知タイプはデフォルトで「標準プッシュ」に設定されており、変更できません。Push Storiesやインライン画像（Android）など、別のプッシュを作成したい場合は、デバイスタイプごとに個別のキャンペーンを作成してください。

### 多変量テスト {#multivariate-testing}

モバイルプラットフォームで複数のデバイス（iOSとAndroidの両方など）を選択した場合、キャンペーンで多変量テストは利用できません。多変量テストを実行したい場合は、デバイスタイプごとに個別のキャンペーンを作成してください。

### デバイス固有の設定 {#device-specific-settings}

エディターでプラットフォーム固有の設定を編集できます。これには、[プッシュアクションボタン]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons/)、通知チャネルとグループ、TTL、表示優先度、サウンドなどの設定が含まれます。

クイックプッシュキャンペーンを使用してiOSとAndroidの両方をターゲットにする場合、プッシュアクションボタンはサポートされていないことに注意してください。デバイス固有の設定の詳細については、以下の記事コレクションを参照してください。

- [iOSオプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/)
- [Androidオプション]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/)