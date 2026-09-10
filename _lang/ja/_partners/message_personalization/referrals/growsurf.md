---
date_published: "2026-09-08"
nav_title: GrowSurf
article_title: GrowSurf
description: "このリファレンス記事では、BrazeとGrowSurfのパートナーシップについて説明します。GrowSurfは紹介プログラムおよびアフィリエイトプログラムのプラットフォームで、参加者データをBrazeに同期してセグメンテーションやLiquidパーソナライゼーションに活用できます。"
alias: /partners/growsurf/
page_type: partner
search_tag: Partner
---

# GrowSurf

> [GrowSurf](https://www.growsurf.com/)は、紹介プログラムおよびアフィリエイトプログラムの参加者データをBrazeのユーザープロファイルに送信します。この連携により、紹介リンク、参加者の詳細、紹介数、招待数、インプレッション数、マイルストーンの進捗状況がカスタム属性として追加され、Brazeのセグメンテーションやのパーソナライゼーションに使用できます。

_この連携はGrowSurfによって維持管理されています。_

## 連携について {#about-the-integration}

GrowSurfは紹介プログラムおよびアフィリエイトプログラムのソフトウェアです。この単方向の連携により、GrowSurfの参加者の紹介データがBrazeで利用可能になり、参加者のセグメント作成、紹介リンクや進捗状況でのメッセージのパーソナライゼーション、Brazeからのタイムリーなプログラムコミュニケーションの送信が可能になります。

## ユースケース {#use-cases}

- 各参加者の紹介リンクをBrazeメッセージに追加します。
- 紹介ステータス、紹介数、マイルストーンの進捗状況からセグメントを作成します。
- 参加者や紹介者の属性を使ってキャンペーンやキャンバスをパーソナライズします。

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
| --- | --- |
| GrowSurfアカウント | この連携にはGrowSurfの有料プランが必要です。 |
| Braze REST APIキー | `users.track`権限を持つBraze REST APIキー。このキーは、Brazeダッシュボードの**設定** > **APIと識別子** > **APIキー**から作成します。詳細については、[REST APIキーの作成]({{site.baseurl}}/api/basics#creating-rest-api-keys)を参照してください。 |
| Braze RESTエンドポイント | Braze RESTエンドポイントURL（例：`https://rest.iad-01.braze.com`）。詳細については、[REST APIエンドポイント]({{site.baseurl}}/api/basics#endpoints)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携 {#integration}

以下のステップに従って、GrowSurfプログラムをBrazeに接続します。詳細な手順については、[GrowSurf Braze連携ドキュメント](https://docs.growsurf.com/integrations/braze)を参照してください。

### ステップ1：Braze REST APIキーを作成する {#step-1-create-a-braze-rest-api-key}

1. Brazeで、**設定** > **APIと識別子** > **APIキー**に移動します。
2. `users.track`権限を持つREST APIキーを作成します。
3. APIキーをコピーし、同じBrazeワークスペースのRESTエンドポイントをメモします。

### ステップ2：GrowSurfでBrazeを接続する {#step-2-connect-braze-in-growsurf}

1. GrowSurfで、**Program Editor** > **4. Options** > **Integrations** > **Braze**に移動します。
2. 一致するBraze RESTエンドポイントを選択します。
3. REST APIキーを入力し、**Submit**を選択します。

### ステップ3：最初の参加者同期を確認する {#step-3-verify-the-first-participant-sync}

1. GrowSurfでテスト参加者を追加または更新します。
2. Brazeで、**オーディエンス** > **ユーザー検索**に移動し、メールアドレスで検索して一致するユーザープロファイルを開きます。
3. `grsf_`カスタム属性がプロファイルに表示されていることを確認します。

## BrazeにおけるGrowSurf属性 {#growsurf-attributes-in-braze}

GrowSurfはBrazeで15件の紹介属性を利用可能にします。最初の同期では全セットが送信されます。その後、参加者データが変更されるとGrowSurfが更新を送信します。GrowSurfで値が削除されると、対応するBraze属性もクリアされます。カウント値は数値として送信されます。

### 文字列属性 {#string-attributes}

| カスタム属性 | 説明 |
| --- | --- |
| `grsf_share_url` | 参加者の紹介シェアURL。 |
| `grsf_participant_id` | 参加者のGrowSurf ID。 |
| `grsf_referral_status` | 参加者の紹介ステータス。 |
| `grsf_participant_first_name` | 参加者の名。 |
| `grsf_participant_last_name` | 参加者の姓。 |
| `grsf_referrer_first_name` | 紹介者の名。 |
| `grsf_referrer_last_name` | 紹介者の姓。 |
| `grsf_referrer_email` | 紹介者のメールアドレス。 |
| `grsf_next_milestone` | 参加者が目指している次のマイルストーン。 |
| `grsf_next_monthly_milestone` | 参加者が目指している次の月間マイルストーン。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="文字列属性" }

### 数値属性 {#number-attributes}

| カスタム属性 | 説明 |
| --- | --- |
| `grsf_total_referral_count` | 参加者の紹介合計数。 |
| `grsf_monthly_referral_count` | 参加者の当月の紹介数。 |
| `grsf_prev_monthly_referral_count` | 参加者の前月の紹介数。 |
| `grsf_total_invite_count` | 参加者の招待合計数。 |
| `grsf_total_impression_count` | 参加者の紹介リンクのインプレッション合計数。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="数値属性" }

## BrazeでのGrowSurfの使用 {#use-growsurf-with-braze}

GrowSurfの紹介属性をBrazeのセグメンテーションやLiquidパーソナライゼーションに使用します。GrowSurfは参加者が追加されたり紹介データが変更されたりすると、これらの属性を更新します。すでにプログラムに参加している参加者も同期できます。

### ステップ1：セグメントを作成する {#step-1-build-segments}

1. Brazeで、関連する`grsf_`カスタム属性を使用してセグメントを作成します。
2. 紹介ステータス、紹介数、またはマイルストーンの進捗状況によって参加者をターゲットまたは除外します。

### ステップ2：メッセージをパーソナライズする {#step-2-personalize-messages}

1. Liquidを使用して`grsf_share_url`カスタム属性をBrazeメッセージに追加します：{% raw %}`{{custom_attribute.${grsf_share_url}}}`{% endraw %}。

{: start="2"}
2. その他の`grsf_`属性を使用して、紹介ステータス、カウント数、マイルストーンの進捗状況をパーソナライズします。

## 注意事項 {#considerations}

- GrowSurfはカスタム属性のみを送信します。カスタムイベント、購入、購読の変更は送信しません。
- GrowSurfは参加者のメールアドレスでBrazeプロファイルを識別します。一致するプロファイルが存在しない場合、Brazeはメールのみのプロファイルを作成します。
- 同じメールアドレスが複数の接続済みGrowSurfプログラムの参加者に属している場合、最後に同期されたプログラムのデータがそのBrazeプロファイルに表示されます。
- 参加者をインポートする前にBrazeを接続してください。既存の参加者を同期するには、GrowSurfの既存参加者同期オプションを使用してください。

## トラブルシューティング {#troubleshooting}

- Braze REST APIキーに`users.track`権限があること、および選択したRESTエンドポイントが同じBrazeワークスペースに属していることを確認してください。
- 1人の参加者の同期に失敗した場合は、その参加者が有効なメールアドレスを持っていることを確認してください。
- 同期結果については、参加者のGrowSurfアクティビティログを確認してください。
- GrowSurfは一時的なBrazeエラーを自動的にリトライします。GrowSurfが更新を確認できない場合、次回そのBrazeプロファイルが同期される際にすべての紹介属性を送信します。APIキーまたはRESTエンドポイントが無効な場合は、設定を修正して連携を再接続してください。

トラブルシューティングの詳細については、[GrowSurf Braze連携ドキュメント](https://docs.growsurf.com/integrations/braze#troubleshooting)を参照してください。