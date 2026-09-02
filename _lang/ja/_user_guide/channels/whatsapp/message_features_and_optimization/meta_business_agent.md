---
nav_title: Meta Business Agent
article_title: Meta Business AgentとBraze WhatsApp
page_order: 8
description: "このガイドでは、Meta Business AgentがBrazeに接続されたWhatsApp Businessの電話番号とどのように連携するか、また有効にした場合に何が起こるかについて説明します。"
page_type: reference
channel:
  - WhatsApp
alias: /meta_business_agent/
hidden: true
noindex: true
---

# Meta Business AgentとBraze WhatsApp {#meta-business-agent-and-braze-whatsapp}

> Meta Business Agentは、Brazeにも接続されているWhatsApp Businessの電話番号で受信メッセージに返信できます。この記事では、2つのシステムがメッセージの可視性をどのように共有するか、Metaのツールでエージェントを有効にする方法、および課金の仕組みについて説明します。この内容は、2026年8月時点のMeta Business Agentの製品機能とドキュメントに基づいています。

Metaは引き続きMeta Business Agentを積極的に開発しているため、一部の詳細が変更される可能性があります。最新情報については、[MetaのBusiness Agentドキュメント](https://developers.facebook.com/documentation/meta-business-agent/overview)を参照してください。

## Meta Business Agentとは {#what-is-meta-business-agent}

Meta Business Agentは、MetaがWhatsApp Businessの電話番号上で直接運用するAI搭載の応答システムです。対象の電話番号で有効にすると、Metaのツールで設定されたナレッジ（ビジネス情報、FAQ、ファイル、Webサイトのコンテンツ）やコネクターを使用して、ビジネスに代わってユーザーからの受信メッセージに返信できます。

Meta Business Agentの有効化は、WhatsApp マネージャーとMeta Business Suiteで完全に設定され、Brazeのワークスペースとは別のものです。設定にBrazeは必要なく、現在Brazeダッシュボードにはこの機能を制御する設定はありません。

## Brazeに接続された電話番号との連携 {#how-it-interacts-with-your-braze-connected-number}

Meta Business AgentとBrazeは同じWhatsApp Businessの電話番号上で共存できますが、現時点ではすべてのメッセージの可視性を共有しているわけではありません。

- **Brazeから送信されるアウトバウンドメッセージには影響しません。** Meta Business Agentが有効かどうかにかかわらず、Brazeはキャンペーンやキャンバスを通じてWhatsAppテンプレートメッセージや応答メッセージを従来どおり送信し続けます。
- **受信メッセージはMeta Business Agentによってルーティングされます。** ユーザーからの受信メッセージごとに、Meta Business AgentがBrazeに渡すか、自身で処理するかを判断します。
  - **MetaがメッセージをBrazeにルーティングした場合：** 現在のWhatsApp受信メッセージと同じ方法で処理されます。既存のキャンペーンやキャンバスのアクションベースのトリガーやアクションパスは、すでに構築されたロジックに従って動作します。
  - **Meta Business Agentがメッセージを自身で処理した場合：** Brazeは現在、そのアクティビティを伝える別のチャネル（スタンバイメッセージやメッセージエコー）を処理していません。エージェントが処理すると判断した受信メッセージと、それらのメッセージに対するエージェント自身の返信は、現在Brazeのどの画面にも表示されません。

| メッセージフロー | 現在の動作 |
| --- | --- |
| キャンペーンやキャンバスステップを通じて送信されるWhatsAppテンプレートメッセージと応答メッセージ | 影響なし。Brazeは設定どおりに送信を継続します |
| MetaがBrazeにルーティングした受信メッセージ | 通常どおり処理され、既存のトリガーとアクションパスが適用されます |
| Meta Business Agentが自身で処理した受信メッセージ | 現在Brazeには表示されません。受信メッセージ用の既存のトリガーとアクションパスは動作しません |
| Meta Business Agentが送信したアウトバウンドメッセージ | 現在Brazeには表示されません |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メッセージフロー" }

## Meta Business Agentを有効にする {#enable-meta-business-agent}

Meta Business Agentは、BrazeではなくMetaのツールで電話番号ごとに有効にします。

1. [WhatsApp マネージャー](https://business.facebook.com/wa/manage/home/)で対象の電話番号の適格性を確認し、Meta Business Agent利用規約に同意して有効にします。
2. Metaの[エージェント設定API](https://developers.facebook.com/documentation/meta-business-agent/reference/configure/agent-skills)を通じて、エージェントのナレッジとスキル（ビジネス情報、FAQ、ファイル、コネクター）を設定します。
3. [Agent Settings](https://developers.facebook.com/documentation/meta-business-agent/reference/onboard/agent-settings)を使用してエージェントをオンにします。

## 有効にする前に検討すべきこと {#things-to-weigh-before-enabling-it}

- **Braze側のトグルはありません：** Meta Business Agentの有効化、設定、無効化はすべてMetaのツールで行います。Brazeでオンまたはオフにする機能はありません。
- **課金：** Meta Business Agentの導入に伴い、テンプレート以外のメッセージは、サービス（既存カテゴリー）またはMeta Business Agent（新カテゴリー）の2つのカテゴリーのいずれかに分類されるようになりました。
  - Brazeが処理するテンプレート以外の応答は、2026年10月1日からサービスメッセージとして課金されます。
    - 受信メッセージにマーケティング、ユーティリティ、または認証テンプレートで応答した場合は、そのテンプレートの種類に応じて課金されます。
  - Meta Business Agentのメッセージは、2026年8月1日からMetaによって直接課金されます。詳細についてはMetaの料金体系を参照してください。
  - メッセージは1つのカテゴリーにのみ分類されるため、同じメッセージに対して二重に課金されることはありません。