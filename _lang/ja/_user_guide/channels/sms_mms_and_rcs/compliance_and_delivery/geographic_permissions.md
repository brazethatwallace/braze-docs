---
nav_title: "地理的権限"
article_title: "地理的権限"
description: "この記事では、地理的権限の国許可リストについて説明します。これにより、SMS、MMS、RCSを配信できる国を選択できます。"
page_order: 4
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# 地理的権限 {#geographic-permissions}

> 地理的権限は、メッセージを送信できる国に対するコントロールを適用することで、セキュリティを強化し、不正なSMS、MMS、RCSトラフィックから保護します。国の許可リストを指定して、SMS、MMS、RCSメッセージが承認された地域にのみ送信されるようにできます。国の許可リストを変更できるのは管理者のみです。管理者以外のユーザーは、サブスクリプショングループがどの国に送信できるかを示す読み取り専用バージョンの許可リストにアクセスできます。

管理者の場合、許可リストに含める国を設定できます。国の許可リストは[サブスクリプショングループ]({{site.baseurl}}/sms_rcs_subscription_groups/)レベルで設定されます。**オーディエンス** > **サブスクリプション**に移動し、SMS、MMS、またはRCSサブスクリプショングループを選択してアクセスできます。許可リストは**Geographic Permissions**の下にあります。

![管理者向けの編集可能なSMS地理的権限セクション。「Country allowlist」にいくつかの国が選択されている。]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

### 国の選択 {#selecting-countries}

ドロップダウンを使用して許可リストに国を追加します。最も一般的なSMSおよびRCSの国が上部に表示され、その他の国はその下に表示されます。テキストフィールドに入力して国を検索することもできます。

![「Country allowlist」ドロップダウン。最も一般的な国が上部に表示されている。]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

以前に選択した国を削除するには、その横にあるチェックボックスをクリアします。

### 変更の保存 {#saving-your-changes}

変更は**Save**を選択した後に有効になります。許可リストから国を削除すると、それらの国の番号へのすべてのSMS、MMS、RCSメッセージの送信が停止されます。

![許可リストから削除される国を確認する警告モーダル。]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## 高リスクの国 {#high-risk-countries}

特定の国では、SMSおよびRCSトラフィックポンピングのリスクが高くなっています。これらの国は、国のドロップダウンで**High Risk**タグで示されます。

![国のドロップダウンでアゼルバイジャンに「High Risk」タグが表示されている。]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

これらの国への送信を許可する場合、その国が許可リストに追加される前に、まずリスクを承認する必要があります。

{% alert note %}
許可リストの国は、ビジネスニーズをサポートするために必要な国のみに制限してください。これにより、不正トラフィックの可能性を最小限に抑えることができます。SMSトラフィックポンピングの防止に関する詳細なガイダンスについては、[SMSトラフィックポンピング詐欺FAQ]({{site.baseurl}}/sms_traffic_pumping_fraud/)をご覧ください。
{% endalert %}

## ブロックされた送信の可視性 {#visibility-of-blocked-sends}

許可リストにない国への送信試行は中止されます。中止されたメッセージは[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log/)および[SMS中止メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)に記録されます。

ブロックされた送信による中止メッセージは**Aborted Message Errors**として表示され、「The recipient's phone number is in a blocked country」というメッセージが含まれます。

![中止ログ。電話番号がブロックされた国にあるためブロックされた複数のSMS送信が表示されている。]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}