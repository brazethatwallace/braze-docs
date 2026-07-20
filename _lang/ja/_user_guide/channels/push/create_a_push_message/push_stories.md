---
nav_title: "Push Stories"
article_title: "Push Stories"
page_order: 2
page_type: reference
description: "このリファレンス記事では、Push Storiesとは何か、その作成方法、およびよくある質問について説明します。"
channel:
  - push

---

# Push Stories {#push-stories}

> Push Storiesは、InstagramやFacebookで普及したフォトカルーセル機能を活用し、マーケターがプッシュ通知内にカルーセル形式のページを作成して、リッチで一貫性のあるストーリーを伝えることを可能にします。これらのページは、画像、クリックアクション、タイトル、説明で構成されます。ユーザーはこれらのページをスワイプして、あなたが伝えるストーリーを閲覧できます。

| Androidの例（展開時） | iOSの例（展開時） |
| :-----: | :----------: |
| ![Push StoriesのAndroidプレビュー]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | ![Push StoriesのiOSプレビュー]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push Stories" }

{% alert note %}
iOS SDKバージョン3.13.0以降では、SDKが画像をダウンロードする方法の変更により、プッシュの縮小表示で最初の画像のサムネイルが表示されません。メッセージのコピーで、画像を表示するためにプッシュを展開するようユーザーに促してください。
{% endalert %}

## 前提条件 {#prerequisites}

Push Storiesを受信するには、以下のSDKバージョンが必要です。

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Push Storiesの使用方法 {#how-to-use-push-stories}

![Push Storiesコンポーザーのドロップダウン]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Push Storiesを使用するには、以下の手順を実行します。

1. [プッシュキャンペーン]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)を作成します。
2. **通知タイプ**で**Push Stories**を選択します。
3. **iOS**または**Android**を選択します。プッシュメッセージで両方を選択した場合、Push Storyを作成するオプションは表示されません。

### Push Storyコンポーザー {#push-story-composer}

ページを作成するには、以下のステップを実行します。

1. メインコンポーザーから**新しいページを追加**を選択します。
2. 各ページに画像を挿入し、その画像のクリック動作を設定します。
3. 必要に応じて、各ページに**タイトル**と**説明**を追加します。1つのページにタイトルと説明を使用する場合は、すべてのページに挿入する必要があります。

プレビューは反映され、インタラクティブに操作できます。

![Push Storiesコンポーザー]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)で画像を取得する場合は、画像URLが`https://`で始まることを確認してください。`http://`を使用するとアプリがクラッシュします。
{% endalert %}

### 画像とテキストの仕様 {#image-and-text-specifications}

以下の画像とテキストの仕様は、Push Storiesのフォトカルーセル部分に適用されます。ユーザーがPush Storyを起動するために操作する基本的なプッシュについては、[プッシュメッセージと画像フォーマット]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats)を参照してください。

{% tabs %}
{% tab 画像 %}

- **画像比率：** 2:1（必須）
- **推奨画像サイズ：** 500 KB
- **最大画像サイズ：** 5 MB
- **ファイルタイプ：** PNG、JPEG

{% endtab %}
{% tab テキスト %}

- **タイトル：** 30文字（推奨）
- **説明：** 30文字（推奨）

{% alert note %}
デバイスによって文字数に多少の差異がある場合がありますが、Push Storiesのタイトルと説明はそれぞれ1行に制限されています。メッセージの残りの部分は切り捨てられます。必ず実際のデバイスでメッセージをテストしてください。
{% endalert %}

{% endtab %}
{% endtabs %}

### Push Storyのセグメンテーション {#push-story-segmentation}

キャンペーンまたはキャンバスを作成する際、Push Storyページをクリックしたかどうかに基づいてターゲットユーザーをフィルタリングできます。次に、ユーザーをターゲットするために使用するキャンペーンとページを選択します。

### Push Storiesの分析 {#push-stories-analytics}

分析は、プッシュ通知の現在の分析セクションと非常に似ています。Push Storiesの分析では、**直接開封数**指標を開いてページごとのクリック数を確認できます。

![iOSプッシュパフォーマンステーブル。サンプル分析と直接開封数指標の展開された詳細が表示されています。]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## トラブルシューティング {#troubleshooting}

### iOS

#### Push Storyを自分に送信したが、通知を受信しなかった {#i-sent-myself-a-push-story-but-didnt-receive-the-notification}

Appleには、さまざまな要因に基づいて特定の種類の通知がデバイスに送信されないようにする特定のルールがあります。これには、顧客のデータプラン、通知サイズ、顧客のストレージ容量の評価が含まれます。その結果、顧客に通知が送信されない場合があります。

これらはAppleによって課された制限であり、Push Storyを設計する際に考慮する必要があります。

#### Push Storyを自分に送信したが、縮小表示が表示された {#i-sent-myself-a-push-story-but-saw-the-condensed-view-instead}

すべてのページが読み込まれない特定の状況（たとえば、データ接続の喪失など）では、Push Storyは縮小された通知のみを表示します。

### Android

#### 画像をクリックした後にPush Storyが閉じない {#push-story-doesnt-dismiss-after-clicking-the-image}

デフォルトでは、Androidではユーザーが画像をクリックした後にPush Storiesは閉じられません。通知を閉じたい場合は、[`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721)を呼び出してください。