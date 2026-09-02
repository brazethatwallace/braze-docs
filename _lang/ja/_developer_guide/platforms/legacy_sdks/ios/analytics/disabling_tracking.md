---
nav_title: iOS SDKのトラッキングを無効にする
article_title: iOS向けSDKトラッキングを無効化する
platform: iOS
page_order: 8
description: "この記事では、iOSアプリケーションのデータ収集を無効にする方法を説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# iOSでのデータ収集を無効にする {#disable-data-collection-for-ios}

データプライバシー規制に準拠するために、iOS SDKのデータトラッキングアクティビティは[`disableSDK`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a8d3b78a98420713d8590ed63c9172733)メソッドを使用して完全に停止できます。このメソッドによってすべてのネットワーク接続がキャンセルされ、Braze SDKはBrazeサーバーにデータを渡しません。後でデータ収集を再開する場合は、[`requestEnableSDKOnNextAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#a781078a40a3db0de64ac82dcae3b595b)メソッドを使用してデータ収集を再開できます。

また、[`wipeDataAndDisableForAppRun`](http://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#ac8d580f60ec0608cd91240a8a3aa23a3)メソッドを使用して、デバイスに保存されているすべてのクライアント側データを完全に消去できます。

特定のデバイス上で、同じベンダーのすべてのアプリをユーザーがアンインストールしない限り、`wipeDataAndDisableForAppRun()`を呼び出した後のBraze SDKおよびアプリの次回実行時に、サーバーはそのユーザーをデバイス識別子（IDFV）によって再識別します。すべてのユーザーデータを完全に削除するには、`wipeDataAndDisableForAppRun`の呼び出しと、Braze [REST API]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)を介したサーバー上のデータ削除リクエストを組み合わせる必要があります。

## iOS SDK v5.7.0以降 {#ios-sdk-v570}
iOS SDK v5.7.0以降を使用しているデバイスでは、[IDFV収集を無効にしている]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#optional-idfv-collection---swift)場合、[`wipeData`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata())を呼び出しても、サーバーがデバイス識別子（IDFV）を使用してそのユーザーを再識別することはありません。