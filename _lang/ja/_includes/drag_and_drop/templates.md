{% if include.section == "SDK requirements" %}

## 前提条件 {#prerequisites}

### 最小SDKバージョン {#minimum-sdk-versions}

ドラッグ＆ドロップエディターを使用して作成されたメッセージは、以下の最小SDKバージョンのユーザーにのみ送信できます。詳細については、[ドラッグ＆ドロップによるアプリ内メッセージの作成：前提条件]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#prerequisites)を参照してください。

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### テキストリンクのSDKバージョン {#sdk-versions-for-text-links}

メッセージを閉じないテキストリンクを含めるには、以下の最小SDKバージョンが必要です。

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
アプリ内メッセージにURLへリダイレクトするリンクを含めていて、ユーザーが指定された最小SDKバージョンを使用していない場合、リンクをクリックするとメッセージが閉じられ、ユーザーはフォームを送信するためにメッセージに戻ることができません。
{% endalert %}

{% endif %}

{% if include.section == "message style" %}

テンプレートのカスタマイズを始める前に、サイドメニューを使用してメッセージ全体のメッセージレベルのスタイルを設定できます。例えば、メッセージに含まれるすべてのテキストのフォントやすべてのリンクの色をカスタマイズしたい場合があります。メッセージをモーダルまたは全画面表示タイプにすることもできます。

{% endif %}


<!-- Add this after the disclaimers are added to all email sign-up templates: "We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes."-->

{% if include.section == "email disclaimer" %}

メッセージには、オプトインの文言とブランドのプライバシーポリシーおよび利用規約へのリンクを含めることをお勧めします。法務チームと協力して、特定のブランドに合わせた文言を作成してください。

{% alert note %}
配信性のベストプラクティスは法的要件を超えることが多く、メール送信に関する明示的な同意を常に取得し、ユーザーが簡単に拒否できるようにすることをお勧めします。
{% endalert %}

{% endif %}

{% if include.section == "email validation" %}

ユーザーが受け付けられない特殊文字を含むメールアドレスを入力した場合、一般的なエラーインジケーターが表示され、フォームを送信できません。このエラーメッセージはカスタマイズできません。エラーの動作は、**プレビュー＆テスト**タブとテストデバイスで確認できます。Brazeがメールアドレスをどのようにフォーマットするかについては、[メールバリデーション]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation)を参照してください。

{% endif %}

{% if include.section == "email double opt-in" %}

### ダブルオプトイン認証 {#double-opt-in-verification}

リストにサインアップした人が本当にサインアップするつもりであり、正しいメールアドレスを提供したことを確認するために、メールサインアップフォームを通じてサインアップした人に[ダブルオプトイン](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in)フローを送信して、再確認を取得することをお勧めします。

これを設定する方法の1つとして、キャンバスを使用する方法があります。

1. アクションベースのキャンバスを作成し、ユーザーがBrazeにメールアドレスを追加したときにトリガーするように設定します。プラットフォームに新しいユーザーもターゲットにできるようにしてください（例えば、キャンバスでフィルターのないセグメントを使用するなど）。
2. {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquidタグへのハイパーリンクを持つCTA付きのメールメッセージステップを作成します。これにより、ユーザーがボタンをクリックすると、メール購読ステータスが`opted_in`に変更されます。
3. [アクションパスステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths)を追加します。
4. 最初のパスでは、ユーザーがメール購読ステータスを`opted_in`に変更したときにメールをトリガーします。このメールで、ユーザーにメールアドレスが確認されたことを通知します。
5. ウィンドウの有効期限が切れた後にキャンバスを終了するように、もう1つのパスを設定します。

{% endif %}

{% if include.section == "reporting" %}

キャンペーンの開始後、リアルタイムで結果を分析して、キャンペーンにエンゲージしたユーザー数を確認できます。購読グループにオプトインしたユーザーの数を確認するには、アプリ内メッセージを受信してフォームを送信したユーザーをフィルタリングして、購読グループに登録したユーザーの[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment)します。

{% endif %}