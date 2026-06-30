---
nav_title: 機能導入
article_title: 機能導入
page_order: 3
page_type: reference
description: "この記事では、Braze Canvasテンプレートを使用して、メリットや使い方のヒントを強調するタイムリーでパーソナライズ済みのメッセージを配信する方法について説明します。"
tool: Canvas
---

# 機能導入 {#feature-adoption}

> このテンプレートは、新機能、既存製品、追加サービス、その他顧客に体験してもらいたいあらゆる領域の利用を促進するために設計されています。パーソナライズされたコミュニケーションと構造化されたメッセージセットを活用することで、ユーザーにシームレスに新機能を紹介し、貴重なフィードバックを収集できます。

この記事では、ユーザーライフサイクルのリテンションおよびロイヤルティ段階を対象とした**機能導入**テンプレートのユースケースについて説明します。この記事を読み終えると、ユーザーに新機能の利用を促し、ユーザーの感想を収集するユーザージャーニーをカスタマイズできるようになります。

## 前提条件 {#prerequisites}

このテンプレートを正しく使用するには、ユーザーが機能を使用したタイミングを参照する[カスタムイベント]({{site.baseurl}}/user_guide/data/activation/events/custom_events)が必要です。

## テンプレートをニーズに合わせて調整する {#tailoring-the-template-to-your-needs}

例として、フードデリバリーアプリ「Calorie Rocket」で働いていて、定期的なフードデリバリーをスケジュールする機能「Cruise Control」を最近リリースし、より多くのユーザーにこの新機能を導入してもらいたいとします。この例では、カスタムイベント`scheduled_delivery`を使用して、ユーザーがCruise Control機能を試したタイミングを追跡します。

テンプレートにアクセスするには、新しいキャンバスを作成する際に、**キャンバステンプレートを使用** > **Brazeテンプレート**を選択します。次に、**機能導入**の横にある**テンプレートを適用**を選択します。これで、テンプレートをニーズに合わせて調整できます。

### ステップ 1: 詳細を設定する {#step-1-set-up-the-details}

キャンバスの詳細を目標に合わせて調整しましょう。

1. テンプレート名の横にある**編集**を選択します。

![キャンバスの現在のタイトルと説明。]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2. キャンバス名を更新して、ユーザーのフィードバックを収集するためにユーザーをターゲットにするキャンバスであることを明記します。
3. 説明を更新して、新しいCruise Control機能に対するフィードバックの送信を促し、ユーザーの感想を追跡するためのキャンバスであることを明記します。
4. **機能導入**タグを追加して、キャンバスホームページでフィルターできるようにします。

![キャンバスの新しい名前と説明。新しい説明には「定期的なフードデリバリーをスケジュールする機能であるCruise Controlの導入状況とユーザーの感想を追跡するための機能導入キャンバス」と記載されています。]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### ステップ 2: コンバージョンイベントを割り当てる {#step-2-assign-a-conversion-event}

次に、機能導入を示すコンバージョンイベントをキャンバスに追加しましょう。これにより、後でユーザージャーニーの実験パスを調整できるようになります。

1. **コンバージョンイベントの割り当て**で、**コンバージョンイベントを追加**を選択します。
2. **1次コンバージョンイベント - A**で、**コンバージョンイベントタイプ**として**カスタムイベントを実行**を選択します。
3. カスタムイベント`scheduled_delivery`を選択します。
4. コンバージョン期限は3日間のままにします。

![キャンバスのコンバージョンイベントウィンドウ。]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### ステップ 3: エントリスケジュールを調整する {#step-3-tailor-the-entry-schedule}

ユーザーにCruise Controlの導入を促すことが目標ですが、メッセージングの頻度が高すぎないようにしたいところです。そのため、このキャンバスはスケジュールされた配信のままにし、**時間ベースのオプション**セクションで以下の調整を行います。

1. **エントリ頻度**を**毎週**に更新します。
2. 繰り返し設定はそのままにします。
3. **月曜日**を選択して、週の初めにユーザーをターゲットにします。
4. キャンバスの開始時間を選択します。
5. **終了パラメーター**を更新して、年末にキャンバスを終了するようにします。

ユーザーがローカルタイムゾーンでキャンバスにエントリできるオプションはそのままにします。

### ステップ 4: ターゲットオーディエンスを選択する {#step-4-select-the-target-audience}

次に、テンプレートの以下の詳細を更新して、ターゲットオーディエンスを設定しましょう。

1. **すべてのユーザー**セグメントを選択します。
2. テンプレートの追加のフィルターを削除します。
3. カスタムイベントを使用してこのフィルターを作成します：`Has scheduled_delivery for exactly 0 times`。これにより、すでに機能を使用したユーザーをキャンバスへのエントリから除外できます。

![Cruise Controlを使用していないすべてのユーザーのセグメント。]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4. Calorie Rocketが以前、一部のユーザーに新機能Cruise Controlのベータテストを許可していたことを考慮し、これらのユーザーをキャンバスへのエントリから除外するように終了条件を更新します。

### ステップ 5: 送信設定を選択する {#step-5-select-your-send-settings}

デフォルトのサブスクリプション設定をそのまま使用し、メッセージや通知の受信を購読またはオプトインしたユーザーにのみ送信します。その他の設定（フリークエンシーキャップ、静寂時間、シードグループ）はスキップします。

### ステップ 6: キャンバスをカスタマイズする {#step-6-customize-your-canvas}

#### アクションパスを構築する {#build-out-the-action-path}

次に、ユーザーが新機能に興味を持っているかどうかを示すための最初のアクションパスステップを構築しましょう。テンプレートに以下の調整を行います。

1. Cruise Control機能はカートに注文が追加された後にのみ利用可能なため、最初のアクショングループに**Added to cart**と名前を付け、カスタムイベントとして`added_to_cart`を選択します。

![アクショングループ名が「Added to cart」に設定され、「Perform Custom Event」が「added_to_cart」に設定されている画面。]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2. 2番目のアクショングループ**Taken Tour**はそのままにします。ユーザーがアプリのツアーを完了したかどうかを評価し、完了した場合は2番目のパスに進むようにするためです。
3. 後続のアクションパス**Assess Usage**で、**Used Feature >3x**を**Viewed Cruise Control settings**に置き換えます。
4. **Perform Custom Event**ドロップダウンを選択し、カスタムイベントとして`scheduled_delivery`を選択します。

![アクショングループ名が「Used Feature >3x」に設定され、「Perform Custom Event」が「scheduled_delivery」に設定されている画面。]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### フィードバック調査を設定する {#set-up-feedback-survey}

次に、**Feedback Survey**というメッセージステップに移動して、ユーザーがCruise Controlを初めて使用した後に記入するフィードバック調査を含めます。調査の回答オプションは以下のとおりです。

- **Loved it!**
- **Not for me.**

1. 2つの調査選択肢について、Cruise Controlに関するフィードバックをキャプチャおよび追跡するためのカスタム属性として**Experience Feedback**を選択します。このカスタム属性には、調査回答を表す2つの値（`good`と`bad`）があります。
2. 属性値を調査オプションに合わせて更新します。これにより、ユーザーの回答を追跡できるようになります。

### ステップ 7: キャンバスをテストして起動する {#step-7-test-and-launch-your-canvas}

キャンバスをテストおよび確認して期待どおりに動作することを確かめた後、**キャンバスを起動**を選択してキャンバスを起動します。これで、パーソナライズされたユーザージャーニーでユーザーをターゲットにし、新機能Cruise Controlの導入を促すことができます。

{% alert tip %}
キャンバスの起動前後に考慮すべき事項については、[起動前後のチェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)をご確認ください。
{% endalert %}