---
nav_title: マージの動作
article_title: ユーザーマージの動作
page_order: 1
page_type: reference
description: "削除対象としてマークされたユーザー、テストユーザー、グローバルコントロールグループユーザーに対して、Brazeがユーザーマージをどのように処理するかについて説明します。"
---

# ユーザーマージの動作 {#user-merge-behavior}

> デフォルトの動作が適用されない3つのユーザータイプ（削除対象としてマークされたユーザー、テストユーザー、グローバルコントロールグループユーザー）を含め、Brazeがユーザーマージをどのように処理するかについて説明します。

この動作は、[個別マージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#individual-merging)、[一括マージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#bulk-merging)、または[ユーザーマージAPIエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)のいずれを使用する場合でも、すべてのマージに適用されます。

## 一般的なマージの動作 {#general-merge-behavior}

2つのユーザープロファイルをマージすると、Brazeは保持するプロファイルの空のフィールドを、マージするプロファイルの値で埋めます。両方のプロファイルにフィールドの値がある場合、Brazeは保持するプロファイルの値を維持します。

たとえば、値が一方のプロファイルにのみ存在する場合、Brazeはその値を保持します。

| フィールド | マージするプロファイル | 保持するプロファイル | 結果のプロファイル |
|---|---|---|---|
| `first_name` | Alex | （空白） | Alex |
| `last_name` | （空白） | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

両方のプロファイルに同じフィールドの値がある場合、Brazeは保持するプロファイルの値を維持します。

| フィールド | マージするプロファイル | 保持するプロファイル | 結果のプロファイル |
|---|---|---|---|
| `first_name` | Alex | Al | Al |
| `last_name` | （空白） | Sterling | Sterling |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

この動作はデフォルト属性とカスタム属性に対してうまく機能します。ただし、Brazeは以下のユーザータイプについては異なる処理を行います。

## 動作の概要 {#behavior-summary}

| ユーザータイプ | 動作 | 理由 |
|---|---|---|
| 削除対象としてマークされたユーザー | マージしない | 削除対象としてマークされたプロファイルは7日以内に削除されるため、データを保持する必要がありません。 |
| テストユーザー | マージし、テストユーザーステータスを保持 | テストユーザーステータスを維持することで、マージ後も使用可能なテスト母集団を保持できます。 |
| グローバルコントロールグループユーザー | マージしない | マージするとランダムバケット番号が変更され、実験やレポートに影響を与えます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 削除対象としてマークされたユーザー {#users-marked-for-deletion}

[一括ユーザー削除ツール]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)を使用してセグメントを削除すると、Brazeはそれらのユーザープロファイルに7日以内の削除フラグを付けます。Brazeは、保持するプロファイルであってもマージするプロファイルであっても、削除対象としてマークされたプロファイルをマージしません。

削除対象としてマークされたプロファイルをマージする必要がある場合は、まず[セグメントの削除をキャンセル]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users#cancel)するか、ユーザーを削除対象から除外して、プロファイルのフラグを解除してください。

## テストユーザー {#test-users}

Brazeはテストユーザープロファイルのマージを許可し、結果のプロファイルにテストユーザーステータスを保持します。これは、保持するプロファイルの値を維持する[一般的なマージの動作](#general-merge-behavior)とは異なります。

以下の表は、各組み合わせにおけるテストユーザーステータスの結果を示しています。

| マージするプロファイル | 保持するプロファイル | 結果のプロファイル |
|---|---|---|
| テストユーザーではない | テストユーザーではない | テストユーザーではない |
| テストユーザー | テストユーザー | テストユーザー |
| テストユーザー | テストユーザーではない | テストユーザー |
| テストユーザーではない | テストユーザー | テストユーザー |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

テストユーザーの詳細については、[内部グループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)を参照してください。

## グローバルコントロールグループユーザー {#global-control-group-users}

Brazeは、保持するプロファイルであってもマージするプロファイルであっても、[グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)内のユーザープロファイルをマージしません。

グローバルコントロールグループのメンバーシップは、ユーザーの[ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)によって決定されます。マージすると、グループに属するユーザーが変更され、実験やレポートに影響を与えます。

## 関連記事 {#related-articles}

- [重複ユーザーのマージ]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users)
- [POST: ユーザーのマージ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge)
- [ユーザーの削除]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)
- [グローバルコントロールグループ]({{site.baseurl}}/user_guide/audience/global_control_group)
- [ランダムバケット番号]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers)
- [内部グループ]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups)