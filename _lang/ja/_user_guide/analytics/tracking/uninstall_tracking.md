---
nav_title: アンインストール追跡
article_title: アンインストール追跡
page_order: 1
page_type: reference
description: "このリファレンス記事では、キャンペーンレベルとアプリレベルの統計情報を得るためのアンインストール追跡の実装について説明します。"
tool: Reports

---

# アンインストール追跡 {#uninstall-tracking}

> この記事では、アプリのアンインストールの集計を時系列で表示し、傾向や異常を特定する方法と、キャンペーンレベルのアンインストールを追跡し、特定のキャンペーンがアプリのインストールを促進しているのか妨げているのかを判断する方法を紹介します。

Brazeのアンインストール追跡では、以下の詳細が提供されます。

1. アプリレベルの日次アンインストール統計情報: **ホーム**ページの時系列グラフに表示されます。
2. キャンペーンレベルのアンインストール統計情報: 特定キャンペーンの**Campaign Details**ページの時系列グラフに表示されます。この統計情報は、アンインストールしたキャンペーン受信者の日次数を示します。

{% alert note %}
Brazeダッシュボードでアンインストール追跡をオプトインする必要があります。この機能は、iOS、Android、Fire OSのアプリで利用できます。
{% endalert %}

## 仕組み {#how-it-works}

Brazeでは、通常のプッシュキャンペーンから基本レベルのアンインストール情報を自動的に収集します。しかし、ユーザーによってプッシュキャンペーンを受け取る頻度が異なる可能性があるため、アンインストール追跡を提供し、ユーザーのアンインストール活動をより正確に把握できるようにしています。

Brazeがアンインストールを検出すると、そのユーザーにはアンインストール済みのタグが付けられます。Campaignで**Has Not Uninstalled**フィルターを使用すると、これらのタグ付きユーザーは除外されます。ユーザーがアプリを再インストールしても開かなかった場合、アンインストールタグはプロファイルに残ります。タグが削除されるのは、再インストールしたアプリでユーザーが新しいセッションを開始したときのみです。つまり、再インストールしてもアプリを一度も開かないユーザーは、引き続きアンインストール済みとして表示されます。

アンインストール追跡の使い方については、ブログ記事 [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/) をご覧ください。

## アンインストール追跡をオンにする {#turning-on-uninstall-tracking}

アンインストール追跡は、追跡するアプリごとに、**設定**の**アプリ設定**ページで有効にできます。

アプリのアンインストール追跡を有効にすると、Brazeは24時間以内にセッションを記録していない、またはプッシュ通知を受信していないユーザーに対し、毎晩バックグラウンドでプッシュメッセージを送信します。

### 設定 {#configuration}

iOSアプリケーションのアンインストール追跡を設定するには、[ユーティリティメソッド]({{site.baseurl}}/developer_guide/analytics/tracking_uninstalls/?sdktab=swift)を使用します。Androidアプリケーションの場合は、[`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html)を使用します。Brazeがアンインストールを検出した場合、アンインストール追跡または通常のプッシュキャンペーン配信のいずれであっても、ユーザーにおけるアンインストールの最良推定時間を記録します。この時刻はユーザープロファイルに標準属性項目として保存され、win-backキャンペーンのユーザーSegmentを定義するために使用できます。

## アンインストールによるSegmentのフィルタリング {#filtering-segments-by-uninstalls}

**Uninstalled**フィルターを使用すると、一定期間内にアプリをアンインストールしたユーザーを選択できます。アンインストールの正確な時刻を特定することは難しいため、アンインストールフィルターには、アンインストールしたすべてのユーザーがある時点でSegmentに該当するように、より広い時間範囲を設定することを推奨します。

アンインストールに関する日次統計は**ホーム**ページに表示されます。

![アンインストールSegment。]({% image_buster /assets/img_archive/Uninstall_Segment.png %} "Uninstall Segment")

このグラフは、Brazeが提供する他の統計と同様に、アプリやSegmentごとに分類できます。**Performance overview**セクションで、日付範囲と、必要であればアプリを選択します。次に、**Performance Over Time**グラフまでスクロールダウンし、以下を実行します。

1. **Statistics For**ドロップダウンで、**Uninstalls**を選択します。
2. **Breakdown**ドロップダウンで、**By segment**を選択します。
3. **Breakdown Values**ドロップダウンで、グラフに含めるSegmentsを選択します。

{% alert note %}
アンインストール追跡が有効になっていないアプリでは、一部のユーザー（プッシュ通知対象のユーザー）のアンインストール数のみが報告されるため、日次アンインストール総数は表示されている数より多くなる可能性があります。
{% endalert %}

## Campaignのアンインストール追跡 {#uninstall-tracking-for-campaigns}

Campaignのアンインストール追跡は、特定のCampaignを受信し、その後選択した期間内にアプリをアンインストールしたユーザー数を示します。このツールは、Campaignが意図しないネガティブなユーザー行動を促している可能性についてのインサイトを提供し、Campaign全体の効果を測定するのに役立ちます。

Campaignのアンインストール統計は、特定のCampaignの**Campaign Analytics**ページにあります。マルチチャネルCampaignと多変量Campaignの場合、アンインストール数はそれぞれチャネル別とバリアント別の内訳で表示できます。

![キャンペーンレベルでのアンインストール。]({% image_buster /assets/img_archive/campaign_level_uninstall_tracking.png %})

### 仕組み

Brazeは、ユーザーのデバイスに送信されたプッシュメッセージがFirebase Cloud Messaging (FCM) またはApple Push Notification Service (APNs) から、アプリがインストールされていないというシグナルを返すタイミングを観察することで、アンインストールを追跡します。アプリでグローバルアンインストール追跡を有効にすると、Brazeはユーザーがアンインストールしたかどうかを検知するため、毎日サイレントプッシュメッセージを送信します。Brazeはこの「サイレント」プッシュをすべてのユーザーに送信します（ユーザーがアプリ設定でサイレントプッシュを無効にしていない限り）。このプッシュはユーザーには表示されません。Brazeがユーザーのアンインストールを検知した場合、以下の処理を行います。

* アプリの総アンインストール数を1増やします。
* ユーザーが過去24時間に正常に受信したすべてのCampaignのアンインストール数を1増やします。
* あるユーザーが24時間以内に3つのCampaignを受信し、その後アンインストールした場合、3つのCampaignすべてについて「アンインストール」のカウントを増加させます。

FCMとAPNsはアンインストール追跡に制限を設けています。Brazeは、FCMやAPNsからユーザーがアンインストールしたと通知があった場合にのみ、アンインストール数を増加させます。ただし、これらのサードパーティシステムは、いつでもアンインストールを通知してくる可能性があります。アンインストール追跡は、正確な統計ではなく方向性の傾向を検出するために使用してください。

Brazeは、以下のFCMレスポンスをトークン削除（アンインストール）レスポンスとして扱います: `DEVICE_UNREGISTERED`、`BAD_REGISTRATION`、`SENDER_ID_MISMATCH`。

アンインストール追跡の使い方については、ブログ記事 [Uninstall Tracking: An Industry Look at its Strengths and Limitations](https://www.braze.com/blog/uninstall-tracking-an-industry-look-at-its-strengths-and-limitations/) をご覧ください。

## トラブルシューティング {#troubleshooting}

### ユーザーのプロファイルはいつアンインストール済みとしてフラグが付けられますか？アンインストールタグはいつクリアされますか？ {#when-is-a-users-profile-flagged-as-uninstalled-when-is-the-uninstall-tag-cleared}

Brazeは、デバイス上にアプリが存在しないことを検出した時点で、ユーザーにアンインストール済みのフラグを付けます（検出方法については[仕組み](#how-it-works)を参照してください）。ユーザーがアプリを再インストールした後も、**アプリを開いて新しいセッションを開始する**まで、アンインストールタグはプロファイルに残ることがあります。再インストールだけではタグはクリアされません。そのセッションが開始されるまで、アンインストール状態を使用するSegmentやフィルター（例: **Has Not Uninstalled**）は、そのユーザーを引き続きアンインストール済みとして扱います。

### なぜ突然アンインストールが急増したのですか？ {#why-am-i-suddenly-seeing-a-spike-in-uninstalls}

アプリのアンインストール数が急増している場合、Firebase Cloud Messaging (FCM) とApple Push Notification Service (APNs) が古いトークンを異なる頻度で取り消したことが原因である可能性があります。

{% alert note %}
プライバシー上の理由から、Brazeのプッシュプロバイダーは不定期にトークンを無効化する場合があります。つまり、特定の期間においてアンインストール数が急増することがあります。<br><br>これらの変更を検証するには、アンインストール追跡と、直接プッシュ開封率などのユーザー行動指標を併せて監視してください。アンインストール数が急増しても直接プッシュの開封率が安定している場合、この急増は実際のユーザー行動ではなく、パートナーが古いトークンを無効化したことを反映している可能性が高いです。
{% endalert %}

### 特定のCampaignがアンインストールの原因かどうかを判断するにはどうすればよいですか？ {#how-do-i-determine-if-a-specific-campaign-caused-uninstalls}

アンインストールの急増が発生した時期と同じ頃にメッセージを送信したCampaignの分析を確認してください。特定のメッセージがアンインストールの増加と相関している場合、そのメッセージがユーザーのアンインストールに影響を与えている可能性があります。

Segmentごとのアンインストールを表示するには:
1. ダッシュボードの**ホーム**ページに移動します。
2. **Performance Over Time**セクションで、**Statistics For**に**Uninstalls**を、**Breakdown**に**By Segment**を選択します。

[分析トラッキング]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)が有効な離脱ユーザーを追跡するSegmentがある場合、そのアンインストール傾向をアプリ全体の傾向と比較してください。

### アンインストールが本物であることを確認するにはどうすればよいですか？ {#how-do-i-confirm-uninstalls-are-genuine}

APNsの場合、ユーザープロファイルで `BadDeviceToken` プッシュエラーを確認してください。このエラーがアンインストールの急増と同じ時期に大量に発生している場合、アンインストールは本物である可能性が高いです。`BadDeviceToken` は、デバイスのプッシュトークンが無効になったことを示しており、これは通常アプリがアンインストールされた場合に発生します。

### アプリのアンインストール数がAPNsの内容と異なるのはなぜですか？ {#why-are-the-number-of-app-uninstalls-different-from-whats-in-apns}

この差異は想定されるものです。

Appleはランダムスケジュールを使用して、プッシュトークンが無効になった時点の報告を遅延させます。つまり、ユーザーがアプリをアンインストールした後でも、APNsは一定期間プッシュ通知に対して成功応答を返し続ける可能性があります。この遅延は意図的なものであり、ユーザーのプライバシーを保護することを目的としています。APNsが無効なトークンに対して `410` ステータスを返すまで、バウンスや失敗は報告されません。