---
nav_title: プッシュ通知
article_title: プッシュ通知
page_order: 7
page_type: landing
description: "モバイルおよびWebプッシュ通知を通じて、時間的制約のあるアクションを促すメッセージを送信し、ユーザーの再エンゲージメントとアクションを促進します。"
channel:
  - push
search_rank: 3
---

# プッシュ通知 {#push}

> プッシュ通知は、モバイルやWebデバイスに時間的制約のあるアクションを促すメッセージを送信し、しばらくアプリを利用していないユーザーを再エンゲージメントします。関連するコンテンツに直接誘導し、プロダクトの継続的な価値を示すことができます。このハブでは、プッシュの統合、オプトイン戦略、メッセージタイプ、ベストプラクティス、iOS・Android・Web向けのプラットフォーム固有の設定について説明します。システム許可をリクエストする前に、[プッシュプライマーメッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)の利用をご検討ください。開始するには、[iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)、[Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)、[Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)の統合ガイドを参照してください。

[![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## 前提条件 {#prerequisites}

始める前に、以下が準備できていることを確認してください。

- **アプリまたはWebサイトにプッシュが統合されていること。** 開発者と協力してセットアップを行ってください。詳細な手順については、[iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications?tab=android)、および[Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)の統合ガイドを参照してください。
- **プッシュオプトイン戦略があること。** ユーザーはデバイスでプッシュ許可を付与する必要があります。プロンプトを表示する前に、[プッシュプライマーメッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を使用してその価値を説明することを検討してください。

## ユースケース {#use-cases}

| ユースケース | 説明 |
| --- | --- |
| 初期オンボーディング | ユーザーがアプリの利用に向けた最初のステップ（アカウント登録など）を踏むまで、その価値は大幅に制限されます。プッシュ通知を使用して、これらのステップの完了を促し、アプリをフルに活用できるようにしましょう。 |
| 初回購入 | ユーザーがアプリの使用に慣れたら、プッシュ通知を使用してアプリ内購入者への転換を促進できます。 |
| 新機能 | プッシュ通知は、エンゲージメントが低下したユーザーに対して、アプリへの復帰を促す新機能を知らせるのに効果的です。 |
| 期間限定オファー | オファーに期限がある場合、プッシュは有効期限が切れる前にユーザーに知らせる優れた方法です。これらのメッセージは一般的に高い緊急性を伴い、最近離脱したユーザーにアプリを思い出してもらうのに最適です。たとえば、ゲームアプリで毎日連続プレイするとゲーム内通貨ボーナスがもらえる場合、一定日数に達した後に連続プレイが途切れるリスクがあることを通知するのは、効果的なプッシュになります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

## プッシュメッセージに関する規制 {#push-message-regulations}

プッシュはユーザーのデバイスに直接届くため、アプリやストアのポリシーによって使用方法が制限されています。

{% alert important %}
プッシュメッセージは[Apple App Store審査ガイドライン](https://developer.apple.com/app-store/review/guidelines/)および[Google Playポリシー](https://support.google.com/googleplay/android-developer/answer/9888379)に準拠する必要があります。これには、広告、スパム、プロモーション、および関連するトピックにプッシュを使用する際のルールが含まれます。
{% endalert %}

| ポリシーの出典 | 概要 |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | 許容されない使用例として、App Storeに類似したサードパーティアプリ、拡張機能、またはプラグインを表示するインターフェイスの作成や、一般的な興味関心のコレクションとしての利用が含まれます。 |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | プッシュはアプリの機能に必須であってはならず、機密性の高い個人情報や秘密情報を含んではなりません。顧客がアプリのUIで同意文言を通じて明示的にオプトインし、アプリ内でオプトアウトできる場合を除き、プロモーションやダイレクトマーケティングにプッシュを使用しないでください。 |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | プッシュ通知、カメラ、ジャイロスコープなどの組み込み機能や、Apple MusicやiCloudなどのAppleサービスを収益化してはなりません。 |
| Google Play — [システム機能の不正使用または模倣](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | アプリはシステム通知を模倣したり干渉したりしてはなりません。システムレベルの通知は、アプリの不可欠な機能にのみ使用できます（たとえば、航空会社アプリがユーザーにお得な情報を通知する場合や、ゲームアプリがゲーム内プロモーションを通知する場合など）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュメッセージに関する規制" }

## よくある質問 {#frequently-asked-questions}

### Brazeはプッシュの送信成功をいつ記録しますか？ {#when-does-braze-record-a-successful-send-for-push}

Brazeは通常、メッセージがBrazeからApple、Google、またはWebプッシュサービスに向けて送信された時点で**送信**を記録します。**配信**、開封、バウンス、アンインストールのシグナルは個別に追跡され、後から届く場合があります。**送信**と下流の指標にずれがある場合は、ステップレベルおよびキャンペーンレベルの分析と[プッシュのトラブルシューティング]({{site.baseurl}}/user_guide/channels/push/troubleshooting)を併用してください。

## 次のステップ {#next-steps}

- [プッシュのセットアップ]({{site.baseurl}}/user_guide/channels/push/push_setup)
- [プッシュメッセージを作成する]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)