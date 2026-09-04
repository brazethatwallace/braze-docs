---
nav_title: メッセージアクティビティログ
article_title: "メッセージアクティビティログ {#dev-console-troubleshooting}"
page_order: 3
page_type: reference
description: "このリファレンス記事では、キャンペーンや送信に関連するメッセージを表示するメッセージアクティビティログについて説明します。ログメッセージの理解方法についても確認できます。"
---

# メッセージアクティビティログ {#dev-console-troubleshooting}

> **メッセージアクティビティログ**では、キャンペーンや送信に関連するあらゆるメッセージ（特にエラーメッセージ）を確認できます。

APIキャンペーンのトランザクションの確認、失敗したメッセージの詳細のトラブルシューティング、通知配信の改善方法や既存の技術的問題の解決に関するインサイトの収集が可能です。

ログにアクセスするには、**設定** > **セットアップとテスト** > **メッセージアクティビティログ**に移動します。

![メッセージアクティビティログ]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
この記事に加えて、[品質保証とデバッグツール](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze Learningコースもご確認ください。メッセージアクティビティログを使用して独自のトラブルシューティングやデバッグを行う方法を解説しています。
{% endalert %}

**メッセージアクティビティログ**に記録される以下のコンテンツでフィルタリングできます。

- プッシュ通知エラー
- 中止されたテンプレートアプリ内メッセージエラー
- Webhookエラー
- メールエラー
- APIメッセージレコード
- コネクテッドコンテンツエラー
- REST API接続オーディエンスエラー
- ユーザーエイリアスエラー
- ABテストエラー
- SMS/MMSエラー
- WhatsAppエラー
- ライブアクティビティエラー
- 不正なユーザートリガーエラー
- Brazeエージェントの[1日あたりの呼び出し制限]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#monitor-your-agent)エラー
- Brazeエージェントの利用不可[モデル]({{site.baseurl}}/user_guide/brazeai/agents/reference#models)エラー

これらのメッセージは、Brazeのシステム、お客様のアプリやプラットフォーム、またはサードパーティパートナーから送信される場合があります。そのため、このログに表示されるメッセージの数は無限に存在する可能性があります。

## ログメッセージの理解 {#understanding-log-messages}

メッセージの意味を判断するには、各メッセージの表現と、それに対応するカラムに注目してください。コンテキストの手がかりを使ってトラブルシューティングするのに役立ちます。

たとえば、**Aborted Message Error** のエントリは、[Liquid のメッセージ中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)だけでなく、多くの理由で発生する可能性があります。具体的な理由については、**Message** カラムをお読みください。

- 送信が Liquid の `abort_message` タグによって中止された場合、**Message** カラムには呼び出された正確な Liquid スニペットが表示されます。たとえば {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %} のように表示されます。
- その他の中止理由の場合、**Message** カラムに送信が中止された理由が説明されます。

### API キャンペーンのペイロード {#api-campaign-payloads}

メッセージアクティビティログは、API キャンペーンの種類に応じて異なる情報を記録します。[`/messages/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)は API メッセージレコードにメッセージ本文（messages）を記録しますが、[`/campaigns/trigger/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)はリクエストペイロードや `api_trigger_properties` をメッセージアクティビティログに記録しません。

### 一般的なメッセージ {#common-messages}

よく見かけるメッセージタイプがいくつかあり、問題の診断と修正に役立つトラブルシューティングリンクが提供される場合もあります。

以下に記載されているメッセージは例示目的であり、ログの **Message** カラムに表示される内容と完全に一致しない場合があります。

| メッセージタイプ | 想定されるメッセージ | 説明 |
|---|---|---|
| ソフトバウンス | The email address same@example.com soft bounced. | メールアドレスは有効で、メールメッセージは受信者のメールサーバーに到達しましたが、「一時的な」問題により拒否されました。<br><br>ソフトバウンスの一般的な理由には次のものがあります。{::nomarkdown} <ul> <li> メールボックスが満杯だった（ユーザーが容量制限を超過した） </li> <li> サーバーがダウンしていた </li> <li> メッセージが受信者の受信トレイに対して大きすぎた </li>  </ul> {:/} メールがソフトバウンスを受けた場合、通常72時間以内に再試行しますが、再試行の回数は受信者によって異なります。 |
| ハードバウンス | The email account that you tried to reach does not exist. Try double-checking the recipient's email address for typos or unnecessary spaces. | メッセージはこの人の受信トレイに届きませんでした。到達すべき受信トレイが存在しなかったためです。さらに詳しく調べたい場合、このようなメッセージには **View Details** カラムに意図した受信者のプロファイルを確認できるリンクが含まれていることがあります。|
| ブロック | Spam message is rejected because of anti-spam policy. | メッセージがスパムとして分類されました。このメールエラーは、メールサービスプロバイダー (ESP) からメールがドロップされたことを示すイベントを受信した場合に、ユーザーに対して記録されます。この問題は対象の受信者のみに該当する場合もありますが、このメッセージが頻繁に表示される場合は、送信習慣やメッセージの内容を再評価する必要があるかもしれません。また、[IP ウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)を行いましたか？まだの場合は、Braze に連絡して開始するためのアドバイスを受けてください。|
| メッセージ中止エラー | {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %} | 送信が Liquid の `abort_message` タグによって中止された場合、**Message** カラムには呼び出された正確な Liquid スニペットが表示されます。その他の **Aborted Message Error** エントリには、中止理由を説明する別のメッセージが含まれている場合があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="一般的なメッセージ" }

### なぜここにメッセージが記載されていないのですか？ {#why-isnt-my-message-listed-here}

メッセージアクティビティログに表示されるメッセージは、Braze、お使いのアプリやプラットフォーム、またはサードパーティパートナーなど、さまざまなソースから発信されます。つまり、このログに表示される可能性のあるメッセージの数は無限であり、すべてをリストすることはできません。

たとえば、前述の表に記載されているものに加えて、「ブロック」メッセージとして表示される可能性のあるものには以下があります。

- Unfortunately, messages from [_IP_ADDRESS_] weren't sent. Please contact your Internet Service provider since part of their network is on our block list.
- Message rejected due to local policy.
- The message was blocked by the receiver as spam.
- Service unavailable, Client host [_IP_ADDRESS_] blocked using Spamhaus.

## ストレージ保持期間 {#storage-retention-period}

過去60時間のエラーがメッセージアクティビティログで確認できます。60時間以上経過したログはクリーンアップされ、アクセスできなくなります。

### 保存されるエラーログの件数 {#number-of-error-logs-stored}

保存されるログの件数は、いくつかの条件によって変わります。たとえば、スケジュールされたキャンペーンが数千人のユーザーに送信された場合、メッセージアクティビティログにはすべてのエラーではなく、エラーのサンプルが表示される可能性があります。以下は、保存されるログ件数に影響する条件の概要です。
- 以下のエラータイプについて、同一キャンペーンまたはキャンバスステップごとに、1時間の固定時間枠内で同じエラータイプのエラーログが最大20件保存されます。
    - Connected Content エラー
    - メッセージ中止エラー
    - Webhook エラー
    - SMS 拒否エラー
    - SMS 配信失敗エラー
    - WhatsApp 失敗エラー
    - ABテストエラー
- 以下のエラータイプについて、同一キャンペーンまたはキャンバスステップとアプリの組み合わせごとに、同じエラータイプのプッシュ通知エラーログが最大20件保存されます。
    - 無効なプッシュ認証情報
    - 無効なプッシュトークン
    - プッシュ認証情報なし
    - トークンエラー
    - クォータ超過
    - リトライタイムアウト
    - 無効なペイロード
    - 予期しないエラー
- 以下のエラータイプについて、同一アプリごとに、1時間の固定時間枠内で同じエラータイプのエラーログが最大100件保存されます。
    - ライブアクティビティエラー（プッシュ認証情報なし）
    - ライブアクティビティエラー（無効なプッシュ認証情報）
    - その他のライブアクティビティエラー
    - APNS フィードバックによるトークン削除エラー
- 以下のエラータイプについて、同一キャンペーンまたはキャンバスステップごとに、1時間の固定時間枠内で同じエラータイプのエラーログが最大100件保存されます。
    - メールソフトバウンスエラー
    - メールハードバウンスエラー
    - メールブロックエラー
- 同一ワークスペースごとに、1時間の固定時間枠内でユーザーエイリアスエラーログが最大100件保存されます。

## テスト送信 {#test-sends}

**メッセージアクティビティログ**には、以下のメッセージングチャネルのテストログが表示されます。

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

テスト送信ログは、メール、Content Cards、アプリ内メッセージ、プッシュの各チャネルでは利用できません。

テスト送信ログには「[TEST SEND]」というプレフィックスが付きますが、すべてのテスト送信ログにプレフィックスが付くとは限りません（例えば、コネクテッドコンテンツのエラーにはプレフィックスが付きません）。