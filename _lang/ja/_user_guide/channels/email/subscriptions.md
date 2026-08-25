---
nav_title: "サブスクリプション"
article_title: "サブスクリプション"
page_order: 5
description: "このリファレンス記事では、さまざまなユーザーの購読状態、メール購読の管理方法、および購読に基づいてユーザーをセグメント化する方法について説明します。"
channel:
  - email

---

# メールのサブスクリプション {#email-subscriptions}

> グローバルなメール購読状態、フッターと購読解除ページ、ユーザー設定センター、およびキャンペーンのターゲティングについて説明します。すべてのチャネルにわたる購読グループについては、[購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups)を参照してください。

この文書は情報提供のみを目的としています。いかなる形でも法的助言を提供することを意図しておらず、また法的助言として依拠することはできません。マーケティングメールやトランザクションメールの送信は、特定の法的要件の対象となる場合があります。お客様の会社に適用されるすべての法律、規則、規制を遵守していることを確認するために、法務顧問や規制コンプライアンスチームに助言を求めてください。

## 購読状態 {#subscription-states}

Brazeはグローバル購読状態を使用して、メールを受信するユーザーを制御します。`opted-in`、`subscribed`、`unsubscribed` の定義、グローバルステータスと購読グループの違い、他のチャネルでの購読ステータスの仕組みについては、[購読ステータス]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#email)を参照してください。

### 配信停止されたメールアドレス {#unsubscribed-email-addresses}

Brazeは、[カスタムフッター]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer)を通じて手動で配信停止したユーザーを自動的に配信停止にします。ユーザーがメールアドレスを更新し、**送信設定**で**ユーザーがメールを更新したときに再購読する**が有効になっている場合、通常の送信が再開されます。

ユーザーがメールの1つ以上をスパムとしてマークした場合、Brazeはそのユーザーにトランザクションメールのみを送信します。トランザクションメールとは、**ターゲットオーディエンス**の**配信停止ユーザーを含むすべてのユーザーに送信**オプションを指します。

{% alert tip %}
ユーザーを効果的に再エンゲージする方法については、[IPウォームアップ]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)のベストプラクティスを参照してください。
{% endalert %}

### バウンスと無効なメール {#bounces-and-invalid-emails}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} {% multi_lang_include analytics/metrics.md metric='Soft Bounce' %}

メールアドレスがハードバウンスした場合、Brazeはユーザーの購読状態を自動的に「配信停止」に設定しません。アドレスがハードバウンスした場合（無効または存在しない場合）、Brazeはそのアドレスを無効としてマークし、それ以上の送信を試みません。ユーザーがメールアドレスを変更した場合、Brazeは送信を再開します。Brazeはソフトバウンスを72時間再試行します。

### メールの購読状態の更新 {#updating-email-subscription-states}

ユーザーのメール購読状態を更新するには、4つの方法があります。

#### SDK統合 {#sdk-integration}

Braze SDKを使用して、ユーザーの購読状態を更新します。

#### REST API

[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、ユーザーの[`email_subscribe`属性]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)を更新します。たとえば、ユーザーがカスタム配信停止リンクを使用した際にメールの購読状態を配信停止に設定するには、リクエストのユーザー属性に `email_subscribe: "unsubscribed"` を含めます。

#### ユーザープロファイル {#user-profile}

1. **ユーザー検索**でユーザーを見つけます。
2. **エンゲージメント**で、**配信停止**、**購読中**、または**オプトイン**を選択して、ユーザーの購読ステータスを変更します。

ユーザープロファイルには、ユーザーの購読が最後に変更されたタイムスタンプも表示されます。タイムスタンプは、状態が**オプトイン**または**配信停止**の場合に記録されますが、**購読中**の場合は記録されません。たとえば、明示的にオプトインもオプトアウトもしたことがない新しく作成されたプロファイルには、購読のタイムスタンプがありません。

#### ユーザー設定センター {#preference-center}

メールの下部に[ユーザー設定センター](#email-preference-center)のLiquidを含めて、ユーザーがオプトインまたはオプトアウトできるようにします。Brazeはユーザー設定センターからの購読状態の更新を管理します。

### メールの購読状態の確認 {#checking-email-subscription-state}

![John Doeのユーザープロファイル。メールの購読状態が「購読中」に設定されています。]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

ユーザーのメール購読状態は、以下の方法で確認できます。

1. **REST APIエクスポート:** [セグメントごとのユーザーエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)または[識別子ごとのユーザーエクスポート]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)エンドポイントを使用して、個々のユーザープロファイルをJSON形式でエクスポートします。
2. **ユーザープロファイル:** [ユーザー検索]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)ページでユーザーのプロファイルを見つけ、**エンゲージメント**タブを選択してユーザーの購読状態を表示および手動で更新します。

ユーザーがメールアドレスを更新すると、購読状態は購読中に設定されます。更新されたメールアドレスがBrazeワークスペース内の別の場所にすでに存在する場合、ユーザーはその既存ユーザーの購読状態を引き継ぎます。ただし、**送信設定**で**ユーザーがメール設定を更新したときに再購読する**が有効になっている場合は除きます。

購読状態の変更をトラブルシューティングするには、ユーザープロファイルログの**メール購読状態の変更**で履歴とソースを確認してください。以下のソースがメール購読状態の変更をトリガーする可能性があります。

| ソース | 説明 |
| ------ | ----------- |
| SDK | Braze SDKを通じて送信されたユーザー属性の更新 |
| REST API | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントを通じて送信されたユーザー属性の更新 |
| ダッシュボード | ユーザープロファイルページで手動で変更された購読状態 |
| CSVインポート | ユーザーCSVインポート時に設定された購読状態 |
| ユーザー設定センター | Brazeがホストするユーザー設定センターからユーザーが設定を更新 |
| 購読ページ | ユーザーがメール内の配信停止リンクを選択し、Brazeの購読ページに遷移 |
| List-Unsubscribe | ユーザーがメールクライアントのネイティブList-Unsubscribeヘッダーを通じて配信停止 |
| キャンバスのユーザー更新ステップ | キャンバスの[ユーザー更新ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update)によって更新された購読状態 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="メール購読状態の更新ソース" }

ユーザーのグローバルメール購読状態が変更されると、Brazeはその状態を同じメールアドレスを共有する他のプロファイルに伝播します（変更ごとに最大100プロファイル）。同じメールアドレスを共有するプロファイルが100を超える場合、Brazeは伝播を保証しません。同じメールアドレスを共有するユーザーが異なる購読状態を示す場合は、Brazeサポートにお問い合わせください。

## 購読グループ {#subscription-groups}

メール購読グループを使用すると、ユーザーはグローバルなメール購読ステータスを変更することなく、特定のメールカテゴリ（ニュースレターやプロモーションなど）のオプトインまたはオプトアウトができます。作成したグループは[ユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)に追加できます。

グループの作成、セグメンテーション、アーカイブ、チャネル固有の動作について詳しくは、[購読グループ]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_groups#email-subscription-groups)を参照してください。

## メール設定センター {#email-preference-center}

メール設定センターを使用すると、どのユーザーが購読グループのニュースレターを受信するかを管理できます。ダッシュボードの **Subscription Groups** から確認できます。作成した各購読グループは、設定センターのリストに追加されます。

設定センターの追加またはカスタマイズの詳細については、[ユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)を参照してください。

## メールサブスクリプションの変更 {#changing-email-subscriptions}

ほとんどの場合、ユーザーは受信したメールに含まれるリンクを通じてメールサブスクリプションを管理します。すべてのメールの下部に、購読解除リンクを含む法的に準拠したフッターを挿入してください。ユーザーが購読解除URLを選択すると、Brazeはそのユーザーの購読を解除し、変更を確認するランディングページを表示します。このLiquidタグを含めてください: {%raw%}`${set_user_to_unsubscribed_url}`{%endraw%}。

{% alert note %}
{%raw%}`${set_user_to_unsubscribed_url}`{%endraw%} Liquidタグは、メールキャンペーンとキャンバスでのみ使用できます。他のメッセージングチャネルではこのタグを使用できません。
{% endalert %}

ユーザーがユーザー設定センターで「上記のすべてのメールタイプの配信を停止する」を選択すると、Brazeはそのユーザーのグローバルメールサブスクリプションステータスを`unsubscribed`に設定し、すべてのグループから購読解除します。

受信者側のメール購読解除（購読解除リンク、list-unsubscribe、ユーザー設定センターの送信、メールサービスプロバイダー (ESP) が報告した購読解除）は、Snowflakeの`USERS_MESSAGES_EMAIL_UNSUBSCRIBE`テーブルに表示されます。REST APIを通じて行われた購読解除はこのテーブルには含まれません。それらの場合は、代わりに[`users.behaviors.subscriptiongroup.StateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#subscription-group-state-change-events)または[`users.behaviors.subscription.GlobalStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#global-subscription-state-change-events)イベントが発行されます。テーブルスキーマについては、[USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_MESSAGES_EMAIL_UNSUBSCRIBE_SHARED)を参照してください。

### カスタムフッターの作成 {#custom-footer}

デフォルトのフッターを使用したくない場合は、ワークスペース全体のカスタムメールフッターを作成し、{% raw %}`{{${email_footer}}}`{% endraw %}を使用してすべてのメールにテンプレート化します。

これにより、メールテンプレートやメールキャンペーンごとに新しいフッターを作成する必要がなくなります。手順については、[カスタムメールフッター]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer)を参照してください。

#### 中国のIPアドレスに対するサブスクリプション状態の管理 {#managing-subscription-states-for-chinese-ip-addresses}

中国のIPアドレスが予想される場合は、`unsubscribed`リストの維持を購読解除リンクのみに頼らないでください。サポートチケットやカスタマー担当者のメールなど、代替の購読解除手段を提供してください。

### カスタム購読解除ページの作成 {#creating-a-custom-unsubscribe-page}

ユーザーがメール内の購読解除URLを選択すると、サブスクリプションの変更を確認するデフォルトのランディングページが開きます。

代わりにカスタムランディングページを使用するには:

1. **メール設定** > **購読ページおよびフッター**に移動します。
2. カスタムページのHTMLを追加します。

再購読リンク（例: {% raw %}`{{${set_user_to_subscribed_url}}}`{% endraw %}）を含めて、ユーザーが誤った購読解除を元に戻せるようにしてください。{% raw %}`${set_user_to_unsubscribed_url}`{% endraw %}と同様に、このタグはメールキャンペーンとキャンバスでのみ使用できます。

また、ユーザーをサイトに誘導し、Braze REST APIでステータスを更新することもできます（例: {% raw %}`?user_id={{${user_id}}}`{% endraw %}を含むリンクを使用し、[`/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status)を呼び出します）。

{% alert note %}
HTMLコンテンツブロックのみではなくダッシュボードフッターを使用する場合、テンプレートには保存するために{% raw %}`{{${set_user_to_unsubscribed_url}}}`{% endraw %}が含まれている必要があります。一時的に別の購読解除URLを使用するには、デフォルトのタグをコメントアウトできます。例: {% raw %}`<!-- {{${set_user_to_unsubscribed_url}}} -->`{% endraw %}。
{% endalert %}

![「お別れは残念です！」というプレビューが表示されたカスタム購読解除ページ。]({% image_buster /assets/img/custom_unsubscribe.png %})

### カスタムオプトインページの作成 {#creating-a-custom-opt-in-page}

カスタムオプトインページを使用して、ユーザーがサブスクリプション前に通知設定を確認および管理できるようにします。この追加のコミュニケーションにより、メールキャンペーンがスパムフォルダーに入るのを防ぐことができます。

1. **設定** > **メール設定**に移動します。
2. **購読ページおよびフッター**を選択します。
3. **カスタムオプトインページ**セクションでスタイルをカスタマイズして、ユーザーに購読されたことがどのように表示されるかを確認します。

ユーザーは{% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}タグを通じてこのページにアクセスします。他のメールサブスクリプションLiquidタグと同様に、このタグはメールキャンペーンとキャンバスでのみ使用できます。

{% alert tip %}
ダブルオプトインプロセスを使用して、アウトリーチを改善しましょう。Brazeは追加の確認メールを送信し、ユーザーはリンクを通じて通知設定を確認します。確認後、ユーザーはオプトインされます。
{% endalert %}

![「引き続きご連絡をお待ちいただけて嬉しいです」というメッセージが表示されたカスタムオプトインメール。]({% image_buster /assets/img/custom_optin.png %})

## サブスクリプションとキャンペーンターゲティング {#subscriptions-and-campaign-targeting}

デフォルトでは、Brazeはプッシュまたはメールメッセージを含むキャンペーンを、購読中またはオプトインのユーザーにターゲティングします。**ターゲットオーディエンス**で**これらのユーザーに送信:**の横にあるドロップダウンを選択して変更します。

Brazeは3つのターゲティング状態をサポートしています。

- 購読中またはオプトインのユーザー（デフォルト）。
- オプトインのユーザーのみ。
- 配信停止したユーザーを含むすべてのユーザー。

{% alert important %}
これらのターゲティング設定を使用する際は、適用される[スパム法]({{site.baseurl}}/help/best_practices/spam_regulations#spam-regulations)を遵守する責任があります。
{% endalert %}

## ユーザーサブスクリプションによるセグメント化 {#segmenting-by-user-subscriptions}

「メールサブスクリプションステータス」および「プッシュサブスクリプションステータス」フィルターを使用して、サブスクリプションステータスでユーザーをセグメント化します。

これを使用して、オプトインもオプトアウトもしていないユーザーをターゲットにし、明示的なオプトインを促します。「メール/プッシュサブスクリプションステータスが購読中」のフィルターでセグメントを作成し、購読中だがオプトインしていないユーザーにキャンペーンを送信します。

![セグメントフィルターとして使用されているメールサブスクリプションステータス。]({% image_buster /assets/img_archive/not_optin.png %})