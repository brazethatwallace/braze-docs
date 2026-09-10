---
nav_title: GPI
article_title: Globalization Partners International
date_published: "2026-09-09"
description: "このリファレンス記事では、BrazeとGlobalization Partners International（GPI）の翻訳サービスプロバイダーとのパートナーシップについて説明します。GPI Translation Services ConnectorはBrazeのコンテンツを抽出して翻訳し、完成した翻訳をBrazeの翻訳APIを通じてインポートします。"
alias: /partners/gpi/
page_type: partner
search_tag: Partner
---

# Globalization Partners International

> [Globalization Partners International](https://www.globalizationpartners.com/)（GPI）は、Braze用のGPI Translation Services Connectorを提供しています。このコネクタは、キャンペーン、キャンバス、メールテンプレート、Content Blocksからコンテンツを抽出して翻訳し、翻訳APIを通じて完成した翻訳をBrazeにインポートします。GPIは、200以上の言語にわたる人間翻訳、AI翻訳、およびエキスパートのポストエディティングを伴うAI翻訳をサポートしています。

_このインテグレーションはGlobalization Partners Internationalによって管理されています。_

## インテグレーションについて {#about-the-integration}

GPI Translation Services Connectorは、Brazeのネイティブ多言語モデルおよび翻訳APIと連携します。GPI Translation Portalから翻訳可能なコンテンツを抽出し、GPIに翻訳を依頼し、完成した翻訳を手動のコピー＆ペーストなしでBrazeにインポートできます。GPIはワークフロー全体を通じてLiquidタグとパーソナライゼーションを保持します。

## ユースケース {#use-cases}

### グローバルキャンペーンのローンチ {#global-campaign-launch}

Brazeでキャンペーン、キャンバス、またはメールテンプレートを選択し、ソース言語とターゲット言語を設定して、プロの人間翻訳のためにコンテンツをGPIに送信します。GPIはローンチ前に下書きプレビューでローカライゼーションと品質保証を行います。

### 時間的に厳しい案件や大量のローカライゼーション {#time-sensitive-or-high-volume-localization}

フラッシュセール、緊急のライフサイクルメッセージ、またはContent Blocksの大量バッチをコネクタ経由でルーティングし、翻訳を自動的にBrazeにインポートします。所要時間は選択するワークフローによって異なり、数週間から数分まで幅があります。

### 国際化サポート {#internationalization-support}

GPIは、アラビア語、ヘブライ語、ペルシア語などの右から左（RTL）言語を含む、Brazeローカライゼーションのフォーマットとベストプラクティスに関するガイダンスを提供します。

### 継続的な大規模ローカライゼーション {#ongoing-localization-at-scale}

GPIは翻訳メモリを使用して、用語とスタイルの一貫性のために過去の翻訳を再利用し、完全一致、繰り返し、ファジーマッチのコストを削減します。Brazeでソース言語のキャンペーンを更新し、改訂したコンテンツをGPIに送信して対応する翻訳を更新します。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| Globalization Partners Internationalアカウント | このインテグレーションを使用するには、GPIアカウントが必要です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー：<br>- `campaigns.list`<br>- `campaigns.details`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `canvas.list`<br>- `canvas.details`<br>- `canvas.translations.get`<br>- `canvas.translations.update`<br>- `content_blocks.list`<br>- `content_blocks.info`<br>- `content_blocks.translations.get`<br>- `content_blocks.translations.update`<br>- `templates.email.list`<br>- `templates.email.info`<br>- `templates.email.translations.get`<br>- `templates.email.translations.update`<br><br>このキーはBrazeダッシュボードの**設定** > **APIと識別子** > **APIキー**から作成します。詳細については、[REST APIキーの作成]({{site.baseurl}}/api/basics#creating-rest-api-keys)を参照してください。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/api/basics#endpoints)。エンドポイントはお使いのインスタンスのBraze URLによって異なります。 |
| Braze多言語設定 | ターゲットロケールは、Brazeの**設定** > **ローカライゼーション設定**で設定されている必要があります。詳細については、[多言語設定]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## インテグレーション {#integration}

### ステップ1：Braze REST APIキーを作成する {#step-1-create-a-braze-rest-api-key}

1. Brazeで**設定** > **APIと識別子** > **APIキー**に移動します。
2. [前提条件](#prerequisites)に記載されている権限を持つREST APIキーを作成します。
3. APIキーをコピーし、インスタンスのRESTエンドポイントをメモします。

### ステップ2：設定をGPIに送信する {#step-2-send-settings-to-gpi}

1. APIキーとRESTエンドポイントをGPIのアカウントマネージャーに送信します。
2. コネクタへのアクセスが必要なユーザーのリストを送信し、GPIがアクセスを有効にできるようにします。
3. GPIがお客様の認証情報でコネクタを設定し、接続を検証します。

### ステップ3：Brazeでローカライゼーション設定を行う {#step-3-configure-localization-settings-in-braze}

1. Brazeで**設定** > **ローカライゼーション設定**に移動し、ターゲットロケールが有効になっていることを確認します。
2. 翻訳に送信するコンテンツで、必要なロケールが有効になっていることを確認します。ロケールが有効になっていないコンテンツは、インポートされた翻訳を受け取ることができません。
3. 翻訳が必要なコンテンツの周りに[翻訳Liquidタグ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)を追加します。
4. RTL言語の場合、言語に基づいてコンテンツの方向をサポートするLiquidタグを追加します。RTLレンダリングに影響しないことを確認できない限り、配置スタイルのディレクティブは使用しないでください。

## GPIをBrazeで使用する {#use-gpi-with-braze}

Brazeで翻訳できるのは、下書きまたはローンチ後の下書きステータスのコンテンツのみです。

### ステップ1：翻訳用にコンテンツをエクスポートする {#step-1-export-content-for-translation}

1. [GPI Translation Portal](https://www.translationportal.com)で、**Braze**コネクタを開き、**New Request**を選択します。
2. **Information**タブに入力し、**Content**タブを開きます。**Categories**から**キャンペーン**、**キャンバス**、**Email Template**、または**Content Block**を選択し、エクスポートするアイテムを選択します。
3. **Submit**を選択してGPIに見積もりリクエストを送信します。見積もりの確認と承認の準備ができると、GPIのアカウントマネージャーから連絡があります。

### ステップ2：翻訳をBrazeにインポートする {#step-2-import-translations-into-braze}

1. **Braze**コネクタで、インポートするプロジェクトを見つけます。
2. **Actions**列の**Import**アイコンを選択します。
3. インポート確認メッセージを待ちます。インポートジョブのステータスは**Jobs**ページで確認できます。

### ステップ3：翻訳リクエストのステータスを確認する {#step-3-check-translation-request-status}

1. [GPI Translation Portal](https://www.translationportal.com)にアクセスします。
2. **Sign In**を選択し、認証情報を入力します。
3. GPI Translation Portalのナビゲーションで**Braze**を選択してコネクタのダッシュボードを開きます。**Quotes**テーブルと**Projects**テーブルでリクエストとプロジェクトのステータスを確認します。

### ステップ4：Brazeで翻訳をプレビューする {#step-4-preview-translations-in-braze}

翻訳をインポートしたら、Brazeでプレビューします。

1. 翻訳したキャンペーンまたはメッセージの**編集**画面を開きます。
2. **メッセージ作成画面**で、**プレビューとテスト**タブまたは**テスト**タブに移動します。
3. **ユーザーとしてメッセージをプレビュー**で**多言語ユーザー**を選択し、表示したいロケールを選択します。
4. ターゲット言語でプレビューを確認します。外部のレビュー担当者と共有するには、プレビューリンクを生成します。

## 留意事項 {#considerations}

- Braze用のGPI Translation Services Connectorは無料で提供されます。

## トラブルシューティング {#troubleshooting}

Braze用のGPI Translation Services ConnectorまたはGPIの翻訳プロジェクトに関するサポートが必要な場合は、GPIのプロジェクトマネージャーに連絡するか、+1-866-272-5874に電話するか、[support@globalizationpartners.com](mailto:support@globalizationpartners.com)にメールしてください。