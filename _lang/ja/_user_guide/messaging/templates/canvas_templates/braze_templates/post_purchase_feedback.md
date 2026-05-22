---
nav_title: 購入後フィードバック
article_title: 購入後フィードバック
page_order: 6
page_type: reference
description: "この記事では、Braze キャンバステンプレートを使用して、フィードバックに対応しユーザーとの関係を構築するパーソナライズされた体験をオーケストレーションする方法について説明します。"
tool: Canvas
---

# 購入後フィードバック {#post-purchase-feedback}

> 購入後フィードバックテンプレートを使用して、顧客がブランドとどのようにやり取りしているかについて重要なインサイトを得て、引き続きポジティブな体験を提供できるようにしましょう。パーソナライズされたコミュニケーションと構造化されたメッセージセットを活用することで、顧客との関係を継続的に構築し、育てることができます。

この記事では、ユーザーライフサイクルのコンバージョンステップ向けに設計された**購入後フィードバック**テンプレートのユースケースについて説明します。完了すると、ユーザーにアプリへのフィードバック提供を促すキャンバスが作成されます。

## 前提条件 {#prerequisites}

このテンプレートを正しく使用するには、以下が必要です。

- フィードバック調査結果を参照するための[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes)。
- 使用するパートナーとオーディエンスで設定済みの[Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/)。

## テンプレートをニーズに合わせてカスタマイズする {#tailoring-the-template-to-your-needs}

モバイルビデオゲーム開発会社 Decorumsoft で働いているとしましょう。購入後フィードバックテンプレートを使用して、最新のビデオゲーム「Proxy War 3: War of Thirst」のフィードバックを収集します。このフィードバックを使用して、拡張パック「Liquid Mirage」の開発計画に反映させます。

キャンバスを作成する前に、[Braze Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) インテグレーションを設定し、BrazeのユーザーデータをGoogle Audiencesに追加して、行動トリガー、セグメンテーションなどに基づいた広告を配信できるようにします。

購入後フィードバックテンプレートにアクセスするには、新しいキャンバスを作成する際に、**キャンバステンプレートを使用** > **Brazeテンプレート**を選択します。次に、**購入後フィードバック**の横にある**テンプレートを適用**を選択します。これで、テンプレートをニーズに合わせてカスタマイズできます。

### ステップ1:キャンバスの詳細を設定する {#step-1-set-up-canvas-details}

キャンバスの詳細を目標に合わせて調整しましょう。

1. テンプレート名の横にある**編集**を選択します。

![キャンバスの現在のタイトルと説明。]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2. キャンバス名を更新して、最近のユーザーをターゲットにするキャンバスであることを明示します。
3. 説明を更新して、ユーザーにフィードバックの送信を促すキャンバスであることを明示します。
4. **フィードバック**タグを追加して、キャンバスホームページでフィルタリングできるようにします。

![キャンバスの新しい名前と説明。新しい説明には「PWD3の今後の拡張パック Liquid Mirage への関心を測定するための購入後フィードバックキャンバス」と記載されています。]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### ステップ2:コンバージョンイベントを割り当てる {#step-2-assign-conversion-events}

次に、コンバージョンイベントを割り当てましょう。**1次コンバージョンイベント - A** を**特定の購入を行う**に更新し、**Proxy War** を選択します。

![Proxy War ゲーム製品の購入というコンバージョンイベントタイプの「コンバージョンイベントの割り当て」セクション。]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

最新のユーザーをターゲットにしたいため、テンプレートのコンバージョン期限である3日間をそのまま使用します。

### ステップ3:エントリスケジュールを設定する {#step-3-set-an-entry-schedule}

1. エントリスケジュールタイプを**アクションベース**のままにします。
2. エントリウィンドウの**開始時間**をゲームの発売日に設定します。

### ステップ4:キャンバスに入るユーザーを決定する {#step-4-determine-who-enters-the-canvas}

フィードバックのターゲットオーディエンスは、最近 Proxy War 3 を購入したユーザーです。

1. ターゲットセグメントの「Purchased Proxy War 3」を選択します。これはゲームを購入したユーザーで構成されています。
2. 「Proxy War 3」を「0」回より多く購入したユーザーを含めるフィルターを選択します。

![ゲームを購入したユーザーをセグメント化する「Purchased Proxy War 3」という名前のセグメント。]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3. エントリコントロールを更新して、キャンバスの最大期間後にユーザーがキャンバスに再エントリできないようにします。

### ステップ5:送信設定を選択する {#step-5-select-your-send-settings}

デフォルトのサブスクリプション設定をそのまま使用し、メッセージや通知の受信を購読またはオプトインしたユーザーにのみ送信します。

送信に配慮するため、**サイレント時間を有効にする**を選択して、ユーザーのタイムゾーンで午後11時から午前10時の間にフィードバックを要求しないようにし、次に利用可能な時間にのみ送信します。

![購読中またはオプトインしたユーザーをターゲットにする「送信設定」ステップ。サイレント時間がオンになっています。]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

この例では、その他の設定（フリークエンシーキャップとシードグループ）はスキップします。

### ステップ6:キャンバスをカスタマイズする {#step-6-customize-your-canvas}

次に、ユーザーに送信するメッセージングチャネルとコンテンツをカスタマイズしてキャンバスを構築します。メール、アプリ内メッセージ、Webhookチャネルのみを使用してフィードバックを収集するため、テンプレートを確認してメッセージステップからSMSバリアントを削除します。

各メッセージングコンポーネントを確認してコンテンツを更新することから、カスタマイズを始めます。参照するカスタム属性は `Experience Feedback` です。

1. キャンバスビルダーで、ユーザージャーニーの最初のメッセージステップを選択します。
2. **メール**バリアントを選択します。
3. ユーザーのフィードバックを促す件名で**送信情報**を入力します。
4. **メッセージを編集**を選択して、テンプレートのメールメッセージをフィードバック調査メッセージに置き換えます。これには、各コールトゥアクションのリンクを置き換えて、選択されたオプションをキャプチャすることが含まれます。これはユーザージャーニーのアクションパスステップで参照されます。

{% alert tip %}
[キャンバスエントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)を使用して、参照している製品に基づいてキャンバス内のメッセージをカスタマイズできます。
{% endalert %}

#### フィードバック調査を設定する {#set-up-feedback-survey}

次に、**アプリ内メッセージ**バリアントの詳細を入力する必要があります。ここで、ユーザーフィードバックのセンチメントを示す `Experience Feedback` カスタム属性を指定する必要があります。（これは後続のアクションパスステップでも参照します。）

1. 同じ最初のメッセージステップで、**In-App Messages** バリアントを選択します。メッセージコントロールはそのままにします。
2. ヘッダーと本文には、ユーザーに Proxy War 3 の体験について正直に回答するよう促す文言を使用します。
3. 調査の回答をプロファイルに記録したいため、調査を**単一選択**および**送信時に属性を記録**のままにします。
4. 3つの調査選択肢それぞれについて、カスタム属性として **Experience Feedback** を選択します。
5. これらの値はカスタム属性と一致しているため、ユーザープロファイルの属性値はそのままにします。

![ユーザーに最近の Proxy War 3 の購入を楽しんだかどうかを尋ねる調査。「とても気に入った」、「まあまあだった」、「自分には合わなかった」の3つの選択肢があります。]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### アクションパスを構築する {#build-out-the-action-path}

カスタム属性 `Experience Feedback` と前のセクションの属性値を使用して、テンプレートのアクションパスを属性と値に合わせて更新します。

![調査で「とても気に入った」と回答したユーザーを含むアクションパスステップの「良いフィードバック」グループ。]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### 広告リターゲティングを設定する {#set-up-ad-retargeting}

**広告リターゲティング**ステップでGoogle Audience Syncが設定されていることを確認します。これには、広告アカウント、既存のオーディエンス、およびオーディエンスにユーザーを追加するオプションの選択が含まれます。

### Webhookサポートケースを設定する {#set-up-webhook-support-cases}

次に、潜在的なサポートケースをトリガーするWebhookを設定しましょう。これは、ユーザーフィードバックの分析と組み合わせると特に有益なインサイトを得ることができます。

**サポートケース作成**という名前のメッセージステップで、購入に不満があり返金を希望するユーザー向けのWebhookを作成するようにテンプレートを更新します。

![Proxy War 3 の購入に対してネガティブなセンチメントを持ち、返金を希望する顧客のサポートケースを作成するWebhook。]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### ステップ6:キャンバスをテストして起動する {#step-6-test-and-launch-the-canvas}

キャンバスをテストして確認し、期待どおりに動作することを確認したら、**キャンバスを起動**を選択してキャンバスを起動します。これで、Proxy War 3 の最近の購入に基づいてフィードバック調査への回答を促す、パーソナライズされたユーザージャーニーでユーザーを配慮を持ってターゲティングできます！

{% alert tip %}
キャンバスを起動する前後に考慮すべき事項については、[起動前後のチェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)をご確認ください。
{% endalert %}