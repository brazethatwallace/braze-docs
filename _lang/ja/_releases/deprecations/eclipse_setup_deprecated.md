---
nav_title: EclipseでのSDK初期セットアップ
page_order: 1
page_type: update
noindex: true
description: "このアーカイブ記事では、EclipseでSDKの初期セットアップを行う方法について説明しています。BrazeはEclipse IDEのサポートを廃止しました。"
---

# EclipseでのSDK初期セットアップ {#initial-sdk-setup-with-eclipse}

{% alert update %}
Googleが[Eclipse Android Developer Toolsプラグインのサポートを終了](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)したため、BrazeはEclipse IDEのサポートを中止しました。移行前にEclipseの統合に関するサポートが必要な場合は、[サポートにメールで]({{site.baseurl}}/support_contact/)お問い合わせください。
{% endalert %}

## ステップ 1 {#step-1}
コマンドラインで、[Braze Android GitHubリポジトリ](https://github.com/braze-inc/braze-android-sdk)をクローンします。

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## ステップ 2 {#step-2}
Brazeプロジェクトをローカルのワークスペースにインポートします。

Eclipseの場合:

  - **File** > **Import** に移動します。

    ![File Import]({{site.baseurl}}/assets/img_archive/file_import.png)
  - **Android** > **Existing Android Code into Workspace** を選択します。

    ![Android Import]({{site.baseurl}}/assets/img_archive/android_import.png)
  - **Browse** をクリックします。

    ![Browse]({{site.baseurl}}/assets/img_archive/click_browse.png)
  - Braze UIプロジェクトフォルダーにチェックを入れ、「copy project into workspace」を選択して、**Finish** をクリックします。

    ![Select Android UI Project]({{site.baseurl}}/assets/img_archive/select_project_android.png)

## ステップ 3 {#step-3}
自分のプロジェクトでBrazeを参照します。
Eclipseの場合:

  - プロジェクトを右クリックし、**Properties** を選択します。

    ![Click Properties]({{site.baseurl}}/assets/img_archive/click_properties.png)
  - **Android** で、ライブラリーセクションの **Add...** をクリックし、android-sdk-uiをライブラリーとしてアプリに追加します。

    ![Braze Add]({{site.baseurl}}/assets/img_archive/add_appboy_ui.png)

## ステップ 4 {#step-4}
依存関係エラーを解決し、ビルドターゲットを修正します。

この時点で、Brazeのコードにエラーが表示される場合があります。これは依存関係が設定されておらず、ビルドターゲットが正しくない可能性があるためです。

   - Braze UIプロジェクトを右クリックし、**Properties** > **Android** を選択して、ビルドターゲットがBrazeの最新ビルドツールバージョンに設定されていることを確認します。

      ![Build Target]({{site.baseurl}}/assets/img_archive/build_target.png)
   - Braze UIプロジェクトを右クリックし、**Properties** > **Java Build Path** > **Add JARs…** を選択して、メインアプリケーションから「android-support-v4.jar」をライブラリーとして追加します。

      ![Support]({{site.baseurl}}/assets/img_archive/android_support_v4.png)

## ステップ 5 {#step-5}

最終的な要素を追加します。

  - SDKバージョン1.10.0以降の場合は、
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  をAndroidManifest.xmlに追加する必要があります。Eclipseではマニフェストマージがサポートされていないためです。

  - SDKバージョン1.7.0以降では、「assets/fontawesome-webfont.ttf」をライブラリープロジェクトからアプリケーションにコピーする必要があります。Eclipseでは、ライブラリーのアセットフォルダーは自動的には含まれません。