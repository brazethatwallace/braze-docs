---
nav_title: SDKによるデータ収集
article_title: SDKによるデータ収集
page_order: 1
page_type: reference
description: "このリファレンス記事では、パーソナライズされた連携、自動的に収集される連携を通じてSDKによって収集されるデータについて説明します。"
---

# SDKによるデータ収集 {#sdk-data-collection}

> Braze SDKをお客様のアプリやサイトと連携すると、Brazeは特定タイプのデータを自動的に収集します。このデータには、当社のプロセスに必須のものと、お客様が必要に応じてオン/オフを切り替えられるものがあります。セグメンテーションやメッセージングをさらに強化するために、Brazeを設定して追加タイプのデータを収集することもできます。

Brazeは、柔軟にデータ収集ができるように設計されています。このため、Braze SDKを次のように連携できます。

- **[最小限の連携](#minimum-integration):** Brazeは、Brazeサービスと通信するために必要なデータを自動的に収集します。
- **[デフォルトで収集されるオプションのデータ]({{site.baseurl}}/developer_guide/getting_started/sdk_overview):** Brazeは、お客様のほとんどのユースケースで広く役立つデータを自動的に取得します。Brazeサービスとの通信に必要でない場合は、このデータの自動収集を無効にできます。
- **[デフォルトで収集されないオプションのデータ](#data-not-collected-by-default):** Brazeは、特定のユースケースにとって有用なデータを取得しますが、広範なコンプライアンス上の理由から、収集が自動的に有効になることはありません。ユースケースに適している場合にはこのデータを収集することを選択できます。
- **[パーソナライズされた連携](#personalized-integration):** Brazeでは、デフォルトのオプションデータに加えて、データを柔軟に収集できます。

## 最小限のインテグレーション {#minimum-integration}

SDKを初期化する際にBrazeが生成・受信する、厳密に必要なデータを以下に示します。このデータは設定変更ができず、コアプラットフォーム機能に不可欠です。セッション開始とセッション終了を除き、その他の自動トラッキングデータはデータポイント使用量にカウントされません。

| 属性 | 説明 | 収集される理由 |
| --------- | ----------- | ------------------ |
| App-Version-Name /<br> App-Version-Code | 最新のアプリバージョン | この属性は、アプリバージョンの互換性に関連するメッセージを正しいデバイスに送信するために使用されます。サービスの中断やバグをユーザーに通知するために使用できます。 |
| Country | IPアドレスのジオロケーションで特定される国。IPアドレスのジオロケーションが利用できない場合は、[デバイスロケール](#optional-data-collected-by-default)で特定されます。値は、SDKが`setCountry`で直接設定したものになる場合もありますが、SDKまたはAPIを通じて属性値を渡すとデータポイントが記録される点に注意してください。**SDKメソッド、REST API、またはCSVアップロードを通じて手動で国が設定された後は、SDKはこの値を自動的に更新しなくなります。**| この属性は、位置情報に基づいてメッセージをターゲティングするために使用されます。 |
| Device ID | デバイス識別子（ランダムに生成された文字列） | この属性は、ユーザーのデバイスを区別し、正しいデバイスにメッセージを送信するために使用されます。 |
| OS and OS version | 現在報告されているデバイスまたはブラウザーとデバイスまたはブラウザーのバージョン | この属性は、互換性のあるデバイスにのみメッセージを送信するために使用されます。セグメンテーション内でユーザーにアプリバージョンのアップグレードをターゲティングするためにも使用できます。 |
| Session start and session end | ユーザーが統合されたアプリまたはサイトの使用を開始した時点 | Braze SDKは、Brazeダッシュボードがユーザーエンゲージメントやその他の分析を計算するために使用するセッションデータを報告します。これはユーザーを理解するために不可欠です。セッション開始とセッション終了がアプリまたはサイトによって呼び出されるタイミングは、開発者が設定可能です（[Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android)、[iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift)、[Web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)）。 |
| SDK message interaction data | プッシュの直接開封、アプリ内メッセージのインタラクション、Content Cardsのインタラクション | この属性は、メッセージが受信されたか、送信が重複していないかを確認するなど、品質管理の目的で使用されます。 |
| SDK version | 現在のSDKバージョン | この属性は、互換性のあるデバイスにのみメッセージを送信し、サービスの中断を防ぐために使用されます。 |
| Session ID and session timestamp | セッション識別子（ランダムに生成された文字列）とセッションタイムスタンプ | ユーザーが新しいセッションを開始しているか既存のセッションを継続しているかを判断し、このユーザーを対象としたメッセージの再適格性を判断するために使用されます。<br><br>アプリ内メッセージやContent Cardsなどの特定のメッセージングチャネルは、セッション開始時にデバイスと同期されます。その後、バックエンドは最後にBrazeサーバーに接続した時点に関連するデータ（デバイスが保存して返送するもの）を使用して、ユーザーが新しいメッセージの対象かどうかを判断します。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="最小限のインテグレーション" }

### 算出指標 {#calculated-metrics}

Brazeは3つのインプットから算出指標を生成します：[SDKトラッキングデータ](#minimum-integration)（例：[セッション開始とセッション終了]({{site.baseurl}}/developer_guide/analytics/tracking_sessions)）、[非SDKチャネルのメッセージインタラクションデータ]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)、および[Braze派生レポートフィールド]({{site.baseurl}}/user_guide/analytics/metrics_glossary)です。これらの値はBrazeサービスによって生成されるため、ユーザープロファイルにはSDKトラッキングデータとBraze生成データの両方が含まれる場合があります。

算出指標には、チャネルベースの指標（[レポート指標用語集]({{site.baseurl}}/user_guide/analytics/metrics_glossary)に記載）および以下の属性が含まれます。

| 属性                                      | 説明                                                          |
|------------------------------------------------|----------------------------------------------------------------------|
| First used app                                 | 時刻                                                                 |
| Last used app                                  | 時刻                                                                 |
| Total session count                            | 数値                                                               |
| Clicked カード                                   | 数値                                                               |
| Last received any message                      | 時刻                                                                 |
| Last received email campaign                   | 時刻                                                                 |
| Last received push campaign                    | 時刻                                                                 |
| Number of フィードバック items                       | 数値                                                               |
| Number of sessions in the last Y days          | 数値と時刻                                                      |
| Received message from campaign                 | ブール値。このフィルターは、以前のキャンペーンを受信したかどうかに基づいてユーザーをターゲティングします。 |
| Received message from campaign with tag        | ブール値。このフィルターは、現在タグが付いているキャンペーンを受信したかどうかに基づいてユーザーをターゲティングします。 |
| Retarget campaign                              | ブール値。このフィルターは、過去に特定のメール、プッシュ、またはアプリ内メッセージを開封またはクリックしたかどうかに基づいてユーザーをターゲティングします。 |
| Uninstalled                                    | ブール値と時刻                                                     |
{: .reset-td-br-1 .reset-td-br-2 aria-label="算出指標" }

最小限のインテグレーションとは、[最小限のインテグレーション](#minimum-integration)に記載されている必要なデータのみを収集し、[オプションのSDKデータ収集をブロック](#optional-data-collected-by-default)することで[デフォルトで収集されるオプションデータ](#optional-data-collected-by-default)をオプトアウトすることを意味します。

{% alert important %}
最小限のインテグレーションを希望し、mParticle、セグメント、Tealium、またはGTMを使用している場合は、以下の点に注意してください。
- **モバイルプラットフォーム**: これらの設定に対してコードを手動で更新する必要があります。mParticleとセグメントは、それぞれのプラットフォームを通じてこれを行う方法を提供していません。
- **Web**: 最小限のインテグレーション設定を可能にするために、Brazeインテグレーションはネイティブで行う必要があります。タグマネージャーは、それぞれのプラットフォームを通じてこれを行う方法を提供していません。
{% endalert %}

## デフォルトで収集されるオプションデータ {#optional-data-collected-by-default}

最小統合データに加えて、SDK統合を初期化すると、以下の属性がBrazeによって自動的にキャプチャされます。これらの属性の収集を[オプトアウト]({{site.baseurl}}/developer_guide/getting_started/sdk_overview)して、最小統合のみにすることができます。

| 属性               | プラットフォーム          | 説明                                                                        | 収集される理由                                                                                                                                                      |
|-------------------------|-------------------|------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ブラウザ名            | Web               | ブラウザの名前                                                                | この属性は、互換性のあるブラウザにのみメッセージを送信するために使用されます。ブラウザベースのセグメンテーションにも使用できます。                                     |
| デバイスロケール           | Android、iOS、Web | デバイスのデフォルトロケール                                                   | この属性は、ユーザーの優先言語にメッセージを翻訳するために使用されます。                                                                                            |
| 最新のデバイスロケール           | Android、iOS、Web | デバイスの最新のデフォルトロケール                                                   | この属性はユーザーのデバイス設定から取得され、ユーザーの優先言語にメッセージを翻訳するために使用されます。`Most Recent Location` 属性とは独立しています。                                                                                            |
| デバイスモデル            | Android、iOS      | デバイスの特定のハードウェア                                                | この属性は、互換性のあるデバイスにのみメッセージを送信するために使用されます。セグメンテーション内でも使用できます。                                                 |
| デバイスブランド            | Android           | デバイスのブランド（例：Samsung）                                         | この属性は、互換性のあるデバイスにのみメッセージを送信するために使用されます。                                                                                          |
| デバイスのワイヤレスキャリア | Android、iOS      | モバイルキャリア                                                                 | この属性は、メッセージターゲティングにオプションで使用されます。<br><br>**注:** このフィールドはiOS 16で非推奨となり、将来のiOSバージョンではデフォルトで `--` になります。 |
| 言語                | Android、iOS、Web | デバイスロケールから取得されるデバイスまたはブラウザの言語                                                           | この属性は、ユーザーの優先言語にメッセージを翻訳するために使用されます。デバイスロケールに基づいています。                                                                                            |
| 通知設定   | Android、iOS、Web | このアプリでプッシュ通知が有効になっているかどうか                                   | この属性は、プッシュ通知を有効にするために使用されます。                                                                                                                    |
| 解像度              | Android、iOS、Web | デバイスまたはブラウザの解像度                                                          | オプションで、デバイスベースのメッセージターゲティングに使用されます。この値の形式は「`<width>`x`<height>`」です。                                                                 |
| タイムゾーン               | Android、iOS、Web | デバイスまたはブラウザのタイムゾーン                                                           | この属性は、各ユーザーのローカルタイムゾーンに合わせて適切な時間にメッセージを送信するために使用されます。                                                   |
| ユーザーエージェント              | Web               | [ユーザーエージェント](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) | この属性は、互換性のあるデバイスにのみメッセージを送信するために使用されます。セグメンテーション内でも使用できます。                                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="デフォルトで収集されるオプションデータ" }

デバイスレベルのプロパティ（デバイスのワイヤレスキャリア、タイムゾーン、解像度など）のトラッキングについて詳しくは、プラットフォーム固有のドキュメントを参照してください：[Android]({{site.baseurl}}/developer_guide/storage?tab=android)、[iOS]({{site.baseurl}}/developer_guide/storage?tab=swift)、[Web]({{site.baseurl}}/developer_guide/storage#cookies)。

## デフォルトで収集されないデータ {#data-not-collected-by-default}

デフォルトでは、以下の属性は収集されません。各属性は手動で統合する必要があります。

| 属性                  | プラットフォーム     | 説明                                                                                                                                                                                                                                                                                                               | 収集されない理由                                                                                                                                                                                                                                                                 |
|----------------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| デバイス広告トラッキング有効 | Android、iOS | iOSの場合:<br>[`set(adTrackingEnabled:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(adtrackingenabled:))<br><br>Androidの場合:<br>[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) | このプロパティにはアプリレベルの追加権限が必要であり、インテグレーターによって付与される必要があります。                                                                                                                                                                                      |
| デバイスIDFA                | iOS          | 広告主向けデバイス識別子                                                                                                                                                                                                                                                                                         | これにはAd Tracking Transparencyフレームワークが必要であり、App Storeからの追加のプライバシー審査がトリガーされます。詳細については、[`set(identifierForAdvertiser:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:))を参照してください。 |
| Google広告ID      | Android      | Google Playアプリ内での広告用識別子                                                                                                                                                                                                                                                                        | これにはアプリがGAIDを取得してBrazeに渡す必要があります。詳細については、[オプションのGoogle広告ID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id)を参照してください。                                         |
| 最新の位置情報 | Android、iOS | ユーザーのデバイスの最後に確認されたGPS位置情報です。セッション開始時に更新され、ユーザーのプロファイルに保存されます。 | ユーザーがアプリに位置情報の権限を付与する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="デフォルトで収集されないデータ" }

{% alert note %}
Braze SDKはIPアドレスをローカルに保存しません。
{% endalert %}

## パーソナライズされたインテグレーション {#personalized-integration}

Brazeを最大限に活用するために、SDK実装者は多くの場合、自動的に収集されるデータに加えて、Braze SDKを実装し、ビジネスに関連する[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#set-custom-attributes)、[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events#logging-custom-events)、[購入イベント]({{site.baseurl}}/user_guide/data/activation/events/purchase_events#log-purchase-events)を記録します。

パーソナライズされたインテグレーションにより、ユーザーの体験に関連するカスタマイズされたコミュニケーションが可能になります。

{% alert important %}
Brazeは、5,000,000を超えるセッション、20,000を超える個別のカスタムイベント名、または購入における20,000を超える個別の商品名を持つユーザープロファイル（「ダミーユーザー」）をブロックし、SDKおよびREST APIの両方からそのプロファイルへのすべての受信データの取り込みを停止します。詳細については、[スパムブロッキング]({{site.baseurl}}/user_archival)を参照してください。
{% endalert %}