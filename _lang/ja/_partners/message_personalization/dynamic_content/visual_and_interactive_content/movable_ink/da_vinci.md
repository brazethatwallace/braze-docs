---
title: "Movable Ink Da Vinci"
article_title: Movable Ink Da Vinci
alias: "/partners/movable_ink_da_vinci/"
description: "BrazeとMovable Ink Da Vinciの統合により、ブランドはDa VinciのAIドリブン型コンテンツ決定エンジンを活用して、高度にパーソナライズされたメッセージングを配信できます。Da Vinciはユーザーごとに最も関連性の高いコンテンツをキュレートし、Brazeを通じてメッセージをシームレスに展開します。"
page_type: partner
search_tag: Partner

---

# Movable Ink Da Vinci

> BrazeとMovable Ink [Da Vinci](https://movableink.com/da-vinci)の統合により、ブランドはDa VinciのAIドリブン型コンテンツ決定エンジンを活用して、高度にパーソナライズされたメッセージングを配信できます。Da Vinciはユーザーごとに最も関連性の高いコンテンツをキュレートし、Brazeを通じてメッセージをシームレスに展開します。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|------------|-------------|
| Movable Ink Da Vinci | このパートナーシップを利用するには、Movable Ink Da Vinciのアカウントが必要です。 |
| Braze Currents - メッセージエンゲージメントイベント | メッセージエンゲージメントイベントデータをMovable Inkに送信するには、Brazeカスタム Currentsエクスポートが必要です。 |
| Braze REST APIキー | `messages.send`、`sends.id.create`、`campaigns.details`の権限が付与されたBraze REST APIキーが必要です。これは、Brazeダッシュボードの**設定** > **API キー**で作成できます。<br><br>詳細な設定方法については、Movable Inkのアカウントチームに直接お問い合わせください。[統合](#integration)セクションを参照してください。|
| BrazeのDa Vinciアプリインスタンス | Brazeで Da Vinci専用のアプリインスタンスを作成します。新しいアプリは、Brazeダッシュボードの**設定** > **アプリ設定** > **アプリを追加**で作成できます。アプリ名を「**Movable Ink - Da Vinci**」とし、任意のプラットフォームを選択します（プラットフォームの選択は必須ですが、タイプは機能に影響しません）。[新しいアプリを追加する方法]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/#step-3-add-your-app-instances)について詳しくはこちらをご覧ください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

統合を開始するには、Movable Inkのアカウントチームにお問い合わせください。Movable Inkからアクセスと設定に関する手順が適宜提供されます。Da VinciがBrazeのMessaging APIを通じてメールデプロイメントを送信できるようにするには、Braze API認証情報のセットをMovable Inkに提供する必要があります。

接続後、Movable Inkは以下を実行します。

- クライアントおよびBrazeと協力して、ブランドのDa VinciアカウントをBrazeでの展開に向けて設定します。
- メッセージングのユースケースに合わせて、ブランド固有の設定をキャプチャします。
- 包括的なテストと品質保証を実施し、メールが意図したとおりに配信され、パフォーマンスと運用のすべての基準を満たしていることを検証します。