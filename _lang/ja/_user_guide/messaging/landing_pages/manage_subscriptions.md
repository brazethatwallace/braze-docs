---
nav_title: 購読管理ブロック
article_title: 購読管理ブロック
description: "この記事では、Brazeランディングページに購読管理フォームブロックを追加・設定して、消費者がメール購読グループにオプトインおよび管理できるようにする方法について説明します。"
page_order: 5
---

# 購読管理ブロック {#manage-subscriptions-block}

> ランディングページに**購読管理**ブロックを追加して、ユーザーがメール購読グループを表示、オプトイン、更新できるようにします。

**購読管理**ブロックは、2つの主要なユースケースをサポートしています。

- **[既存の購読を管理する](#update-existing-subscriptions):** ランディングページの[Liquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)をメールやその他のチャネルメッセージで共有します。識別済みのユーザーがページを開くと、ブロックは各購読グループのチェックボックスに現在の購読状態を自動的に事前入力するため、ユーザーは設定を確認して更新できます。
- **[新しいオプトインを取得する](#capture-new-subscribers):** リードジェネレーションランディングページに**メールキャプチャ**ブロックと一緒にこのブロックを追加して、新しい訪問者がフォームを送信する際に参加する購読グループを選択できるようにします。

{% alert important %}
**購読管理**ブロックは[メール購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups)のみをサポートしています。SMS、RCS、またはWhatsApp購読グループはサポートされていません。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| メール購読グループ | 少なくとも1つの[メール購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups)が、[ダッシュボードから作成]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#create-a-subscription-group)されているか、[購読グループエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups)を使用して作成されている必要があります。 |
| ランディングページの権限 | ランディングページの作成および編集に必要な同じ[権限]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites)。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ1：購読管理ブロックを追加する {#step-1-add-the-manage-subscriptions-block}

ドラッグ＆ドロップランディングページエディターで、**ビルド**セクションに移動し、**フォームブロック**を選択します。**購読管理**をページ上の行にドラッグします。列幅に自動的に調整されます。

このブロックは、購読グループを追加するまで空の状態です。

## ステップ2: 購読グループを選択する {#step-2-select-the-subscription-groups}

**購読管理**ブロックを選択した状態で、右側の**ブロックプロパティ**パネルで**+ 購読グループを追加**を選択します。これにより、ワークスペースで利用可能な[メール購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups)のリストが表示されます。

含めたい各購読グループの横にあるチェックボックスを選択し、選択内容を確認してブロックに追加します。各購読グループは、ランディングページ上で個別に選択可能なチェックボックスとして表示されます。

{% alert note %}
**購読管理**ブロックには、明示的に追加したグループのみが表示されます。ブロックに購読グループを追加しても、訪問者が自動的にそのグループに購読登録されるわけではありません。訪問者がそのグループのチェックボックスを選択し、フォームを送信する必要があります。
{% endalert %}

## ステップ3：ブロック設定を構成する {#step-3-configure-the-block-settings}

**ブロックプロパティ**パネルを使用して、ブロックの動作と外観を調整します。

### 購読グループ {#subscription-groups}

- **グループの並べ替え：**購読グループのハンドルをドラッグして、ブロック内での表示順序を変更します。
- **グループの追加または削除：** **+ 購読グループを追加**を選択してグループを追加するか、グループの横にある削除アイコンを選択してブロックから削除します。

### 説明文を含める {#include-descriptions}

**説明文を含める**をオンにすると、各購読グループの説明テキストが名前の横に表示され、訪問者がオプトインする内容についてより多くの情報を得られるようになります。

### 「すべてに購読」チェックボックス {#subscribe-to-all-checkbox}

**「すべてに購読」チェックボックス**設定をオンにすると、ブロックにチェックボックスが追加されます。訪問者がこれを選択すると、ブロック内のすべての購読グループのチェックボックスが選択されます。一覧に表示されているすべてのグループにすばやくオプトインしたい場合に便利です。

## 既存の購読を更新する {#update-existing-subscriptions}

既存のユーザーがメールの購読を確認および更新できるようにするには、メール、キャンバスステップ、またはその他のメッセージで[Liquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)を使用してランディングページを共有します。ユーザーがそのリンクからページを開くと、Brazeがユーザーを識別し、**Manage Subscriptions**ブロック内の各購読グループのチェックボックスを現在の購読状態に合わせて自動的に事前入力します。これは[メールのユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)と同様の動作です。

ユーザーはチェックボックスを選択またはクリアして購読を更新し、フォームを送信して変更を保存できます。

{% alert note %}
**Manage Subscriptions**ブロックでユーザーの現在の購読状態を事前入力する機能はデフォルトで含まれており、[Landing Pages Proティア]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers)は必要ありません。これは、Landing Pages Proが必要な他のフォームフィールド向けの[Liquidベースの事前入力]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields)とは異なります。
{% endalert %}

## 新規購読者の獲得 {#capture-new-subscribers}

新規購読者を収集するには（例えば、リードジェネレーションのランディングページで）、**購読管理**ブロックと[メールキャプチャブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)を組み合わせて、消費者のメールアドレスと購読グループの選択を同時に取得します。

消費者が識別されていない場合（例えば、ランディングページのLiquidタグなしでアクセスした場合）、チェックボックスは未選択の状態で表示されます。フォームを送信すると、選択した購読グループに購読されます。

## 知っておくべきこと {#things-to-know}

- **SMS、RCS、WhatsAppの同意:** メールの代わりにランディングページでこれらのチャネルの同意を収集するには、[電話キャプチャブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)を使用してください。
- **確認エクスペリエンス:** **購読を管理**を含むフォームブロック付きのランディングページでは、送信後に確認エクスペリエンスが必要です。[確認ページを作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional)し、**送信**ボタンからリンクしてください。
- **エディターブロックリファレンス:** すべてのランディングページブロックとそのプロパティの完全なリファレンスについては、[エディターブロック（ランディングページ）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)を参照してください。