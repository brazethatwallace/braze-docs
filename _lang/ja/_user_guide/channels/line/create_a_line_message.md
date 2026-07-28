---
nav_title: LINE メッセージの作成
article_title: LINE メッセージの作成
page_order: 1
description: "この記事では、LINE メッセージのキャンペーンまたはキャンバスを作成する方法について説明します。"
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# LINE メッセージの作成 {#create-a-line-message}

> LINEキャンペーンを使用すると、顧客に直接リーチし、プログラムによるチャットが可能になります。Liquidやその他のダイナミックコンテンツを使用して、ユーザーとのパーソナルな体験を作り出し、ブランドとの控えめなユーザー体験を促進・向上させる環境を構築できます。

## 前提条件 {#prerequisites}

LINEメッセージを作成する前に、以下を行ってください：

1. LINEの概要を確認します。
2. ポリシー、制限、コンテンツルールを確認します。
3. [LINE接続を設定します]({{site.baseurl}}/user_guide/channels/line/line_setup)。

BrazeからLINEメッセージを送信すると、アカウントのメッセージクレジットまたはアクションクレジットが消費されます。

## ステップ1: メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

メッセージをキャンペーンとキャンバスのどちらで送信すべきかわからない場合は、キャンペーンは単一のターゲットメッセージングに適しており、キャンバスはマルチステップのユーザージャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**手順:**

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **LINE**を選択するか、複数のチャネルをターゲットにするキャンペーンの場合は**マルチチャネルキャンペーン**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンの検索やレポートの作成が容易になります。
5. キャンペーンに必要な数のバリアントを追加し、名前を付けます。追加したバリアントごとに、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**手順:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## ステップ2: LINEメッセージを作成する {#step-2-compose-your-line-message}

パーソナライゼーション（LiquidやConnected Contentなど）を必要に応じて使用してメッセージを作成します。LINEでは、各メッセージに最大5つのメッセージバブルを含めることができ、テキスト、画像、リッチ、カードベースのいずれかのメッセージレイアウトを使用できます。

![プレビューにメッセージが表示されたLINEコンポーザー。]({% image_buster /assets/img/line/line_composer.png %})

### ヒント {#tips}

#### Liquidの使用 {#using-liquid}

Liquidを使用する場合は、パーソナライゼーションにデフォルト値を必ず含めてください。これにより、ユーザープロファイルが不完全な受信者に空白のプレースホルダーが表示されるのを防ぎます。例えば、ユーザーが「こんにちは、！」というメッセージを受け取る代わりに、「こんにちは、新規購読者さん！」というメッセージを受け取ることができます。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### 右から左に読むメッセージの作成 {#creating-right-to-left-messages}

右から左に読むメッセージの最終的な表示は、サービスプロバイダーのレンダリング方法に大きく依存します。できるだけ正確に表示される右から左に読むメッセージを作成するためのベストプラクティスについては、[右から左に読むメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

## ステップ3: メッセージをプレビューしてテストする {#step-3-preview-and-test-your-message}

**Test**タブに切り替えて、コンテンツテストグループまたは個別のユーザーにテストLINEメッセージを送信するか、Braze内でユーザーとしてメッセージを直接プレビューします。

![テストメッセージのプレビューが表示された「Tests」タブ。]({% image_buster /assets/img/line/test_preview.png %})

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=line)を参照してください。

## ステップ4: キャンペーンまたはキャンバスの残りの部分を構築する {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

キャンペーンの残りの部分を構築します。LINEメッセージを構築するためのツールの最適な使用方法については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

LINEメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。スケジュールとトリガーオプションの詳細については、[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

ユーザーがキャンペーンを[再受信可能]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)にすることや、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)ルールを有効にするなど、配信コントロールを指定できます。アクションベースの配信では、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)も設定できます。

### ターゲットユーザーを選択する {#choose-users-to-target}

セグメントまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)にします。購読グループはすでに選択されているはずです。これにより、ユーザーが希望するコミュニケーションのレベルやカテゴリーで絞り込まれます。

セグメントからより広いオーディエンスを選択し、必要に応じて[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)でそのセグメントをさらに絞り込みます。おおよそのセグメント人口のスナップショットが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に常に計算されることに留意してください。

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度をトラッキングできます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間のウィンドウを設定するオプションがあります。

コンバージョンイベントは、キャンペーンの成功を測定するのに役立ちます。例えば：

- ジオターゲティングを使用して、ユーザーに購入を促すことを最終目標とするLINEメッセージをトリガーする場合、コンバージョンイベントを`Purchase`に設定します。
- ユーザーをアプリに誘導しようとしている場合、コンバージョンイベントを`Starts Session`に設定します。

特定のユースケースに基づいてカスタムコンバージョンイベントを設定することもできます。クリエイティブに考えて、このキャンペーンの成功をどのように測定したいかを検討してください。

{% endtab %}
{% tab キャンバス %}

まだ完了していない場合は、キャンバスの残りのセクションを完成させてください。キャンバスの残りの部分の構築方法、多変量テストやインテリジェントセレクションの使用方法などの詳細については、[キャンバスを作成する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ5: 確認とデプロイ {#step-5-review-and-deploy}

キャンペーンまたはキャンバスの構築が完了したら、詳細を確認し、テストしてから送信してください。

次に、[LINEレポート]({{site.baseurl}}/line/reporting)を参照して、LINEキャンペーンの結果にアクセスする方法を確認してください。