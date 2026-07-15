---
nav_title: ユーザーの削除
article_title: ユーザーの削除
page_order: 6
toc_headers: h2
description: "Brazeダッシュボードから直接、個々のユーザーまたはセグメントのユーザーを削除する方法を説明します。"
alias: /delete_users/
---

# ユーザーの削除 {#delete-users}

> Brazeダッシュボードから直接、個々のユーザーまたはセグメントのユーザーを削除する方法を説明します。

## 前提条件 {#prerequisites}

ユーザーを削除するには、管理者であるか、**Delete Users**権限を持っている必要があります。ユーザー削除レコードを表示するには、管理者であるか、**View User Deletion Records**権限を持っている必要があります。以下の権限がユーザーの削除と削除レコードを制御します。

| 権限 | 説明 |
|------------|-------------|
| Delete Users | ユーザーを個別または一括で完全に削除します。 |
| View User Deletion Records | ユーザー削除レコードを表示します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユーザー削除について {#about-user-deletion}

ユーザー削除を使用すると、不要になったプロファイル、誤って作成されたプロファイル、またはコンプライアンス（GDPRやCCPAなど）のために削除が必要なプロファイルを削除してデータベースを管理できます。

| 考慮事項 | 詳細 |
|---------------|---------|
| 最大サイズ | セグメントを削除する際、最大1,000万件のユーザープロファイルを削除できます。 |
| 待機期間 | すべてのセグメント削除には、7日間の待機期間と削除処理にかかる時間が必要です。 |
| ジョブの制限 | 一度に削除できるセグメントは1つのみで、7日間の待機期間が含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ユーザー削除について" }

## ユーザーの削除 {#deleting-users}

Brazeダッシュボードから[個々のユーザー](#delete-individual)または[セグメントのユーザー](#delete-segment)を削除できます。

### 個々のユーザーの削除 {#delete-individual}

Brazeから個々のユーザーを削除するには、**オーディエンス** > **ユーザーを検索**に移動し、ユーザーを検索して選択します。重複するユーザープロファイルを削除する場合は、正しいプロファイルを選択していることを確認してください。

![Brazeの「ユーザーを検索」ページ。]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:75%;"}

{% alert warning %}
単一ユーザーの削除は永続的です。削除後にプロファイルを復元することはできません。
{% endalert %}

プロファイルページで、<i class="fa-solid fa-ellipsis-vertical"></i> **Show options** > **Delete User**を選択します。ユーザーがBrazeで完全に削除されるまで数分かかる場合があります。


### セグメントの削除 {#delete-segment}

まだ作成していない場合は、削除したいユーザープロファイルを含む[セグメントを作成]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)してください。重複ユーザーを削除する場合は、すべてのユーザープロファイルを含めるようにしてください。

Brazeで、**Audience** > **Manage Audience**に移動し、**Delete Users**タブを選択します。

![Brazeダッシュボードの「Manage Audience」セクションにある「Delete Users」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

**Delete users**を選択し、削除するセグメントを選択してから、**Next**を選択します。

![削除するセグメントが選択されたポップアップウィンドウ。]({% image_buster /assets/img/audience_management/deleting_users/choose_segment_to_delete.png %}){: style="max-width:75%;"}

リクエストを確認するために**DELETE**と入力し、**Delete users**を選択します。

![確認ボックスに「DELETE」と入力された確認ページ。]({% image_buster /assets/img/audience_management/deleting_users/confirm_segment_delete.png %}){: style="max-width:75%;"}

このセグメントのユーザーはすぐには削除されません。代わりに、次の7日間は削除保留としてマークされます。この期間が過ぎると、ユーザーが削除され、メールで通知されます。

{% alert tip %}
セグメントの変更に関係なくこれらのユーザーが確実に削除されるように、**Pending Deletion**というセグメントフィルターが自動的に作成されます。このフィルターを[使用して]({{site.baseurl}}/user_guide/audience/segments/managing_segments#filters)、保留中の削除のステータスを確認できます。
{% endalert %}

## セグメント削除の確認 {#confirming-segment-deletions}

Brazeは、削除保留中のプロファイル数を記載した確認メールを送信します。

削除を続行するには、Brazeにログインして削除リクエストを確認してください。

メールに表示された期間内に確認しない場合、削除リクエストは期限切れとなり、処理されません。

## セグメント削除のキャンセル {#cancel}

保留中のセグメント削除をキャンセルするには7日間の猶予があります。キャンセルするには、**Audience** > **Manage Audience**に移動し、**Delete Users**タブを選択します。

![Brazeダッシュボードの「Manage Audience」セクションにある「Delete Users」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

保留中のセグメント削除の横にある<i class="fa-solid fa-eye"></i> **View details**を選択して、削除レコードの詳細を開きます。

![「Delete Users」タブの保留中のセグメント削除。]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

削除レコードの詳細で、**Cancel deletion**を選択します。

![「Delete Users」タブの「Deletion Record Details」ウィンドウ。]({% image_buster /assets/img/audience_management/deleting_users/deletion_record_details.png %}){: style="max-width:55%;"}

{% alert tip %}
一括ユーザー削除が進行中の場合、いつでもキャンセルできます。ただし、キャンセル前にすでに削除されたユーザーは復元できません。
{% endalert %}

## 削除ステータスの確認 {#status}

削除のステータスは、[セグメントフィルター](#segment-filters)、[オーディエンスの管理](#manage-audience)ページ、または[セキュリティイベントレポート](#security-event-report)を使用して確認できます。

### セグメントフィルター {#segment-filters}

ユーザーのセグメント削除をリクエストすると、**Pending Deletion**という[セグメントフィルター]({{site.baseurl}}/user_guide/audience/segments/managing_segments#filters)が自動的に作成されます。このフィルターを使用して以下のことができます。

- 特定の削除実行日に関連付けられた正確なユーザーセットを確認する。
- それらのユーザーをキャンペーンから除外して、削除前にメッセージを受信しないようにする。
- コンプライアンスや記録保持のためにリストをエクスポートする。

### オーディエンスの管理 {#manage-audience}

{% alert note %}
削除される正確なユーザーのリストを取得するには、代わりに[Pending Deletionセグメントフィルター](#segment-filters)を使用してください。
{% endalert %}

**Audience** > **Manage Audience**に移動し、**Delete Users**タブを選択します。

![Brazeダッシュボードの「Manage Audience」セクションにある「Delete Users」タブ。]({% image_buster /assets/img/audience_management/deleting_users/delete_users_tab.png %}){: style="max-width:85%;"}

このページでは、現在および保留中のすべての削除について、以下の一般情報を確認できます。

| フィールド | 説明 |
|-------|-------------|
| リクエスト日 | リクエストが最初に行われた日付です。**Pending Deletion**フィルターと組み合わせて、削除保留中のプロファイルのリストを取得できます。 |
| リクエスター | 削除リクエストを開始したユーザーです。 |
| セグメント名 | 削除保留中のユーザーを選択するために使用されたセグメントの名前です。 |
| ステータス | 削除リクエストが保留中、進行中、または完了のいずれであるかを示します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="オーディエンスの管理" }

特定のリクエストの詳細を確認するには、<i class="fa-solid fa-eye"></i> **View details**を選択して削除レコードの詳細を表示します。ここから[保留中のセグメント削除をキャンセル](#cancel)することもできます。

![「Delete Users」タブの保留中のセグメント削除。]({% image_buster /assets/img/audience_management/deleting_users/pending_deletion.png %})

### セキュリティイベントレポート {#security-event-report}

セキュリティイベントレポートをダウンロードして、過去の削除のステータスを確認することもできます。詳細については、[セキュリティ設定]({{site.baseurl}}/user_guide/administer/global/admin_settings/security_settings#security-event-report)を参照してください。

## よくある質問 {#faq}

### 1,000万人以上のユーザーを含むセグメントを削除できますか？ {#can-i-delete-segments-with-more-than-10-million-users}

いいえ。1,000万人以上のユーザーを含むセグメントは削除できません。このサイズのセグメントの削除についてサポートが必要な場合は、[Brazeサポート]({{site.baseurl}}/user_guide/administer/personal/braze_support)にお問い合わせください。

### 一度に削除できるのは最大1,000万人までです。これはバグですか？ {#i-can-only-delete-up-to-10-million-users-at-a-time-is-this-a-bug}

いいえ、これはバグではありません。1回のセグメント削除で削除できるユーザープロファイルの最大数は1,000万件です。

### 自動ユーザーマージはユーザー削除に影響しますか？ {#does-automated-user-merging-affect-user-deletion}

スケジュールされたマージに削除保留中のユーザープロファイルが含まれている場合、Brazeはそれらのプロファイルをスキップし、マージしません。これらのプロファイルをマージするには、削除から除外する必要があります。

### 削除保留中のユーザーに送信されたデータはどうなりますか？ {#what-happens-to-data-sent-to-users-pending-deletion}

外部システムやSDKから送信されたデータは引き続き受け入れられますが、ユーザーはアクティビティに関係なくスケジュール通りに削除されます。

### キャンバスやキャンペーンは削除保留中のユーザーに対してトリガーされますか？ {#do-canvases-and-campaigns-trigger-for-users-pending-deletion}

はい。ただし、**Pending Deletion** [セグメントフィルター](#segment-filters)を使用して、すべての削除保留中のユーザーを除外するセグメント包含フィルターを追加できます。

### 削除されたユーザープロファイルを復元できますか？ {#can-i-recover-deleted-user-profiles}

個々のユーザーの削除は永続的です。

最初の7日以内であれば[セグメント削除をキャンセル](#cancel)できます。ただし、キャンセル前にすでに削除されたユーザーは復元できません。

### ダッシュボードの代わりにAPIを使用してユーザーを削除できますか？ {#can-i-delete-users-with-the-api-instead-of-the-dashboard}

はい。少量のバッチの場合は、[`/users/delete`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)を使用できます。このエンドポイントはリクエストごとに最大50件の識別子を受け付け、そのエンドポイントの[レート制限]({{site.baseurl}}/api/endpoints/user_data/post_user_delete#rate-limit)が適用されます。セグメントベースのダッシュボード削除は非常に大規模なオーディエンスに適していますが、[7日間の待機期間](#about-user-deletion)が含まれます。