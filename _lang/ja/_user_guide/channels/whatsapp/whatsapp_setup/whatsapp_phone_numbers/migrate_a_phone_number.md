---
nav_title: "電話番号の移行"
article_title: "WhatsApp電話番号の移行"
page_order: 2
description: "このリファレンス記事では、WhatsApp電話番号を移行する方法について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp電話番号の移行 {#migrate-a-whatsapp-phone-number}

> Metaの埋め込みサインアップを使用して、WhatsApp Business Account間でWhatsApp電話番号を移行します。

## 前提条件 {#prerequisites}

電話番号が移行の対象となるには、Metaの要件を満たしている必要があります。

- Meta Business Accountが認証済みであること。
- 既存のWhatsApp Business Accountが承認済みであること。
- 既存のWhatsApp Business Accountの**Payment Settings**に有効な支払い方法が設定されていること。
- ビジネス用電話番号の2段階認証がオフになっていること。WhatsApp Business Accountを所有している場合は、WhatsApp Managerでその電話番号の2段階認証をオフにできます。それ以外の場合は、ソリューションプロバイダーにオフにするよう依頼する必要があります。

WhatsApp電話番号の移行に関する情報については、Metaのドキュメント「[Migrating phone numbers between WhatsApp Business Accounts via Embedded Signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/)」を参照してください。

## WhatsApp電話番号の移行手順 {#migrating-your-whatsapp-phone-number}

1. WhatsApp Managerで、電話番号に関連付けられたWhatsApp Business Account（WABA）を選択し、**Account tools** > **Phone numbers**に移動します。
2. **Turn off two-step verification**を選択し、表示されるステップを完了します。<br><br>![WhatsApp Business Managerの「Phone numbers」ページ。]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> 別のWhatsApp Business Groupに電話番号を移行する場合で、Metaの埋め込みサインアップで表示名の一致が求められる場合は、**Phone Numbers**ページの既存の表示名をメモしてください。次のステップでその名前を入力します。<br><br>![WhatsApp Business ManagerのPhone Numbersページで、電話番号の横に「Braze」という表示名が表示されている。]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Metaの埋め込みサインアップワークフローを最後まで完了します。