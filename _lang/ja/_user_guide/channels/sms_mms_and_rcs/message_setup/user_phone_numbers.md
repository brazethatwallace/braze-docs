---
nav_title: "ユーザーの電話番号"
article_title: SMSユーザーの電話番号
page_order: 3
description: "このリファレンス記事では、SMS電話番号のフォーマット、電話番号のインポート方法、およびSMS購読グループへのユーザー追加方法について説明します。"
page_type: reference
alias: /user_phone_numbers/
channel:
  - SMS
  - MMS
  - RCS
---

# ユーザーの電話番号 {#user-phone-numbers}

> この記事では、ユーザーや顧客の電話番号に関するさまざまなトピックについて説明します。自社の番号に関する情報をお探しの場合は、[送信電話番号]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)の記事をご覧ください。

## 推奨フォーマット {#recommended-format}

異なる国コードや市外局番を持つ複数の地域に送信する場合の正確性を確保するために、米国ベースの電話番号であっても[`E.164`](https://en.wikipedia.org/wiki/e.164)形式で電話番号をインポートすることをお勧めします。

- **米国番号：**すべての米国番号は、有効な市外局番を持つ有効な10桁の電話番号である必要があります。10桁の電話番号に`+`や国コードが含まれていない場合、Brazeは米国番号としてマッピングします。プエルトリコの電話番号は、米国式の市外局番を持つ10桁のフォーマットを使用しますが、`+`と国コードが必要です。
- **国際番号：**すべての国際番号は`+`で始まり、その後に国コード、電話番号が続く必要があります。例：`+442071838750`

![有効なE.164国際電話番号の例。]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

ローカル番号のフォーマットと`E.164`フォーマットの違いを示すいくつかの例は以下の通りです。

| 国 | ローカル | 国コード | `E.164` |
|---|---|---|---|
| 米国 | `4155552671` | 1 | `+14155552671` |
| 英国 | `2071838750` | 44 | `+442071838750` |
| ブラジル | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="推奨フォーマット" }

## 電話番号のインポート {#import-phone-numbers}

電話番号をインポートする際は、[推奨フォーマット](#recommended-format)に従うことが重要です。電話番号をインポートするには、以下のいずれかの方法を使用します。

- [BrazeにCSVをアップロードする]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)
- [`/users/track`エンドポイントを使用する]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
ユーザーの電話番号はBrazeでは数字の文字列として表示されます。先頭の{% raw %}`+`{% endraw %}以外に数字でない文字（`,`、`-`、`(`など）を含む番号をインポートした場合、Brazeでの表示時にそれらの文字は削除されます。たとえば、`+1 (724) 123-4567`をインポートすると、`+17241234567`と表示されます。
{% endalert %}

## 電話番号のバリデーション {#phone-number-validation}

Brazeは、電話番号のバリデーションにGoogleの[libphonenumber](https://github.com/google/libphonenumber)ライブラリを使用しています。新しいモバイル番号プレフィックスが導入された場合、上流のライブラリが更新されるとサポートが追加されます。Brazeは有効なプレフィックスの個別リストを管理していません。

### 無効な電話番号の処理 {#handling-invalid-phone-numbers}

電話番号が無効と判定された場合、Brazeはそのユーザーの電話番号を無効としてマークし、その電話番号への以降の通信送信を試みません。無効な電話番号は、ユーザープロファイルの**エンゲージメントタブ**に表示されます。

![Brazeでの無効な電話番号に対するエラーメッセージの例。]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

電話番号は、以下の理由で無効とみなされます。

- **プロバイダーエラー**：SMSおよびRCSプロバイダーから永続的なエラーが返されました。これは、提供された電話番号のフォーマットが正しくないか、SMSまたはRCSメッセージを永続的に受信できないことを示しています。
- **無効化済み**：携帯電話の加入者がサービスを終了し、キャリアから番号を解放したため、電話番号が無効化されています（最終的にリサイクルされて新しいユーザーに割り当てられる可能性があります）。無効化された電話番号は、その電話番号にSMSやRCSメッセージを送信したことがなくても、無効としてマークされることがあります。

これらの無効な電話番号は、[SMSおよびRCSエンドポイント]({{site.baseurl}}/api/endpoints/sms)を使用して管理できます。

{% alert note %}
複数のユーザープロファイルが同じ電話番号を持ち、その電話番号が無効としてマークされた場合、その番号を持つ既存のすべてのユーザープロファイルが無効として表示されます。新しく作成されたユーザープロファイルは、最初から無効としてマークされることはありません。
{% endalert %}

また、[セグメントの作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-4-add-filters-to-your-segment)時に、無効な電話番号を持つユーザーを含めたり除外したりすることもできます。

## セグメンテーションからリジェクトされたSMS送信を除外する {#exclude-rejected-sms-sends-from-segmentation}

{% alert important %}
SMSのリジェクトは、Brazeとの契約やSMSプロバイダーによっては、SMSの割り当てにカウントされる場合があります。請求に関する詳細は、[レポート]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)を参照してください。
{% endalert %}

リジェクトされたSMS送信があるユーザーをセグメントから除外するには、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)を使用して、以下の手順を実行します。

1. **オーディエンス** > **セグメントエクステンション**に移動します。
2. **新しいエクステンションを作成** > **フルリフレッシュ**または**増分リフレッシュ**を選択します。
3. SMSのリジェクトがあるユーザーを特定するSQLクエリを作成します。たとえば、`USERS_MESSAGES_SMS_REJECTION_SHARED`イベントをクエリして、SMSのリジェクトを受けたユーザーを見つけることができます。
4. セグメントエクステンションを保存します。
5. SMSセグメントを作成する際に、このセグメントエクステンションに含まれるユーザーを除外するフィルターを追加します。

## SMSおよびRCS購読グループへのユーザーの追加 {#add-users-to-sms-and-rcs-subscription-groups}

ユーザーがSMSまたはRCSメッセージを受信するには、有効な電話番号を持ち、購読グループにオプトインしている必要があります。購読グループは、運用しているSMSまたはRCSプログラムに紐付けられています（[SMS、MMS、およびRCSに関する法的要件]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)に従い、各顧客の同意を記録してください）。詳細については、[SMSおよびRCS購読グループ]({{site.baseurl}}/sms_rcs_subscription_groups)を参照してください。

## サードパーティのソーシングと検証 {#third-party-sourcing-and-verification}

Brazeは無効な番号のソースにサードパーティのツールを利用しています。Brazeはこれらのサービスの停止や誤情報について責任を負いません。そのため、このツールを無効な番号の検証に関するコンプライアンスの唯一の方法として依存すべきではありません。

## 電話番号の取得 {#phone-number-capture}

アプリ内メッセージを通じて電話番号を取得するには、[SMS、RCS、WhatsAppサインアップフォーム]({{site.baseurl}}/phone_number_capture)を参照してください。