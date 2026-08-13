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

異なる国コードや市外局番を持つ複数の地域に送信する場合でも正確性を確保するため、電話番号は[`E.164`](https://en.wikipedia.org/wiki/e.164)形式でインポートすることを推奨します&#8212;米国ベースの電話番号であっても同様です。

- **米国の番号：** すべての米国の番号は、有効な市外局番を持つ有効な10桁の電話番号である必要があります。10桁の電話番号に`+`と国コードが欠けている場合、Brazeはそれを米国の番号としてマッピングします。プエルトリコの電話番号は、米国スタイルの市外局番を使用した10桁のフォーマットであっても、`+`と国コードが必要です。
- **国際番号：** すべての国際番号は`+`で始まり、その後に国コード、そして電話番号が続く必要があります。例：`+442071838750`。

![有効なE.164国際電話番号の例。]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

以下は、ローカルフォーマットと`E.164`フォーマットの違いを示す例です。

| 国 | ローカル | 国コード | `E.164` |
|---|---|---|---|
| 米国 | `4155552671` | 1 | `+14155552671` |
| 英国 | `2071838750` | 44 | `+442071838750` |
| ブラジル | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="推奨フォーマット" }

## 電話番号のインポート {#import-phone-numbers}

電話番号をインポートする際は、[推奨フォーマット](#recommended-format)に従うことが重要です。電話番号をインポートするには、以下のいずれかの方法を使用してください。

- [BrazeにCSVをアップロードする]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)
- [`/users/track`エンドポイントを使用する]({{site.baseurl}}/api/endpoints/user_data/post_user_track)

{% alert important %}
ユーザーの電話番号はBrazeでは数字の文字列として表示されます。先頭の{% raw %}`+`{% endraw %}以外に数字以外の文字（`,`、`-`、`(`など）を含む番号をインポートした場合、Brazeでレンダリングされる際にそれらの数字以外の文字は削除されます。例えば、`+1 (724) 123-4567`をインポートすると、`+17241234567`と表示されます。
{% endalert %}

## 電話番号のバリデーション {#phone-number-validation}

Brazeは電話番号のバリデーションにGoogleの[libphonenumber](https://github.com/google/libphonenumber)ライブラリを使用しています。新しいモバイル番号プレフィックスが導入された場合、上流のライブラリが更新されるとサポートが追加されます。Brazeは有効なプレフィックスの個別リストを管理していません。

### 無効な電話番号の処理 {#handling-invalid-phone-numbers}

電話番号が無効と判断された場合、Brazeはそのユーザーの電話番号を無効としてマークし、その電話番号への以降の通信送信を試みません。無効な電話番号は、ユーザープロファイルの**エンゲージメントタブ**にマークされます。

![Brazeでの無効な電話番号のエラーメッセージの例。]({% image_buster /assets/img/sms/invalid_banner.png %}){: style="max-width:50%;border: 0;"}

電話番号が無効と見なされる理由は以下のとおりです。

- **プロバイダーエラー**：SMSおよびRCSプロバイダーから永続的なエラーが返されました。これは、提供された電話番号のフォーマットが正しくないか、SMSまたはRCSメッセージを永続的に受信できないことを示しています。
- **無効化**：モバイルサブスクライバーがサービスを終了し、キャリアから番号を解放したため、電話番号が無効化されました（最終的にリサイクルされ、新しいユーザーに割り当てられる可能性があります）。無効化された電話番号は、その電話番号にSMSまたはRCSメッセージを送信していなくても無効としてマークされることがあります。

これらの無効な電話番号は、[SMSおよびRCSエンドポイント]({{site.baseurl}}/api/endpoints/sms)を使用して管理できます。

{% alert note %}
複数のユーザープロファイルが同じ電話番号を持ち、その電話番号が無効としてマークされた場合、その番号を持つ既存のすべてのユーザープロファイルが無効として表示されます。新しく作成されたユーザープロファイルは、最初から無効としてマークされることはありません。
{% endalert %}

[セグメントを作成する]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#step-4-add-filters-to-your-segment)際に、無効な電話番号を持つユーザーを含めたり除外したりすることもできます。

## 拒否されたSMS送信をセグメンテーションから除外する {#exclude-rejected-sms-sends-from-segmentation}

{% alert important %}
SMSの拒否はSMS割り当てに対して課金されます。
{% endalert %}

拒否されたSMS送信を持つユーザーをセグメントから除外するには、[SQLセグメントエクステンション]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)を使用して以下の手順を実行してください。

1. **オーディエンス** > **セグメントエクステンション**に移動します。
2. **新規エクステンションを作成** > **フルリフレッシュ**または**インクリメンタルリフレッシュ**を選択します。
3. SMSの拒否を持つユーザーを特定するSQLクエリを記述します。例えば、`USERS_MESSAGES_SMS_REJECTION_SHARED`イベントをクエリして、SMSの拒否を受けたユーザーを見つけることができます。
4. セグメントエクステンションを保存します。
5. SMSセグメントを作成する際に、このセグメントエクステンションに含まれるユーザーを除外するフィルターを追加します。

## SMSおよびRCS購読グループへのユーザー追加 {#add-users-to-sms-and-rcs-subscription-groups}

ユーザーがSMSまたはRCSメッセージを受信するには、有効な電話番号を持ち、購読グループにオプトインしている必要があります。購読グループは、実行しているSMSまたはRCSプログラムに紐づいています（[SMS、MMS、およびRCSの法的要件]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)に従い、各顧客の同意を記録していることを確認してください）。詳細については、[SMSおよびRCS購読グループ]({{site.baseurl}}/sms_rcs_subscription_groups)を参照してください。

## サードパーティのソーシングと検証 {#third-party-sourcing-and-verification}

Brazeは無効な番号のソーシングにサードパーティツールを利用しています。Brazeはこれらのサービスの停止や誤情報について責任を負いません。したがって、このツールは無効な番号の検証におけるコンプライアンスの唯一の方法として依存すべきではありません。

## 電話番号のキャプチャ {#phone-number-capture}

アプリ内メッセージを通じて電話番号をキャプチャする方法については、[電話番号のキャプチャ]({{site.baseurl}}/phone_number_capture)を参照してください。