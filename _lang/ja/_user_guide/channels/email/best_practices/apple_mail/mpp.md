---
nav_title: Apple Mail のプライバシー保護
article_title: iOS 15のApple Mailプライバシー保護
page_order: 1
description: "この参照記事では、Apple Mailのプライバシー保護のプライバシーアップデート、影響を受けるユーザー、およびこの機能に備えるための次のステップについて説明します。"
channel:
  - email

---

# Appleのメールプライバシー保護 {#apples-mail-privacy-protection}

> この記事では、Appleのメールプライバシー保護（MPP）の概要、影響を受けるユーザー、およびメール配信可能性指標への影響に備える方法について説明します。

## Appleのメールプライバシー保護の更新とは？ {#what-is-apples-mail-privacy-protection-update}

Appleのメールプライバシー保護（MPP）は、2021年9月中旬にリリースされたiOS 15、iPadOS 15、macOS Monterey、およびwatchOS 8のApple Mailアプリのユーザー向けに利用可能なプライバシー更新です。MPPにオプトインするユーザー（ほとんどのユーザーがそうすると予測されます）の場合、メールはプロキシサーバーを使用してプリロードされ、画像がキャッシュされ、[開封トラッキング]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences#changing-location-of-tracking-pixel)などの指標のためのトラッキングピクセルを利用する機能が制限されます。

ブランドとしては、MPPによって、メール配信可能性指標に関する問題や、これらの指標に基づいてトリガーされる既存のCampaignやCanvasesに関する問題が発生することが予想されます。メール配信可能性への影響を理解するには、[メールレポート]({{site.baseurl}}/user_guide/channels/email/reporting)を参照してください。

### 影響を受けるユーザー {#who-will-this-affect}

以下のデバイスでネイティブのApple Mailアプリを使用しているすべての受信者が対象です。

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

これは、メールアカウントをApple Mailアプリに接続し、セキュリティ機能にオプトインしたすべてのユーザーに適用されます。メールサービス（Gmail、Outlook、Yahoo、AOLなど）に関係なく影響を受けます。この影響は、Apple/iCloud/me.comのメールアドレスでメールを受信するサブスクライバーに限定されるものではありません。

{% alert important %}
メール配信可能性に対するこれらの更新は重要ですが、MPPはメールと配信を管理するルールを根本的に変えるものではありません。むしろ、MPPは成功のベンチマーク方法や、今後使用できるメールツールと機能に影響を与えます。
{% endalert %}

## MPPへの準備方法 {#how-to-prepare-for-mpp}

MPPへの対応方法とメールマーケティングおよび全体的なカスタマーエンゲージメントへの潜在的な影響について検討を始めたばかりのブランドにとって、時間は非常に重要です。以下の対応をお勧めします。

- MPPがマーケティング活動にもたらすリスクを評価する
- Brazeプラットフォームでのオートメーション調整に対応し、配信可能性のベストプラクティスを強化し、パフォーマンスを測定するためのより幅広い指標を開発するための、ターゲットを絞ったMPP対応計画を策定する
- できるだけ早くその対応計画を実施する

Appleのメールプライバシー保護に備える方法の詳細な概要については、[ブログ記事](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare)をご覧ください。