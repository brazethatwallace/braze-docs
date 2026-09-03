---
nav_title: "Windowsオブジェクト"
article_title: Windowsメッセージングオブジェクト
page_order: 14
page_type: reference
channel: push
platform:
  - Windows Universal
description: "このリファレンス記事では、Brazeで使用されるさまざまなWindowsオブジェクトを一覧にして説明します。"
hidden: true
---
# Windowsオブジェクト仕様 {#windows-object-specification}

`windows_phone8_push`および`windows_universal_push`オブジェクトは、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を介して、Windows Phone 8 PushおよびWindows Universal Pushコンテンツに関連する情報を定義または要求するために使用されます。

## Windows Phone 8 プッシュオブジェクト {#windows-phone-8-push-object}

```json
{
   "push_type": (optional, string) must be "toast",
   "toast_title": (optional, string) the notification title,
   "toast_content": (required, string) the notification message,
   "toast_navigation_uri": (optional, string) page uri to send user to,
   "toast_hash": (optional, object) additional keys and values to send,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Phone 8 Push Message)
}
```

## Windows Universalプッシュオブジェクト {#windows-universal-push-object}

`push_type`のオプションの詳細については、Windows Universalの[トーストテンプレートカタログ](https://msdn.microsoft.com/en-us/library/windows/apps/hh761494.aspx)を参照してください。

```json
{
   "push_type": (required, string) one of: "toast_text_01", "toast_text_02", "toast_text_03", "toast_text_04", "toast_image_and_text_01", "toast_image_and_text_02", "toast_image_and_text_03", or "toast_image_and_text_04",
   "toast_text1": (required, string) the first line of text in the template,
   "toast_text2": (optional, string) the second line of text (for templates with > 1 line of text),
   "toast_text3": (optional, string) the third line of text (for the *_04 templates),
   "toast_text_img_name": (optional, string) the path for the image for the templates that include an image,
   "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under (must be a Windows Universal Push Message),
   "extra_launch_string": (optional, string) used to add deep linking functionality by passing extra values to the launch string
}
```

`extra_launch_string`パラメーターを使用した[ディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#what-is-deep-linking)の詳細については、[Windows Universalでのディープリンク]({{site.baseurl}}/hidden/archive_docs/windows_universal/push_notifications#step-5-deep-linking-from-push-into-your-app)を参照してください。