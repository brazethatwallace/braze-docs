---
nav_title: 9月
page_order: 5
noindex: true
page_type: update
description: "この記事には2018年9月のリリースノートが含まれています。"
---
# 2018年9月 {#september-2018}

## iOS 12の通知グループ：追加機能 {#ios-12-notification-groups-additional-abilities}

Brazeを使って[Appleの通知グループ機能]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#notification-groups)にアクセスできるようになりました！概要引数とグループの追加、重要なアラートの利用、仮承認済みユーザーのフィルタリング、ユーザープロファイルでの仮承認ステータスの表示が可能です。

## サイレント時間 {#quiet-time}

キャンバスに[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-5-select-your-send-settings)（メッセージを送信しない時間帯）を指定できるようになりました。**キャンバスの送信設定**で「サイレント時間を有効にする」にチェックを入れるだけです。次に、ユーザーの現地時間でサイレント時間を選択し、そのサイレント時間内にメッセージがトリガーされた場合の後続のアクションを選択します。

キャンペーンでも、「1日のうち特定の時間帯にこのメッセージを送信する」の代わりにサイレント時間を使用するようになりました。

## Adjustのお客様 {#adjust-customers}

[Adjust]({{site.baseurl}}/partners/message_orchestration/attribution/adjust/)を使用しているBrazeのお客様が、Braze APIキーとBrazeインスタンスURLを確認できるようになりました。これらはAdjustプラットフォームでの統合に使用します。

## セグメント除外フィルター {#not-in-segment-filter}

[特定のセグメントに含まれていない]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#retargeting)ユーザーからセグメントを作成できるようになりました。

## キャンバス受信者のCSVエクスポート {#canvas-recipient-csv-exports}

キャンバスにエントリーしたユーザーの[データをエクスポート]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data/)できるようになりました。生成されるCSVはキャンペーンのCSVと同様のものになります。

## iOS 12の仮承認セグメントフィルター {#provisionally-authorized-ios-12-segment-filter}

特定のアプリのiOS 12で仮承認されているユーザーを見つけることができる[セグメントフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#other)が追加されました。

## アプリ内メッセージ画像アップローダー {#in-app-message-image-uploader}

アプリ内メッセージ用の画像アップローダーがデザインパネルから作成パネルに移動しました。

## ユーザープロファイルページの読み取り専用権限 {#read-only-permissions-on-user-profile-page}

このリリースより前は、[読み取り専用権限]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#available-limited-and-team-role-permissions)を持つユーザープロファイルでサブスクリプションステータスとメールアドレスを変更できました。`import_user`権限の名前を`import_and_update_user`権限に変更し、サブスクリプションステータスとメールアドレスの編集アクセスを制限しました。現在、開発者が読み取り専用でなりすましている場合やこの権限を持っていない場合、サブスクリプションステータスやメールアドレスを変更することはできません。