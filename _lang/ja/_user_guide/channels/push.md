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

始める前に、以下の準備が整っていることを確認してください。

- **プッシュがアプリまたはWebサイトに統合されていること。** 開発者と協力してセットアップしてください。詳細な手順については、[iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)、[Android]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android)、[Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)の統合ガイドを参照してください。
- **プッシュオプトイン戦略があること。** ユーザーはデバイスでプッシュ許可を付与する必要があります。プロンプトを表示する前に、[プッシュプライマーメッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を使用して価値を説明することを検討してください。

## ユースケース {#use-cases}

| ユースケース | 説明 |
| --- | --- |
| 初期オンボーディング | ユーザーがアプリの利用に向けた初期ステップ（アカウント登録など）を完了するまで、ユーザーの価値は大幅に制限されます。プッシュ通知を使用して、これらのステップの完了を促し、アプリをフルに活用できるようにしましょう。 |
| 初回購入 | ユーザーがアプリの使い方に慣れたら、プッシュ通知を使用してアプリ内課金ユーザーへの転換を促進できます。 |
| 新機能 | プッシュ通知は、エンゲージメントが低下したユーザーにアプリへの復帰を促す可能性のある新機能を通知するのに効果的です。 |
| 期間限定オファー | オファーに期限がある場合、プッシュは有効期限前にユーザーに知らせる優れた手段です。これらのメッセージは一般的に高い緊急性を持ち、最近離脱したユーザーにアプリを思い出してもらうのに最適です。たとえば、アプリがゲームで、毎日連続プレイすることでゲーム内通貨ボーナスを提供している場合、一定日数に達したユーザーに連続記録が途切れる危険があることを通知するのは、効果的なプッシュとなります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

## プッシュメッセージの規制 {#push-message-regulations}

プッシュは顧客のデバイスに直接届くため、アプリやストアのポリシーによって使用方法が制限されています。

{% alert important %}
プッシュメッセージは、[Apple App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)および[Google Playポリシー](https://support.google.com/googleplay/android-developer/answer/9888379)に準拠する必要があります。これには、広告、スパム、プロモーション、および関連するトピックにおけるプッシュの使用に関するルールが含まれます。
{% endalert %}

| ポリシーソース | 概要 |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | 許容されない用途には、App Storeに類似したサードパーティのアプリ、拡張機能、またはプラグインを表示するインターフェイスの作成や、一般的な興味に基づくコレクションとしての使用が含まれます。 |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | プッシュはアプリの機能に必須であってはならず、機密性の高い個人情報や秘密情報を送信してはなりません。顧客がアプリのUIで同意文言を通じて明示的にオプトインし、アプリ内でオプトアウトできる場合を除き、プロモーションやダイレクトマーケティングにプッシュを使用しないでください。 |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | プッシュ通知、カメラ、ジャイロスコープなどの組み込み機能や、Apple MusicやiCloudなどのAppleサービスを収益化してはなりません。 |
| Google Play — [システム機能の不正使用または模倣](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | アプリはシステム通知を模倣したり、干渉したりしてはなりません。システムレベルの通知は、アプリの不可欠な機能にのみ使用されます（例：航空会社のアプリがユーザーにお得な情報を通知する場合や、ゲームがユーザーにゲーム内プロモーションを通知する場合）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュメッセージの規制" }

## よくある質問 {#frequently-asked-questions}

### Brazeはプッシュの送信成功をいつ記録しますか？ {#when-does-braze-record-a-successful-send-for-push}

Brazeは通常、メッセージがBrazeからApple、Google、またはWebプッシュサービスに向けて送出された時点で**送信**を記録します。**配信**、開封、バウンス、およびアンインストールのシグナルは個別にトラッキングされ、遅れて届く場合があります。**送信**と下流の指標にずれがある場合は、ステップレベルおよびキャンペーンレベルの分析を[プッシュトラブルシューティング]({{site.baseurl}}/user_guide/channels/push/troubleshooting)と併せて確認してください。

## 次のステップ {#next-steps}

- [プッシュのセットアップ]({{site.baseurl}}/user_guide/channels/push/push_setup)
- [プッシュメッセージを作成する]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)