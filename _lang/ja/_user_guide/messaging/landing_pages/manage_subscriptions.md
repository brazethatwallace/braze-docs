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
**購読管理**ブロックは[メール購読グループ]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)のみをサポートしています。SMS、RCS、またはWhatsApp購読グループはサポートされていません。
{% endalert %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| --- | --- |
| メール購読グループ | 少なくとも1つの[メール購読グループ]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)が、[ダッシュボードから作成]({{site.baseurl}}/user_guide/channels/email/subscriptions#creating-a-subscription-group)されているか、[購読グループエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups)から作成されている必要があります。 |
| ランディングページの権限 | ランディングページの作成と編集に必要な同じ[権限]({{site.baseurl}}/user_guide/messaging/landing_pages#prerequisites)。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ1:購読管理ブロックを追加する {#step-1-add-the-manage-subscriptions-block}

ドラッグ＆ドロップランディングページエディターで、**ビルド**セクションに移動し、**フォームブロック**を選択します。**購読管理**をページの行にドラッグします。列幅に自動的に調整されます。

ブロックは、購読グループを追加するまで空の状態です。

## ステップ2:購読グループを選択する {#step-2-select-the-subscription-groups}

**購読管理**ブロックを選択した状態で、右側の**ブロックプロパティ**パネルで**+ 購読グループを追加**を選択します。ワークスペースで利用可能な[メール購読グループ]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-groups)のリストが表示されます。

含めたい各購読グループの横にあるチェックボックスを選択し、選択を確認してブロックに追加します。各購読グループは、ランディングページ上で個別の選択可能なチェックボックスとして表示されます。

{% alert note %}
**購読管理**ブロックには、明示的に追加したグループのみが表示されます。購読グループをブロックに追加しても、訪問者が自動的にそのグループに購読されるわけではありません。訪問者がグループのチェックボックスを選択してフォームを送信する必要があります。
{% endalert %}

## ステップ3:ブロック設定を構成する {#step-3-configure-the-block-settings}

**ブロックプロパティ**パネルを使用して、ブロックの動作と外観を調整します。

### 購読グループ {#subscription-groups}

- **グループの並べ替え:** 購読グループのハンドルをドラッグして、ブロック内の表示順序を変更します。
- **グループの追加または削除:** **+ 購読グループを追加**を選択してグループを追加するか、グループの横にある削除アイコンを選択してブロックから削除します。

### 説明を含める {#include-descriptions}

**説明を含める**をオンにすると、各購読グループの説明テキストが名前の横に表示され、訪問者がオプトインする内容についてより多くのコンテキストを得られます。

### 「選択をクリア」チェックボックス {#clear-selections-checkbox}

**「選択をクリア」チェックボックス**設定をオンにすると、ブロックに追加のチェックボックスが追加されます。訪問者がこれを選択すると、ブロック内のすべての購読グループチェックボックスが選択解除されます。これは、フォームを送信する前にリストされているすべてのグループからすばやくオプトアウトしたい場合に便利です。

### 「すべてに購読」チェックボックス {#subscribe-to-all-checkbox}

**「すべてに購読」チェックボックス**設定をオンにすると、ブロックに追加のチェックボックスが追加されます。訪問者がこれを選択すると、ブロック内のすべての購読グループチェックボックスが選択されます。これは、リストされているすべてのグループにすばやくオプトインしたい場合に便利です。

## 既存の購読を更新する {#update-existing-subscriptions}

既存のユーザーがメール購読を確認・更新できるようにするには、ランディングページの[Liquidタグ]({{site.baseurl}}/user_guide/messaging/landing_pages/tracking_users)を使用して、メール、キャンバスステップ、またはその他のメッセージでランディングページを共有します。ユーザーがそのリンクからページを開くと、Brazeはユーザーを識別し、**購読管理**ブロック内の各購読グループチェックボックスに現在の購読状態を自動的に事前入力します。これは[メールユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)と同様の動作です。

ユーザーはチェックボックスを選択またはクリアして購読を更新し、フォームを送信して変更を保存できます。

{% alert note %}
**購読管理**ブロックでのユーザーの現在の購読状態の事前入力はデフォルトで含まれており、[Landing Pages Proティア]({{site.baseurl}}/user_guide/messaging/landing_pages#plan-tiers)は必要ありません。これは、他のフォームフィールドの[Liquidベースの事前入力]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages#pre-fill-form-fields)とは異なり、Landing Pages Proが必要です。
{% endalert %}

## 新しい購読者を取得する {#capture-new-subscribers}

リードジェネレーションランディングページなどで新しい購読者を収集するには、**購読管理**ブロックを[メールキャプチャブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)と組み合わせて、消費者のメールアドレスと購読グループの選択を同時にキャプチャします。

消費者が識別されていない場合（たとえば、ランディングページのLiquidタグなしでアクセスした場合）、チェックボックスは未選択の状態で開始されます。フォームを送信すると、選択した購読グループに購読されます。

## 知っておくべきこと {#things-to-know}

- **SMS、RCS、WhatsAppの同意:** メールの代わりにこれらのチャネルの同意をランディングページで収集するには、[電話番号キャプチャブロック]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)を使用します。
- **確認エクスペリエンス:** **購読管理**を含むフォームブロックがあるランディングページには、送信後の確認エクスペリエンスが必要です。[確認ページを作成]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages#step-4-create-a-confirmation-page-optional)し、**送信**ボタンからリンクします。
- **エディターブロックリファレンス:** すべてのランディングページブロックとそのプロパティの完全なリファレンスについては、[エディターブロック（ランディングページ）]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=landing%20pages)を参照してください。