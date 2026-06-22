---
nav_title: "通知チャネル"
article_title: プッシュ通知チャネル
page_order: 4
page_type: reference
description: "このリファレンス記事では、Android Oへの移行、Brazeへのチャネルの追加、フォールバックチャネルの設定など、Androidプッシュ通知チャネルに関するトピックについて説明しています。"
platform: Android
channel:
  - push

---

# 通知チャネル {#notification-channels}

> [通知チャネル](https://www.braze.com/blog/android-o-push-notifications-channels/)は、Android Oで追加されたプッシュ通知を整理するための仕組みです。O以降、すべてのプッシュ通知にはメッセージの種類を示す通知チャネルが必要です（例：「チャット通知」や「フォロー通知」）。ユーザーは個々のチャネルに基づいて、通知のさまざまな側面（スヌーズ、音/バイブレーション設定、オプトアウトなど）をコントロールできます。

通知チャネルはアプリケーションのコード内でのみ作成でき、Brazeダッシュボードでプログラム的に作成することはできません。エンジニアリングチームとマーケターが連携して、必要な通知チャネルがダッシュボードに適切に追加されるようにすることをお勧めします。

APIレベル26（Android O）以降、プッシュ通知を表示するには有効なチャネルが必要です。アプリがAndroid O以降をターゲットにしている場合、Braze SDKバージョン2.1.0以降を使用する必要があります。開発チームは、使用するチャネルと各チャネルの推奨通知設定（重要度、サウンド、ライトなど）をアプリケーションコード内で定義する必要があります。詳細については、[Android開発者ドキュメント](https://developer.android.com/preview/features/notification-channels.html)および[Braze開発者ドキュメント]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#step-5-define-notification-channels)をご覧ください。

{% alert note %}
Androidはチャネル名のローカライゼーションをサポートしているため、アプリケーションのコード内で1つのチャネルIDを複数のチャネル名の翻訳に関連付けることができます。
{% endalert %}

これらのチャネルが作成されたら、エンジニアは関連するチャネルIDをマーケティングチームに共有する必要があります。チームはCampaignsやCanvasesで使用するために、チャネル名とチャネルIDをBrazeダッシュボードに入力する必要があります。

Brazeダッシュボードにチャネルを追加するには、Androidプッシュ作成画面に移動し、通知チャネルフィールドを選択してから「チャネルを管理」を選択します。
{% alert important %}
「アプリを管理」権限を持つユーザーのみがチャネルを管理できます。
{% endalert %}

## SDKデフォルトチャネル {#sdk-default-channel}

Androidでは、APIレベル26（Android O）以降でプッシュ通知を表示するために有効なチャネルが必要です。Braze Android SDK 2.1.0には「General」というデフォルトチャネルが含まれており、ダッシュボードで追加のチャネルを指定しない場合や、無効なチャネルに送信しようとした場合に作成・使用されます。SDK内でこのラベルの名前を変更し、チャネルの説明を提供できます。より良いユーザーエクスペリエンスを提供するために、これを検討することをお勧めします。

チャネルがアプリケーションに追加されると、削除することもできます。ただし、消費者は[削除された][3]チャネルの数を常に確認できます。Brazeダッシュボードにはチャネルをプログラム的に作成する機能は含まれていません。シームレスなエクスペリエンスを提供するために、チャネルはアプリケーションのコード内で作成・定義する必要があります。

繰り返しになりますが、Android Oへのターゲティングをスムーズに移行するために、エンジニアリングチームと連携することをお勧めします。

## ダッシュボードフォールバックチャネル {#dashboard-fallback-channel}

Brazeでは、ダッシュボードフォールバックチャネルを指定できます。ダッシュボードフォールバックチャネルの目的は、明示的なチャネル選択がないレガシープッシュメッセージにチャネルIDを提供することです。チャネル選択とは、Androidプッシュ作成画面でチャネルを選択することを指します。

チャネルが選択されていないメッセージは、ダッシュボードフォールバックチャネルIDで送信されます。ダッシュボードフォールバックチャネルを変更すると、明示的にチャネルが選択されていないすべてのメッセージは、新しいフォールバックチャネルのIDで送信されます。

ダッシュボードフォールバックチャネルの想定される動作の例を以下に示します。

ダッシュボードフォールバックチャネルが「Marketing」で、チャネルを一度も選択していないAndroidプッシュメッセージが10件あるとします。「Marketing」チャネルがダッシュボードフォールバックチャネルであるため、これらのCampaignsは「Marketing」チャネルを通じて送信されます。

さらに、「Social Notifications」チャネルで送信するよう選択した15件のメッセージと、「Marketing」チャネルで送信するよう選択した5件のメッセージがあるとします。

その後、ダッシュボードのデフォルトチャネルを「Marketing」から「Updates」に変更することにしたとします。

この場合、以前「Marketing」チャネルを通じて送信されていたチャネル選択のない10件のCampaignsは、フォールバックチャネルを通じて送信されるため、「Updates」チャネルで送信されるようになります。「Social Notifications」チャネルを通じて送信されていた15件のメッセージは、引き続き「Social Notifications」チャネルで送信されます。「Marketing」チャネルを通じて送信されていた5件のメッセージは、引き続き「Marketing」チャネルで送信されます。

無効なチャネルIDがBrazeに提供された場合（開発者がSDKで作成していないチャネルIDを提供した場合など）、SDKデフォルトチャネルを通じて通知が配信されます。そのため、開発中にBrazeダッシュボードで通知チャネルをテストすることを強くお勧めします。

チャネルの想定される動作をより理解するために、以下の表を参照してください。

| シナリオ | 結果 |
| ---|-------------|
| **会社ABC**がAndroid OをサポートするSDKに更新<br>**会社ABC**がBrazeダッシュボードにチャネルを追加しない<br>**会社ABC**がSDKデフォルトチャネルの名前を変更しない | Android Oデバイスに送信されるプッシュ通知は「General」というチャネルを作成し、通知は「General」チャネルを通じて送信される
| **会社XYZ**がAndroid OをサポートするSDKに更新<br>**会社XYZ**がBrazeダッシュボードにチャネルを追加しない<br>**会社XYZ**がSDKデフォルトチャネルの名前を「Marketing」に変更 | Android Oデバイスに送信されるプッシュ通知は「Marketing」というチャネルを作成し、通知は「Marketing」チャネルを通じて送信される
| **会社LMN**がAndroid OをサポートするSDKに更新<br>**会社LMN**がアプリケーションコードで「Promotions」と「Order Updates」の2つのチャネルを定義<br>**会社LMN**が「Promotions」と「Order Updates」のチャネルIDをBrazeダッシュボードに追加<br>**会社LMN**が「Promotions」をダッシュボードフォールバックチャネルに指定<br>**会社LMN**がSDKデフォルトチャネルの名前を「Marketing」に変更 | Android Oデバイスに送信されるプッシュ通知はチャネルを作成しない<br><br>マーケターが「Order Updates」または「Marketing」チャネルで通知を送信するよう明示的に指定しない限り、チャネルがダッシュボードに追加される前に作成されたすべての通知は「Promotions」チャネルを通じて送信される<br><br>SDKデフォルトチャネル「Marketing」は、会社が無効なチャネルIDで通知を送信しようとした場合、または明示的に選択された場合にのみ作成・使用される
| **会社HIJ**がAndroid Oに更新するが、Braze Android SDKを2.1.0以降に更新しない | Android O以降を実行しているユーザーに送信された通知は表示されない |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ダッシュボードフォールバックチャネル" }

## Brazeダッシュボードへのチャネルの追加 {#adding-channels-to-the-braze-dashboard}

1. Androidプッシュを含むCampaignまたはCanvasを開くか新規作成します。
2. Androidプッシュメッセージ作成画面に移動します。
3. **Manage Notification Channels**を選択します。ここで追加されたチャネルは、すべてのCampaignsとCanvasesでグローバルに利用可能になります。チャネルを管理するには、ワークスペースの「Manage Apps」[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/#limited-and-team-role-permissions)が必要です。

通知チャネルを特定のCampaignまたはキャンバスステップに適用すると、**到達可能なユーザー**数（ターゲットオーディエンスステップにあります）はAndroidプッシュで変化しないように見えます。ただし、選択した通知チャネルを購読しているユーザーのみがメッセージを受け取り、Campaignの分析（クリック数など）はこのオーディエンスに基づいて測定されます。

![]({% image_buster /assets/img_archive/push_notification_channels.png %})

{:start="4"}
4. **Add Notification Channel**をクリックします。
5. 追加する通知チャネルの名前とIDを入力します。<br><br>![]({% image_buster /assets/img_archive/push_notifications_channels_manage.png %})<br><br>
6. 追加する通知チャネルごとにステップ4と5を繰り返します。
7. **Save**を押して変更を保存します。

## フォールバックチャネルの指定 {#specifying-your-fallback-channel}

フォールバックチャネルは、メッセージにチャネルが選択されていない場合にBrazeがAndroidメッセージの送信を試みるチャネルです。チャネル選択のないAndroidメッセージを持つCampaignsとCanvasesは、チームがBrazeダッシュボードにチャネルを追加する前に作成されたCampaignsとCanvasesのみです。フォールバックチャネルを変更すると、明示的なチャネル選択のないすべてのCampaignsとCanvasesにグローバルに変更が適用されます。

1. 既存のCampaignまたはCanvasを開きます。
2. Androidプッシュ作成画面に移動します。
3. 通知チャネルオプションを展開した後、**Manage Notification Channels**を選択します。
4. チャネルをダッシュボードに追加します（まだ追加されていない場合）。
5. フォールバックチャネルとして指定するチャネルの横にあるラジオボタンを選択します。
6. 変更を保存します。変更はグローバルに適用されます。

## Androidプッシュメッセージへのチャネルの追加 {#adding-channels-to-your-android-push-messages}

1. CampaignまたはCanvasのAndroidプッシュ作成画面に移動します。
2. ドロップダウンから使用するチャネルを選択します。ドロップダウンがなく以下のビューが表示される場合は、Campaignsで選択する前にチャネルを追加する必要があります。

![プッシュ通知チャネルの作成画面]({% image_buster /assets/img_archive/push_notifications_channels_composer.png %})

[3]: https://developer.android.com/preview/features/notification-channels.html#DeletingChannels