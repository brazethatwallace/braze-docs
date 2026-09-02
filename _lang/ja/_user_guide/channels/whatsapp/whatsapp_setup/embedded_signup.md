---
nav_title: 埋め込みサインアップ
article_title: WhatsApp埋め込みサインアップ
page_order: 1
description: "このリファレンス記事では、BrazeにおけるWhatsApp埋め込みサインアップワークフローへのアクセス方法、Metaサインアップ前の準備事項、およびサインアップ完了後の動作について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp埋め込みサインアップ {#whatsapp-embedded-signup}

> 埋め込みサインアップを使用して、Metaがホストするサインアップフローを通じてBrazeをWhatsApp Businessアカウント（WABA）に接続します。

WhatsApp埋め込みサインアップワークフローは、Brazeワークスペースに初めて[WhatsAppを統合する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)とき、および既存の統合に[WhatsApp Businessアカウントまたは電話番号を追加する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)ときに開きます。

{% alert note %}
Brazeワークスペースには[複数のWhatsApp Businessアカウント]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/multiple_business_accounts)を追加できます。ただし、各WhatsApp Businessアカウントは1つのBrazeワークスペースにのみ追加できます。
{% endalert %}

## ワークフローへのアクセス {#accessing-the-workflow}

1. **パートナー連携** > **テクノロジーパートナー**に移動します。
2. **WhatsApp**を検索して選択します。
3. ユースケースに合ったオプションを選択します:
   - **初回連携：** **Begin Integration**を選択します。
   - **追加のアカウントまたは番号：** **WhatsApp Messaging Integration**ページで、**Add account or number**または**Add WhatsApp Business Account**を選択します。

Metaの埋め込みサインアップフローは、どちらのエントリポイントから開始しても同じです。ワークスペースには、設定に応じて**Native Integration**や**BYO Connector - Infobip**などの連携タブが表示される場合もあります。開始する前に、設定に合ったタブを選択してください。

## サインアップの準備 {#prepare-for-signup}

**連携を開始**を選択すると、Brazeがオンボーディングウィンドウを開きます。各スライドを確認し、再度**連携を開始**を選択してMetaの埋め込みサインアップを起動します。

開始する前に、以下を準備してください。

- **Meta Business Managerへのアクセス：** ほとんどの企業では、Meta Business Managerを使用してFacebookページ、広告、および関連するビジネスアセットを管理しています。アクセス権がない場合は、管理者に権限の付与を依頼するか、サインアップ中にBusiness Managerアカウントを作成してください。
- **電話番号：** [MetaのWhatsApp電話番号要件](https://developers.facebook.com/docs/whatsapp/phone-numbers)を満たす番号を使用してください。サインアップ中に、テキストメッセージまたは電話で1回限りの認証コードを受け取ります。

{% alert important %}
初回の埋め込みサインアップは連携パスごとに1回のみ完了します。ビジネスの詳細情報はできるだけ正確に入力してください。
{% endalert %}

## WhatsApp埋め込みサインアップワークフロー {#whatsapp-embedded-signup-workflow}

BrazeがMetaの埋め込みサインアップを起動したら、自社のBusiness ManagerにアクセスできるMetaアカウントでサインインしてください。サインアップ画面はMetaがホストしており、Brazeはそのレイアウトやラベルを制御していません。

{% alert note %}
Metaは予告なく埋め込みサインアップ画面を変更する場合があります。ワークフローがこの記事と異なる場合は、Metaのプロンプトに従い、[Metaの埋め込みサインアップドキュメント](https://developers.facebook.com/docs/whatsapp/embedded-signup/embed-the-flow)を参照してください。
{% endalert %}

一般的に、Metaは以下のステップを案内します。

1. **サインインして権限を付与する。** Metaで認証し、BrazeがWhatsApp Businessアカウントに接続することを許可します。
2. **ビジネスポートフォリオを選択する。** WhatsApp Businessアカウントを所有するBusiness Managerポートフォリオを接続します。期待するポートフォリオが表示されない場合は、Metaの権限を確認してください。
3. **WhatsApp Businessアカウントを接続または作成する。** プロンプトが表示されたら、新しいアカウントを作成するか、未使用のアカウントを選択します。別のメッセージングプロバイダーに現在接続されているWhatsApp Businessアカウントを選択しないでください。その接続はBrazeで成功しません。[別のプロバイダーから番号を移行する]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers/migrate_a_phone_number)場合は、開始前にBrazeアカウントチームにお問い合わせください。
4. **ビジネスおよび表示の詳細を入力する。** WhatsApp Businessアカウントに対してMetaが要求するアカウント名、表示名、カテゴリを入力します。
5. **電話番号を確認する。** WhatsAppメッセージングに使用する番号を追加し、テキストメッセージまたは電話で確認を完了します。

Metaの埋め込みサインアップが完了すると、制御がBrazeに戻ります。

## Braze連携を完了する {#complete-the-braze-integration}

埋め込みサインアップの後、Brazeは設定ステップを自動的に実行します。**WhatsApp Messaging Integration** ページに、Brazeが以下の処理を行っている間、**Sign-up flow completed, integration with WhatsApp in progress** などの進行状況メッセージが表示される場合があります。

- MetaからWhatsApp BusinessアカウントIDと電話番号を取得する
- Brazeシステムユーザーを WhatsApp Businessアカウントに追加する
- 電話番号を登録し、Webhookイベントを購読する
- 接続された番号ごとにBraze[購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)を作成する

メッセージを送信する前に、連携が完了するまでお待ちください。設定に失敗した場合は、連携ページでエラーを確認し、一般的なガイダンスについては [WhatsApp設定]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)を参照してください。

## 次のステップ {#next-steps}

- [WhatsApp電話番号の取得または移行]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/whatsapp_phone_numbers)
- [WhatsAppメッセージの作成]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message)
- [購読グループの管理]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)