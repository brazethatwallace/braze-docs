---
nav_title: プッシュ通知
article_title: "Braze SDKのプッシュ通知"
page_order: 2.3
description: "このランディングページは、プッシュ通知に関するすべての情報をまとめたページです。"
---

# プッシュ通知 {#push-notifications}

> [プッシュ通知]({{site.baseurl}}/user_guide/channels/push/)を使用すると、重要なイベントが発生したときにアプリから通知を送ることができます。新しいインスタントメッセージを配信したり、ニュース速報を送信したり、ユーザーのお気に入りのテレビ番組の最新エピソードがダウンロードしてオフライン視聴する準備ができたときに、プッシュ通知を送信することがあります。また、必要なときにのみアプリケーションが起動するため、バックグラウンドでの取得よりも効率的です。

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
{% multi_lang_include developer_guide/android_tv/push_notifications.md %}
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