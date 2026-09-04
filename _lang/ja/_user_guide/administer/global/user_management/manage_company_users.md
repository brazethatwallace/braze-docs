---
nav_title: 会社ユーザー
article_title: 会社ユーザーの管理
page_order: 0
page_type: reference
description: "このページでは、ユーザーの追加や削除、ユーザー権限の設定、チームの作成、会社の設定の管理など、会社ユーザーの管理について説明します。"
---

# 会社ユーザーの管理 {#manage-company-users}

> 会社アカウントのユーザーの管理方法（ユーザーの追加、一時停止、削除など）について説明します。

## 会社ユーザーの追加 {#adding-company-users}

Braze アカウントにユーザーを追加するには、管理者権限が必要です。

新しいユーザーを追加するには:

1. **設定** > **会社設定** > **ユーザー管理** > **会社ユーザー** に移動します。
2. **+ 新しいユーザーを追加** を選択します。
3. メールアドレス、部署、[ユーザーロール]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#creating-a-role)など、求められた情報を入力します。
4. 管理者でないユーザーの場合、そのユーザーに付与する会社レベルおよびワークスペースレベルの[権限]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#edit-a-users-permissions)を選択します。

![カスタム権限フィールドのセクションがあるワークスペースレベルの権限。]({% image_buster /assets/img/add_new_user_3.png %})

### メールアドレスの要件 {#email-address-requirements}

[インスタンス]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)で使用されるすべてのメールアドレスは一意でなければなりません。つまり、そのインスタンスで会社ワークスペースへのアクセス権を持っていた、または現在も持っているユーザーにすでに関連付けられているメールアドレスを追加しようとすると、エラーメッセージが表示されます。

チームで Gmail を使用していて、メールアドレスの追加に問題が発生している場合は、メールアドレスに「+1」や「+test」のようにプラス記号（+）を追加してエイリアスを作成できます。たとえば、`contractor@braze.com` のエイリアスとして `contractor+1@braze.com` を作成できます。`contractor+1@braze.com` 宛のメールは引き続き `contractor@braze.com` に配信されますが、エイリアスは一意のメールアドレスとして認識されます。

エイリアスを使用せずに1つのアカウントを複数の会社で使用するには、[マルチ会社開発者の使用]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#use-multi-company-developers)を参照してください。SSO を使用している場合は、複数のメールアドレスで登録する前に、[シングルサインオン（SSO）に関する考慮事項]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account#considerations-for-single-sign-on-sso)を確認してください。

### Braze アカウントのメールアドレスを変更できますか？ {#can-i-change-my-braze-accounts-email-address}

セキュリティ上の理由から、ユーザーは Braze アカウントに関連付けられたメールアドレスを変更できません。メールアドレスを更新したい場合は、管理者が希望するメールアドレスで[新しいアカウントを作成](#adding-company-users)する必要があります。

## ユーザーアクセスと責任の割り当て {#assigning-user-access-and-responsibilities}

{% multi_lang_include permissions/differences.md content="Differences" %}

## 会社ユーザーの一時停止 {#suspending-company-users}

ユーザーを一時停止すると、そのアカウントは非アクティブ状態になり、ユーザーはログインできなくなりますが、アカウントに関連付けられたデータは保持されます。会社ユーザーの一時停止および一時停止の解除は、管理者のみが行えます。なお、一時停止中のユーザーも引き続きBrazeから通知を受け取る場合があります。

ユーザーを一時停止するには、**設定** > **会社設定** > **ユーザー管理** > **会社ユーザー**に移動し、対象のユーザー名を見つけて、<i class="fa-solid fa-user-lock" aria-label="ユーザーを一時停止"></i> **一時停止**を選択します。

![ユーザーを一時停止するオプション。]({% image_buster /assets/img_archive/suspend_user.png %})

管理者は、リストからユーザー名を選択し、フッターの**ユーザーを一時停止**を選択することでも一時停止できます。

![ユーザーの詳細を編集する際にユーザーを一時停止する。]({% image_buster /assets/img_archive/suspend_user2.png %}){: style="max-width:70%;"}

## 会社ユーザーの削除 {#deleting-company-users}

ユーザーを削除するには、**設定** > **会社の設定** > **ユーザー管理** > **会社ユーザー**に移動し、ユーザー名を見つけて、<i class="fa fa-trash-can"></i> **ユーザーを削除**を選択します。

会社ユーザーを削除できるのは管理者のみであり、会社ユーザーは自分自身のアカウントを削除することはできません。管理者は自分のダッシュボードアカウントを削除できないため、別の管理者が代わりに削除する必要があります。

![ユーザーの削除。]({% image_buster /assets/img_archive/delete_user_new.png %})

ユーザーが削除されると、Brazeは以下のアカウントデータを一切保持しません：

- ユーザーが持っていた属性
- メールアドレス
- 電話番号
- 外部ユーザー ID
- 性別
- 国
- 言語
- その他の類似データ

Brazeは以下のアカウントデータを保持します：

- アカウントに関連付けられたカスタム属性またはテストデータ
- ユーザーが作成したキャンペーンまたはキャンバス（ただし、**最終編集者**列などにユーザーの名前は表示されません）

### ダッシュボードユーザーの削除による影響 {#impact-of-deleting-a-dashboard-user}

ダッシュボードユーザーを削除しても、そのユーザーがダッシュボード内で作成したキャンペーン、セグメント、キャンバスなどのアセットに大きな影響はありません。ただし、これらのアセットの**作成者**フィールドには、削除されたユーザーのメールアドレスの代わりに「null」値が表示されます。

削除されたユーザーと同じメールアドレスで新しいダッシュボードユーザーが作成された場合、Brazeは削除されたユーザーが作成したアセットを新しいユーザーに再関連付けしません。新しいダッシュボードユーザーはまっさらな状態から始まり、ダッシュボード内の既存アセットの作成者としてクレジットされることはありません。

## トラブルシューティング {#troubleshooting}

### ユーザーを追加する際に「アクションを実行できません」と表示される {#unable-to-perform-action-when-adding-a-user}

ダッシュボードユーザーの追加が「アクションを実行できません」（または類似の）エラーで失敗する場合：

- メールアドレスの先頭や末尾にあるスペースや非表示文字を削除してください。
- そのアドレスが組織で有効なメール形式であることを確認してください。一部の特殊文字は拒否されます。
- 同じ[クラスター]({{site.baseurl}}/user_guide/administer/personal/accessing_your_account)内の2人のダッシュボードユーザーに同じメールアドレスを使用することはできません。そのアドレスが同じクラスター上の別のワークスペースに既に登録されている場合は、別のアドレスまたは `user+1@company.com` のようなエイリアスを使用してください。

### ユーザーを追加しようとすると「メールアドレスは既に使用されています」と表示される {#email-is-already-taken-when-trying-to-add-a-user}

新しいユーザーを追加しようとしてメールアドレスが既に使用されているというエラーが表示されるが、ユーザーリストにそのユーザーが見つからない場合、そのユーザーは同じBrazeダッシュボードクラスターの別のインスタンスに存在している可能性があります。

この新しいユーザーを作成するには、次のいずれかを行います：

1. 新しいインスタンスでユーザーを作成する前に、他のインスタンスからそのユーザーを削除する。
2. 別のメール文字列（`testing+01@braze.com` など）または別のメールエイリアスを使用してユーザーを作成する。

`testing+01@braze.com` を使用した際に受信トレイでメッセージのアクティベーションを受信しない場合は、その種類のメールアドレスからのメッセージを受信できるかどうかITチームに確認してください。一部の管理者は、`+` を含むメールアドレスに送信されたメッセージをフィルタリングしています。

## 次のステップ {#next-steps}

ユーザーを追加した後、アクセスを管理します:

{% article_tiles %}
- name: 権限
  link: /docs/user_guide/administer/global/user_management/permissions
  description: 各ユーザーがダッシュボードで実行できる操作を設定します。
- name: チーム
  link: /docs/user_guide/administer/global/user_management/teams
  description: 特定のダッシュボードオブジェクトへの共有アクセス権を持つグループにユーザーを整理します。
{% endarticle_tiles %}