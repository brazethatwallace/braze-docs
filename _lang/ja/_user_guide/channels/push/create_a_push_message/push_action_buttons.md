---
nav_title: "プッシュアクションボタン"
article_title: "プッシュアクションボタン"
page_order: 1
page_type: reference
description: "このリファレンス記事では、プッシュアクションボタンの概要と、iOSおよびAndroidプラットフォーム間の違いについて説明します。"
channel:
  - Push

---

# プッシュアクションボタン {#push-action-buttons}

> プッシュアクションボタンを使用すると、BrazeのiOSおよびAndroidプッシュ通知を使用する際に、ボタンのコンテンツとアクションを設定できます。アクションボタンを使用すると、ユーザーはアプリ内のエクスペリエンスにクリックして移動することなく、通知から直接アプリを操作できます。

![「承認」と「辞退」の2つのプッシュアクションボタンが表示されたiOSプッシュ通知。]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

## アクションボタンの作成 {#creating-action-buttons}

各インタラクティブボタンは、Webページやディープリンクにリンクしたり、アプリを開いたりすることができます。

- 標準のプッシュCampaignの場合、ダッシュボードのプッシュメッセージ作成画面の**On-Click Behavior**セクションでプッシュアクションボタンを指定できます。
- [マルチプラットフォームプッシュCampaign]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push/)の場合、**設定**タブで各プラットフォームごとにアクションボタンを個別に設定できます。

{% tabs %}
{% tab iOS %}
### iOS {#ios}

iOSプッシュメッセージでアクションボタンを使用するには、以下の手順に従ってください。

1. **作成**タブでアクションボタンを有効にします。
2. 以下の利用可能なボタンの組み合わせから**iOS Notification Category**を選択します。
 - Accept / Decline
 - Yes / No
 - Confirm / Cancel
 - More
 - 事前登録済みのカスタムiOSカテゴリ

![iOS Notification Categoryのドロップダウンメニュー。]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
iOSのボタン処理の仕様により、プッシュアクションボタンを設定する際には追加の統合ステップが必要です。詳細は[開発者ドキュメント]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories)に記載されています。特に、iOSカテゴリを設定するか、特定のデフォルトボタンオプションから選択する必要があります。Androidの統合では、これらのボタンは自動的に動作します。
{% endalert %}

**Yes** / **No**などのプリセットペアでは、2番目のボタンがデフォルトで却下（**CLOSE**）アクションにマッピングされるため、1番目のボタンと同じようにアプリを開くことはありません。**_直接開封数_**にはこの種のタップは含まれませんが、CurrentsやSnowflakeの**Push Notification Open**データでは、`button_action_type`と`button_string`とともにログに記録される場合があります。詳細については、[プッシュアクションボタンとレポート]({{site.baseurl}}/user_guide/channels/push/reporting/#push-action-buttons-and-reporting)を参照してください。
{% endtab %}
{% tab Android %}
### Android {#android}

Androidプッシュメッセージでアクションボタンを使用するには、以下の手順に従ってください。

1. **作成**タブでアクションボタンを有効にします。
2. <i class="fas fa-plus-circle"></i> **Add Button**を選択し、ボタンテキストと**On-Click Behavior**を指定します。以下の利用可能なアクションから選択できます。
  - Open App
  - Redirect to Web URL
  - アプリケーションへの[ディープリンク]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/)

![通知ボタンのクリック時の動作として「Open App」を選択している画面。]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

プッシュには最大3つのボタンを追加できます。

#### Androidの文字数制限 {#android-character-limits}

スタック表示されるiOSボタンとは異なり、Androidボタンは横一列に並んで表示されます。つまり、ボタンを追加するほど（最大3つ）、ボタンのコピーに使えるスペースが少なくなります。

![テキストが切り詰められたAndroidプッシュアクションボタン。]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

以下の表は、ボタンの数に応じて、ボタンのコピーが切り詰められるまでに追加できる文字数を示しています。

| ボタン数 | ボタンあたりの最大文字数 |
| --- | --- |
| 1 | 46文字 |
| 2 | 20文字 |
| 3 | 11文字 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Androidの文字数制限" }
{% endtab %}
{% endtabs %}