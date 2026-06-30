---
nav_title: Unity SDK
article_title: Unity SDKリポジトリガイド
page_order: 9
description: "GitHubからミラーリングされたBraze Unity SDK READMEリファレンスです。"
---

<!-- BEGIN GENERATED README CONTENT -->
## Braze Unity SDKについて {#about-the-braze-unity-sdk}

Braze Unity SDKは、Brazeのメッセージング、分析、およびユーザーエンゲージメント機能をアプリケーションに統合するのに役立ちます。

開始するには、以下のリソースを参照してください。

- [Brazeユーザーガイド]({{site.baseurl}}/user_guide/introduction)
- [Braze開発者ガイド]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity)

## プラグインのセットアップ {#plugin-setup}

UnityスクリプトでBrazeの使用を開始する前に、プラグインファイルをUnityプロジェクトにインポートする必要があります。

**推奨:** AndroidおよびiOSプラグインは、[SDKリリースページ][1]からダウンロード可能なUnityパッケージとしてバンドルされています。

**手動プラグインセットアップ:** または、プラグインをUnityプロジェクトに手動でコピーすることもできます。
  1. まず、このリポジトリをクローンします。
  2. 他のプラグインを使用していない場合は、このリポジトリの`Plugins`ディレクトリをUnityプロジェクトの`Assets`フォルダにコピーするだけです。
  3. すでに`/<your-project>/Assets/Plugins`ディレクトリがある場合（おそらく別のプラグインを使用しているため）、`Plugins/Appboy/AppboyBinding.cs`を`/<your-project>/Assets/Plugins`にコピーします。次に、このリポジトリの`Plugins/iOS`と`Plugins/Android`の内容をそれぞれ`/<your-project>/Assets/Plugins/iOS`と`/<your-project>/Assets/Plugins/Android`にコピーします。

## 統合のセットアップ {#integration-setup}

BrazeをUnityアプリケーションに統合するには、[Braze Unity SDKの統合][2]の手順を完了してください。

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: {{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity

## お問い合わせ {#contact}

ご質問がある場合は、[support@braze.com](mailto:support@braze.com)までお問い合わせください。
<!-- END GENERATED README CONTENT -->

リポジトリの詳細とサンプルプロジェクトについては、[https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk)を参照してください。