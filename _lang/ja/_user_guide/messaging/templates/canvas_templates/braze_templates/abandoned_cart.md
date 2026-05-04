---
nav_title: 放棄カート
article_title: 放棄カート
page_order: 1
page_type: reference
description: "この記事では、Braze Canvasテンプレートを使用して、ユーザーにリアルタイムでエンゲージし、購入を完了するよう促す方法について説明します。"
tool: Canvas
---

# 放棄カート {#abandoned-cart}

> ユーザーにリアルタイムでエンゲージし、購入を完了するよう促しましょう。このテンプレートを使用して、放棄カートについてユーザーにリマインドするタイムリーでパーソナライズされたメッセージの送信に焦点を当てたユーザージャーニーを作成します。製品のメリットを強調し、割引コードなどのインセンティブを提供できます。

この記事では、ユーザーライフサイクルの検討段階を対象とした**Abandoned Intent**テンプレートのユースケースについて説明します。この記事を読み終えると、カートにアイテムを追加した後に購入を完了していないユーザーに購入を促すユーザージャーニーをカスタマイズできるようになります。

## 前提条件 {#prerequisites}

このテンプレートを正しく使用するには、以下が必要です。

- このCanvasで購入するとユーザーがCanvasを退出するため、購入後のユーザージャーニー用の別のCanvas。
- 使用するパートナーとオーディエンスで設定済みの[Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/)。

## テンプレートをニーズに合わせてカスタマイズする {#tailoring-the-template-to-your-needs}

キッチン用品を専門とする小売ブランド「Kitchenerie」で働いていて、最新製品「Enormous Paper Plate」をカートに追加したが購入を完了していないユーザーに再エンゲージすることが目標だとしましょう。

Canvasを作成する前に、[Braze Audience Sync to Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/)インテグレーションを設定し、BrazeのユーザーデータをFacebookオーディエンスに追加して、行動トリガーやセグメンテーションなどに基づいた広告を配信できるようにします。

Abandoned Intentテンプレートにアクセスするには、新しいCanvasを作成する際に、**Use a Canvas template** > **Braze templates**を選択します。次に、**Abandoned Intent**の横にある**Apply Template**を選択します。これで、テンプレートをニーズに合わせてカスタマイズできます。

### ステップ 1:詳細を設定する {#step-1-set-up-the-details}

目標に合わせてCanvasの詳細を調整しましょう。

1. テンプレート名の横にある**Edit**を選択します。

![Canvasの現在のタイトルと説明。]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2. Canvas名を更新して、放棄カートのあるユーザーをターゲットにするCanvasであることを明示します。
3. 説明を更新して、最新の季節限定キッチン用品の発売から購入を完了するようユーザーに促すCanvasであることを明示します。
4. **Abandon Cart**タグを追加して、Canvasホームページでフィルタリングできるようにします。

![Canvasの新しい名前、説明、タグ。]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### ステップ 2:コンバージョンイベントを割り当てる {#step-2-assign-your-conversion-events}

次に、コンバージョンイベントを割り当てましょう。「Enormous Paper Plate」製品に焦点を当てているため、**Primary Conversion Event A**で以下を行います。

1. **Conversion event type**で**Makes Purchase**を選択します。
2. **Make a specific purchase**を選択します。これにより、特定の製品名を選択できます。
3. **Enormous Paper Plate**を選択します。

![1次コンバージョンイベント - A。コンバージョンタイプは「Makes Purchase」で、製品名は「Enormous Paper Plate」。コンバージョン期限は3日間。]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### ステップ 3:エントリスケジュールを設定する {#step-3-set-an-entry-schedule}

このテンプレートのエントリスケジュールは**API-Triggered**に設定されていますが、カート放棄（アクション）をしたユーザーに焦点を当てたいため、このCanvasではアクションベースのエントリの方が適しています。

1. エントリスケジュールタイプとして**Action-Based**を選択します。
2. トリガーとして**Abandoned Cart**を選択します。
3. エントリウィンドウで、開始時刻の日付を選択します。
4. ユーザーがローカルタイムゾーンでエントリできるオプションを選択します。これにより、メッセージングの関連性を保ち、最適な時間にメッセージが送信されることでエンゲージメントが向上する可能性があります。

![カート放棄したユーザーをターゲットにするアクションベースのCanvas。エントリウィンドウは2024年10月15日午後3時20分、ユーザーのローカルタイムゾーン。]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### ステップ 4:Canvasにエントリするユーザーを決定する {#step-4-determine-who-enters-the-canvas}

次に、過去90日間にオンラインのみで買い物をしたユーザーをターゲットオーディエンスとして定義しましょう。これにより、製品にエンゲージしていることがわかっているユーザーにオーディエンスを絞り込むことができます。

![このCanvasでターゲットにするユーザーのSegmentとして「Online Shoppers Segment - 90 Days」。]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

エントリコントロールはそのままにしておきます。ユーザーがこのCanvasに再エントリすることは許可されず、このCanvasにエントリできる人数に制限はありません。

退出条件として、「Enormous Paper Plate」を購入したユーザーはCanvasを退出します。これにより、すでに購入したアイテムに関するメッセージを受け取ることがなくなります。

![Enormous Paper Plateの特定の購入を行ったユーザーがCanvasを退出する退出条件。]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### ステップ 5:送信設定を選択する {#step-5-select-your-send-settings}

デフォルトのサブスクリプション設定をそのまま使用し、メッセージや通知の受信を購読またはオプトインしたユーザーにのみ送信します。その他の設定もそのままにしておきます。

### ステップ 6:Canvasをカスタマイズする {#step-6-customize-your-canvas}

次に、テンプレートのステップをカスタマイズしてCanvasを構築します。

1. アクションパスステップを選択し、**Made purchase**アクショングループ名を選択します。
2. **Make Purchase**で、**Make A Specific Purchase**を選択し、製品として**Enormous Paper Plate**を選択します。退出条件と同様に、この製品を購入したユーザーはCanvasを退出します。

![ユーザーがEnormous Paper Plateを購入した場合にCanvasを退出する「Made purchase」アクショングループ。]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3. メッセージステップで、**Edit message**を選択して、放棄カート内のアイテムについてユーザーに通知するメールをカスタマイズします。
4. 遅延ステップはそのままにしておきます。
5. オーディエンスパスステップに続くメッセージステップで、ユーザーが受け取るメールとSMSメッセージをカスタマイズします。ここで、パーソナライズされたメッセージングで製品の購入を促します。

![ユーザーが受け取るSMSメッセージのプレビュー：「こんにちは、Enormous Paper Plateがカートに残っています！今すぐ購入を完了して、ホスティングゲームをレベルアップしましょう。チェックアウト時にコードMYPLATEを使用すると、注文が20%オフになります！」]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6. 次のアクションパスステップで、**Made purchase**アクショングループを選択します。次に、**Make a specific purchase**を選択し、製品として**Enormous Paper Plate**を選択します。このステップは最初のアクションパスステップと同様に、製品を購入したユーザーを退出させ、それ以上のメッセージを受け取らないようにします。
7. Audience SyncステップがFacebookに同期するように設定されていることを確認します。これにより、広告のリターゲティングがさらに強化されます。

{% alert tip %}
[Canvasエントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)を使用して、参照している製品に基づいてCanvas内のメッセージをカスタマイズできます。
{% endalert %}

### ステップ 7:Canvasをテストして起動する {#step-7-test-and-launch-the-canvas}

Canvasをテストして確認し、期待どおりに動作することを確認したら、**Launch Canvas**を選択してCanvasを起動します。これで、パーソナライズされたユーザージャーニーでユーザーに的確にターゲティングし、カートに追加した製品のチェックアウトを促すことができます！

{% alert tip %}
Canvasの起動前後に考慮すべき事項については、[起動前後のチェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)をご確認ください。
{% endalert %}