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

> プッシュ通知は、モバイルやWebを通じて時間的制約のあるアクションを促すメッセージを送信し、しばらくアプリを利用していないユーザーを再エンゲージメントするための実績ある方法です。ユーザーをコンテンツに直接誘導し、アプリケーションの価値を示すことができます。

[![Braze Learningコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/push-fundamentals){: style="float:right;width:120px;border:0;" class="noimgborder"}

## 前提条件 {#prerequisites}

始める前に、以下を確認してください。

- **アプリまたはWebサイトにプッシュ通知が統合されていること。** セットアップについては開発者と連携してください。詳細な手順については、[iOS]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift)、[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications?tab=android)、および[Web]({{site.baseurl}}/developer_guide/push_notifications?sdktab=web)の統合ガイドを参照してください。
- **プッシュ通知のオプトイン戦略があること。** ユーザーはデバイスでプッシュ通知の許可を付与する必要があります。プロンプトを表示する前に価値を説明するために、[プッシュプライマーメッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)の使用を検討してください。

## ユースケース {#use-cases}

| ユースケース | 説明 |
| --- | --- |
| 初回オンボーディング | ユーザーがアプリの利用に向けた初期ステップ（アカウント登録など）を完了するまで、その価値は大幅に制限されます。プッシュ通知を使用して、これらのステップを完了するようユーザーに促し、アプリをフルに活用できるようにしましょう。 |
| 初回購入 | ユーザーがアプリの使用に慣れたら、プッシュ通知を使用してアプリ内購入者への転換を促進できます。 |
| 新機能 | プッシュ通知は、エンゲージメントが低下したユーザーに対して、アプリに呼び戻す可能性のある新機能を通知するのに効果的です。 |
| 期間限定オファー | オファーに期限がある場合、プッシュ通知は期限切れ前にユーザーに知らせる優れた方法です。これらのメッセージは一般的に緊急性が高く、最近離脱したユーザーにアプリを思い出してもらうのに最適です。たとえば、アプリがゲームで、毎日のプレイ連続記録に対してゲーム内通貨ボーナスを提供している場合、一定日数に達した後に連続記録が途切れるリスクがあることをユーザーに通知することは、効果的なプッシュ通知になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユースケース" }

## プッシュ通知に関する規制 {#push-message-regulations}

プッシュ通知は顧客のデバイスに直接届くため、アプリやストアのポリシーによって使用方法が制限されています。

{% alert important %}
プッシュメッセージは、[Apple App Storeレビューガイドライン](https://developer.apple.com/app-store/review/guidelines/)および[Google Playポリシー](https://support.google.com/googleplay/android-developer/answer/9888379)に準拠する必要があります。これには、広告、スパム、プロモーション、および関連トピックにプッシュを使用する際のルールが含まれます。
{% endalert %}

| ポリシーソース | 概要 |
| --- | --- |
| Apple [3.2.2](https://developer.apple.com/app-store/review/guidelines/#unacceptable) | 許容されない使用例には、App Storeに類似したサードパーティアプリ、拡張機能、またはプラグインを表示するインターフェイスの作成や、一般的な関心事のコレクションとしての使用が含まれます。 |
| Apple [4.5.4](https://developer.apple.com/app-store/review/guidelines/#apple-sites-and-services) | プッシュ通知はアプリの機能に必須であってはならず、機密性の高い個人情報や秘密情報を含んではなりません。顧客がアプリのUIで同意の文言を通じて明示的にオプトインし、アプリ内でオプトアウトできる場合を除き、プロモーションやダイレクトマーケティングにプッシュを使用しないでください。 |
| Apple [4.10](https://developer.apple.com/app-store/review/guidelines/#monetizing-built-in-capabilities) | プッシュ通知、カメラ、ジャイロスコープなどの組み込み機能や、Apple Music、iCloudなどのAppleサービスを収益化してはなりません。 |
| Google Play — [システム機能の不正使用または模倣](https://developers.google.com/android/play-protect/mobile-unwanted-software#muws-categories) | アプリはシステム通知を模倣したり、干渉したりしてはなりません。システムレベルの通知は、アプリの不可欠な機能にのみ使用できます（たとえば、航空会社アプリがユーザーにお得な情報を通知する場合や、ゲームがユーザーにゲーム内プロモーションを通知する場合など）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="プッシュ通知に関する規制" }

## よくある質問 {#frequently-asked-questions}

### Brazeはプッシュの送信成功をいつ記録しますか？ {#when-does-braze-record-a-successful-send-for-push}

Brazeは通常、メッセージがBrazeからApple、Google、またはWebプッシュサービスに向けて送信された時点で**送信**を記録します。**配信**、開封、バウンス、およびアンインストールシグナルは別途追跡され、後から届く場合があります。**送信**と下流の指標にずれがある場合は、ステップレベルおよびキャンペーンレベルの分析と[プッシュのトラブルシューティング]({{site.baseurl}}/user_guide/channels/push/troubleshooting)を併用してください。

## 次のステップ {#next-steps}

- [プッシュのセットアップ]({{site.baseurl}}/user_guide/channels/push/push_setup)
- [プッシュメッセージの作成]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)