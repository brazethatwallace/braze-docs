---
page_order: 0
nav_title: ホーム
article_title: テクノロジーパートナー
alias: /partners/partners/
layout: dev_guide
search_tag: Partner
description: "Brazeのテクノロジーパートナー（Alloys）をカテゴリ別にご覧いただけます。パーソナライゼーション、オーケストレーション、データ、eコマース、Audience Syncなどの連携ドキュメントをご確認ください。"

guide_top_header: "テクノロジーパートナー"
guide_top_text: "Braze Alloysテクノロジーパートナーのドキュメントへようこそ。パートナーカテゴリを参照して、技術連携ガイドをご確認ください。<br><br>Brazeのすべてのテクノロジーパートナーの検索・フィルター可能な一覧については、<a href='https://marketplace.braze.com/t/type/technology-partner'>Braze Marketplace</a> をご覧ください。Brazeを活用して顧客体験を革新するコミュニティへの参加をご検討の場合は、<a href='https://brazefirebrands.splashthat.com/'>Customer Champions Program</a> をご覧ください。"

guide_featured_title: "パートナーカテゴリ"
guide_featured_list:
  - name: メッセージのパーソナライゼーション
    link: /docs/partners/message_personalization
    image: /assets/img/braze_icons/magic-wand-02.svg
  - name: メッセージのオーケストレーション
    link: /docs/partners/message_orchestration
    image: /assets/img/braze_icons/send-01.svg
  - name: データと分析
    link: /docs/partners/data_and_analytics
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: キャンバス Audience Sync
    link: /docs/partners/canvas_audience_sync
    image: /assets/img/braze_icons/refresh-ccw-02.svg
  - name: eコマース
    link: /docs/partners/ecommerce
    image: /assets/img/braze_icons/shopping-cart-03.svg
  - name: 追加チャネルと拡張機能
    link: /docs/partners/additional_channels_and_extensions
    image: /assets/img/braze_icons/puzzle-piece-01.svg
  - name: AIモデルプロバイダー
    link: /docs/partners/ai_model_providers
    image: /assets/img/braze_icons/stars-01.svg
---

## パートナー接続のトラブルシューティング {#troubleshooting-partner-connections}

連携にBraze側での設定が必要な場合は、Brazeダッシュボードにログインし、**パートナー連携** > **テクノロジーパートナー**に移動してください。

{% alert note %}
完全にパートナー側で管理されている連携は、ここに表示されない場合があります。連携の所有者と設定手順を確認するには、パートナー固有のドキュメントを参照してください。
{% endalert %}

Brazeでパートナーに対して**認証情報が無効です**と表示されているが、そのパートナーのダッシュボードでは連携が正しく設定されているように見える場合は、テクノロジーパートナーページで連携を切断してから再接続し、パートナー側でAPIキー、OAuthトークン、権限を確認してください。

一部の外部ダッシュボード（到達性や受信トレイ監視ツールなど）では、Brazeのテクノロジーパートナーページとは異なる接続状態や検証ステータスが表示されることがあります。同期や送信にBrazeが依存する接続状態については、Braze内のパートナータイルをご確認ください。