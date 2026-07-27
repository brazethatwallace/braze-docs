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

> Metaの埋め込みサインアップを使用して、WhatsApp Businessアカウント間でWhatsApp電話番号を移行します。

## 前提条件 {#prerequisites}

電話番号の移行を行うには、Metaの要件を満たしている必要があります。

- Meta Businessアカウントが認証済みであること。
- 既存のWhatsApp Businessアカウントが承認済みであること。
- 既存のWhatsApp Businessアカウントの**Payment Settings**に有効な支払い方法が設定されていること。
- ビジネス用電話番号の2段階認証がオフになっていること。WhatsApp Businessアカウントを所有している場合は、WhatsAppマネージャーで電話番号の2段階認証をオフにできます。それ以外の場合は、サービスプロバイダーにオフにするよう依頼する必要があります。

WhatsApp電話番号の移行について詳しくは、Metaのドキュメント「[Migrating phone numbers between WhatsApp Business Accounts via Embedded Signup](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/)」を参照してください。

## WhatsApp Businessアカウント間の移行 {#migrate-between-whatsapp-business-accounts}

1. WhatsAppマネージャーで、電話番号に関連付けられたWhatsApp Businessアカウント（WABA）を選択し、**Account tools** > **Phone numbers**に移動します。
2. **Turn off two-step verification**を選択し、表示されるステップを完了します。<br><br>![WhatsApp Businessマネージャーの「Phone numbers」ページ。]({% image_buster /assets/img/whatsapp/waba_manager.png %}){: style="max-width:80%;"} <br><br> 電話番号を別のWhatsApp Businessグループに移行する場合で、Metaの埋め込みサインアップで表示名の一致が求められるときは、**Phone Numbers**ページに表示されている既存の表示名をメモしてください。次のステップでその名前を入力します。<br><br>![WhatsApp Businessマネージャーの「Phone Numbers」ページで、電話番号の横に「Braze」という表示名が表示されている。]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Metaの埋め込みサインアップワークフローを最後まで完了します。

## 別のビジネスソリューションプロバイダー（BSP）からの移行 {#migrate-from-another-business-solution-provider}

WhatsApp電話番号が別のBSPに登録されている場合、Brazeがその番号で送信できるようにするには、Braze接続のWhatsApp Businessアカウントに番号を移行する必要があります。

### 移行前の準備 {#before-you-migrate}

- 電話番号は一度に1つのBSPでのみアクティブにできます。移行すると送信がBrazeに切り替わり、以前のBSPはその番号へのアクセスを失います。
- 現在のプロバイダーとの契約と請求内容を確認してください。メッセージ履歴やテンプレートは自動的に移行されない場合があります。
- Metaの要件に従い、その番号の2段階認証をオフにしてください。
- サポート用とマーケティング用で別々の番号が必要な場合は、WhatsApp FAQの[統合、データ、およびレポート]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting)を参照してください。

### 移行パス {#migration-paths}

| 現在の設定 | 推奨パス |
|---|---|
| 別のBSPに番号があり、完全にBrazeに移行する場合 | [埋め込みサインアップ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup)を通じて、新規または既存のBraze WABAに移行します |
| Brazeネイティブ統合に番号があり、Infobip課金に移行する場合 | [BYO WhatsAppコネクター]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/byo_connector)（Infobipのみ） |
| マーケティングはBraze、サポートは別のWABAで運用する場合 | 別々のWABAと電話番号を維持します。[WhatsApp FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/faq#integrations-data-and-reporting)および[WhatsAppと外部システム]({{site.baseurl}}/user_guide/channels/whatsapp/use_cases/whatsapp_and_external_systems)を参照してください |
{: .reset-td-br-1 .reset-td-br-2 aria-label="移行パス" }

## 開発環境と本番環境のワークスペース {#development-and-production-workspaces}

Brazeでは、可能な限り開発環境と本番環境で別々のWhatsApp Businessアカウントを使用することを推奨しています。

- 本番環境の電話番号をサンドボックスや開発ワークスペースにバインドしないでください。
- 統合テストには専用のテスト用WABAと電話番号を使用してください。
- テンプレートの承認はWABA単位で適用されます。送信を行うワークスペースに紐づいたWABAでテンプレートを承認してください。