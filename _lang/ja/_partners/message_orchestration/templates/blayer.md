---
nav_title: B.Layer
article_title: B.Layer
description: "このリファレンス記事では、BrazeとB.Layerのパートナーシップについて説明します。B.Layerはアプリ内メッセージビルダーであり、カスタム設計のアプリ内メッセージをコーディングなしで簡単、迅速に作成するために使用できます。"
alias: /partners/blayer-inapps/
page_type: partner
search_tag: Partner

---

# B.Layer

> [B.Layer](https://blayer.phiture.com)はPhitureのアプリ内メッセージビルダーで、モバイルアプリのCRMチームがコーディングなしで、シンプルかつ迅速にカスタムデザインのアプリ内メッセージを作成できるよう支援します。

_この統合はB.Layerによって管理されています。_

## 統合について {#about-the-integration}

BrazeとB.Layerの統合により、B.Layerアプリ内メッセージビルダーを使用して、ZIPファイルまたはインラインHTMLとしてBrazeにエクスポートできるオンブランドのアプリ内メッセージを構築できます。この統合には追加の開発者リソースが不要であるため、時間と予算を節約できます。

![B.Layerビルダーのインターフェイスでブランドに合わせたアプリ内メッセージをプレビューしている画面。]({% image_buster /assets/img/blayer/blayer2.png %})

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| B.Layerアカウント | このパートナーシップを活用するには、[B.Layer](https://blayer.phiture.com)アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

B.Layerでは、製品レコメンデーションスライダー、マルチスクリーンオンボーディングやアンケート、NPS、メールキャプチャ、特別オファーなど、構築して試してみる機会が無限にあります。

Lifesum、Blinkist、OnX Huntなどの多数のブランドと協力し、追加のリソースを必要とせずにユーザーエクスペリエンスを改善できるよう支援しています。また、APS Awards 2022のアプリイノベーション部門のファイナリストにも選ばれています。

## 統合 {#integration}

### ステップ1:アプリ内メッセージを作成する {#step-1-create-your-in-app-message}

#### ブランドカラーとフォントを設定する {#set-brand-colors-and-fonts}

B.Layerで、ページ上部のハンバーガーメニューから、**Brand assets > add your brand assets** をクリックします。ここで、ブランドカラーとフォントを割り当てることができます。
これで準備完了です。アプリ内メッセージのデザインを開始できます。

![B.Layerのブランドアセット画面でカラーとフォントを設定している画面。]({% image_buster /assets/img/blayer/blayer4.png %})

#### アプリ内メッセージをデザインする {#design-your-in-app-message}

アプリ内メッセージをデザインするには、単一のアプリ内メッセージを選択します。次に、メッセージをスタイリングし、必要なコンポーネントを追加します。各コンポーネントは調整可能です。

![B.Layerのメッセージエディターでコンポーネントとスタイルコントロールを表示している画面。]({% image_buster /assets/img/blayer/blayer5.png %})

### アプリ内メッセージをダウンロードする {#download-your-in-app-message}

完了したら、メッセージをダウンロードします。メッセージはZIPまたはインラインHTMLとしてダウンロードできます。

### ステップ2:B.Layerカスタムコードを追加する {#step-2-add-blayer-custom-code}

Brazeで、カスタムコードのアプリ内メッセージを作成します。ZIPファイルをお持ちの場合は、このセクションのアップロードボックスにドラッグ＆ドロップします。インラインHTMLファイルがある場合は、インラインHTMLをHTMLセクションに貼り付けます。

![BrazeのカスタムコードIn-App Messagesエディターに B.Layerのエクスポートコンテンツが表示されている画面。]({% image_buster /assets/img/blayer/blayer6.png %})

## ボタントラッキング {#button-tracking}

B.Layerを使えば、ボタン操作やテキスト入力をBrazeの属性として記録できます。この作業はエディター内で行うことができます。代表的な例としてNPSアンケートがあります。

B.Layerは、入力したリンク（例：`?button=0`）に追加されたBrazeボタンのトラッキングを使用します。こうすることで、キャンペーンの分析パートでボタンのクリック数を確認できます。