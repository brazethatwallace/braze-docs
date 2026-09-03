---
nav_title: 品質評価とメッセージング制限
article_title: 品質評価とメッセージング制限
description: "このリファレンス記事では、MetaがWhatsAppチャネルの品質評価とメッセージング制限にどのように影響するかについて説明しています。"
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
---

# 品質評価とメッセージング制限 {#quality-rating-and-messaging-limits}

> Metaは、WhatsAppチャネルの使用を開始した時点から品質評価と[メッセージング制限](https://developers.facebook.com/docs/whatsapp/messaging-limits)に影響を与え、WhatsAppの使用状況に応じて引き続き影響を与えます。

## 定義 {#definitions}

| 用語 | 定義 |
| --- | --- |
| 品質評価 | 過去7日間に顧客が受信した最近のメッセージに基づく評価です。この評価は、電話番号のブロック理由やその他の報告問題など、顧客からのフィードバックによって決定されます。[品質評価について](https://www.facebook.com/business/help/896873687365001)詳しくはMetaのドキュメントをご覧ください。|
| メッセージング制限 | ローリング24時間の期間内に、各電話番号で開始できるビジネス主導の会話の最大数です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definitions" }

## オンボーディング {#onboarding}

新しいWhatsApp Businessアカウントが作成されると、Metaはさまざまな要素を使用して初期送信制限を決定します。この制限はWhatsApp Business マネージャーで確認でき、追加の詳細は電話番号インサイトページで確認できます。

[制限の確認](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit)と[電話番号の要件](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)について詳しくはMetaのドキュメントをご覧ください。

## スループット {#throughput}

Metaは、登録された各ビジネス電話番号に対して、1秒あたり80メッセージのスループットで開始します。1秒あたり1,000メッセージへのアップグレードは、自動的に、またはリクエストに応じて行われます。

[スループット](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput)について詳しくはMetaのドキュメントをご覧ください。

## テンプレートペーシング {#template-pacing}

最近作成されたマーケティングテンプレートや、一時停止後に再開されたマーケティングテンプレートは、ペーシングの対象となる可能性があります。Metaのペーシング選択基準は、主にテンプレートの品質履歴によって決まります。最近作成されたマーケティングテンプレートや最近再開されたマーケティングテンプレートを使用すると、未指定のしきい値に達するまでメッセージは通常どおり送信されます。このしきい値に達すると、そのテンプレートを使用する後続のメッセージは、顧客からのフィードバックを得るための十分な時間を確保するために保留されます。

[テンプレートペーシング](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing)について詳しくはMetaのドキュメントをご覧ください。