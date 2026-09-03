---
nav_title: 重複ユーザーの統合
article_title: 重複ユーザーの統合
description: "Brazeダッシュボードで重複ユーザーを見つけて統合する方法を説明します。"
page_order: 4
---

# 重複ユーザーの統合 {#merge-duplicate-users}

> 重複ユーザーを見つけて統合し、キャンペーンやキャンバスの効果を最大化する方法を説明します。

## REST API: ユーザーの識別と統合 {#rest-api-identify-and-merge-users}

このページのツールは、ダッシュボードで重複プロファイルを統合します。Brazeの[ユーザーデータエンドポイント]({{site.baseurl}}/api/endpoints/user_data)を使用して、プロファイルの結合や再ポイントも可能です。

- [POST: ユーザーの識別]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)（`/users/identify`）：エイリアスのみ、メールのみ、または電話番号のみのプロファイルを、`external_id`を持つプロファイルと結合します。
- [POST: ユーザーの統合]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)（`/users/merge`）：あるユーザープロファイルを別のプロファイルに統合します。両方のプロファイルがすでに`external_id`を持っている場合も含みます。このエンドポイントを呼び出す前に、[前提条件]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#prerequisites)と[マージの動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)を確認してください。

匿名プロファイルが既存の識別済みプロファイルと一致した場合（たとえばSDKの`changeUser()`呼び出しや`/users/identify`を通じて）、Brazeは匿名プロファイルを孤立させ、特定のフィールドのみを識別済みプロファイルにコピーします。詳細については、[匿名ユーザーを識別した場合の動作]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)を参照してください。

ユーザーの統合は元に戻すことが困難です。複数の`external_id`値にまたがる複雑な統合や大規模なプロファイル移行を計画している場合は、`/users/merge`に依存する前に、Brazeカスタマーサクセスマネージャーにガイダンスを求めてください。

Brazeは統合時に、削除対象としてマークされたユーザー、テストユーザー、グローバルコントロールグループユーザーの3種類のユーザーを異なる方法で処理します。詳細については、[ユーザーマージの動作]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior)を参照してください。

## 個別マージ {#individual-merging}

ユーザー検索で重複プロファイルが返された場合、Brazeダッシュボードのユーザープロファイルから各プロファイルを個別に統合できます。

### ステップ1: 重複プロファイルを検索する {#step-1-search-for-a-duplicate-profile}

Brazeで、**オーディエンス** > **ユーザー検索**を選択します。

![ナビゲーションメニューでハイライトされた「ユーザー検索」タイル。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

メールアドレスや電話番号などのユニーク識別子を入力して重複プロファイルを検索し、**検索**を選択します。

![Brazeダッシュボードの「ユーザー検索」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### ステップ2: 重複を統合する {#step-2-merge-duplicates}

統合プロセスを開始するには、**Merge duplicates**を選択します。

![重複ユーザーのプロファイルの1つ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

保持するユーザープロファイルと統合するユーザープロファイルを選択し、**Merge profiles**を選択します。すべての重複プロファイルが統合されるまで、このプロセスを繰り返します。


{% alert warning %}
重複ユーザープロファイルは、統合後に復元できません。
{% endalert %}

## 一括マージ {#bulk-merging}

重複ユーザーを一括マージすると、Brazeは一致する識別子（メールアドレスなど）を持つプロファイルを検索し、1つのプロファイルを保持します。Brazeはまず`external_id`を持つプロファイルを優先し、次に**Resolving ties**設定（**Resolve ties using**と**Prioritization**）を適用します。`external_id`を持つプロファイルがない場合、Brazeは`external_id`を持たないプロファイル全体に対して**Resolve ties using**と**Prioritization**を使用します。Brazeは、これらの設定で保持するプロファイルが1つに特定できる場合にのみユーザーを統合します。たとえば、**Resolve ties using**が**Updated date**で、両方のプロファイルの最終更新タイムスタンプが同じ場合、Brazeはタイブレークを解決できないため、それらのユーザーは統合されません。

### ステップ1: オーディエンスの管理に移動する {#step-1-go-to-manage-audience}

Brazeダッシュボードで、**オーディエンス** > **オーディエンスを管理**を選択します。

![ナビゲーションメニューでハイライトされた「オーディエンスを管理」タイル。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### ステップ2: 結果をプレビューする（オプション） {#step-2-preview-the-results-optional}

重複を統合する前に結果をプレビューするには、**Generate list of duplicates**を選択します。

![「Generate list of duplicates」がハイライトされた「オーディエンスを管理」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Brazeがプレビューを生成し、CSVファイルとしてメールアドレスに送信します。

CSVには**Created from**列が含まれており、各プロファイルが最初にどのように作成されたか（たとえば[SDK]({{site.baseurl}}/developer_guide/sdk_integration)、[REST API]({{site.baseurl}}/api/basics)、または[CSVインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)を通じて）を示します。これにより、重複を統合する前にプロファイルのソースを把握できます。

重複行を確認する際は、**Created from**を`external_id`、メールアドレス、電話番号などの識別子と比較してください。このコンテキストを使用して、**Merge all duplicates**を選択する前に、どのプロファイルをプライマリプロファイルとして保持すべきかを判断します。

**Created from**フィールドは、重複プロファイルに類似した値が含まれているが、異なる取り込みパスから作成された場合に特に役立ちます。チームがマージの判断を行うためのコンテキストを提供し、さらなるレビューが完了するまで別々に保持したいプロファイルの誤ったマージを減らすのに役立ちます。


次の例では、Brazeはユーザーのexternal IDを使用して重複プロファイルにフラグを付け、保持するプロファイルを特定します。これらのプロファイルが一括マージされた場合、Brazeはexternal IDを持つプロファイルをユーザーの新しいプライマリプロファイルとして使用します。

{% tabs local %}
{% tab CSVファイルの例 %}
| メールアドレス | External ID | 電話番号 | Braze ID | ルールの識別子 | 作成元 | 保持するプロファイル | 統合するプロファイル |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | ------------ | --------------- | ---------------- |
| jane.doe@example.com   | 123-external-id | 555 123-4567 | example-id-12345 | email               | sdk          | TRUE            | FALSE            |
| john.doe@example.com   |                 | 555 123-4567 | example-id-12346 | email               | rest         | FALSE           | TRUE             |
| jordan.doe@example.com |                 | 555 123-4567 | example-id-12347 | email               | csv          | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="ステップ2: 結果をプレビューする（オプション）" }
{% endtab %}
{% endtabs %}

#### マージの動作 {#merge-behavior}

Brazeは、保持されるプロファイルの空のフィールドを、統合されるプロファイルの値で埋めます。埋められるフィールドの一覧については、[マージの動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merge-behavior)を参照してください。

### ステップ3: 重複を統合する {#step-3-merge-your-duplicates}

プレビューの結果に問題がなければ、**Merge all duplicates**を選択します。

{% alert warning %}
重複ユーザープロファイルは、統合後に復元できません。
{% endalert %}


## ルールベースのマージ {#rules-based-merging}

ルールを使用して、マージ実行時に重複プロファイルの解決方法を制御し、最も関連性の高いユーザープロファイルを保持できます。ルールが設定されると、Brazeは条件に一致するプロファイルを保持します。

### ステップ1: ルールを定義する {#step-1-define-your-rules}

1. **オーディエンス** > **オーディエンスを管理** > **Edit rules**に移動します。
2. **Edit rules**パネルの**Profile to keep**セクションで、重複統合時に保持するプロファイルの**Identifier**を選択します。メールアドレスまたは電話番号を指定できます。
3. **Resolving ties**セクションで、**Profile to keep**の一致条件を持つプロファイル間のタイブレーク方法を決定する条件を選択します。以下を選択できます:<br>
- **Resolve ties using**: Created date、Updated date、Last session
- **Prioritization**: Newest、Oldest

![「Profile to keep」と「Resolving ties」のオプションを選択するセクションがある「Edit rules」パネル。]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

たとえば、電話番号を持つプロファイルを保持するように設定できます。複数のユーザーが同じ電話番号を持つ場合、**Updated date**フィールドを使用してタイブレークを解決し、最も最近更新されたユーザーを優先できます。

### ステップ2: 結果をプレビューする（オプション）

ルールを保存した後、**Generate a list of duplicates**を選択してルールの動作をプレビューできます。Brazeがプレビューを生成し、ルールが適用された場合にどのユーザーが保持され、統合されるかを示すCSVファイルをメールアドレスに送信します。

### ステップ3: 重複を統合する {#step-3-merge-duplicates}

プレビューの結果に問題がなければ、**オーディエンスを管理**ページに戻り、**Merge all duplicates**を選択します。

{% alert warning %}
重複ユーザープロファイルは、統合後に復元できません。
{% endalert %}

## スケジュールマージ {#scheduled-merging}

ルールベースのマージと同様に、スケジュールマージでは、事前設定されたルールを使用してユーザープロファイルの統合を毎日自動化できます。

![「schedule」ボタンがある「オーディエンスを管理」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

この機能を有効にすると、Brazeはユーザーの会社のタイムゾーンで毎日午前0時頃にマージプロセスを実行するタイムスロットを自動的に割り当てます。スケジュールマージはいつでも無効にできます。Brazeは、スケジュールされたマージが実行される24時間前にワークスペースの管理者に通知し、設定を確認するためのリマインダーと時間を提供します。

{% alert warning %}
重複ユーザープロファイルは、統合後に復元できません。
{% endalert %}

## 同じメールアドレスに複数のユーザープロファイルが関連付けられている理由 {#why-are-multiple-user-profiles-associated-with-the-same-email-address}

Brazeは、異なる識別子、インポート、または識別前の匿名セッションを通じてプロファイルが作成された場合、同じメールアドレスを共有する複数のユーザープロファイルを保存します。これは、ユーザーが単一の`external_id`を共有していない場合に想定される動作です。

重複を統合する前に、[識別子によるユーザープロファイルのエクスポートエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)を使用して、メールアドレスに対してどのプロファイルが存在し、各プロファイルにどのフィールドが含まれているかを確認してください。また、**オーディエンス** > **ユーザー検索**でメールアドレスを検索して、ダッシュボードで重複を確認することもできます。

## 関連記事 {#related-articles}

- [ユーザーマージの動作]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior)
- [POST: ユーザーの統合]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)
- [ユーザーの削除]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)