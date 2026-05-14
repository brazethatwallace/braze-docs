---
nav_title: Inbox Monster
article_title: Inbox Monster
alias: /partners/inbox_monster/
description: "この参考記事では、BrazeとオンラインメールマーケティングツールInbox Monsterのパートナーシップについて概説しています。Inbox Monsterは、Brazeの顧客が受信トレイのパフォーマンスを向上させるための強力な配信インサイトとクリエイティブ分析を可能にするツールです。"
page_type: partner
search_tag: Partner

---

# Inbox Monster

> [Inbox Monster](https://inboxmonster.com/) は、企業ブランドがすべての送信を成功させるためのインボックスシグナルプラットフォームです。配信到達性、クリエイティブレンダリング、SMSモニタリングのための統合ソリューションスイートであり、最新のCRMチームを強化し、送信の不安を解消します。

BrazeとInbox Monsterの統合により、手動でのシードリストテストを排除し、強力で実用的な受信トレイ配置シグナルの作成を自動化し、メールクリエイティブアセットのレビューと承認プロセスを簡素化し、配信到達性に関する貴重なインサイトを取得できます。また、クリエイティブ診断やデバイスプレビュー用のメールテンプレートをシームレスにインポートすることもできます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Inbox Monsterプラットフォームアカウント | このパートナーシップを活用するには、Inbox Monsterプラットフォームアカウントが必要です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー:  <br> - `messages.send` <br>  - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> - `templates.email.list` <br><br> また、以下のIPがホワイトリストに登録されている必要があります: <br> - `3.136.16.19` <br>  - `3.140.233.31`<br> - `18.220.127.138` <br><br> これは、Brazeダッシュボードの**設定** > **APIキー**の**APIキー**タブで作成できます。 |
| Brazeアプリ識別子 | Brazeアプリ識別子。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**の**アプリ識別子**タブで確認できます。 |
| Brazeエンドポイント | [Brazeエンドポイント]({{site.baseurl}}/api/basics/#endpoints)はBrazeダッシュボードのURLに対応しています。<br><br> たとえば、ダッシュボードURLが`https://dashboard-03.braze.com`の場合、エンドポイントは`dashboard-03`になります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

Inbox Monsterを統合するには、[Integrating with Inbox Monster](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3)のステップに従ってください。

## 使用方法 {#usage}

Inbox Monsterを介してスケジュールされた受信トレイ配置テストを送信する方法については、[Scheduled Inbox Placement Tests](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e)を参照してください。