---
nav_title: Figma
article_title: Figma
description: "このリファレンス記事では、BrazeとFigmaのパートナーシップについて説明します。この連携により、画像やビジュアルアセットをBrazeメディアライブラリに送信できます。"
alias: /partners/figma/
page_type: partner
search_tag: Partner
---

# Figma

> [Figma](https://www.figma.com/)は、製品の構築、デザイン、プロトタイプ作成を可能にするコラボレーションデザインプラットフォームです。

## 連携について {#about-the-integration}

BrazeとFigmaの連携により、Figmaから直接Brazeメディアライブラリに画像やビジュアルアセットを送信できます。

この連携の仕組みについては、以下の動画をご覧ください。

{% multi_lang_include video.html id="ab5ywsi72n" source="wistia" %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Figmaアカウント | このパートナーシップを利用するには、Figmaアカウントが必要です。 |
| Brazeメディアライブラリへのアクセス | Brazeでメディアライブラリアセットの追加、編集、削除を行うには、「Manage Media Library Assets」権限が必要です。 |
| Brazeワークスペースへのアクセス | Figmaの画像やビジュアルアセットをアップロードするBrazeのワークスペースへのアクセス権が必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

### ステップ1:Figma to Braze Exportプラグインをインストールする {#step-1-install-the-figma-to-braze-export-plugin}

FigmaのCommunityにアクセスして、[Braze Exportプラグイン](https://www.figma.com/community/plugin/1606726267245196698/figma-to-braze-export)を見つけます。**Open In**を選択して、Figmaファイルにプラグインを読み込みます。

Figmaでは、**Plugins**セクションからもFigma to Braze Exportプラグインを見つけることができます。

### ステップ2:Brazeに接続する {#step-2-connect-to-braze}

インストール後、**Connect to Braze**を選択してBrazeアカウントを接続し、**Continue**を選択します。

次に、**Braze workspace**ドロップダウンからBrazeのワークスペースを選択するか、ワークスペース名を入力します。

### ステップ3:Figmaアセットを選択する {#step-3-select-your-figma-assets}

Brazeにエクスポートする画像やビジュアルアセットを選択します。複数のアセットを選択するには、<kbd>Shift</kbd>キーを押すか、アセット上でカーソルをドラッグ＆ドロップします。

エクスポートされる画像やビジュアルアセットの名前には、Figmaで選択したフレームの名前が使用されます。

### ステップ4:Brazeにエクスポートする {#step-4-export-to-braze}

**Export to Braze**を選択します。画像やビジュアルアセットがBrazeメディアライブラリにアップロードされます。この連携を使用してインポートされたすべての画像は、ソースが**Figma**に設定されます。