---
nav_title: はじめに
article_title: Braze Pilotを始める
page_order: 2
page_type: reference
description: "このリファレンス記事では、エンジニアや開発者に必要な統合ステップを簡単に説明します。"
---

# Braze Pilotを始める {#get-started-with-braze-pilot}

> この記事では、Braze Pilotの使用を開始する方法について説明します。ここでは、アプリのダウンロード方法、Brazeダッシュボードとの接続の初期化、そしてセットアップの完了までの手順をご案内します。

## ステップ1: Braze Pilotをダウンロードする {#step-1-download-braze-pilot}

Braze Pilotを使い始めるには、まずApple App StoreまたはGoogle Play Storeからアプリをダウンロードする必要があります。アプリストアでアプリを検索するか、以下のセクションのQRコードをスキャンして、お使いのデバイス用のアプリページにアクセスできます。

## ステップ2: 利用規約に同意する {#step-2-accept-the-terms-and-conditions}

次に、利用規約に同意し、フォームに職場のメールアドレスを入力します。メールアドレスはアプリの利用状況分析にのみ使用され、マーケティング目的には一切使用されません。

![Braze Pilotのウェルカムページ。]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![仕事用のメールアドレスを入力するオプション。]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## ステップ3: Braze SDKとの接続を初期化する {#step-3-initialize-the-connection-with-the-braze-sdk}

Braze Pilotでは、任意のBrazeダッシュボードに対してBraze SDKを初期化できます。SDKが初期化されると、PilotはエンゲージメントデータをBrazeに送信し始め、そのBrazeダッシュボードから起動されたあらゆるメッセージングをトリガーできるようになります。

PilotでSDK接続を設定するには、デモ用QRコードとセットアップウィザードの2つの方法があります。

{% tabs local %}
{% tab デモQRコード %}

### 方法1: デモQRコード {#method-1-demo-qr-codes}

SDKの初期化に必要なすべての詳細情報を含むQRコードをスキャンします。これにより、ユーザープロファイルが作成され、Braze Pilot内の特定のアプリシミュレーションにディープリンクされます。デモ用QRコードは、無料トライアルの特定のデモキャンペーンのコンパニオンドロワーに表示されます。

| Android用Pilot | iOS用Pilot |
| --- | --- |
| ![Android用QRコード。]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![iOS用QRコード。]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="方法1: デモQRコード" }

{% endtab %}
{% tab セットアップウィザード %}

### 方法2: セットアップウィザード {#method-2-setup-wizard}

Brazeダッシュボードの**アプリ設定**ページから、ダッシュボードワークスペースとの接続を初期化するためのステップバイステップガイドに従います。

![Braze Pilotセットアップウィザードのステップ1。]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

この接続はワークスペース固有です。つまり、デモワークスペースから接続を初期化した後、無料トライアルダッシュボードでライブワークスペースに切り替えた場合、そのワークスペースで起動されたキャンペーンを受信するには、そのワークスペースからSDKを再初期化する必要があります。

![Brazeダッシュボードのワークスペースドロップダウンで、「Demo - Braze」がアクティブなワークスペースとして選択されている状態。]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## ステップ4: プッシュ権限を許可する {#step-4-allow-push-permissions}

最後に、アプリを通じてプッシュ通知機能をテストしたい場合は、アプリにプッシュ通知の送信権限を許可することをお勧めします。アプリにこれらの権限を付与するには、デバイスの設定でアプリの設定を更新する方法と、Brazeからアプリにプッシュプライマーメッセージを送信する方法があります。

{% tabs local %}
{% tab アプリの設定を更新する %}

デバイスの設定を開き、Braze Pilotを見つけます。次に、設定を更新して通知がロック画面に表示されるようにします。

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab プッシュプライマーメッセージを送信する %}

Brazeのアプリ内メッセージを使用して、アプリのプッシュ通知権限をリクエストできます。これは自社の消費者向けに行う場合と同じです。このタイプのメッセージをBrazeで作成する方法については、[プッシュプライマーアプリ内メッセージ]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages)を参照してください。

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## ステップ5: PilotでBrazeメッセージングを体験する {#step-5-experience-braze-messaging-in-pilot}

これで、Braze Pilotのユーザーとして、Brazeダッシュボードからキャンペーンやキャンバスを受け取る準備が整いました！デモワークスペースで公開済みのキャンペーンにアクセスして、Brazeのユースケースを簡単に確認してから、ライブワークスペースに移動して自身のメッセージ配信を開始しましょう。

Brazeでのキャンペーンとキャンバスの設定方法の詳細については、[はじめに: キャンペーンとキャンバス]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases)を参照してください。