---
nav_title: Bynder
article_title: Bynder
description: "このリファレンス記事では、BrazeとBynderのパートナーシップについて説明します。Bynderはデジタルアセット管理（DAM）プラットフォームであり、Universal Compact View Chrome拡張機能を通じて、承認済みアセットのURLを検索してBrazeのキャンペーンやキャンバスに挿入できます。"
alias: /partners/bynder/
page_type: partner
search_tag: Partner
---

# Bynder

> [Bynder](https://www.bynder.com)は、顧客が承認済みのデジタルアセット（画像、動画、その他のクリエイティブ）を単一の信頼できるソースから作成、管理、検索、配布できるデジタルアセット管理（DAM）プラットフォームです。Brazeと統合すると、BynderのUniversal Compact View（UCV）Google Chrome拡張機能により、マーケターはBrazeダッシュボードを離れることなくBynderアセットを検索・選択できます。それらのアセットへのリンクをキャンペーンやキャンバスに直接挿入できます。

_この統合はBynderによって管理されています。_

## この統合について {#about-this-integration}

UCV Chrome拡張機能を通じてBynderをBrazeに接続すると、マーケターはBrazeコンテンツエディター内でBynderアセットライブラリにアクセスできます。Brazeダッシュボードを含む任意のブラウザタブでUniversal Compact Viewをオーバーレイとして開きます。適切なクリエイティブを検索またはフィルターし、アセットのURLをキャンペーンに貼り付けます。

これにより、Brazeキャンペーンは常にBynderの単一の信頼できるソースと整合性が保たれます。正しい権限、最新のファイルバージョン、正しい使用権が維持されます。

## ユースケース {#use-cases}

- Brazeでメール、アプリ内メッセージ、またはコンテンツブロックを作成するマーケターは、Bynderから直接取得したヒーロー画像、バナー、プロモーション動画リンクを挿入でき、キャンペーンでアセットの最新の承認済みバージョンを使用できます。
- キャンペーンマネージャーは、Universal Compact Viewの検索・フィルターバーを使用して、特定のオーディエンスセグメント向けの承認済みリージョナルまたはローカライズされたクリエイティブを見つけてから、キャンバスステップに追加できます。
- クリエイティブチームは、BynderのDynamic Asset Transformationを適用して、特定のチャネル向けにアセットのサイズ変更やフォーマット変換を行ってから、リンクをBrazeにコピーできます。たとえば、プッシュ通知用にコンパクトなクロップを使用したり、メール用にフルサイズのバナーを使用したりできます。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 要件 | 説明 |
| --- | --- |
| Bynderアカウント | Brazeで参照したいDAMアセットにアクセスできるBynderアカウント。 |
| Bynder Universal Compact View（UCV）Chrome拡張機能 | Chrome Web Storeからインストールし、Bynderポータルに接続済みであること。Google Chromeでのみ利用可能です。 |
| パブリックアセットとデリバティブ | リンクするアセットおよび特定のデリバティブは、メッセージ受信者に対してURLが正しく解決されるよう、Bynderでパブリックとしてマークされている必要があります。 |
| Brazeアカウント | アセットが使用されるメッセージングチャネル（メール、コンテンツブロック、アプリ内メッセージ、キャンバスなど）へのアクセス。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ1:Bynder UCV Chrome拡張機能をインストールして接続する {#step-1-install-and-connect-the-bynder-ucv-chrome-extension}

1. Chrome Web Storeの[Bynder UCV拡張機能](https://chromewebstore.google.com/detail/bynders-universal-compact/ilghhphnbdblpbdhmbdfiaidganphema)にアクセスします。
2. **Chromeに追加**をクリックし、要求された権限を確認してから、**拡張機能を追加**をクリックします。
3. Chromeツールバーから、Bynder UCVアイコンを選択します（まだ表示されていない場合は、先にツールバーにピン留めしてください）。
4. Bynderポータルドメインを入力し（`https://`なし）、**Connect**をクリックします。
5. 開いたウィンドウで、通常の認証情報を使用してBynderポータルにログインします。

### ステップ2:Bynderアセットを検索して選択する {#step-2-search-for-and-select-a-bynder-asset}

1. 拡張機能が接続された状態で、Brazeダッシュボードを含む任意のブラウザタブからUniversal Compact Viewを開きます。
2. スマートフィルターと検索バーを使用して、必要な画像、動画、ドキュメント、またはオーディオアセットを見つけます。
3. アセットを選択し、使用するデリバティブ（またはパブリックの場合はオリジナルファイル）を選択します。
4. **Add Asset**をクリックして、選択したアセットのURLをクリップボードにコピーします。

### ステップ3:アセットURLをBrazeキャンペーンに追加する {#step-3-add-the-asset-url-to-your-braze-campaign}

1. Brazeで、アセットを追加したいメール、コンテンツブロック、アプリ内メッセージ、またはキャンバスステップを開きます。
2. コピーしたBynderアセットURLを該当するフィールドに貼り付けます。たとえば、`<img src="">`タグやコンテンツブロックの画像URLフィールドを使用します。

   画像URLの例:

   ```html
   <img src="https://your-portal.bynder.com/m/abcdef123456/original/campaign-banner.jpg" alt="Summer Campaign">
   ```

{: start="3"}
3. メッセージを保存してプレビューし、アセットが期待どおりにレンダリングされることを確認します。

## ヒント {#tips}

### URLをコピーする前にDynamic Asset Transformationを適用する {#apply-dynamic-asset-transformations-before-copying-the-url}

Universal Compact View内で、利用可能な変換オプションを使用して、ターゲットとするチャネルに合わせてアセットのサイズ変更、クロップ、またはフォーマット変換を行います。これにより、クロップされた別バージョンをBynderにアップロードする必要がなくなります。

### チャネル固有のデリバティブURLを生成する {#generate-channel-specific-derivative-urls}

各変換またはデリバティブは、それぞれ固有のURLを生成します。メール用、プッシュ用、アプリ内メッセージ用にそれぞれサイズの異なるバージョンを生成し、対応するBrazeチャネルまたはキャンバスステップに貼り付けます。

### 1つのアセットURLを複数のチャネルで再利用する {#reuse-one-asset-url-across-channels}

貼り付けたリンクはBynder内の特定のアセットとデリバティブを指すため、同じURL形式をメール、コンテンツブロック、アプリ内メッセージ、キャンバスステップ全体で再利用できます。これにより、キャンペーンで使用されるすべての場所でクリエイティブの一貫性が保たれます。

### キャンペーンを編集せずにソースアセットを更新する {#update-the-source-asset-without-editing-your-campaigns}

Bynder内の元ファイルが同じパブリックアセットおよびデリバティブ設定を維持したまま置き換えられた場合、そのURLを参照しているライブのBrazeメッセージは自動的に更新を反映します。キャンペーン自体を編集する必要はありません。

## 考慮事項 {#considerations}

- Bynder UCV Chrome拡張機能はGoogle Chromeでのみ利用可能です。他のブラウザでは、Bynderポータルのフルバージョンから直接アセットURLをコピーしてください。
- Bynderでパブリックとしてマークされたアセット（およびリンクされている特定のデリバティブ）のみが、Brazeに貼り付けた際に解決されます。プライベートアセットは受信者にアクセスエラーを返します。
- ポップアップウィンドウが許可されていない場合、またはポータルが別のタブで既に開いている場合、ログインウィンドウが正しく開かないことがあります。接続する前に、ポップアップウィンドウが許可されていることを確認し、ポータルが開いている他のタブを閉じてください。
- 拡張機能内のアクセスは、Bynder DAMにおける企業ユーザーの既存の権限に従うため、ユーザーはアクセスが許可されているアセットのみを表示・選択できます。

## トラブルシューティング {#troubleshooting}

| 問題 | 解決方法 |
| --- | --- |
| 拡張機能のアイコンが表示されない | 拡張機能メニューからBynder UCV拡張機能をChromeツールバーにピン留めしてください。 |
| **Connect**をクリックしてもログインウィンドウが開かない | Bynderポータルドメインに対してChromeのポップアップが許可されていることを確認し、ポータルが既に開いている他のタブを閉じてください。 |
| アセットURLがBrazeでレンダリングされない | Bynderポータルで、アセットおよび使用している特定のデリバティブがパブリックとしてマークされていることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

詳細については、Bynderの[Universal Compact Viewドキュメント](https://support.bynder.com/hc/en-us/sections/16936397091858-Universal-Compact-View-UCV)を参照するか、Bynderサポートにお問い合わせください。