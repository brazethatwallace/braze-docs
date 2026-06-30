---
nav_title: プリファレンス調査によるオンボーディング
article_title: プリファレンス調査によるオンボーディング
page_order: 5.5
page_type: reference
description: "この記事では、Braze Canvasテンプレートを使用して、新規ユーザーにブランドを紹介し、プリファレンスを収集して長期的なエンゲージメントを維持するガイド付きオンボーディングフローで早期導入を促進する方法について説明します。"
tool: Canvas
---

# プリファレンス調査によるオンボーディング {#onboarding-with-preferences-survey}

> プリファレンス調査付きオンボーディングテンプレートを使用して、新規ユーザーをターゲットにしたガイド付きオンボーディングワークフローを作成します。ブランドを紹介し、使い始めをサポートし、プリファレンスを収集して長期的なエンゲージメントを維持します。

この記事では、**プリファレンス調査によるオンボーディング**テンプレートのユースケースについて説明します。このテンプレートは、ユーザーライフサイクルの検討段階向けに設計されています。完了すると、ユーザーがセッションを開始したときやオンボーディングを完了していないときにメールやアプリ内メッセージを送信するCanvasが作成されます。

## 前提条件 {#prerequisites}

このテンプレートを正しく使用するには、以下が必要です。

- ユーザーにオンボーディングの開始を促すウェルカムメール。
- オンボーディングを完了したユーザー向けに、アプリの使い始めのヒントを含むフォローアップメール。
- ユーザーにオンボーディングの完了を促すフォローアップメール。
- ユーザーのプリファレンスを判断するための複数の質問を含む[調査]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/simple_survey)。

## テンプレートをニーズに合わせてカスタマイズする {#tailoring-the-template-to-your-needs}

ここでは、StyleRydeというオンデマンドのライドシェアリングアプリで作業しているとしましょう。このアプリは、ユーザーを目的地まで届けるサービスです。Canvasを作成する前に、アプリでの初回乗車の体験とインプレッションを判断するための一連の質問を含む[シンプルな調査を設定]({{site.baseurl}}/user_guide/data/activation/catalogs/create)します。

テンプレートにアクセスするには、新しいCanvasを作成する際に、**Canvasテンプレートを使用** > **Brazeテンプレート**を選択します。次に、**プリファレンス調査によるオンボーディング**の横にある**テンプレートを適用**を選択します。これで、テンプレートをニーズに合わせて調整できます。

### ステップ 1: 詳細を設定する {#step-1-set-up-the-details}

目標を反映するようにCanvasの詳細を調整しましょう。

1. テンプレート名の横にある**編集**を選択します。

![Canvasの現在のタイトルと説明。]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2. Canvas名を更新して、このCanvasが初めてアプリを使用する新規ユーザーをターゲットにしていることを明示します。
3. 説明を更新して、このCanvasにパーソナライズされたメッセージングが含まれていることを説明します。
4. **オンボーディング**タグを追加して、Canvasホームページでフィルタリングできるようにします。

![Canvasの新しい名前、説明、タグ。]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### ステップ 2: コンバージョンイベントを割り当てる {#step-2-assign-conversion-events}

**Primary Conversion Event - A**を**Performs Custom Event**に更新します。次に、カスタムイベントとして**Last Used App**を選択します。

![コンバージョンイベントの選択されたカスタムイベント名として「Last Used App」が表示されている。]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### ステップ 3: エントリスケジュールをカスタマイズする {#step-3-tailor-the-entry-schedule}

エントリスケジュールは**アクションベース**のままにして、ユーザーがアプリでセッションを開始したときにCanvasにエントリするようにします。これにより、タイムリーなエンゲージメントで関係構築を始めることができます。

このセクションでは、**エントリ時間枠**を希望の日時に調整する更新を1つ行います。

![開始時刻が2025年1月30日午後12時に設定された「エントリ時間枠」セクション。]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### ステップ 4: ターゲットオーディエンスを選択する {#step-4-select-the-target-audience}

ターゲットオーディエンスはそのままにして、StyleRydeアプリを初めて使用してから1日未満のユーザーをターゲットにします。

![エントリオーディエンスをターゲットにするために「これらのアプリを初めて使用してから1日未満」フィルターが選択されている。]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### ステップ 5: 送信設定を選択する {#step-5-select-your-send-settings}

デフォルトのサブスクリプション設定をそのまま使用し、メッセージや通知の受信を購読中またはオプトインしているユーザーにのみ送信します。サイレントアワーをオンにし、その他の設定（フリークエンシーキャップとシードグループ）はスキップします。

![サイレントアワーが午前12時から午後8時の間でオンになっている、購読中またはオプトインしたユーザー向けのサブスクリプション設定を含む「送信設定」セクション。]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### ステップ 6: Canvasをカスタマイズする {#step-6-customize-your-canvas}

次に、ユーザーに送信するコンテンツをカスタマイズしてCanvasを構築します。

1. 最初のメッセージステップ**Welcome Email**では、このステップを更新してStyleRydeのウェルカムメールを含めます。
2. 次に、アクションパスステップはそのままにします。このステップでは、3日間の時間枠でユーザーを2つのグループに分けます。

- セッションを開始したか、オンボーディングメールをクリックしたユーザー
- セッションを開始していないか、オンボーディングメールをクリックしていないユーザー

![セッションを開始したユーザー用のパスとその他のユーザー用のパスの2つに分かれたアクションパスステップ。]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

ここから、上記のグループに基づいてユーザーとメッセージングをターゲットにします。

#### エンゲージメントの高いユーザーをターゲットにする {#target-your-engaged-users}

最初のメッセージステップでセッションを開始したか、オンボーディングメールにエンゲージしたユーザーに対して、**Getting Started Tips**メッセージステップを更新し、新しいStyleRydeユーザー向けの重要な移動と安全に関するヒントを含めます。

ユーザーがオンボーディングを完了すると、Canvasを退出します。

次に、**Content Preferences Survey**メッセージステップを更新して、今後どのトピックに関する情報を受け取りたいかをユーザーに選択してもらうプリファレンス調査を含めます。

![該当するすべての興味を選択するようユーザーに促すプリファレンス調査のプレビュー。]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### オンボーディングを開始していないユーザーにナッジする {#nudge-users-who-havent-started-onboarding}

その他のユーザーに対しては、**Winback Nudge**メッセージステップをフォローアップメールで更新し、ユーザーにオンボーディングの完了を促します。

再エンゲージメントの最後のステップとして、**Step 2**を**Final Winback Nudge**に名前を変更し、新規ユーザーにオンボーディングの完了を促すアプリ内メッセージでステップを更新します。

### ステップ 7: Canvasをテストして起動する {#step-7-test-and-launch-your-canvas}

Canvasをテストして確認し、期待どおりに動作することを確認したら、**Canvasを起動**を選択して起動します。

{% alert tip %}
Canvasの起動前後に考慮すべき事項については、[起動前後のチェックリスト]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)をご覧ください。
{% endalert %}