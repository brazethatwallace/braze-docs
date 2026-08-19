---
nav_title: Unity SDK
article_title: Unity SDKリポジトリガイド
page_order: 9
description: "GitHubからミラーリングされたBraze Unity SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
# Unity SDKリポジトリガイド {#unity-sdk-repository-guide}

## Braze Unity SDKについて {#about-the-braze-unity-sdk}

Braze Unity SDKは、Brazeのメッセージング、分析、およびユーザーエンゲージメント機能をアプリに統合するのに役立ちます。

開始するには、以下のリソースを参照してください。

- [Brazeユーザーガイド](https://www.braze.com/docs/user_guide/introduction/)
- [Braze開発者ガイド](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=unity)

## プラグインの設定 {#plugin-setup}

UnityスクリプトでBrazeを使用する前に、プラグインファイルをUnityプロジェクトにインポートする必要があります。

**推奨：** AndroidおよびiOSプラグインは、[SDKリリースページ][1]からダウンロード可能なUnityパッケージとしてバンドルされています。

**手動プラグイン設定：** または、プラグインをUnityプロジェクトに手動でコピーすることもできます。
  1. まず、このリポジトリをクローンします。
  2. 他のプラグインを使用していない場合は、このリポジトリの`Plugins`ディレクトリをUnityプロジェクトの`Assets`フォルダにコピーするだけです。
  3. すでに`/<your-project>/Assets/Plugins`ディレクトリがある場合（おそらく別のプラグインを使用しているため）、`Plugins/Appboy/AppboyBinding.cs`を`/<your-project>/Assets/Plugins`にコピーします。次に、このリポジトリの`Plugins/iOS`と`Plugins/Android`の内容を、それぞれ`/<your-project>/Assets/Plugins/iOS`と`/<your-project>/Assets/Plugins/Android`にコピーします。

## 統合の設定 {#integration-setup}

BrazeをUnityアプリケーションに統合するには、[Unity Braze SDKを統合する][2]の手順を完了してください。

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=unity

## お問い合わせ {#contact}

ご質問がある場合は、Brazeテクニカルサポートにお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk)を参照してください。