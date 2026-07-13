---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "このリファレンス記事では、Brazeと、有力なオンラインメディアプロフェッショナルにアクション可能なインサイトを提供するインテリジェントデータ分析プラットフォームであるNPAWとのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/)は、_Nice People at Work_ としても知られており、有力なオンラインメディアプロフェッショナルにアクション可能なインサイトを提供するインテリジェントなデータ分析プラットフォームです。NPAWのYOUBORAツールスイートにより、Brazeをご利用のお客様は予測的で強力なAIを活用して顧客行動をより深く理解し、プラットフォーム間のエンゲージメントを促進できるようになります。

# 前提条件 {#prerequisites}

| 要件 | 提供元 | 説明 |
| --------------|------|-------------|
| YOUBORA APIキー | [YOUBORAの設定](https://youbora.nicepeopleatwork.com/users/login) | ユーザー登録時に生成されるAPIキーで、**設定**から確認できます。 |
| ID | [Brazeの設定](https://dashboard.braze.com/sign_in) | YOUBORAでは、***Braze ID***、***外部ユーザーID***、または***ユーザーID***のいずれかを使ってソフトウェアをBrazeにリンクできます。 |
| エンドポイント | [Brazeの設定](https://dashboard.braze.com/sign_in) | Brazeダッシュボードで設定可能な完全にカスタマイズ可能なURLエンドポイントです。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="前提条件" }

# 分析の統合 {#analytics-integration}

## 統合ページへのアクセス {#accessing-the-integrations-page}

YOUBORAツールスイートアカウントにログインしたら、ドロップダウンアカウントメニューから**Integrations**オプションを選択して統合ページに移動します。

![NPAWドロップダウンメニュー]({% image_buster /assets/img/npaw_dropdown.png %})

## 統合の設定 {#configuring-your-integration}

統合ページにアクセスしたら、**Braze**統合オプションが表示されるまでスクロールダウンします。クリックすると展開され、入力が必要なパラメーターがいくつか表示されます。

![NPAWの統合設定画面]({% image_buster /assets/img/npaw_integration.png %})

前提条件のセクションで確認した適切な情報を使用して詳細を入力します。
* **Connector Name**は、将来この統合を参照するために使用される**英数字**の文字列です。この値は、文字と数字**のみ**が含まれている限り、任意の値に設定できます。
* **User ID**は、YOUBORAソフトウェアとBrazeアカウントをリンクするために以前に選択したIDです。たとえば、**Braze ID**でリンクを実行する場合は、ドロップダウンから**Braze ID**を選択して、適切なフィールドに値を割り当てます。
* **API Key**は、**設定**の**API**セクションにあるYOUBORAツールスイートのAPIキーです。
* **Endpoint**は、以前にBrazeダッシュボード内で設定したカスタマイズ可能なURLエンドポイントです。

すべてのフィールドを入力したら、**Connect**ボタンをクリックして接続を確立し、変更を保存します。

## NPAW統合の使用 {#using-your-npaw-integration}

Brazeとの統合の設定が完了したら、**Users**製品に移動し、**Sections Manager**内で**Sample Manager**を選択します。

**Sample Manager**でサンプルを作成した後、行アクションメニューの3つのドットのアイコンをクリックすると、サンプル内のすべてのユーザーをBrazeに送信できます。

![NPAWサンプルマネージャー画面]({% image_buster /assets/img/npaw_sample_manager.png %})

ユーザーをBrazeに送信したら、ユーザーセグメントに対するキャンペーンに注力して、非アクティブなユーザーの再エンゲージメント、最もロイヤルなユーザーへのコンタクトなど、あらゆるユーザーセグメントに対するアクションを実行できます。