---
page_order: 2.1
nav_title: ChatGPTアプリ
article_title: BrazeをChatGPTアプリと統合する
description: "BrazeをChatGPTアプリと統合し、AI搭載アプリケーション内で分析とイベントロギングを有効にする方法を説明します。"
platform:
  - ChatGPT Apps
---

# BrazeをChatGPTアプリと統合する {#integrate-braze-with-chatgpt-apps}

> このガイドでは、BrazeをChatGPTアプリと統合し、AI搭載アプリケーション内で分析とイベントロギングを有効にする方法を説明します。

![ChatGPTアプリに統合されたコンテンツカード。]({% image_buster /assets/img/chatgpt_app_integration.png %}){: style="float:right;max-width:30%;border:none;" }

## 概要 {#overview}

ChatGPTアプリは、AI対話型アプリケーションを構築するための強力なプラットフォームを提供します。BrazeをChatGPTアプリと統合することで、AI時代においてもファーストパーティデータのコントロールを維持し続けることができます。具体的には以下のことが可能です。

- ChatGPTアプリ内でのユーザーエンゲージメントと動作をトラッキングする（例：顧客がどの質問やチャット機能を利用しているかを特定する）
- AIインタラクションパターンに基づいてBraze キャンペーンをセグメント化し、リターゲティングする（例：週に3回以上チャットを利用したユーザーにメールを送信する）

### 主な利点 {#key-benefits}

- **カスタマージャーニーを自分のものに：** ユーザーがChatGPTを通じてブランドとやり取りする間も、その動作、好み、エンゲージメントパターンを把握し続けることができます。このデータはAIプラットフォームの分析だけでなく、Brazeユーザープロファイルに直接流れ込みます。
- **クロスプラットフォームリターゲティング：** ChatGPTアプリでのユーザーインタラクションをトラッキングし、AI利用パターンに基づいたパーソナライズ済みキャンペーンで、自社チャネル（メール、SMS、プッシュ通知、アプリ内メッセージ）全体でリターゲティングできます。
- **ChatGPTの会話に1:1のプロモーションコンテンツを返す：** チームがアプリ用に構築したカスタム対話型UIコンポーネントを使って、ChatGPT体験内で直接Brazeの[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages)、[Content Cards]({{site.baseurl}}/user_guide/channels/content_cards)などを配信できます。
- **収益アトリビューション：** ChatGPTアプリのインタラクションから発生した購入とコンバージョンをトラッキングできます。

<!-- ### Practical Use Cases

- **E-commerce**: Track product inquiries, cart additions, and purchases made through ChatGPT conversations
- **SaaS**: Monitor feature requests, support interactions, and trial-to-paid conversions
- **Content/Media**: Understand what topics users are most interested in and create targeted content campaigns
- **Financial Services**: Track financial advice requests and product recommendations for compliance and optimization
- **Travel**: Monitor destination research, booking inquiries, and trip planning interactions

By integrating Braze with your ChatGPT App, you ensure that every AI interaction becomes a data point in your customer engagement strategy, not just a black box interaction on someone else's platform. -->

## 前提条件 {#prerequisites}

BrazeをChatGPTアプリと統合する前に、以下が必要です。

- Brazeワークスペースに新規のWebアプリとAPIキーが作成されていること
- OpenAIプラットフォームで作成された[ChatGPTアプリ](https://openai.com/index/introducing-apps-in-chatgpt/)（[OpenAIサンプルアプリ](https://github.com/openai/openai-apps-sdk-examples)）

{% multi_lang_include developer_guide/chatgpt_apps/sdk_integration.md %}