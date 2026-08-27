---
nav_title: プッシュ通知
article_title: プッシュ通知
page_order: 2.3
description: "このランディングページは、プッシュ通知に関するすべての情報をまとめたページです。"
---

# プッシュ通知 {#push-notifications}

> [プッシュ通知]({{site.baseurl}}/user_guide/channels/push)を使用すると、重要なイベントが発生したときにアプリから通知を送ることができます。新しいインスタントメッセージを配信したり、ニュース速報を送信したり、ユーザーのお気に入りのテレビ番組の最新エピソードがオフライン視聴用にダウンロードできるようになったときに、プッシュ通知を送信できます。また、必要なときにのみアプリケーションが起動するため、バックグラウンドでの取得よりも効率的です。

{% alert note %}
**Web URLにリダイレクト**で**アプリ内でWeb URLを開く**が選択されていないにもかかわらず、リンクがアプリ内で開かれる場合、アプリがそのURLを処理している可能性があります（例えば、iOSのユニバーサルリンクやAndroidのApp Linksなど）。代わりにブラウザーでリンクを開くには、ユーザーが通知をタップしたときにアプリがURLをシステムブラウザーに委任していることを確認するか、クリックアクションがBrazeダッシュボードの設定と一致するようにアプリのURL処理を調整してください。クリックアクションとURL処理の設定方法については、各プラットフォームのプッシュ通知ドキュメントを参照してください。
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
## Android TVのプッシュ通知について {#about-push-notifications-for-android-tv}

![Android TVプッシュ通知ガイドで使用されるAndroid TVデバイスのイラスト]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

ネイティブ機能ではありませんが、Braze Android SDKとFirebase Cloud Messagingを活用してAndroid TV用のプッシュトークンを登録することで、Android TVプッシュ統合が可能になります。ただし、通知ペイロードを受信した後に表示するためのUIを構築する必要があります。

## 前提条件 {#prerequisites}

この機能を使用するには、以下を完了する必要があります。

- [Braze Android SDKを統合する]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Braze Android SDKのプッシュ通知を設定する]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)

## プッシュ通知の設定 {#setting-up-push-notifications}

Android TVのプッシュ通知を設定するには、以下の手順に従います。

1. アプリにカスタムビューを作成して通知を表示します。
2. [カスタム通知ファクトリー]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display)を作成します。これにより、デフォルトのSDK動作がオーバーライドされ、通知を手動で表示できるようになります。`null`を返すことで、SDKによる処理が防止され、通知を表示するためのカスタムコードが必要になります。これらのステップを完了すると、Android TVへのプッシュ送信を開始できます。<br><br>
3. （オプション）クリック分析を効果的にトラッキングするには、クリック分析トラッキングを設定します。これは、Brazeプッシュの開封および受信インテントをリッスンする[プッシュコールバック]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback)を作成することで実現できます。

{% alert note %}
これらの通知は永続的ではなく、デバイスが表示しているときにのみユーザーに表示されます。これは、Android TVの通知センターが通知履歴をサポートしていないためです。
{% endalert %}

## Android TVプッシュ通知のテスト {#testing-android-tv-push-notifications}

プッシュ実装が成功したかどうかをテストするには、通常のAndroidデバイスと同様に、Brazeダッシュボードから通知を送信します。

- **アプリケーションが閉じている場合**：プッシュメッセージは画面にトースト通知として表示されます。
- **アプリケーションが開いている場合**：独自のホストUIでメッセージを表示できます。Android Mobile SDKのアプリ内メッセージのUIスタイルに従ってください。

## ベストプラクティス {#best-practices}

Brazeを使用するマーケターにとって、Android TVへのキャンペーン配信は、Androidモバイルアプリへのプッシュ配信と同じです。これらのデバイスのみをターゲットにするには、セグメンテーションでAndroid TVアプリを選択してください。

FCMから返される配信およびクリックのレスポンスは、モバイルAndroidデバイスと同じ規則に従います。そのため、エラーはメッセージアクティビティログに表示されます。

{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}