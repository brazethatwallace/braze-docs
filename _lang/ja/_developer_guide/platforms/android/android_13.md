---
nav_title: Android 13へのアップグレード
article_title: Android 13アップグレードガイド
page_order: 9
platform:
  - Android
  - FireOS
description: "この記事では、Android 13、SDKの更新、プッシュアクセス許可の変更、SDKの互換性などについて説明します。"
---

# Android 13へのアップグレード {#upgrading-to-android-13}

> このガイドでは、Android 13 (2022) で導入された関連のある変更と、Braze Android SDK統合に必要なアップグレード手順について説明します。

完全な移行ガイドについては、[Android 13開発者向けドキュメント](https://developer.android.com/about/versions/13)を参照してください。

## Android 13 Braze SDK {#android-13-braze-sdk}

Android 13に備えるには、Braze SDKを[最新バージョン (v21.0.0以降)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300)にアップグレードしてください。そうすることで、新しい[「コードなし」プッシュプライマー機能]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)を利用できるようになります。

## Android 13での変更点 {#changes-in-android-13}

### プッシュアクセス許可 {#push-permission}

Android 13では、ユーザーがプッシュ通知を送信するアプリを管理する方法に[大きな変更](https://developer.android.com/about/versions/13/changes/notification-permission)が導入されています。Android 13では、アプリはプッシュ通知を表示する前にアクセス許可を取得する必要があります。

![「Kitchenerieからの通知を許可しますか？」というAndroidのプッシュメッセージで、メッセージの下に「許可する」と「許可しない」の2つのボタンがある。]({% image_buster /assets/img/android/android-13-push-prompt.png %}){: style="float:right;max-width:430px;width:50%;margin-left:15px;border:0"}

この新しいアクセス許可は、iOSおよびWebプッシュと同様のパターンに従い、許可の取得を1回試行するだけです。ユーザーが`Don't Allow`を選択した場合、またはプロンプトを無視すると、アプリは再度許可を求めることができなくなります。

Android 13に更新する前にプッシュ通知を有効にしていたユーザーに対しては、アプリには[除外が適用](https://developer.android.com/about/versions/13/changes/notification-permission#eligibility)されることに注意してください。これらのユーザーは、Android 13に更新しても、許可をリクエストしなくてもプッシュを受け取ることが[可能](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps)です。

#### アクセス許可プロンプトのタイミング {#push-permission-timing}

**Android 13をターゲットにする場合**

Android 13をターゲットにしているアプリは、許可をリクエストするタイミングとネイティブプッシュプロンプトを表示するタイミングを制御できます。

ユーザーがAndroid 12から13にアップグレードし、アプリが以前にインストールされており、すでにプッシュを送信していた場合、システムは対象となるすべてのアプリに新しい通知アクセス許可を自動的に事前付与します。つまり、これらのアプリはユーザーに通知を送信し続けることができ、ユーザーにはランタイムアクセス許可プロンプトが表示されません。

詳細については、Androidの開発者向けドキュメントの[既存アプリの更新への影響](https://developer.android.com/about/versions/13/changes/notification-permission#existing-apps)を参照してください。

**Android 12以前をターゲットにする場合**

アプリがまだAndroid 13をターゲットにしていない場合、Android 13の新しいユーザーがアプリをインストールすると、アプリが最初の通知チャネルを作成した時点（`notificationManager.createNotificationChannel`経由）で、プッシュアクセス許可プロンプトが自動的に表示されます。すでにアプリをインストールしているユーザーがAndroid 13にアップグレードした場合、プロンプトは表示されず、プッシュアクセス許可が自動的に付与されます。

{% alert note %}
Braze SDK v23.0.0は、プッシュ通知を受信した際にデフォルトの通知チャネルがまだ存在しない場合、自動的に作成します。Android 13をターゲットにしていない場合、これによりプッシュアクセス許可プロンプトが表示されますが、これは通知を表示するために必要です。
{% endalert %}

## Android 13への準備 {#next-steps}

ユーザーにプッシュアクセス許可を求めるタイミングを制御するために、アプリがAndroid 13をターゲットにすることを強くお勧めします。

Android 13をターゲットにすることで、より適切なタイミングでユーザーにプロンプトを表示して[プッシュオプトイン率](https://www.braze.com/resources/articles/android-13-developer-preview-push-opt-ins-arrive-for-android-apps)を最適化でき、アプリがプッシュアクセス許可を求める方法とタイミングにおいてより良いユーザー体験を提供できます。

新しい[「コードなし」プッシュプライマー機能]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages)の使用を開始するには、Android SDKを[最新バージョン (v23.0.0以降)](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2300)にアップグレードしてください。