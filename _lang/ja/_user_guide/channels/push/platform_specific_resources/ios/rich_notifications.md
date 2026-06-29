---
nav_title: リッチ通知の作成
article_title: "iOS向けリッチプッシュ通知の作成"
page_order: 3
page_type: tutorial
description: "このチュートリアルでは、BrazeのCampaignsにおけるiOSリッチ通知の作成要件と手順について説明します。"

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# iOS向けリッチプッシュ通知の作成 {#create-rich-push-notifications-for-ios}

> リッチ通知を使用すると、テキスト以外のコンテンツを追加してプッシュ通知をさらにカスタマイズできます。Androidの通知には以前から「拡張通知画像」としてプッシュ通知に画像が含まれていました。iOS 10以降、顧客はGIF、画像、動画、またはオーディオを含むiOSプッシュ通知を受信できるようになりました。

## 前提条件 {#prerequisites}

iOS向けリッチプッシュ通知を作成する前に、以下の詳細を確認してください。

- アプリがリッチ通知を送信できるようにするには、[iOSプッシュ統合]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications)の手順に従ってください。開発者がアプリにサービス拡張を追加する必要があります。
- 現在ダッシュボードで直接アップロードをサポートしているファイルタイプは、JPEG、PNG、GIFです。これらのファイルは、テンプレート可能なURLフィールドに入力することもでき、追加のファイルタイプ（AIF、M4A、MP3、MP4、WAV）もサポートされています。
- メディアの制限と仕様については、[Appleのドキュメント](https://developer.apple.com/reference/usernotifications/unnotificationattachment)を参照してください。
- iOSは画面に合わせて画像をスケーリングし、アクティブまたはロック画面の表示に合わせてリッチ画像をスケーリングします。

{% alert note %}
2020年1月時点で、iOSリッチプッシュ通知は1038x1038で10&nbsp;MB未満の画像を処理できますが、できるだけ小さいファイルサイズを使用することをお勧めします。実際には、大きなファイルを送信すると不要なネットワーク負荷が発生し、ダウンロードタイムアウトがより頻繁に発生する可能性があります。
{% endalert %}

{% alert important %}
画像のファイルサイズが大きすぎる場合、アスペクト比が正しくない場合、テキストが最大メッセージ長を超えている場合、またはタイトルテキストが最大タイトル長を超えている場合、プッシュ通知の画像が期待どおりに表示されないことがあります。
{% endalert %}

### 文字数 {#character-count}

プッシュに含める正確な文字数について厳密なルールを提供することはできませんが、iOSメッセージを設計する際に考慮すべき[ガイドライン]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats/)を提供しています。画像の有無、ユーザーのデバイスの通知状態と表示設定、デバイスのサイズによって多少の差異が生じる場合があります。迷った場合は、短く簡潔にまとめましょう。

ベストプラクティスとして、Brazeはモバイルプッシュ通知のオプションのタイトルとメッセージ本文の各行を約30〜40文字に収めることを推奨しています。

#### 通知の状態 {#notification-states}

ユーザーはさまざまな状況でプッシュ通知を表示する可能性があり、以下のように異なる長さのテキストが表示されることがあります。

<table aria-label="通知の状態">
  <caption>通知の状態</caption>
<thead>
  <tr>
    <th>ロック画面または通知センター</th>
    <th>展開時</th>
    <th>デバイスアクティブ時</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">これは最も一般的なシナリオです。<br><br><b>タイトル:</b> 1行のテキスト<br><b>本文:</b> 4行のテキスト<br><b>画像:</b> 正方形のサムネイル</td>
    <td width="33%">ユーザーがメッセージを長押しした場合。<br><br><b>タイトル:</b> 1行のテキスト<br><b>本文:</b> 7行のテキスト<br><b>画像:</b> 2:1のアスペクト比（推奨、以下の注記を参照）</td>
    <td width="33%">ユーザーが電話のロックを解除してアクティブな状態でプッシュを受信した場合。<br><br><b>タイトル:</b> 1行のテキスト<br><b>本文:</b> 2行のテキスト</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="通知の状態" }

![ロック画面、展開時、デバイスアクティブ時に表示されるプッシュ通知の例。]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
展開されたプッシュ通知には2:1のアスペクト比を推奨していますが、ほぼすべてのアスペクト比がサポートされています。画像は常に通知の全幅に広がり、高さはそれに応じて調整されます。
{% endalert %}

#### テキスト切り詰めに影響する変数 {#variables-in-text-truncation}

コンテンツを作成する際は、表示されるテキスト量に影響する以下のシナリオを考慮してください。

{% tabs %}
{% tab タイミング %}

ユーザーがプッシュ通知を操作するタイミングによって、タイムスタンプがタイトルテキストを短くする場合があります。

![タイムスタンプが「now」でタイトル文字数が35のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>タイトル文字数: **35**

![タイムスタンプが「3h ago」でタイトル文字数が33のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>タイトル文字数: **33**

![タイムスタンプが「Yesterday, 8:37 AM」でタイトル文字数が22のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>タイトル文字数: **22**

{% endtab %}
{% tab 画像 %}

画像がある場合、本文テキストは1行あたり約10文字短くなります。

![画像なしで本文文字数が179のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>本文文字数: **179**

![画像ありで本文文字数が154のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>本文文字数: **154**

{% endtab %}
{% tab 割り込みレベル %}

iOS 15では、「即時」および「重大」の表示がタイトルをタイムスタンプなしで新しい行に押し下げ、少しスペースが広がります。

![「即時」や「重大」の表示がなく、タイトル文字数が35のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>タイトル文字数: **35**

![「即時」の表示があり、タイトル文字数が39のプッシュ通知の例。]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>タイトル文字数: **39**

{% endtab %}
{% tab その他 %}

以下の詳細もテキストの切り詰めに影響する可能性があります。

- **電話の表示設定:** ユーザーは通常、アクセシビリティの理由から、電話のグローバルUIフォントサイズを拡大または縮小できます。
- **デバイスの幅:** メッセージは小さな電話や幅の広いiPadに表示される可能性があります。
- **コンテンツの種類:** 絵文字や「m」「w」のような幅の広い文字は「i」や「t」よりもスペースを多く取り、「engagement」のような長い単語は短い単語よりも急に改行される場合があります。

{% endtab %}
{% endtabs %}

## iOSリッチ通知の設定 {#setting-up-your-ios-rich-notification}

### ステップ 1: プッシュキャンペーンを作成する {#step-1-create-a-push-campaign}

[キャンペーンの作成]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#creating-a-push-message)の手順に従って、iOS向けのプッシュ通知を作成します。リッチコンテンツを含まないプッシュ通知の設定に使用するのと同じコンポーザーを使用します。

### ステップ 2: メディアを追加する {#step-2-add-media}

メッセージのコンポーザーの**iOS通知画像**フィールドに、画像、GIF、オーディオ、または動画ファイルを追加します。コンテンツファイルの追加方法については、[要件](#requirements)を参照してください。

![プッシュ通知のサマリーテキストの例。]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

また、このメッセージをiOS 10を実行するデバイスを持つユーザーにのみ送信するように制限することもできます。iOS 10にアップグレードしていないユーザーの場合、**リッチ通知対応デバイスにのみ送信**のチェックを外すと、リッチコンテンツなしのテキストのみの通知として表示されます。

![画像を追加するか画像URLを入力できる展開通知画像セクション。]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### ステップ 3: キャンペーンの作成を続ける {#step-3-continue-creating-your-campaign}

リッチ通知コンテンツがダッシュボードにアップロードされたら、[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/#schedule-push-campaign)を続行できます。

ユーザーがプッシュ通知を受信すると、プッシュメッセージを強く押して画像を展開できます。

![ユーザーがプッシュ通知を受信し、メッセージを強く押して「Hello!」と表示された展開画像を表示する様子。]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }