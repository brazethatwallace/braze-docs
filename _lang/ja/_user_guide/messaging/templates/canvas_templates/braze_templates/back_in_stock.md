---
nav_title: 再入荷
article_title: 再入荷
page_order: 2
page_type: reference
description: "この記事では、Brazeキャンバステンプレートを使用して、在庫切れだった商品が再入荷した際にパーソナライズされたメッセージでユーザーに通知し、購入を促進する方法について説明します。"
tool: Canvas
---

# 再入荷 {#back-in-stock}

> 再入荷テンプレートを使用して、以前閲覧したり関心を示したりした在庫切れ商品が購入可能になったユーザーをターゲットにしたメッセージを作成できます。これにより、商品が再び入手可能になった重要なタイミングでユーザーにアプローチし、欲しい商品を手に入れられるよう支援します。

この記事では、ユーザーライフサイクルのコンバージョンステップ向けに設計された**再入荷**テンプレートのユースケースについて説明します。完了すると、商品が再入荷した際にユーザーにプッシュ通知（Webまたはモバイル）、SMS、またはメールを送信し、最大2回のリマインダーを送信するキャンバスを作成できます。

## 前提条件 {#prerequisites}

このテンプレートを正しく使用するには、以下が必要です。

- 商品に関する情報を含む[カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- メッセージを送信したい商品に対して[再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)が設定されていること

## テンプレートをニーズに合わせてカスタマイズする {#tailoring-the-template-to-your-needs}

ここでは、スラックス、ジーンズ、キュロットなど、さまざまなパンツを専門とする消費者直販の衣料品小売業者PantsLabyrinthで働いているとしましょう。再入荷テンプレートを使用して、人気のジーンズ「Classic Straight Leg」が再入荷した際に、さまざまなチャネルで顧客に通知できます。

キャンバスを作成する前に、ストレートレッグパンツの在庫情報を含む[カタログを設定]({{site.baseurl}}/user_guide/data/activation/catalogs/create)し、Classic Straight Legジーンズの[再入荷通知を設定]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications#setting-up-back-in-stock-notifications)しました。ユーザーがアプリでClassic Straight Legジーンズをお気に入りに追加するカスタムイベントを実行した後に通知を購読するように設定しました。

再入荷テンプレートにアクセスするには、新しいキャンバスを作成する際に、**キャンバステンプレートを使用** > **Brazeテンプレート**を選択します。次に、**Back in Stock**の横にある**テンプレートを適用**を選択します。これで、テンプレートをニーズに合わせてカスタマイズできます。

### ステップ1: 詳細を設定する {#step-1-set-up-the-details}

キャンバスの詳細を目標に合わせて調整しましょう。

1. テンプレート名の横にある**編集**を選択します。

![キャンバスの現在のタイトルと説明。]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. キャンバス名を更新して、このキャンバスがClassic Straight Legの再入荷時にユーザーをターゲットにするものであることを明示します。
3. 説明を更新して、このキャンバスにパーソナライズされたメッセージが含まれていることを説明します。
4. **Promotional**タグの下にネストされている**Back in Stock**タグを追加して、キャンバスホームページでフィルタリングできるようにします。

![キャンバス名が「Back in Stock - Classic Straight Leg」で、簡単なキャンバス説明が記載された「キャンバスの詳細を設定」ステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### ステップ2: コンバージョンイベントを割り当てる {#step-2-assign-conversion-events}

**1次コンバージョンイベント - A**を**特定の購入を行う**に変更し、製品名として**Classic Straight Leg**を選択します。

![コンバージョン期限が7日間のClassic Straight Leg製品の購入というコンバージョンイベントタイプの「コンバージョンイベントの割り当て」セクション。]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### ステップ3: エントリスケジュールをカスタマイズする {#step-3-tailor-the-entry-schedule}

エントリスケジュールは**アクションベース**のままにして、ユーザーがアクションを実行した際にキャンバスに入るようにします。テンプレートでは既に**再入荷イベントを実行**に設定されています。

このステップでは2つの調整を行います。

1. Classic Straight Legジーンズの情報を含むカタログを選択します。ここでは「Straight Leg Pants」という名前にしています。

![アクションベースのキャンバスの「エントリスケジュール」ステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2. **開始時刻（必須）**を希望の開始日時に設定します。

![開始時間が2025年1月2日午前0時の「エントリウィンドウ」セクション。]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### ステップ4: ターゲットオーディエンスを選択する {#step-4-select-the-target-audience}

Classic Straight Legジーンズを購入する可能性が高いと思われるユーザーをターゲットオーディエンスとして定義します。

1. ターゲットセグメントの「Favorited - Classic Straight Leg Jeans」を選択します。これは、アプリまたはWebサイトでClassic Straight Legジーンズをお気に入りに追加したユーザーで構成されています。
2. 「Jeans」を「0」回より多く購入したユーザーを含めるフィルターを選択します。

![「Favorited - Classic Straight Leg Jeans」というセグメントが設定された「ターゲットオーディエンス」ステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3. エントリコントロールを調整して、キャンバスの最大期間後にユーザーがキャンバスに再エントリできるようにし、ユーザーが同じステップを同時にトリガーする可能性を防ぎます。

![キャンバスの最大期間でこのキャンバスへの再エントリを許可するチェックボックスがある「エントリコントロール」セクション。]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4. 終了条件を調整して、Classic Straight Legジーンズのお気に入り解除というカスタムイベントを実行したユーザーを除外します。

![「Unfavorited」のカスタムイベントを実行したユーザーの例外がある「終了条件」セクション。]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### ステップ5: 送信設定を選択する {#step-5-select-your-send-settings}

デフォルトの購読設定をそのまま使用し、メッセージや通知の受信を購読またはオプトインしたユーザーにのみ送信します。その他の設定（フリークエンシーキャップ、静寂時間、シードグループ）はスキップします。

![購読中またはオプトインしたユーザーをターゲットにする「送信設定」ステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### ステップ6: キャンバスをカスタマイズする {#step-6-customize-your-canvas}

次に、ユーザーに送信するチャネルとコンテンツをカスタマイズしてキャンバスを構築します。テンプレートの4つのチャネル（モバイルおよびWebプッシュ、SMS、メール）をすべて使用し、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel)フィルターを使用しているため、追加や削除は不要です。

{% alert tip %}
[キャンバスエントリプロパティ]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)を使用して、参照している製品に基づいてキャンバス内のメッセージをカスタマイズできます。
{% endalert %}

各メッセージステップを確認してコンテンツを更新することから、カスタマイズを始めましょう。

1. `!!YOURCATALOGHERE!!`をカタログ名（「Straight_Leg_Pants」）に置き換えます。
2. `[0]`をClassic Straight Legジーンズのインデックス番号「9」に置き換えます。このジーンズはカタログの`items`配列で10番目のアイテムです。（Liquidでは配列はゼロインデックスのため、最初のアイテムは`1`ではなく`0`です。）
3. 残りのすべてのメッセージステップについて、ステップ1と2を繰り返します。対象は以下の通りです。
    - 1日の遅延後に送信される「In-Product Msg & Email」メッセージ
    - 購入していないユーザーに送信される「Push+Email Alert」メッセージ
4. アクションパスステップを更新して、**Purchase**アクショングループを選択します。次に、**特定の購入を行う**を選択し、製品としてClassic Straight Legジーンズを選択します。

![製品が再入荷したことをユーザーに通知するメッセージが表示されたモバイルプッシュのキャンバスステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### ステップ7: キャンバスをテストして起動する {#step-7-test-and-launch-your-canvas}

キャンバスをテストおよび確認して期待通りに動作することを確認したら、**キャンバスを起動**を選択して起動します。これで、Classic Straight Legジーンズをお気に入りに追加し、メッセージングチャネルを購読しているユーザーは、再入荷時に通知を受け取ります！

{% alert tip %}
キャンバスの起動前後に考慮すべき事項については、[起動前後のチェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)をご確認ください。
{% endalert %}