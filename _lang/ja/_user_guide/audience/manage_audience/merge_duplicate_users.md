---
nav_title: 重複ユーザーの統合
article_title: 重複ユーザーの統合
description: "Brazeダッシュボードで重複ユーザーを見つけて統合する方法を説明します。"
page_order: 4
---

# 重複ユーザーの統合 {#merge-duplicate-users}

> 重複ユーザーを見つけて統合し、CampaignsやCanvasesの効果を最大化する方法を説明します。

{% alert tip %}
Braze REST APIを使用して重複ユーザーを統合するには、[POST: ユーザーの統合]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)を参照してください。
{% endalert %}

## 個別統合 {#individual-merging}

ユーザー検索で重複プロファイルが返された場合、Brazeダッシュボードのユーザープロファイルから各プロファイルを個別に統合できます。

### ステップ 1:重複プロファイルを検索する {#step-1-search-for-a-duplicate-profile}

Brazeで、**Audience** > **User Search**を選択します。

![ナビゲーションメニューでハイライトされた「User Search」タイル。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

メールアドレスや電話番号などのユニーク識別子を入力して重複プロファイルを検索し、**Search**を選択します。

![Brazeダッシュボードの「User Search」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### ステップ 2:重複を統合する {#step-2-merge-duplicates}

統合プロセスを開始するには、**Merge duplicates**を選択します。

![重複ユーザーのプロファイルの1つ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

保持するユーザープロファイルと統合するユーザープロファイルを選択し、**Merge profiles**を選択します。すべての重複プロファイルが統合されるまで、このプロセスを繰り返します。

![重複プロファイルの個別統合ページ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
重複ユーザープロファイルは、統合後に復元できません。
{% endalert %}

## 一括統合 {#bulk-merging}

重複ユーザーを一括統合すると、Brazeは一致する識別子（メールアドレスなど）を持つプロファイルを検索し、1つのプロファイルを保持します。Brazeはまず`external_id`を持つプロファイルを優先し、次に**Resolving ties**設定（**Resolve ties using**と**Prioritization**）を適用します。`external_id`を持つプロファイルがない場合、Brazeは`external_id`を持たないプロファイル全体に対して**Resolve ties using**と**Prioritization**を使用します。Brazeは、これらの設定で保持するプロファイルが1つに特定できる場合にのみユーザーを統合します。たとえば、**Resolve ties using**が**Updated date**で、両方のプロファイルの最終更新タイムスタンプが同じ場合、Brazeはタイブレークを解決できないため、それらのユーザーは統合されません。

### ステップ 1:オーディエンスを管理に移動する {#step-1-go-to-manage-audience}

Brazeダッシュボードで、**Audience** > **Manage Audience**を選択します。

![ナビゲーションメニューでハイライトされた「Manage Audience」タイル。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### ステップ 2:結果をプレビューする（オプション） {#step-2-preview-the-results-optional}

重複を統合する前に結果をプレビューするには、**Generate list of duplicates**を選択します。

![「Generate list of duplicates」がハイライトされた「Manage Audience」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Brazeがプレビューを生成し、CSVファイルとしてメールアドレスに送信します。

![生成されたCSVファイルへのリンクが含まれたBrazeからのメール。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

次の例では、Brazeはユーザーのexternal IDを使用して重複プロファイルにフラグを付け、保持するプロファイルを特定します。これらのプロファイルが一括統合された場合、Brazeはexternal IDを持つプロファイルをユーザーの新しいプライマリプロファイルとして使用します。

{% tabs local %}
{% tab CSVファイルの例 %}
| メールアドレス | External ID | 電話番号 | Braze ID | ルールの識別子 | 保持するプロファイル | 統合するプロファイル |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99   | (555) 123-4567 | 65fcaa547f470494d1370 | email               | TRUE            | FALSE            |
| alex@company.com |             | (555) 987-6543 | 65fcaa547f47d004d1348 | email               | FALSE           | TRUE             |
| alex@company.com |             | (555) 321-0987 | 65fcaa547f47d0049135c | email               | FALSE           | TRUE             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2: Preview the results (optional)" }
{% endtab %}
{% endtabs %}

#### 統合の動作 {#merge-behavior}

Brazeは、保持されるプロファイルの空のフィールドを、統合されるプロファイルの値で埋めます。埋められるフィールドの一覧については、[統合の動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior)を参照してください。

### ステップ 3:重複を統合する {#step-3-merge-your-duplicates}

プレビューの結果に問題がなければ、**Merge all duplicates**を選択します。

{% alert warning %}
重複ユーザープロファイルは、統合後に復元できません。
{% endalert %}

![「Merge all duplicates」がハイライトされた「Manage Audience」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## ルールベースの統合 {#rules-based-merging}

ルールを使用して、統合実行時に重複プロファイルの解決方法を制御し、最も関連性の高いユーザープロファイルを保持できます。ルールが設定されると、Brazeは条件に一致するプロファイルを保持します。

### ステップ 1:ルールを定義する {#step-1-define-your-rules}

1. **Audience** > **Manage Audience** > **Edit rules**に移動します。
2. **Edit rules**パネルの**Profile to keep**セクションで、重複統合時に保持するプロファイルの**Identifier**を選択します。メールアドレスまたは電話番号を指定できます。
3. **Resolving ties**セクションで、**Profile to keep**の一致条件を持つプロファイル間のタイブレーク方法を決定する条件を選択します。以下を選択できます:<br>
- **Resolve ties using**: Created date、Updated date、Last session
- **Prioritization**: Newest、Oldest

![「Profile to keep」と「Resolving ties」のオプションを選択するセクションがある「Edit rules」パネル。]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

たとえば、電話番号を持つプロファイルを保持するように設定できます。複数のユーザーが同じ電話番号を持つ場合、**Updated date**フィールドを使用してタイブレークを解決し、最も最近更新されたユーザーを優先できます。

### ステップ 2:結果をプレビューする（オプション）

ルールを保存した後、**Generate a list of duplicates**を選択してルールの動作をプレビューできます。Brazeがプレビューを生成し、ルールが適用された場合にどのユーザーが保持され、統合されるかを示すCSVファイルをメールアドレスに送信します。

### ステップ 3:重複を統合する {#step-3-merge-duplicates}

プレビューの結果に問題がなければ、**Manage Audience**ページに戻り、**Merge all duplicates**を選択します。

{% alert warning %}
重複ユーザープロファイルは、統合後に復元できません。
{% endalert %}

## スケジュール統合 {#scheduled-merging}

ルールベースの統合と同様に、スケジュール統合では、事前設定されたルールを使用してユーザープロファイルの統合を毎日自動化できます。

![「schedule」ボタンがある「Manage Audience」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

この機能を有効にすると、Brazeはユーザーの会社のタイムゾーンで毎日午前0時頃に統合プロセスを実行するタイムスロットを自動的に割り当てます。スケジュール統合はいつでも無効にできます。Brazeは、スケジュールされた統合が実行される24時間前にワークスペースの管理者に通知し、設定を確認するためのリマインダーと時間を提供します。

{% alert warning %}
重複ユーザープロファイルは、統合後に復元できません。
{% endalert %}