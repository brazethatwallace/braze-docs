---
page_order: 10
nav_title: バージョン管理
article_title: Braze SDKのバージョン管理について
description: "Braze SDKのバージョン管理について説明します。"
---

# バージョン管理について {#about-version-management}

> Braze SDKのバージョン管理について説明します。これにより、アプリは最新の機能と品質の向上を維持できます。古いバージョンのSDKは最新のパッチ、バグフィックス、サポートを受け取らない場合があるため、継続的な開発ライフサイクルの一環として常に最新の状態に保つことをお勧めします。

## バージョン管理の推奨事項 {#versioning-recommendations}

すべてのBraze SDKは[Semantic Versioning Specification (SemVer)](https://semver.org/)に準拠しているため、バージョン番号`MAJOR.MINOR.PATCH`に基づき、以下を推奨します。

| バージョン | このバージョンについて | 推奨事項 |
|-------|------------------|--------------|
| `PATCH` | 更新は常に非破壊的であり、重要なバグ修正を含みます。常に安全です。 | 現在のメジャーバージョンとマイナーバージョンの最新パッチバージョンにすぐに更新してください。 |
| `MINOR` | 更新は常に非破壊的であり、新しい機能が含まれます。アプリケーションコードの変更は不要です。 | すぐに行う必要はありませんが、できるだけ早く現在のメジャーバージョンの最新マイナーバージョンに更新してください。 |
| `MAJOR` | 更新は破壊的変更であり、アプリケーションコードの変更が必要になる場合があります。 | コードの変更が必要な場合があるため、チームに最適なタイミングで最新のメジャーバージョンに更新してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="バージョン管理の推奨事項" }

{% alert note %}
新しいAndroidまたはApple OSの更新により、Braze SDKの変更が必要になる場合があります。アプリを新しいデバイスと互換性のある状態に保つために、SDKを最新の状態に維持することが重要です。
{% endalert %}

## 新しいリリースの通知を受け取る {#getting-notified-of-new-releases}

新しいSDKバージョンがリリースされたときに自動通知を受け取るには、任意のBraze SDKのGitHubリポジトリをウォッチできます。

1. SDKのGitHubリポジトリに移動します（例：[braze-android-sdk](https://github.com/braze-inc/braze-android-sdk)、[braze-swift-sdk](https://github.com/braze-inc/braze-swift-sdk)、[braze-web-sdk](https://github.com/braze-inc/braze-web-sdk)）。
2. 右上の**Watch**をクリックします。
3. **Custom**をクリックし、**Releases**を選択して、**Apply**をクリックします。

新しいリリースが公開されるたびに、GitHub通知（および[通知設定](https://github.com/settings/notifications)に応じてメール）を受け取ります。SDKリポジトリの完全なリストについては、[参照、リポジトリ、サンプルアプリ]({{site.baseurl}}/developer_guide/references)をご覧ください。

## 既知の問題について {#about-known-issues}

変更によってビルドパイプラインが中断されないようにするため、特定のリリースに既知の問題がある場合でも、**ディストリビューションシステムに公開された後にリリースを変更または削除することはありません**&#8212;。

このような場合は、[Braze SDK変更ログ]({{site.baseurl}}/developer_guide/changelogs)に問題を記録し、影響を受けるメジャーバージョンまたはマイナーバージョンの新しいパッチをできるだけ早くリリースします。