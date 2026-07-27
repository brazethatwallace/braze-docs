---
nav_title: "プッシュサブスクリプション状態"
article_title: "プッシュサブスクリプション状態"
page_order: 2
page_type: reference
description: "このリファレンス記事では、Brazeにおけるプッシュ有効化とプッシュサブスクリプション状態の概念について説明します。iOS、Android、Webにおける動作の基本的な違いも含まれています。"
channel:
  - push

---

# プッシュ有効化とプッシュサブスクリプション {#push-enablement-and-push-subscription}

> このリファレンス記事では、Brazeにおけるプッシュ有効化とプッシュサブスクリプション状態の概念について説明します。iOS、Android、Webにおける動作の基本的な違いも含まれています。

{% multi_lang_include push/subscription_states.md %}

## プッシュ登録とステータスの確認場所 {#where-push-registration-and-status-appear}

プッシュサブスクリプション状態、登録、有効化は、Brazeの主に3つの場所で確認できます。

1. **[ユーザープロファイル](#user-profiles-and-push-changelog)**（**エンゲージメント**タブ）
2. **[セグメンテーション](#segmentation-and-push-filters)**（セグメントビルダー）
3. **[キャンペーンおよびキャンバスの分析](#campaign-and-canvas-analytics)**（各メッセージの分析ページ）

### ユーザープロファイルとプッシュ変更ログ {#user-profiles-and-push-changelog}

ユーザーのプロファイル（[**ユーザー検索**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) > ユーザーを選択 > **エンゲージメント**タブ）では、**Contact Settings**にプッシュサブスクリプション状態が表示され、**Push Registered For**（Brazeがそのプロファイルにフォアグラウンドプッシュを送信するために使用できるアプリとプラットフォーム）、およびトークンの移動、エラー、登録更新に関する**Push Changelog**が表示されます。**Push Registered For**とフォアグラウンドおよびバックグラウンドの認可の読み方については、[プッシュ登録ステータスの確認]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status)を参照してください。

iOSおよびAndroidでは、デバイスがフォアグラウンドプッシュ認可からバックグラウンドのみに移行した場合（たとえば、ユーザーがシステム設定で通知をオフにし、SDKがその変更を報告した場合）、プッシュ変更ログに「Push token was updated from foreground push enabled to foreground push disabled」などのエントリが含まれることがあります。

新しいSDKデータを期待している場合（たとえば、テストセッションの直後）、値が古く見える場合はユーザープロファイルで**Refresh**を選択してください。SDKがデータをフラッシュしてからプロファイルに最新のプッシュ登録が反映されるまでに短い遅延が発生する場合があります。

[内部グループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)に追加したユーザーについては、そのグループの**Internal Group Settings**で**Record User Events for group members**を選択すると、SDKリクエストがログに表示されます。次に、**設定** > **Event User Log**で[イベントユーザーログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log)を開き、ユーザーのSDKリクエストを見つけて、生のペイロードを展開します。デバイスがリモート通知を有効または無効として報告しているかどうかを検証しながら、`remote_notification_enabled`などのフィールドを確認できます。

### セグメンテーションとプッシュフィルター {#segmentation-and-push-filters}

セグメントビルダーでは、**`Foreground Push Enabled`**、**`Foreground Push Enabled for App`**、**`Background or Foreground Push Enabled`**、およびプッシュサブスクリプションフィルターなどのフィルターを使用して、設定やデバイスレベルの認可によってユーザーをターゲティングまたは監査できます。iOSでは、特定のユーザーに対するこれらのフィルターの読み取り方は、OSプロンプトを完了したかどうか、設定を変更したかどうか、または[仮承認](#provisional-push)を使用しているかどうかによって異なります。[iOSユーザーアクションとプッシュステータス](#ios-user-actions-push-status)および[その他のプラットフォーム固有のシナリオ](#foreground-push-enabled)を参照してください。

### キャンペーンおよびキャンバスの分析 {#campaign-and-canvas-analytics}

プッシュ**キャンペーン**または**キャンバス**の分析ページでは、*送信数*、*バウンス数*、*開封数*などの指標がその送信の配信とエンゲージメントを反映します。これらの数値を個々のプロファイルと照合するには、**キャンペーンの詳細**または**キャンバスの詳細**から**ユーザーデータ**（CSV）を使用して受信者をエクスポートします。手順と権限については、[キャンペーンデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data)および[キャンバスデータのエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data)を参照してください。分析とエクスポートの間でカウントが一致しない場合は、エクスポートのトラブルシューティングの[キャンペーンおよびキャンバスの分析]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting#campaign-and-canvas-analytics)を参照してください。

## iOSユーザーアクションとプッシュステータス {#ios-user-actions-push-status}

以下の表は、さまざまなユーザーアクションがBrazeにおけるiOSプッシュ有効化、フォアグラウンドまたはバックグラウンドプッシュ登録、およびプッシュサブスクリプションステータスにどのように影響するかを示しています。ユーザーがアプリをインストールして最初のセッションを開始すると、その状態は通常、最初の行に示されているとおりになります。後続の各アクションにより、これらの値の一部が更新される場合がありますが、すべてが更新されるわけではありません。

| ユーザーアクション | `Foreground Push Enabled` | `Foreground Push Enabled for App` | プッシュ登録タイプ | プッシュサブスクリプションステータス |
| --- | --- | --- | --- | --- |
| ユーザーがアプリをインストールしてセッションを記録する | `false`* | 更新なし | バックグラウンド | `Subscribed` |
| ユーザーがiOSネイティブプッシュプロンプトを受け取り、**Allow**を選択する | `true` | `true` | フォアグラウンド | `Opted-In`** |
| ユーザーがiOSネイティブプッシュプロンプトを受け取り、**Don't Allow**を選択する | `false` | 更新なし | バックグラウンド | 更新なし |
| ユーザーがデバイス設定からプッシュを有効にしてセッションを記録する | `true` | `true` | フォアグラウンド | `Opted-In`** |
| ユーザーがデバイス設定からプッシュを無効にしてセッションを記録する | `false` | `false` | バックグラウンド | 更新なし |
| ユーザーがアプリを削除する | 更新なし | プッシュトークンが無効化された時に更新 | プッシュトークンが無効化された時に更新 | 更新なし |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="iOSユーザーアクションとプッシュステータス" }

<sup>* アプリが仮承認プッシュを使用していない場合、ユーザーがプッシュ通知を許可するまで`Foreground Push Enabled`は`false`です。アプリが仮承認プッシュを使用している場合、最初のセッション開始時に`Foreground Push Enabled`は`true`になります。詳細については、[仮承認とサイレントプッシュ](#provisional-push)を参照してください。</sup>

<sup>** [Braze Swift SDKバージョン7.5.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0)以降、`optInWhenPushAuthorized`設定プロパティにより、プッシュ権限が承認された際にプッシュサブスクリプション状態が自動的に`Opted-In`に設定されるかどうかを制御できます。詳細については、[プッシュトークン](#push-tokens)を参照してください。</sup>

## プッシュ通知の許可 {#push-permission}

プッシュ通知が有効なすべてのプラットフォーム（iOS、Web、Android）では、OSレベルのシステムプロンプトによる明示的なオプトインが必要です。プラットフォームごとの若干の違いについては、以下のセクションで説明します。

ユーザーの決定は最終的なものであり、一度拒否された後に再度尋ねることはできないため、[プッシュプライマー]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)のアプリ内メッセージを使用することは、オプトイン率を向上させるための重要な戦略です。

**ネイティブOSプッシュ許可プロンプト**

|プラットフォーム|スクリーンショット|説明|
|--|--|--|
|iOS| ![「My Appが通知を送信します」というメッセージの下部に「許可しない」と「許可」の2つのボタンがあるiOSネイティブプッシュプロンプト。]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | [仮承認プッシュ](#provisional-push)の許可をリクエストする場合、これは適用されません。|
|Android| ![「Kitchenerieからの通知を許可しますか？」というメッセージの下部に「許可」と「許可しない」の2つのボタンがあるAndroidプッシュメッセージ。]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | このプッシュ許可はAndroid 13で導入されました。Android 13より前のバージョンでは、プッシュ通知の送信に許可は必要ありませんでした。|
|Web| ![「Braze.comが通知を表示しようとしています」というメッセージの下部に「ブロック」と「許可」の2つのボタンがあるWebブラウザのネイティブプッシュプロンプト。]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="プッシュ通知の許可" }

### Android

Android 13より前のバージョンでは、プッシュ通知の送信に許可は必要ありませんでした。Android 12以下では、Brazeが自動的にプッシュトークンをリクエストする最初のセッション時に、すべてのユーザーが`Subscribed`と見なされます。この時点で、ユーザーはそのデバイスの有効なプッシュトークンと`Subscribed`のデフォルト購読ステータスを持つ**プッシュ有効**状態になります。

[Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13)以降では、プッシュ許可をユーザーにリクエストし、承認を得る必要があります。アプリは適切なタイミングでユーザーに手動で許可をリクエストできますが、リクエストしない場合は、アプリが[通知チャネル](https://developer.android.com/reference/android/app/NotificationChannel)を作成した際に自動的にプロンプトが表示されます。

### iOS

![「Yachtrアプリからの通知を引き続き受信しますか？」というメッセージの下に「受信を続ける」と「オフにする」の2つのボタンがある、システム通知センターの通知。]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

アプリは仮承認プッシュまたは承認済みプッシュをリクエストできます。

承認済みプッシュでは、通知を送信する前にユーザーからの明示的な許可が必要ですが、[仮承認プッシュ](https://www.braze.com/resources/articles/mastering-provisional-push)では、音やアラートなしに通知センターに直接__静かに__通知を送信できます。

#### 仮承認と静かなプッシュ {#provisional-push}

iOS 12（2018年リリース）より前のバージョンでは、すべてのユーザーがプッシュ通知を受信するために明示的にオプトインする必要がありました。

iOS 12で、Appleは[仮承認](https://www.braze.com/resources/articles/mastering-provisional-push)を導入しました。これにより、ブランドはユーザーが明示的にオプトインする前に、ユーザーの通知センターに静かなプッシュ通知を送信でき、メッセージの価値を早い段階で示す機会が得られます。詳しくは[仮承認]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push)を参照してください。

### Web {#web}

Webでは、ネイティブブラウザの許可ダイアログを通じて、明示的なユーザーオプトインをリクエストする必要があります。

iOSやAndroidではアプリがいつでも許可プロンプトを表示できますが、一部のモダンブラウザでは「ユーザージェスチャー」（マウスクリックやキーストローク）によってトリガーされた場合にのみプロンプトが表示されます。サイトがページ読み込み時にプッシュ通知の許可をリクエストしようとすると、ブラウザによって無視されるか、非表示にされる可能性があります。

そのため、ページが読み込まれたときにランダムにリクエストするのではなく、ユーザーがWebサイト上のどこかをクリックしたときにのみ許可をリクエストするようにしてください。

## プッシュトークン {#push-tokens}

[プッシュトークン]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle)は、ユーザーのデバイスによって生成される一意の匿名識別子であり、各受信者の通知をどこに送信するかを識別するためにBrazeに送信されます。

[プッシュトークン]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle)には、プッシュ通知がユーザーにどのように送信されるかを理解するうえで不可欠な2つの分類方法があります。

1. **フォアグラウンドプッシュ**は、ユーザーのデバイスのフォアグラウンドに通常の可視プッシュ通知を送信する機能を提供します。
2. **バックグラウンドプッシュ**は、特定のデバイスがそのブランドからのプッシュ通知の受信をオプトインしているかどうかに関係なく利用できます。バックグラウンドプッシュにより、ブランドはサイレントプッシュ通知（意図的に表示されない通知）をデバイスに送信して、[アンインストール追跡]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)などの主要な機能をサポートできます。

ユーザープロファイルにアプリに関連付けられた有効なフォアグラウンドプッシュトークンがある場合、Brazeはそのユーザーを該当アプリの「プッシュ登録済み」とみなします。Brazeは、これらのユーザーを識別するために、`Foreground Push Enabled for App,` という特定のセグメンテーションフィルターを提供しています。

{% alert note %}
`Foreground Push Enabled for App` フィルターは、該当アプリの有効なフォアグラウンドおよびバックグラウンドプッシュトークンの存在のみを考慮します。一方、より汎用的な[`Foreground Push Enabled`](#foreground-push-enabled)フィルターは、ワークスペース内のいずれかのアプリでプッシュ通知を明示的に有効にしたユーザーをセグメント化します。このカウントにはフォアグラウンドプッシュのみが含まれ、購読解除したユーザーは含まれません。これらのフィルターやその他のフィルターの詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)を参照してください。

ごく少数のユーザーについては、処理の遅延により一時的な不一致が発生する場合があります。ユーザーのプロファイルに有効なフォアグラウンドプッシュトークンがあるにもかかわらず、`Foreground Push Enabled` フィルターに一致しないことがあります。トークンが存在しているにもかかわらず、プロファイル上ではフォアグラウンドプッシュが有効になっていないと一時的に表示される場合があります。これは通常、処理が追いつくと解消されます。
{% endalert %}

### 1つのデバイスに複数のユーザー {#multiple-users-on-one-device}

プッシュトークンはデバイスとアプリの両方に固有であるため、プッシュトークンを使用して同じデバイスを使用している複数のユーザーを区別することはできません。

たとえば、CharlieとKimという2人のユーザーがいるとします。Charlieが自分のスマートフォンでアプリのプッシュ通知を有効にしており、KimがCharlieのスマートフォンを使ってCharlieのプロファイルからログアウトし、自分のプロファイルにログインした場合、プッシュトークンはKimのプロファイルに再割り当てされます。その後、Kimがログアウトし、Charlieが再度ログインするまで、プッシュトークンはそのデバイス上でKimのプロファイルに割り当てられたままになります。

アプリまたはWebサイトでは、デバイスごとに1つのプッシュ購読のみを持つことができます。そのため、ユーザーがデバイスまたはWebサイトからログアウトし、新しいユーザーがログインすると、プッシュトークンは新しいユーザーに再割り当てされます。これは、ユーザーのプロファイルの**エンゲージメント**タブの**連絡先設定**セクションに反映されます。

![ユーザーのプロファイルの**エンゲージメント**タブにあるプッシュトークンの変更ログ。プッシュトークンが別のユーザーに移動された日時とそのトークンの内容が表示されます。]({% image_buster /assets/img/push_token_changelog.png %})

プッシュプロバイダー（APNs/FCM）が1つのデバイス上の複数のユーザーを区別する方法がないため、最後にログインしたユーザーにプッシュトークンを渡して、デバイス上でプッシュのターゲットとするユーザーを決定します。

### 複数のデバイスと1人のユーザー {#multiple-devices-and-one-user}

プッシュ購読状態はユーザーベースであり、個々のアプリに固有のものではありません。プッシュ購読状態は、最後に設定された値です。したがって、ユーザーがプッシュ通知をオプトインした場合、そのプッシュ購読状態はすべての対象デバイスで`Opted-In`になります。その後、ユーザーがアプリケーションまたはブランドが提供するその他の方法を通じてプッシュ通知を明示的に購読解除した場合、プッシュ購読状態は`Unsubscribed`に更新され、プッシュ登録済みのデバイスはプッシュ通知を受信できなくなります。

## Foreground Push Enabledフィルター {#foreground-push-enabled}

`Foreground Push Enabled`は、Brazeのセグメンテーションフィルターであり、マーケターがBrazeにプッシュ通知の送信を許可しているユーザーと、プッシュ通知を受け取らないという意思を表明していないユーザーを簡単に識別できます。

`Foreground Push Enabled`フィルターは以下を考慮します：
- Brazeがプッシュ通知を送信できるかどうか（フォアグラウンドプッシュトークン）
- ユーザーのいずれかのデバイスでプッシュを受信するための全体的な設定（プッシュサブスクリプション状態）

![ユーザーが「Push Registered for Marketing (iOS)」であることを示すダッシュボードのスクリーンショット]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

ユーザーは、ワークスペース内のアプリのアクティブなフォアグラウンドプッシュトークンを持っている場合、「プッシュ有効」または「プッシュ登録済み」と見なされます。つまり、プッシュ有効化ステータスはアプリ固有です。

{% alert note %}
プッシュ登録状態の確認方法については、[プッシュ登録ステータス]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status)を参照してください。
{% endalert %}

## プッシュ登録とチェンジログ情報の確認 {#finding-push-registration-and-changelog-information}

ダッシュボードでは、プッシュ登録とプッシュチェンジログに関する情報を以下の場所で確認できます。

- **セグメンテーション** – ユーザーの購読状態、有効状態、フォアグラウンドおよびバックグラウンドの有効状態でフィルタリングします。
- **キャンペーン分析** – 単一のキャンペーンまたはキャンバスのプッシュ統計とフィードバックを表示します。
- **ユーザープロファイル（エンゲージメントタブ）** – 特定のユーザーの**連絡先設定**とプッシュチェンジログを表示します。

プッシュ有効状態を確認する際、**プッシュ登録先**は、そのユーザーに対してBrazeがフォアグラウンドプッシュを送信できるプラットフォームを示します。iOSおよびAndroidでは、ユーザーがフォアグラウンドプッシュ有効からバックグラウンドプッシュ有効（`remote_notification_enabled`）に移行した場合、プッシュチェンジログに「プッシュトークンがフォアグラウンドプッシュ有効からフォアグラウンドプッシュ無効に更新されました」と記録されます。

ユーザーがテストユーザーとして追加されている場合、**開発者コンソール** > **ユーザーイベントログ**で、ユーザープロファイルに`remote_notification_enabled`が`true`または`false`のSDKリクエストが表示されます。SDKの更新がユーザープロファイルに反映されるまでわずかな遅延があるため、ユーザープロファイルを更新する必要がある場合があります。

**iOSプッシュ状態のセグメンテーションフィルター:**

- **iOSフォアグラウンドおよびバックグラウンドプッシュ無効:** ユーザーにはまだプッシュプロンプトが表示されていません。
- **iOSバックグラウンド有効:** ユーザーにプッシュプロンプトが表示され、拒否したか、許可した後にデバイス設定でプッシュ通知をオフにしました（ユーザーがセッションを持った後に反映されます）。
- **iOSフォアグラウンド有効:** ユーザーにプッシュプロンプトが表示され、フォアグラウンドプッシュを受信する資格があります。

キャンペーン分析には、このセクションで前述した詳細に沿ったプッシュ統計が表示されます。また、キャンペーンまたはキャンバスに参加したユーザープロファイルをダウンロードして、ユーザープロファイルを照合することもできます。

## その他のプラットフォーム固有のシナリオ {#other-platform-specific-scenarios}

{% tabs %}
{% tab Web %}

ユーザーがネイティブのプッシュ許可プロンプトを承認すると、購読ステータスが`opted in`に変更されます。

購読を管理するには、ユーザーメソッド[`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype)を使用してサイトに設定ページを作成し、ダッシュボードでオプトアウトステータスによってユーザーをフィルタリングできます。

ユーザーがブラウザ内で通知を無効にした場合、そのユーザーに送信される次のプッシュ通知はバウンスし、Brazeはユーザーのプッシュトークンを適宜更新します。これは、プッシュ有効フィルター（`Background or Foreground Push Enabled`、`Foreground Push Enabled`、`Foreground Push Enabled for App`）の適格性を管理するために使用されます。ユーザーのプロファイルに設定された購読ステータスはユーザーレベルの設定であり、プッシュがバウンスしても変更されません。

### 410 Webプッシュトークンエラー {#410-web-push-token-errors}

`410: Gone`エラーが発生した場合、これはユーザーがOSの設定からブラウザのWebプッシュ通知を無効にした場合、同じデバイスで別のユーザーとしてログインしている場合、またはユーザーがしばらくWebサイトにアクセスしていない場合に発生する可能性があります。

`410: Endpoint Not Valid`エラーが発生した場合、これはWebプッシュトークン（基本的にはURL）の有効期限が切れたことを意味する可能性があります。これは、ユーザーが再びサイトにアクセスしない場合や、ブラウザがトークンを無効にした場合に発生する可能性があります。また、ブラウザによっては定期的に（多くの場合数か月ごとに）発生することもあります。ユーザーが再びサイトにアクセスし、ブラウザが「許可」に設定されている場合、Brazeはデバイスの新しいトークンを自動的に収集します。これは、SDKの初期化時に[`disablePushTokenMaintenance`初期化オプション](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions)が使用されていないことを前提としています。

{% alert note %}
Webプラットフォームでは、バックグラウンドまたはサイレントプッシュは許可されていません。
{% endalert %}
{% endtab %}
{% tab Android %}

フォアグラウンドプッシュが有効なユーザーがOSの設定でプッシュを無効にした場合、次のセッション開始時に以下が発生します：
- Brazeはそのユーザーをフォアグラウンドプッシュ無効としてマークし、プッシュメッセージの送信を試みなくなります。
- `Foreground Push Enabled for App (Android)`フィルターおよび`Foreground Push Enabled`セグメンテーションフィルター（ユーザープロファイル上の他のアプリに有効なフォアグラウンドプッシュトークンがない場合）は`false`を返します。

このシナリオでは、バックグラウンドプッシュトークンは引き続き存在するため、セグメンテーションフィルター`Background or Foreground Push Enabled = true`を使用してバックグラウンド（サイレント）プッシュ通知を送信し続けることができます。

Androidの場合、Brazeは以下の状況でユーザーをプッシュ無効と見なします：

- ユーザーがデバイスからアプリをアンインストールした場合。
- バウンスによりプッシュメッセージの配信に失敗した場合。これは通常アンインストールが原因ですが、アプリの更新、新しいプッシュトークンバージョン、またはフォーマットが原因の場合もあります。
- Firebase Cloud Messagingへのプッシュ登録が失敗した場合（ネットワーク接続の不良や、FCMへの接続失敗、または有効なトークンの返却失敗が原因の場合があります）。
- ユーザーがデバイスの設定でアプリのプッシュ通知をブロックし、その後セッションを記録した場合。

{% alert note %}
Androidのプッシュ通知をインターセプトできるのは、アプリがフォアグラウンドまたはバックグラウンド（ただし実行中）にある場合のみです。アプリが終了または完全に強制終了されている場合、通知をインターセプトすることはできません。
{% endalert %}

{% endtab %}
{% tab iOS %}

ユーザーがフォアグラウンドプッシュのオプトインプロンプトを承認したかどうかに関係なく、Xcodeでリモート通知が有効になっており、アプリが[`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications)を呼び出している場合、バックグラウンドプッシュを送信できます。

アプリが仮承認されている場合、またはユーザーがプッシュにオプトインしている場合、フォアグラウンドプッシュトークンを受け取り、すべての種類のプッシュを送信できます。Brazeでは、フォアグラウンドプッシュが有効なiOSユーザーを、明示的（アプリレベル）または仮承認（デバイスレベル）のいずれかでプッシュ有効と見なします。

ユーザーがOSレベルでプッシュ通知の受信を拒否した場合、プッシュ購読ステータスは`Subscribed`となり、プロファイルにはフォアグラウンドプッシュトークンが登録されたことは表示されません。

最初にOSレベルでオプトインしたユーザーがOSの設定でプッシュ通知を無効にした場合、次のセッション開始時に以下が発生します：
- Brazeはそのユーザーをフォアグラウンドプッシュ無効としてマークし、プッシュメッセージの送信を試みなくなります。
- `Foreground Push Enabled for App (iOS)`フィルターおよび`Foreground Push Enabled`セグメンテーションフィルター（ユーザープロファイル上の他のアプリに有効なフォアグラウンドプッシュトークンがない場合）は`false`を返します。

このシナリオでは、バックグラウンドプッシュトークンは引き続き存在するため、セグメンテーションフィルター`Background or Foreground Push Enabled = true`を使用してバックグラウンド（サイレント）プッシュ通知を送信し続けることができます。

{% alert note %}
iOSでは、プッシュ通知が表示される前にアプリがプッシュ通知をインターセプトすることは許可されていません。つまり、アプリ（およびBraze）は通知を表示するか非表示にするかを制御できません。ユーザーはデバイスの設定でアプリのプッシュ通知をオプトアウトできますが、それはオペレーティングシステムによって制御されます。
{% endalert %}

{% endtab %}
{% endtabs %}

## ベストプラクティス {#best-practices}

Brazeでのプッシュの活用を最適化するための詳細なガイダンスについては、[プッシュのベストプラクティス]({{site.baseurl}}/user_guide/channels/push/best_practices)に関する専用の記事を参照してください。