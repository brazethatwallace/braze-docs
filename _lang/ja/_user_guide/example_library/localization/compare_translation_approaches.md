---
nav_title: 翻訳アプローチの比較
article_title: 多言語翻訳管理のアプローチを比較する
page_order: 1
page_type: reference
description: "手動Liquid、Content Blocks、カタログ、多言語メッセージ、翻訳パートナー、Connected Contentを比較して、Kitchenerieがローカライズされたコピーを管理する方法を選択します。"
tool:
  - Campaigns
  - Canvas
---

# 多言語翻訳管理のアプローチを比較する {#compare-approaches-for-managing-multi-language-translations}

> ローカライズされたコピーの保存、更新、プレビュー、送信の方法を評価し、QAワークフロー、チャネル構成、更新頻度に合ったローカライゼーションアプローチを選択できます。

## この例について {#about-this-example}

キッチン用品小売店のKitchenerieは、メール、プッシュ、アプリ内メッセージを英語、フランス語、ドイツ語で送信しています。マーケティングチームと開発チームは、キャンペーン全体で翻訳を管理するための再現可能でスケーラブルな方法を必要としています。

Brazeはいくつかのローカライゼーションパターンをサポートしています。

- **手動条件付きLiquid:** メッセージ本文に言語ごとのコピーを入力
- **Content Blocks:** 再利用可能なブロック（多言語翻訳タグの有無を問わず）
- **カタログ:** ロケールをキーとした構造化された翻訳行
- **多言語メッセージ:** 翻訳タグ、CSVアップロード、翻訳API（早期アクセス）
- **翻訳パートナー:** Smartling、Phrase、Lokaliseなど
- **Connected Content:** 送信時にCMSまたはAPIからフェッチされるローカライズされた文字列

この例ではトレードオフを比較し、QAワークフロー、チャネル構成、更新頻度、チームリソースに合ったアプローチを選択できるようにします。個別の方法のステップバイステップのセットアップを置き換えるものではありません。機能のウォークスルーについては、[ローカライゼーション]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)と[多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)から始めてください。

## 考慮事項 {#considerations}

- パターンを選択する前に、ダッシュボードプレビューとQA、プロフェッショナルな翻訳ワークフロー、高頻度のコンテンツ更新、またはリアルタイムのCMS駆動コピーが必要かどうかを決定してください。
- [多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)は、メール、プッシュ、バナー、アプリ内メッセージ、Content Blocksをサポートしています。SMSとWhatsAppは他のローカライゼーションパターンを使用します。手動Liquid、Content Blocks、カタログ、パートナー、Connected Contentは、それらの機能がサポートされているチャネル全体に適用できます。
- Brazeは翻訳を生成しません。ダッシュボード、CSV、API、カタログインポート、パートナーワークフロー、または外部CMSを通じてコピーを提供します。
- 手動Liquidと条件付きを埋め込んだContent Blocksは、言語が増えるにつれて命名規則とレビュープロセスが必要になります。多言語およびパートナーワークフローは更新を一元化しますが、CSVまたはAPIのメンテナンスが必要になる場合があります。
- Connected Contentと一部のパートナーフローは外部システムに依存します。送信時にAPIまたはCMSが利用できない場合、ローカライズされたコンテンツの読み込みに失敗する可能性があります。
- 重複は一般的です。たとえば、同じプログラム内でメール本文に多言語タグ、共有フッターにContent Blocks、商品コピーにカタログを使用する場合があります。

## 設定 {#setup}

### ステップ1: ローカライゼーション要件を把握する {#step-1-capture-your-localization-requirements}

| 要件 | 回答すべき質問 |
| --- | --- |
| プレビューとQA | マーケターは送信前にBrazeコンポーザーで各ロケールをプレビューする必要がありますか？ |
| スケール | 何言語に対応し、コピーはどのくらいの頻度で変更されますか？ |
| ワークフロー | 翻訳者のレビュー、修正、承認が必要ですか？ |
| データ形状 | コピーは自由形式のマーケティングテキストですか、それとも構造化された商品フィールド（名前、価格、URL）ですか？ |
| オートメーション | CMSが変更されたときに翻訳が自動的に更新される必要がありますか？ |
| チームスキル | チームはLiquid、CSVアップロード、API、またはパートナー連携を維持できますか？ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ローカライゼーション要件を把握する" }

### ステップ2: アプローチを一覧で比較する {#step-2-compare-approaches-at-a-glance}

| 観点 | 手動Liquid | Content Blocks | カタログ | 多言語メッセージ | 翻訳パートナー | Connected Content |
| --- | --- | --- | --- | --- | --- | --- |
| ダッシュボードプレビュー / QA | はい | はい | はい | はい | パートナーにより異なる | 限定的 — フェッチされたコンテンツのプレビューが困難 |
| デフォルト（連携なし） | はい | はい | 部分的 — カタログの設定が必要 | はい | いいえ — ベンダーの設定が必要 | いいえ — APIまたはCMSが必要 |
| チャネルカバレッジ | サポートされているすべてのチャネル | サポートされているすべてのチャネル | サポートされているすべてのチャネル | メール、プッシュ、バナー、アプリ内メッセージ、Content Blocks | パートナーにより異なる | サポートされているすべてのチャネル |
| 実装工数 | 低 | 低〜中 | 中 | 低 | 高（パートナー依存） | 中 |
| 継続的（BAU）工数 | 高 — メッセージごとの編集 | 中 — ブロックのメンテナンス | 中 — CSVまたはAPIの更新 | 中 — CSVアップロード | 中 — プラットフォーム内で管理 | 低 — 送信時にフェッチ |
| 高頻度更新 | いいえ | 部分的 | いいえ | 部分的 | はい | はい |
| プロフェッショナルな翻訳ワークフロー | いいえ | いいえ | いいえ | いいえ | はい | いいえ |
| 構造化 / 商品データ | 限定的 | 限定的 | はい — キー付きコピーに最適 | 限定的 | パートナーにより異なる | はい — 外部ソース経由 |
| 外部依存リスク | なし | なし | なし | なし | 中 | 中 — ソースがダウンすると送信が失敗 |
| 最適な用途 | 少数の言語、低頻度の更新 | メッセージ間の共有コンポーネント | 多数のロケールの構造化文字列 | 多言語でコピー＆ペーストの手間を削減 | 承認付きのエンタープライズ翻訳 | ダイナミックなCMS駆動のローカライゼーション |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="アプローチを一覧で比較する" }

### ステップ3: Kitchenerieスタイルのシナリオをアプローチに対応させる {#step-3-match-kitchenerie-style-scenarios-to-an-approach}

| Kitchenerieのシナリオ | 推奨される出発点 |
| --- | --- |
| 3言語、月に数回のキャンペーン、小規模なマーケティングチーム | 手動条件付きLiquidまたはLiquidを使用したContent Blocks |
| メールとIAM全体で共有されるヘッダー、フッター、法的ブロック | Content Blocks — ロケールが拡大する場合は[ブロックに多言語翻訳を保存]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#save-translations-in-content-blocks) |
| ロケールをキーとした商品名、プロモーション文、画像URL | [カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs) |
| 8つ以上のロケールでのメールとプッシュ（コンポーザープレビュー付き） | [多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) |
| 翻訳者ワークフローと承認を備えた中央TMS | [ローカライゼーションパートナー]({{site.baseurl}}/partners/message_personalization/localization)（例: SmartlingまたはPhrase） |
| 毎日更新されるCMSが所有するコピー | [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kitchenerieスタイルのシナリオをアプローチに対応させる" }

### ステップ4: 選択したアプローチを実装する {#step-4-implement-the-approach-you-selected}

1. **手動条件付きLiquid:** プロファイルの `language` またはロケール属性を `if` / `elsif` / `else` Liquidで使用します。[代替アプローチ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#alternative-approaches)と[条件付きロジック]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)を参照してください。
2. **Content Blocks:** 再利用可能なブロックを作成し、オプションでブロック内に条件付きLiquidを埋め込みます。[Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)と[翻訳されたメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages)のContent Blocksタブを参照してください。
3. **カタログ:** 翻訳行（例: `id`、`context`、`language`、`body`）をインポートし、Liquid `catalog_items`で参照します。[翻訳されたメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages)のカタログタブを参照してください。
4. **多言語メッセージ:** [ロケールを追加]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)し、コピーを翻訳タグで囲み、CSVをアップロードします。[翻訳エンドポイント]({{site.baseurl}}/api/endpoints/translations)への早期アクセスがある場合は、代わりにAPIで翻訳を更新できます。コンポーザーで**多言語ユーザー**を使用してプレビューします。
5. **翻訳パートナー:** ワークスペースのロケールを設定し、パートナー連携に従います（例: [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling)または[Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase)）。
6. **Connected Content:** 送信時にCMSまたは翻訳APIを呼び出します。十分にテストしてください。プレビューにはライブAPIレスポンスが反映されない場合があります。[Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を参照してください。

リージョン間のキャンバスとキャンペーンのオーケストレーション（1つのジャーニー対国ごとに1つのジャーニー）については、ローカライゼーションページの[翻訳管理]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management)を参照してください。

## 関連記事 {#related-articles}

- [ローカライゼーション]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [多言語メッセージ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [ローカライゼーション設定]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [ローカライゼーションパートナー]({{site.baseurl}}/partners/message_personalization/localization)
- [ローカライズされたメッセージのアクセシビリティ言語設定]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)