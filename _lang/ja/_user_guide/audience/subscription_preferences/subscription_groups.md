---
nav_title: サブスクリプショングループ
article_title: サブスクリプショングループ
page_order: 4
description: "Brazeチャネル全体でのサブスクリプショングループの仕組み、作成と管理の方法、メール、WhatsApp、SMS、MMS、RCS、LINEのチャネル固有の動作について説明します。"
---

# サブスクリプショングループ {#subscription-groups}

> Brazeチャネル全体でのサブスクリプショングループの仕組み、ダッシュボードでの作成と管理の方法、チャネル固有のルールが適用される場面について説明します。

サブスクリプショングループは、チャネル内の特定の送信リソースセットからメッセージを受信できるユーザーを制御します。

メールの場合、サブスクリプショングループはグローバル購読状態の上に追加されるオプションのカテゴリフィルターです。SMS、WhatsApp、LINEの場合、サブスクリプショングループはすべての送信に必要なオーディエンスフィルターです。ニュースレターとプロモーション、トランザクションSMSとマーケティングSMSなど、きめ細かいオプトインとオプトアウトの選択肢を、グローバルチャネル購読状態（存在する場合）を変更せずに提供できます。

[サブスクリプショングループエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups)を使用して、Brazeワークスペースに保存されたサブスクリプショングループをプログラムで管理できます。

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## グローバル購読状態とサブスクリプショングループの比較 {#global-subscription-state-versus-subscription-groups}

一部のチャネルには、グローバル購読状態とサブスクリプショングループの両方があります。

| チャネル | グローバル購読状態 | サブスクリプショングループ |
| --- | --- | --- |
| メール | すべてのメールに対してオプトイン済み、購読中、または購読解除 | メール内のオプションのカテゴリ（ニュースレターやプロモーションなど） |
| SMS、MMS、RCS | グローバルSMS状態なし。購読はグループ単位 | すべての送信に必要。各グループは送信電話番号またはRCS送信者を保持 |
| WhatsApp | グローバルWhatsApp状態なし。購読はグループ単位 | WhatsApp連携時に作成。各グループは送信電話番号にマッピング |
| LINE | グローバルLINE状態なし。購読はグループ単位 | LINEチャネル連携ごとに作成。LINEアプリ内のフォロー・フォロー解除が状態を決定 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="グローバル購読状態とサブスクリプショングループの比較" }

ユーザーはメールにグローバルで購読中でありながら、特定のメールサブスクリプショングループからは購読解除できます。SMSの場合、ユーザーはトランザクショングループに購読中で、同時にプロモーショングループからは購読解除している場合があります。

## サブスクリプショングループの作成 {#create-a-subscription-group}

サブスクリプショングループの取得方法はチャネルによって異なります。メールグループはダッシュボードで作成し、SMS、MMS、RCSグループはオンボーディング時にプロビジョニングされ、WhatsAppとLINEのグループはチャネル連携時に作成されます。チャネル固有のプロビジョニングの詳細については、[チャネル固有の動作](#channel-specific-behavior)を参照してください。

### メール {#email}

1. **オーディエンス** > **サブスクリプショングループ管理**に移動します。
2. **メールサブスクリプショングループを作成**を選択します。
3. 名前と説明を入力します。ワークスペース内の各サブスクリプショングループには一意の名前が必要です。既に存在する名前を入力すると、ダッシュボードにエラーが表示され、グループは保存されません。
4. **保存**を選択します。

![サブスクリプショングループを作成するためのフィールド。]({% image_buster /assets/img/sub_group_create.png %}){: style="max-width:75%"}

## サブスクリプショングループによるセグメンテーション {#segment-with-subscription-groups}

セグメントを作成する際に、サブスクリプショングループフィルターを追加して、そのグループにオプトインしたユーザーをターゲットにできます。これは月刊ニュースレター、クーポンプログラム、メンバーシップティア、その他のカテゴリベースの送信に便利です。

![「Lapsed Users」セグメントで「Weekly Emails」サブスクリプショングループのフィルターを使用してユーザーをターゲットにする例。]({% image_buster /assets/img/segment_sub_group.png %}){: style="max-width:90%"}

## サブスクリプショングループのアーカイブ {#archive-subscription-groups}

アーカイブされたサブスクリプショングループは編集できず、セグメントフィルターやユーザー設定センターに表示されなくなります。アクティブなキャンペーン、キャンバス、またはセグメントでセグメントフィルターとして使用されているグループをアーカイブすると、それらの参照を削除するまでエラーが表示されます。

**サブスクリプショングループ管理**からグループをアーカイブするには、グループを見つけて<i class="fa-solid fa-ellipsis-vertical" aria-label="メニューを開く"></i>メニューから**アーカイブ**を選択します。

Brazeはアーカイブされたグループへのメッセージングをブロックするため、アーカイブされたサブスクリプショングループを新規またはアクティブな送信で使用することはできません。

一部のチャネルには追加のアーカイブルールがあります。ワークスペースと再連携の動作については、[LINEサブスクリプショングループ](#line-subscription-groups)を参照してください。

## ユーザーのサブスクリプショングループの確認 {#check-a-users-subscription-groups}

- **ユーザープロファイル：**[ユーザー検索]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles)からプロファイルを開きます。**エンゲージメント**タブで、メール、SMS、WhatsApp、および関連チャネルのサブスクリプショングループとステータスを確認できます。
- **REST API：**[ユーザーのサブスクリプショングループ一覧]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups)または[ユーザーのサブスクリプショングループステータス一覧]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status)エンドポイントを使用します。

### サブスクリプショングループステータスの更新 {#update-subscription-group-status}

ユーザーのサブスクリプショングループメンバーシップは、REST API、SDK、ユーザーインポート、ユーザープロファイル、メールユーザー設定センター、キャンバスのUser Updateステップ、その他のチャネル固有のフローを通じて更新できます。具体的な方法はチャネルによって異なります。各[チャネルセクション](#channel-specific-behavior)と、SMS固有のタイミングガイダンスについては[SMS、MMS、RCSサブスクリプショングループ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#set-a-users-state)を参照してください。

## ユーザー設定センター {#preference-centers}

メールサブスクリプショングループは[メールユーザー設定センター]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center)に表示でき、ユーザーがカテゴリレベルのメールオプトインを一か所で管理できます。ユーザー設定センターを構築する際に、アクティブなメールサブスクリプショングループを追加できます。レガシーのユーザー設定センターでは、すべてのアクティブなメールグループが自動的にリストされます。

SMSとWhatsAppの場合、REST API、オプトインフロー、キーワード（SMS）、ユーザープロファイル、その他のチャネル固有の方法で購読状態を管理します。詳細は各[チャネルセクション](#channel-specific-behavior)を参照してください。

## チャネル固有の動作 {#channel-specific-behavior}

### メールサブスクリプショングループ {#email-subscription-groups}

メールサブスクリプショングループは[グローバルメール購読状態]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)（オプトイン済み、購読中、購読解除）の上に位置します。グローバルで`unsubscribed`状態のユーザーは、サブスクリプショングループのメンバーシップに関係なくメールを受信しません。

メール固有の詳細：

- **ユーザー設定センター：** 作成したすべてのメールサブスクリプショングループをユーザー設定センターに追加できます。
- **キャンペーン分析：** キャンペーンの**メールメッセージパフォーマンス**ページで、**サブスクリプショングループ**を開くと、その送信の購読数と購読解除数の集計を確認できます。

#### サブスクリプショングループサイズの表示 {#viewing-subscription-group-sizes}

**サブスクリプショングループ管理**では、時系列チャートで以下がレポートされます。

- **サブスクリプショングループサイズ：** 指定日にそのグループに購読しているユーザー数
- **サブスクリプショングループ購読解除サイズ：** 指定日にそのグループから購読解除しているユーザー数

これらのカウントはそのグループのメンバーシップを反映しており、グローバルメール購読状態ではありません。**メール購読ステータスが購読解除**を使用するセグメントとは異なる場合があります。これは[グローバルメール購読状態]({{site.baseurl}}/user_guide/channels/email/subscriptions#subscription-states)を反映しています。

当日のサブスクリプショングループサイズはデフォルトでは計算されません。日付範囲に当日が含まれる場合、**本日の統計を計算**を選択して当日の値を時系列に追加します。非常に大きなワークスペースの場合、Brazeは正確なカウントではなく推定カウントを表示する場合があります。

フッター、購読解除ページ、グローバルメール購読管理については、[メール購読]({{site.baseurl}}/user_guide/channels/email/subscriptions)を参照してください。

### WhatsAppサブスクリプショングループ {#whatsapp-subscription-groups}

WhatsAppサブスクリプショングループは、テクノロジーパートナーポータルを通じてワークスペースに[WhatsAppを連携]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)する際に作成されます。

| 状態 | 定義 |
| --- | --- |
| 購読中 | ユーザーがビジネスからWhatsAppメッセージを受信することを明示的に確認しました。ユーザーはBrazeサブスクリプションAPIまたはオプトインフローを通じて購読できます。 |
| 購読解除 | ユーザーがオプトインしていないか、グループから削除されました。購読解除したユーザーは、そのグループの電話番号からWhatsAppメッセージを受信しません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp購読状態" }

WhatsAppでは明示的なオプトインが必要です。このチャネルではオプトインキーワードはサポートされていません。同意と購読状態はご自身で管理します。オプトインとオプトアウトのフローについては、[WhatsAppオプトインとオプトアウト]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)を参照してください。

アーカイブ手順、キャンバスの更新、REST APIの例については、[WhatsAppサブスクリプショングループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)を参照してください。

### SMS、MMS、RCSサブスクリプショングループ {#sms-mms-and-rcs-subscription-groups}

SMS、MMS、RCSサブスクリプショングループは、これらのチャネルでの送信の基盤です。各グループは、特定のメッセージング目的（トランザクションとプロモーションなど）のための[送信エンティティ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup)（ショートコード、ロングコード、英数字送信者ID、RCS認証済み送信者など）の集合です。

| 状態 | 定義 |
| --- | --- |
| 購読中 | ユーザーはサブスクリプションAPI、オプトインキーワード、その他のサポートされたフローを通じて、そのサブスクリプショングループからのメッセージ受信を購読しています。[ダブルオプトイン]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in)が有効な場合、ステータスが購読中に更新される前にユーザーの確認が必要です。 |
| 購読解除 | ユーザーがキーワードまたはAPI更新を通じてオプトアウトしました。購読解除したユーザーは、そのグループの送信者からSMS、MMS、RCSを受信しません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SMSおよびRCS購読状態" }

SMSまたはRCSメッセージを開始する際、コンポーザーでサブスクリプショングループを選択します。Brazeはオーディエンスフィルターを追加し、購読中のユーザーのみがターゲットになるようにします。Brazeは選択したグループに購読していないユーザーにはSMSやRCSを送信しません。SMSテストメッセージを受信するには、受信者がテスト用に選択したサブスクリプショングループに所属している必要があります。詳細については、[SMS FAQ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages)を参照してください。

SMSのサブスクリプショングループはオンボーディング時にプロビジョニングされます。MMSタグ、RCS送信者の設定、地理的権限、RCS移行、高度なオプトアウト処理については、[SMS、MMS、RCSサブスクリプショングループ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups)を参照してください。

### LINEサブスクリプショングループ {#line-subscription-groups}

各LINEサブスクリプショングループは1つのLINEチャネル連携に接続されます。

| 状態 | 定義 |
| --- | --- |
| 購読中 | ユーザーがLINEアプリ内でLINEチャネルをフォローしました。連携後にユーザーがフォローすると、Brazeは自動的に購読中にします。 |
| 購読解除 | ユーザーがチャネルをフォローしなかった、またはフォローを解除しました。購読解除したユーザーは、そのグループからLINEメッセージを受信しません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="LINE購読状態" }

LINEが購読ステータスの信頼できるソースです。Brazeはフォローおよびフォロー解除イベントを処理してプロファイルを更新します。

LINEサブスクリプショングループはワークスペース間で移動できません。グループをアーカイブして別のワークスペースでチャネルを再連携すると、Brazeは移行先のワークスペースに新しいサブスクリプショングループを作成します。

アーカイブの動作、ユーザーの照合、連携手順については、[LINEサブスクリプショングループ]({{site.baseurl}}/user_guide/channels/line/message_users/subscription_groups)と[LINE設定]({{site.baseurl}}/user_guide/channels/line/line_setup)を参照してください。