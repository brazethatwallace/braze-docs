---
nav_title: カスタムサウンド
article_title: iOS用カスタムプッシュ通知サウンド
platform: iOS
page_order: 3
description: "このリファレンス記事では、iOSプッシュ通知にカスタムサウンドを実装する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# カスタムサウンド {#custom-sounds}

## ステップ 1:アプリでサウンドをホスティングする {#step-1-hosting-the-sound-in-the-app}

カスタムプッシュ通知サウンドは、クライアントアプリケーションのメインバンドル内でローカルにホストする必要があります。以下のオーディオデータ形式が使用できます。

- リニア PCM
- MA4
- µLaw
- aLaw

オーディオデータは AIFF、WAV、または CAF ファイルにパッケージできます。Xcode で、サウンドファイルをアプリケーションバンドルの非ローカライズリソースとしてプロジェクトに追加します。

afconvert ツールを使用してサウンドを変換できます。たとえば、16ビットリニア PCM システムサウンド Submarine.aiff を CAF ファイルの IMA4 オーディオに変換するには、ターミナルで次のコマンドを使用します。

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

QuickTime Player でサウンドを開き、**ムービー**メニューから**ムービーインスペクターを表示**を選択すると、サウンドのデータ形式を確認できます。

カスタムサウンドは再生時間が30秒未満である必要があります。カスタムサウンドがこの制限を超えている場合、デフォルトのシステムサウンドが代わりに再生されます。

## ステップ 2:ダッシュボードにサウンドのプロトコル URL を指定する {#step-2-providing-the-dashboard-with-a-protocol-url-for-the-sound}

サウンドはアプリ内でローカルにホストする必要があります。プッシュコンポーザーの**サウンド**フィールドで、アプリ内のサウンドファイルの場所を示すプロトコルURLを指定する必要があります。このフィールドに「default」を指定すると、デバイスのデフォルトの通知音が再生されます。これは、[messaging API]({{site.baseurl}}/api/endpoints/messaging)、または以下のスクリーンショットに示すようにプッシュコンポーザーの**設定**にあるダッシュボードを使用して指定できます。

![サウンドはアプリ内でローカルにホストする必要があります。プッシュコンポーザーのサウンドフィールドで、アプリ内のサウンドファイルの場所を示すプロトコル URL を指定する必要があります。このフィールドに「default」を指定すると、デバイスのデフォルトの通知音が再生されます。messaging API またはプッシュコンポーザーの設定にあるダッシュボードを使用して指定できます。]({% image_buster /assets/img_archive/sound_push_ios.png %})

指定したサウンドファイルが存在しない場合、またはキーワード「default」を入力した場合、Brazeはデバイスのデフォルトのアラートサウンドを使用します。ダッシュボードとは別に、[messaging API]({{site.baseurl}}/api/endpoints/messaging)でサウンドを設定することもできます。詳細については、[カスタムアラートサウンドの準備](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html)に関する Apple 開発者ドキュメントを参照してください。