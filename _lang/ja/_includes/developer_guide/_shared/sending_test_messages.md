# テストメッセージの送信 {#sending-test-messages}

> メッセージングキャンペーンをユーザーに送信する前に、正しく表示され、意図した通りに動作することを確認するためにテストを行うことをお勧めします。ダッシュボードを使用して、プッシュ通知、アプリ内メッセージ（IAM）、またはメールでテストメッセージを作成して送信できます。

## テストメッセージの送信 {#sending-a-test-message}

### ステップ 1: 指定したテストセグメントを作成する <a class="margin-fix" name="test-segment"></a> {#step-1-create-a-designated-test-segment}

テストセグメントを設定すると、Brazeのあらゆるメッセージングチャネルのテストに使用できます。正しく設定されていれば、この作業は一度だけ行えば済みます。

テストセグメントを設定するには、**セグメント**に移動して新しいセグメントを作成します。**Add Filter**を選択し、テストフィルターのいずれかを選択します。

![ターゲットステップで使用可能なフィルターを表示するBrazeテストキャンペーン。]({% image_buster /assets/img_archive/testmessages1.png %})

テストフィルターを使用すると、指定したメールアドレスまたは[外部ユーザーID]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids)を持つユーザーのみにテストメッセージが送信されるようにできます。

![「Testing」という見出しの下にいくつかのフィルターがリストされたドロップダウンメニュー]({% image_buster /assets/img_archive/testmessages2.png %})

メールアドレスフィルターと外部ユーザーIDフィルターの両方に、以下のオプションがあります。

| 演算子 | 説明 |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals` | 指定したメールまたはユーザーIDと完全に一致するものを検索します。1つのメールまたはユーザーIDに関連付けられたデバイスにのみテストキャンペーンを送信する場合に使用します。 |
| `does not equal` | 特定のメールまたはユーザーIDをテストキャンペーンから除外する場合に使用します。 |
| `matches` | 指定した検索語句の一部と一致するメールアドレスまたはユーザーIDを持つユーザーを検索します。これを使用して`@yourcompany.com`アドレスを持つユーザーのみを検索し、チーム全員にメッセージを送信できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Create a designated test segment a class="margin-fix" name="test-segment"/a" }

「`matches`」オプションを使用し、メールアドレスを &#124; 文字で区切ることで、複数のメールを選択できます。例：「`matches`」「`email1@braze.com` &#124; `email2@braze.com`」。複数の演算子を組み合わせることもできます。たとえば、テストセグメントには「`matches`」「`@braze.com`」というメールアドレスフィルターと、「`does not equal`」「`sales@braze.com`」という別のフィルターを含めることができます。

テストフィルターをテストセグメントに追加した後、**Preview**を選択するか、**Settings** > **CSV Export All User Data**を選択してそのセグメントのユーザーデータをCSVファイルにエクスポートすることで、正しく動作していることを確認できます。

![「セグメント Details」というタイトルのBraze キャンペーンのセクション]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
セグメントのユーザーデータをCSVファイルにエクスポートすることが最も正確な確認方法です。プレビューではユーザーのサンプルのみが表示され、すべてのユーザーが含まれているとは限りません。
{% endalert %}

### ステップ 2: メッセージを送信する {#step-2-send-the-message}

Brazeダッシュボードまたはコマンドラインを使用してメッセージを送信できます。

{% tabs local %}
{% tab ダッシュボードを使用する %}
{% subtabs %}
{% subtab プッシュ通知またはアプリ内メッセージ %}
テストプッシュ通知またはアプリ内メッセージを送信するには、以前に作成したテストセグメントをターゲットにする必要があります。まずキャンペーンを作成し、通常のステップに従います。**Target Audiences**ステップに到達したら、ドロップダウンメニューからテストセグメントを選択します。

![ターゲットステップで使用可能なセグメントを表示するBrazeテストキャンペーン。]({% image_buster /assets/img_archive/test_segment.png %})

キャンペーンを確認して起動し、プッシュ通知とアプリ内メッセージをテストします。

{% alert note %}
1つのキャンペーンを使用して自分自身にテストメッセージを複数回送信する場合は、キャンペーンコンポーザーの**Schedule**部分で**Allow users to become re-eligible to receive campaign**を選択してください。
{% endalert %}
{% endsubtab %}

{% subtab メールメッセージ %}
メールメッセージのみをテストする場合は、必ずしもテストセグメントを設定する必要はありません。キャンペーンコンポーザーの最初のステップでキャンペーンのメールメッセージを作成する際に、**Send Test**をクリックし、テストメールを送信したいメールアドレスを入力します。

![テスト送信タブが選択されたBraze キャンペーン]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
テストメッセージに[TEST（またはSEED）]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines)が追加されるのを有効または無効にすることもできます。
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab コマンドラインを使用する %}
または、cURLと[BrazeメッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)を使用して単一の通知を送信できます。これらの例では`US-01`インスタンスを使用してリクエストを作成しています。ご自身のインスタンスを確認するには、[APIエンドポイント]({{site.baseurl}}/api/basics/#endpoints)を参照してください。

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
`````````bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": {
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
`````````bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

以下のように置き換えます。

| プレースホルダー | 説明 |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY` | 認証に使用するBraze APIキー。Brazeで、**Settings** > **API Keys**に移動してキーを見つけます。 |
| `EXTERNAL_USER_ID` | 特定のユーザーにメッセージを送信するために使用する外部ユーザーID。Brazeで、**Audience** > **Search Users**に移動し、ユーザーを検索します。 |
| `CUSTOM_KEY` | （オプション）追加データ用のカスタムキー。 |
| `CUSTOM_VALUE` | （オプション）カスタムキーに割り当てられたカスタム値。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Send the message" }
{% endtab %}
{% endtabs %}

## テストの制限事項 {#test-limitations}

テストメッセージは、キャンペーンやキャンバスを実際のユーザーに対して起動する場合と完全な機能パリティがない場合があります。このような場合、動作を検証するには、限られたテストユーザーに対してキャンペーンまたはキャンバスを起動する必要があります。

- Brazeの[ユーザー設定センター]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)を**テストメッセージ**から表示すると、送信ボタンがグレーアウトされます。
- list-unsubscribeヘッダーは、テストメッセージ機能によって送信されるメールには含まれません。
- アプリ内メッセージおよびContent Cardsの場合、ターゲットユーザーにはターゲットデバイスのプッシュトークンが必要です。