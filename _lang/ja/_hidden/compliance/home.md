---
nav_title: コンプライアンスドキュメント
article_title: コンプライアンスドキュメント
page_order: 1
permalink: /compliance_documentation/
toc_headers: h2
noindex: true
---

# コンプライアンスドキュメント {#compliance-documentation}

_改訂日：2026 年 3 月 30 日_

## コンプライアンスドキュメントに含まれる内容 {#what-is-included-in-the-compliance-documentation}

以下のコンプライアンスドキュメントには、購入した製品、チャネル、機能、サービスに適用される具体的な条件が記載されています。

- サードパーティプロバイダーの製品、Webサイト、アプリケーション、またはサービスとの連携、統合、またはアクセスを可能にするBrazeサービスの機能について、コンプライアンスドキュメントには、当該機能の使用に適用されるサードパーティプロバイダーの条件が含まれています。
- Brazeの製品、チャネル、機能、サービスの使用にあたり、Brazeの顧客が遵守すべき一般的な業界慣行および基準が含まれています。

## コンプライアンスドキュメントの更新 {#updates-to-the-compliance-documentation}

Brazeのドキュメント（コンプライアンスドキュメントを含む）の更新通知を、[BrazeのGitHubリポジトリ](https://github.com/braze-inc/release-notes)からサブスクライブして受け取ることができます。

## 特定のチャネル、インテグレーション、機能に関するコンプライアンスドキュメント {#compliance-documentation-for-specific-channels-integrations-and-features}

以下は、該当するコンプライアンスドキュメントが存在する製品、チャネル、機能、サービスの一覧です。複数の製品をご利用の場合、関連するすべてのコンプライアンスドキュメントが適用されます。

### 一般条件 {#general-terms}

契約に基づくお客様の義務を制限することなく、また疑義を避けるために、お客様は、以下に記載されたチャネルおよび機能の使用に関連して、必要なすべての権利、同意、認可の取得、および法的に適切なプライバシー通知の提供について、ならびに使用に必要な法的に要求されるすべての同意および認可の取得について、単独で責任を負うものとします。

## チャネルと機能 {#channels-and-features}

1. [モバイルメッセージチャネル](#mobile-messages-channel)
2. [Webhookチャネル](#webhooks-channel)
3. [WhatsAppチャネルコンプライアンスドキュメント](#hatsapp-channel-compliance-documentation)
4. [LINEチャネルコンプライアンスドキュメント](#line-channel-compliance-documentation)
5. [Shopify連携コンプライアンスドキュメント](#shopify-integration-compliance-documentation)
6. [オーディエンス同期コンプライアンスドキュメント](#audience-sync-compliance-documentation)
7. [メッセージアーカイブとフィールドレベル暗号化コンプライアンスドキュメント](#message-archiving-and-field-level-encryption-compliance-documentation)
8. [エージェントコンソールコンプライアンスドキュメント](#agent-console-compliance-documentation)
9. [KakaoTalkチャネルコンプライアンスドキュメント](#kakaotalk-channel-compliance-documentation)

## 1. モバイルメッセージチャネル {#mobile-messages-channel}

以下の追加条件は、お客様によるモバイルメッセージチャネルの使用に関連して適用されます。

### 定義 {#definitions}

「**アグリゲーター**」、「**キャリア**」、または「**モバイルメッセージ仲介者**」とは、(i) モバイルメッセージプロバイダーとキャリア間でモバイルメッセージを送信するサードパーティの仲介者、(ii) ワイヤレスサービスプロバイダー（例：T-Mobile、AT\&T など）、および/または (iii) モバイルメッセージプロバイダーからエンドユーザーへの RCS メッセージの送信に関与する者を意味します。

**「SMS/MMS プロバイダー」または「モバイルメッセージプロバイダー」**とは、[www.braze.com/subprocessors](http://www.braze.com/subprocessors) で特定される、SMS、MMS、および/または RCS メッセージの送信に使用される Braze の復処理者を意味します。

「**SMS/MMS メッセージ**」または「**モバイルメッセージ**」とは、SMS、MMS、および/または RCS メッセージを意味します。

### 適用される業界基準およびベストプラクティス {#applicable-industry-standards-and-best-practices}

モバイルメッセージを送信する際、お客様は、モバイルメッセージプロバイダーの該当する利用規約およびメッセージングポリシー、該当する業界基準およびガイドライン、ならびに該当する場合は、お客様がモバイルメッセージの送信を意図する国の業界コードおよび該当するモバイルメッセージ仲介者のガイドラインに準拠する必要があります。詳細は Braze の[利用規約](https://www.braze.com/company/legal/aup/)に記載されています。

モバイルメッセージの送信に関与するサードパーティ（モバイルメッセージ仲介者を含む）は、その条件または適用法に違反して送信されたモバイルメッセージに基づいて料金またはペナルティを課す場合があります。お客様は、当該サードパーティの条件に対するお客様の違反に起因する料金およびペナルティについて、当該料金またはペナルティがお客様に課されるか Braze に課されるかにかかわらず、支払い責任を負います。

### 復処理者 {#sub-processors}

Braze は、[www.braze.com/subprocessors](https://www.braze.com/subprocessors/) の復処理者リストに含まれるモバイルメッセージプロバイダーを使用する場合があります。

上記にかかわらず、お客様が「Bring Your Own (BYO) SMS Connector」モデルを使用してモバイルメッセージを送信する場合、送信に関与するモバイルメッセージプロバイダーは Braze の復処理者ではなく、サードパーティプロバイダー（契約で定義）とみなされ、以下の免責事項が当該サードパーティプロバイダーに適用されます。

### Webhook 使用例外条件 {#webhook-use-exception-terms}

2024 年 12 月 9 日以降にアクションクレジットを購入したお客様に適用されます（注文書の発効日に基づく）：Webhook チャネルコンプライアンスドキュメントに記載されている制限は、サードパーティプロバイダーのプラットフォームを通じてモバイルメッセージを送信するためのwebhookの使用には適用されません。

### Bring Your Own (BYO) SMS Connector

お客様は、「BYO SMS Connector」モデルを通じて、サードパーティプロバイダーを使用して Braze からモバイルメッセージを送信できます。ただし、お客様は BYO SMS Connector モデルを使用して米国およびカナダへモバイルメッセージを送信してはなりません。

### 免責事項 {#disclaimers}

Braze は、モバイルメッセージの送信または処理に関与するサードパーティプロバイダーまたはモバイルメッセージ仲介者に関する表明、保証、責任、および補償義務を一切否認します。これには、システム容量、メッセージスループット、またはエンドユーザーのデバイスへの実際の配信に関連する責任が含まれます。

## 2. Webhook チャネル {#webhooks-channel}

以下の追加条件は、お客様による Webhook チャネルの使用に関連して適用されます。

### Webhook チャネル使用条件 {#webhooks-channel-use-terms}

該当するチャネルコンプライアンスドキュメントで別途許可されていない限り、(a) お客様は、Braze が同じ結果を達成するためのネイティブ機能を提供している場合にwebhookを使用してはならず、(b) お客様は、Braze サービスを通じてメッセージを送信するためのネイティブメカニズムを Braze が提供している範囲において、サードパーティプロバイダーのプラットフォームを通じてメッセージの送信をトリガーするためにwebhookを使用してはなりません。

Braze がお客様の現在のサブスクリプション期間中に Braze サービスで新規または更新されたメカニズムを一般提供した場合、お客様は、新しいメカニズムの一般リリース日から 6 か月後、またはお客様のサブスクリプション期間の当年度末のいずれか遅い方の時点から、指定されたサードパーティプラットフォームを通じてメッセージ送信をトリガーするためのwebhookの使用が禁止されます。

### Webhook チャネル使用条件の例外 {#exceptions-to-the-webhook-channel-use-terms}

[モバイルメッセージチャネル](#mobile-messages-channel)および [WhatsApp チャネル](#whatsapp-channel-compliance-documentation)を参照してください。

### 免責事項 {#disclaimer}

Braze は、Braze サービス外でメッセージの送信またはその他のアクションをトリガーするためのお客様によるwebhookの使用に関するすべての責任を否認します。

## 3. WhatsApp チャネルコンプライアンスドキュメント {#whatsapp-channel-compliance-documentation}

以下の追加条件は、お客様によるWhatsAppチャネルの使用に関連して適用されます。

### 適用されるサードパーティプロバイダーの条件 {#applicable-third-party-provider-terms}

お客様は、Brazeの[WhatsAppセットアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)ページに記載されている、WhatsApp, LLCおよびそのグループ関連会社が要求する条件を含む、WhatsAppチャネルに適用される前提条件、条件、およびポリシーに準拠する必要があります。

### Webhook使用例外条件

お客様は、カスタマーサポート目的（人間が支援するチャットのユースケースおよび/またはチャットボットのユースケースなど）でない限り、WhatsAppチャネルを通じてメッセージの送信をトリガーするためにwebhookを使用してはなりません。

### Bring Your Own (BYO) WhatsApp Connector

お客様は、「BYO WhatsApp Connector」を使用して、直接のWhatsAppアカウントをBrazeに接続できます。

## 4. LINE チャネルコンプライアンスドキュメント {#line-channel-compliance-documentation}

以下の追加条件は、お客様による LINE チャネルの使用に関連して適用されます。

### 前提条件 {#pre-requisites}

LINE チャネルを通じてメッセージを送信するには、お客様は LINE 認証済み公式アカウントを取得する必要があります。これは LINE の独自の裁量により承認および付与されます。お客様は、LINE チャネルの使用のために Braze アクションクレジットを購入する前に、LINE から認証済み公式アカウントを取得していることを確認する必要があります。

### 適用されるサードパーティプロバイダーの条件

LINE チャネルを使用することにより、お客様は、LY Corporation およびその関連会社（総称して「LINE」）が要求するすべての条件およびポリシー（LINE 公式アカウント利用規約、Official Account API 利用規約、LINE 公式アカウントガイドライン、LINE ユーザーデータポリシー、およびそれらに参照により組み込まれるすべてのポリシー、条件、ガイドライン、ドキュメントを含みますがこれらに限定されません）（総称して「LINE 条件」）に準拠し、拘束されることに同意します。明確にするために、お客様は以下の責任を負います：(i) LINE に関連して処理されるデータが、該当する LINE 条件に従って処理されることを確保すること、および (ii) LINE チャネルに関連した LINE サービスの使用に対して LINE に支払うべき料金または支払い。

LINE 条件に反する定めがある場合でも、お客様は LINE サービスの使用について主たる責任を負います。

## 5. Shopify 統合コンプライアンスドキュメント {#shopify-integration-compliance-documentation}

以下の追加条件は、Braze サービスに関連したお客様による Shopify 統合の使用（「**Shopify 統合**」）に関連して適用されます。

お客様は、Shopify Inc. またはその関連会社（「**Shopify**」）の Shopify 統合の使用に適用される条件、ポリシー、ガイドライン、およびドキュメントに準拠し、拘束されることに同意します。

お客様は、Shopify がいつでもその独自の裁量により以下を行う場合があることを了承します：(i) Braze に対してお客様の Shopify 統合へのアクセスを無効化またはブロックすることを要求すること、または (ii) お客様の Shopify 統合へのアクセスの提供を停止、一時停止、または終了すること。Braze は、Shopify がお客様または Braze サービス全般を通じて Shopify 統合へのアクセスの提供を停止することに関して一切の責任を負いません。

## 6. Audience Sync コンプライアンスドキュメント {audience-sync-compliance-documentation} {#6-audience-sync-compliance-documentation-audience-sync-compliance-documentation}

以下の追加条件は、お客様による Audience Sync の使用に適用されます。

### 適用されるサードパーティプロバイダーの条件

お客様は、Audience Sync インテグレーションに関連して利用するサードパーティプロバイダーの適用される利用規約、ポリシー、ガイドライン、およびドキュメントを遵守し、それらに拘束されることに同意するものとします。

お客様は、サードパーティプロバイダーが自社サービスに関連して使用されるデータ、広告、またはコンテンツを確認、審査、および/または削除する場合があることを了承するものとします。

## 7. メッセージのアーカイブおよびフィールドレベル暗号化コンプライアンスドキュメント {#message-archiving-and-field-level-encryption-compliance-documentation}

### 免責事項

お客様は、メッセージのアーカイブおよび/またはフィールドレベル暗号化（それぞれ「**本機能**」）の使用が、Braze サービスを通じて送信されるメッセージの送信速度に影響を与える可能性があることを了承します。Braze は、そのような影響について一切の責任を負わず、お客様が本機能を使用している場合、送信速度に関するコミットメントは適用されません。本機能はお客様のコンプライアンスへの取り組みを支援するために使用される場合がありますが、お客様は、Braze が本機能自体の使用がお客様のコンプライアンス義務を満たすかどうかについていかなる表明または保証も行わず、これに関連するすべての責任を否認することを了承します。

## 8. エージェントコンソールコンプライアンスドキュメント {#agent-console-compliance-documentation}

### 復処理者またはサードパーティプロバイダーとしての LLM プロバイダー {#llm-providers-as-sub-processors-or-third-party-providers}

お客様が Braze サービスの Braze Auto オプションを通じて Braze が提供する大規模言語モデルとの統合（「Braze 提供 LLM」）を使用する場合、当該 Braze 提供 LLM のプロバイダーは Braze の復処理者として機能し、お客様と Braze 間のデータ処理補遺（DPA）の条件に従います。

お客様が Braze AI 機能との統合のために独自の API キーを持ち込むことを選択した場合、お客様独自の LLM サブスクリプションのプロバイダーは、お客様と Braze 間の契約で定義されるサードパーティプロバイダーとみなされます。

## 9. KakaoTalk チャネルコンプライアンスドキュメント {#kakaotalk-channel-compliance-documentation}

以下の追加条件は、お客様による KakaoTalk チャネルの使用に関連して適用されます。

### 前提条件

KakaoTalk チャネルを通じてメッセージを送信するには、お客様はまず KakaoTalk アカウントを取得し、お客様への KakaoTalk 機能の提供に関与するサードパーティプロバイダー（「KakaoTalk サードパーティプロバイダー」）と KakaoTalk サービスの契約を締結する必要があります。KakaoTalk アカウントは、当該 KakaoTalk サードパーティプロバイダーの独自の裁量により承認および付与されます。

### 適用されるサードパーティプロバイダーの条件

KakaoTalk チャネルを使用することにより、お客様は、KakaoTalk および KakaoTalk サードパーティプロバイダーの該当する条件およびポリシー（総称して「KakaoTalk 条件」）に準拠し、拘束されることに同意し、KakaoTalk サービスの使用について責任を負います。明確にするために、お客様は、KakaoTalk チャネルに関連した当該 KakaoTalk サードパーティプロバイダーのサービスの使用に対して KakaoTalk および/または KakaoTalk サードパーティプロバイダーに支払うべき料金または支払いについて責任を負います。

{% multi_lang_include braze_legal/english_language_governance.md %}