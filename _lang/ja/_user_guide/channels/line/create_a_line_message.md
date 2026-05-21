---
nav_title: LINE メッセージの作成
article_title: LINE メッセージの作成
page_order: 1
description: "この記事では、LINE メッセージのCampaignまたはCanvasを作成する方法について説明します。"
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# LINE メッセージの作成 {#create-a-line-message}

> LINE Campaignsを使用すると、顧客に直接リーチし、プログラムによるチャットが可能になります。Liquidやその他のダイナミックコンテンツを使用して、ユーザーとのパーソナルな体験を作り出し、ブランドとの控えめなユーザー体験を促進・向上させる環境を構築できます。

## 前提条件 {#prerequisites}

LINE メッセージを作成する前に、以下を行ってください。

1. LINEの概要を確認します。
2. ポリシー、制限、コンテンツルールを確認します。
3. [LINE接続を設定します]({{site.baseurl}}/user_guide/channels/line/line_setup/)。

BrazeからLINEメッセージを送信すると、アカウントのメッセージクレジットまたはアクションクレジットが消費されます。

## ステップ 1:メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

メッセージをCampaignで送信するか、Canvasで送信するか迷っていますか？Campaignsは単一のターゲットメッセージングに適しており、Canvasesは複数ステップのユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

**手順:**

1. **Messaging** > **Campaigns** に移動し、**Create Campaign** を選択します。
2. **LINE** を選択するか、複数チャネルをターゲットとするCampaignの場合は **Multichannel Campaign** を選択します。
3. Campaignにわかりやすく意味のある名前を付けます。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams/)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags/)を追加します。
   * タグを使用すると、Campaignsを見つけやすくなり、レポートを作成しやすくなります。
5. Campaignに必要な数のバリアントを追加し、名前を付けます。追加したバリアントごとに、異なるプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing/)を参照してください。

{% alert tip %}
Campaign内のすべてのメッセージが類似している、または同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**Add Variant** ドロップダウンから **Copy from Variant** を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

**手順:**

1. Canvasコンポーザーを使用して[Canvasを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)します。
2. Canvasを設定したら、Canvasビルダーでステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. [ステップスケジュール]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types/#schedule-delay)を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルタリングします。Segmentsを指定し、追加のフィルターを追加することで、このステップの受信者をさらに絞り込むことができます。オーディエンスオプションは、メッセージ送信時に遅延後にチェックされます。
5. [昇格動作]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/)を選択します。
6. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2:LINEメッセージを作成する {#step-2-compose-your-line-message}

必要に応じてパーソナライゼーション（Liquidやコネクテッドコンテンツなど）を使用してメッセージを作成します。LINEでは、各メッセージに最大5つのメッセージバブルを含めることができ、テキスト、画像、リッチ、カードベースなど、利用可能なメッセージレイアウトのいずれかを使用できます。

![プレビューにメッセージが表示されたLINEコンポーザー。]({% image_buster /assets/img/line/line_composer.png %})

### ヒント {#tips}

#### Liquidの使用 {#using-liquid}

Liquidを使用する予定がある場合は、パーソナライゼーションにデフォルト値を含めるようにしてください。これにより、不完全なユーザープロファイルを持つ受信者が空白のプレースホルダーを受け取ることを防ぎます。たとえば、ユーザーが「こんにちは、！」というメッセージを受け取る代わりに、「こんにちは、新しいサブスクライバーさん！」というメッセージを受け取ることができます。

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### 右から左へのメッセージの作成 {#creating-right-to-left-messages}

右から左へのメッセージの最終的な表示は、サービスプロバイダーがどのようにレンダリングするかに大きく依存します。できるだけ正確に表示される右から左へのメッセージを作成するためのベストプラクティスについては、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages/)を参照してください。

## ステップ 3:メッセージをプレビューしてテストする {#step-3-preview-and-test-your-message}

**Test** タブに切り替えて、コンテンツテストグループまたは個々のユーザーにテストLINEメッセージを送信するか、Braze内でユーザーとしてメッセージを直接プレビューします。

![テストメッセージのプレビューが表示された「Tests」タブ。]({% image_buster /assets/img/line/test_preview.png %})

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/?tab=line)を参照してください。

## ステップ 4:CampaignまたはCanvasの残りの部分を構築する {#step-4-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Campaignの残りの部分を構築します。LINEメッセージを構築するためのツールの最適な使用方法の詳細については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

LINEメッセージは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。スケジュールとトリガーオプションの詳細については、[Campaignのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/)を参照してください。

配信コントロールを指定できます。たとえば、ユーザーがCampaignを[再受信可能]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility/#campaigns)にすることや、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#frequency-capping)ルールを有効にすることができます。アクションベースの配信では、Campaignの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/)も設定できます。

### ターゲットユーザーを選択する {#choose-users-to-target}

Segmentsまたはフィルターを選択してオーディエンスを絞り込むことで、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users/)にします。サブスクリプショングループはすでに選択されているはずです。これにより、ユーザーが希望するコミュニケーションのレベルやカテゴリによってユーザーが絞り込まれます。

Segmentsからより大きなオーディエンスを選択し、オプションで[フィルター]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/)を使用してそのSegmentをさらに絞り込みます。おおよそのSegment人口のスナップショットが自動的に表示されます。正確なSegmentメンバーシップは、メッセージが送信される前に常に計算されることに注意してください。

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、Campaignを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events/)）を実行する頻度を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間の時間枠を設定するオプションがあります。

コンバージョンイベントは、Campaignの成功を測定するのに役立ちます。例:

- ジオターゲティングを使用して、ユーザーが購入するという最終目標を持つLINEメッセージをトリガーする場合は、コンバージョンイベントを`Purchase`に設定します。
- ユーザーをアプリに誘導しようとしている場合は、コンバージョンイベントを`Starts Session`に設定します。

特定のユースケースに基づいてカスタムコンバージョンイベントを設定することもできます。創造的に考えて、このCampaignの成功をどのように測定したいかを検討してください。

{% endtab %}
{% tab Canvas %}

まだ完了していない場合は、Canvasの残りのセクションを完了してください。Canvasの残りの部分の構築方法、多変量テストとインテリジェントセレクションの使用方法などの詳細については、[Canvasの作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ 5:確認してデプロイする {#step-5-review-and-deploy}

CampaignまたはCanvasの最後の構築が完了したら、詳細を確認し、テストしてから送信してください。

次に、[LINEレポート]({{site.baseurl}}/line/reporting/)を確認して、LINE Campaignsの結果にアクセスする方法を学びましょう。