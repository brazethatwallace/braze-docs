---
nav_title: デバイスメッセージングAPI
article_title: デバイスメッセージングAPI
search_tag: Endpoint
page_order: 2.2
layout: dev_guide
permalink: /api/device_messaging_api
description: "このランディングページでは、BrazeデバイスメッセージングAPIについて紹介します。"
page_type: landing
hidden: true
guide_top_header: "デバイスメッセージングAPI"
guide_top_text: "BrazeデバイスメッセージングAPIを使用すると、Braze SDKを統合せずに、バナープロパティの取得やバナーのインプレッションおよびクリックイベントのレポートが可能です。デバイスメッセージングAPIはクライアントサイドとサーバーサイドの統合をサポートし、単一のワークスペースにスコープされたクライアントサイドのREST APIキーを使用します。"
guide_top_text2: "注: このAPIは指定されたバナーのプロパティのみを取得し、バナーのHTMLは返しません。"
guide_featured_title: "はじめに"
guide_featured_list:
  - name: "デバイスメッセージングAPIの概要"
    link: /docs/api/device_messaging_api/overview
    image: /assets/img/braze_icons/annotation-info.svg
  - name: "認証とセキュリティ"
    link: /docs/api/device_messaging_api/authentication
    image: /assets/img/braze_icons/key-01.svg
  - name: "エラー処理とリトライ"
    link: /docs/api/device_messaging_api/error_handling
    image: /assets/img/braze_icons/alert-circle.svg
  - name: "レート制限"
    link: /docs/api/device_messaging_api/rate_limits
    image: /assets/img/braze_icons/speedometer-01.svg
guide_menu_title: "バナーエンドポイント"
guide_menu_list:
  - name: "POST: ユーザーのバナーを取得する"
    link: /docs/api/device_messaging_api/endpoints/banners/post_sync_banners
    image: /assets/img/braze_icons/download-01.svg
  - name: "POST: バナー分析イベントをトラッキングする"
    link: /docs/api/device_messaging_api/endpoints/banners/post_track_banner_events
    image: /assets/img/braze_icons/line-chart-up-02.svg
---

{% alert important %}
このページはベータ版です。デバイスメッセージングAPIの機能およびドキュメントは変更される可能性があります。
{% endalert %}