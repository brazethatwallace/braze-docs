---
nav_title: Apple Mail プライバシー保護
article_title: iOS 15 向け Apple Mail プライバシー保護
page_order: 1
description: "この参照記事では、Apple Mail プライバシー保護のプライバシーアップデート、影響を受けるユーザー、およびこの機能に備えるための次のステップについて説明します。"
channel:
  - email

---

# Apple の Mail プライバシー保護

> この記事では、Apple の Mail プライバシー保護 (MPP) の概要、影響を受けるユーザー、およびメール配信指標への影響に備える方法について説明します。

## Apple の Mail プライバシー保護アップデートとは？

Apple の Mail プライバシー保護 (MPP) は、2021年9月中旬にリリースされた iOS 15、iPadOS 15、macOS Monterey、watchOS 8 の Apple Mail アプリユーザーが利用できるプライバシーアップデートです。MPP にオプトインしたユーザー（ほとんどのユーザーがオプトインすると予測されます）のメールは、プロキシサーバーを使用してプリロードされ、画像がキャッシュされるため、[開封トラッキング]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences/#changing-location-of-tracking-pixel)などの指標にトラッキングピクセルを活用する機能が制限されます。

ブランドは、MPP によりメール配信指標に関する問題や、これらの指標に基づいてトリガーされる既存のキャンペーンやキャンバスに問題が生じることを想定する必要があります。メール配信への影響を理解するには、[メールレポート]({{site.baseurl}}/user_guide/channels/email/reporting/)を参照してください。

### 影響を受けるユーザー

以下のデバイスでネイティブの Apple Mail アプリを使用しているすべての受信者が対象です。

- iOS 15
- iPadOS 15
- macOS Monterey
- watchOS 8

これは、メールアカウントを Apple Mail アプリに接続し、セキュリティ機能にオプトインしたすべてのユーザーに適用されます。メールサービス（Gmail、Outlook、Yahoo、AOL など）に関係なく影響を受けます。この影響は、Apple/iCloud/me.com のメールアドレスでメールを受信するサブスクライバーに限定されるものではありません。

{% alert important %}
メール配信に対するこれらのアップデートは重要ですが、MPP はメールと配信を管理するルールを根本的に変えるものではありません。むしろ、成功のベンチマーク方法や、今後使用できるメールツールと機能に影響を与えます。
{% endalert %}

## MPP にどう備えるか？

MPP への対応とメールマーケティングおよび全体的なカスタマーエンゲージメントへの潜在的な影響について検討を始めたばかりのブランドにとって、時間は非常に重要です。以下の対応をお勧めします。

- MPP がマーケティング活動にもたらすリスクを評価する
- Braze プラットフォームでのオートメーション調整、配信のベストプラクティスの強化、パフォーマンスを測定するためのより幅広い指標の開発に対応する、ターゲットを絞った MPP 対応計画を策定する
- できるだけ早くその対応計画を実施する

Apple の Mail プライバシー保護に備える方法の詳細な概要については、[ブログ記事](https://www.braze.com/resources/articles/apple-mail-privacy-protection-how-to-prepare)をご覧ください。