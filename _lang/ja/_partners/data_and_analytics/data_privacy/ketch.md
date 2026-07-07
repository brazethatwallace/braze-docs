---
title: Ketch
nav_title: Ketch
description: "このリファレンス記事では、BrazeとKetchの統合について説明します。Ketchは、簡素化されたプライバシー運用、完全でダイナミックなデータ制御、インテリジェンスを提供します。"
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com)は、企業がデータの責任ある管理者となることを可能にします。Ketchは、簡素化されたプライバシー運用、完全でダイナミックなデータ制御、インテリジェンスを提供します。

_この統合はKetchによって管理されます。_

## 統合について {#about-the-integration}

BrazeとKetchの統合により、Ketchユーザー設定センター内で顧客のコミュニケーション設定を管理し、これらの変更を自動的にBrazeに伝播できます。

{% alert note %}
購読グループの作成に関するガイダンスをお探しですか？<a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>SMS購読グループ</a> と<a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>メール購読グループ</a> の記事をご確認ください。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Ketchアカウント | この統合を有効にするには、管理者権限を持つ[Ketch](https://www.ketch.com)アカウントが必要です。 |
| Braze APIキー | `users.track`、`subscription.status.get`、`subscription.status.set`、`users.delete`、`users.alias.new`、`users.export.ids`、`email.unsubscribe`、`email.blacklist`の権限を持つBraze REST APIキー。<br><br> これはBrazeダッシュボード（**開発者コンソール** > **REST APIキー** > **新規作成**）で作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合 {#integration}

### ステップ 1:Brazeの接続をセットアップする {#step-1-set-up-the-braze-connection}

1. [Ketchインスタンス](https://app.ketch.com)で**Data Systems**に移動し、**Braze**を選択します。次に**New Connection**をクリックします。
2. Braze接続に識別可能な名前を付けます。この名前はAPIベースの処理でこの接続を参照するために使用されます。この接続のためのコードも作成されることに注意してください。このコードは、すべての接続において一意である必要があります。
3. ユーザーのIDマッピングを確認します。デフォルトでは、KetchはユーザーのメールアドレスまたはBrazeの`external_id`によってユーザーIDをマッピングします。
4. Braze APIキーを追加し、APIエンドポイントを指定します。この[APIエンドポイント]({{site.baseurl}}/api/basics/#endpoints)は、組織が使用しているBrazeインスタンスに基づいていることに注意してください。

### ステップ 2:サブスクリプション設定を構成する {#step-2-configure-subscription-preferences}

1. **Policy Center** > **Subscriptions**に移動します。**Policy Center**に**Subscriptions**タブが表示されない場合は、マーケティングユーザー設定センターにアクセスできることを確認し、製品のこの部分にアクセスするための正しいアカウント権限を持っていることを確認してください。
2. **Create New Subscription**をクリックして新しいトピックを作成します。各サブスクリプションには名前とコードがあります。
3. サブスクリプショントピックを送信するチャネルを追加します。各チャネルは、ユーザーのマーケティングユーザー設定センターに表示されます。また、Ketchユーザー設定センターで特定のオプトインシグナルまたはオプトアウトシグナルをオーケストレーションする方法の詳細を追加することもできます。
4. オプトインおよびオプトアウトシグナルのオーケストレーションに使用するBraze接続を選択します。
5. Ketchユーザー設定を送信するサブスクリプショングループのBraze `subscription_group_id`を入力します。

![BrazeサブスクリプショングループID。]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
ユーザーのオプトインおよびオプトアウトシグナルを収集しオーケストレーションするためには、IDが適切に設定されている必要があります。Ketchでは、この統合向けにユーザー設定シグナルをオーケストレーションするために、識別子としてメールを設定することをお勧めしています。
{% endalert %}


### ステップ 3:アイデンティティを設定する {#step-3-configure-identities}

ユーザーは、Ketchがそのユーザーのマーケティングユーザー設定アイデンティティを確認できる場合にのみ、マーケティングユーザー設定センターを表示できます。Ketchがユーザーのアイデンティティを適切にキャプチャできない場合、Ketchがユーザー設定を管理できないため、マーケティング設定ページはそのユーザーに表示されません。

1. マーケティングユーザー設定IDを設定するには、Ketchの**Settings**ページに移動し、**Identity space**をクリックします。新しいアイデンティティスペースを作成するか、既存のアイデンティティスペースを編集して、そのアイデンティティスペースをマーケティングユーザー設定IDとして割り当てる必要があります。プロパティにデプロイされているKetchタグが、そのアイデンティティスペースを適切にキャプチャしていることを確認してください。
2. **Experience Server** > **Properties**に移動し、目的のプロパティを編集します。そのプロパティのデータレイヤーで、カスタムアイデンティティスペースを有効にしてください。次に、このサイトでマーケティングユーザー設定IDをキャプチャする方法を設定します。
3. アイデンティティスペースを設定したら、KetchタグがデプロイされているWebサイトでユーザー設定センターを開いて、ユーザー設定センターが表示されるかどうかをテストします。