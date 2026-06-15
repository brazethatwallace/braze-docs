---
nav_title: プッシュ通知
article_title: Windows Universalのプッシュ通知
platform: Windows Universal
page_order: 1
description: "この記事では、Windows Universalプラットフォーム向けのプッシュ通知統合手順について説明します。"
channel: push
hidden: true
---

# プッシュ通知の統合 {#push-notification-integration}
{% multi_lang_include archive/windows_deprecation.md %}

![Windows Universalプッシュ通知の例。]({% image_buster /assets/img_archive/windows_uni_push_sample.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアプリ外のアラートです。プッシュ通知は、時間的制約があり関連性の高いコンテンツをユーザーに提供したり、ユーザーをアプリに再エンゲージしたりするための効果的な方法です。

その他のベストプラクティスについては、[ドキュメント]({{site.baseurl}}/user_guide/channels/push/best_practices/)を参照してください。

## ステップ 1: プッシュ通知用にアプリケーションを設定する {#step-1-configure-your-application-for-push}

`Package.appxmanifest` ファイルで、以下の設定が構成されていることを確認します。

**Application** タブで、`Toast Capable` が `YES` に設定されていることを確認してください。

## ステップ 2: Brazeダッシュボードを設定する {#step-2-configure-the-braze-dashboard}

1. [SIDとクライアントシークレットを検索する](http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx)
2. Brazeダッシュボードの**設定**ページで、SIDとクライアントシークレットを設定に追加します。<br>![]({% image_buster /assets/img_archive/windows_sid.png %} "Windows SID dashboard")

## ステップ 3: バックグラウンド開封ロギングの更新 {#step-3-update-for-background-open-logging}

`OnLaunched` メソッドで、`OpenSession` を呼び出した後、以下のコードスニペットを追加します。

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);
}
```

## ステップ 4: イベントハンドラを作成する {#step-4-creating-event-handlers}

プッシュが受信され、アクティベート（ユーザーがクリック）されたときに発生するイベントをリッスンするには、イベントハンドラを作成し、`PushManager` のイベントに追加します。

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

イベントハンドラには以下のシグネチャが必要です。

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## ステップ 5: プッシュからアプリへのディープリンク {#step-5-deep-linking-from-push-into-your-app}

### パート 1: アプリのディープリンクを作成する {#part-1-creating-deep-links-for-your-app}

ディープリンクは、アプリケーションの外部からユーザーをアプリケーション内の特定の画面やページに直接ナビゲートするために使用されます。通常これは、オペレーティングシステムにURLスキーム（例: myapp://mypage）を登録し、そのスキームを処理するアプリケーションを登録することで行われます。OSがその形式のURLを開くよう要求されると、アプリケーションに制御が移ります。

WNSのディープリンクサポートは、ユーザーの送信先に関するデータを含めてアプリケーションを起動するため、これとは異なります。WNSプッシュが作成されると、プッシュがクリックされアプリケーションが開かれたときに、アプリケーションの `OnLaunched` に渡される起動文字列を含めることができます。この起動文字列はすでにキャンペーントラッキングに使用されており、アプリが起動したときに解析してユーザーをナビゲートするために使用できる独自のデータを追加する機能をユーザーに提供しています。

ダッシュボードやREST APIで追加の起動文字列を指定すると、作成した起動文字列の末尾、キー「abextras=」の後に追加されます。そのため、起動文字列の例は `ab_cn_id=_trackingid_abextras=page=settings` のようになります。この例では、追加の起動文字列パラメータで `page=settings` を指定しているため、これを解析してユーザーを設定ページに移動できます。

### パート 2: ダッシュボードを使ったディープリンク {#part-2-deep-linking-through-the-dashboard}

プッシュ通知設定の「追加の起動文字列設定」フィールドで、起動文字列に追加する文字列を指定します。

![]({% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Deep Link Click Action")

### パート 3: REST APIによるディープリンク {#part-3-deep-linking-through-the-rest-api}

Brazeでは、REST APIを通じてディープリンクを送信することもできます。[Windows Universalプッシュオブジェクト]({{site.baseurl}}/api/objects_filters/)は、オプションの `extra_launch_string` パラメータを受け付けます。