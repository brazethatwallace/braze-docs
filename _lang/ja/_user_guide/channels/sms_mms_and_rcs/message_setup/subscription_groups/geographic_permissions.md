---
nav_title: "地理的権限"
article_title: "地理的権限"
description: "この記事では、地理的権限の国許可リストについて説明します。これにより、SMS、MMS、RCSを配信できる国を選択できます。"
page_order: 0
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/

---

# 地理的権限 {#geographic-permissions}

> 地理的権限は、メッセージを送信できる国に対するコントロールを適用することで、セキュリティを強化し、不正なSMS、MMS、RCSトラフィックから保護します。国の許可リストを指定して、SMS、MMS、RCSメッセージが承認された地域にのみ送信されるようにできます。メッセージは、それらの国のダイヤルコードを持つ電話番号にのみ送信されます。<br><br> 国の許可リストを変更できるのは管理者のみです。管理者以外のユーザーは、購読グループがどの国に送信できるかを示す読み取り専用バージョンの許可リストにアクセスできます。

管理者の場合、許可リストに含める国を設定できます。国の許可リストは[購読グループ]({{site.baseurl}}/sms_rcs_subscription_groups)レベルで設定されます。**オーディエンス** > **購読グループ管理**に移動し、SMS、MMS、またはRCSの購読グループを選択してアクセスできます。許可リストは**Geographic Permissions**の下にあります。

![管理者向けの編集可能な地理的権限セクション。「Country allowlist」にいくつかの国が選択されている。]({% image_buster /assets/img/sms/sms_geographic_permissions.png %}){: style="max-width:80%;"}

## 国の選択 {#selecting-countries}

ドロップダウンを使用して、許可リストに国を追加します。最も一般的なSMS、MMS、RCSの国が上部に表示され、その他の国はその下のセクションに表示されます。テキストフィールドに入力して国を検索することもできます。

![最も一般的な国が上部に表示されている「国の許可リスト」ドロップダウン。]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

以前に選択した国を削除するには、その横にあるチェックボックスをクリアします。

### 変更の保存 {#saving-your-changes}

変更は保存後に有効になります。許可リストから国を削除すると、その国のダイヤルコードを持つ電話番号へのすべてのSMS、MMS、RCSメッセージの送信が停止されます。

![許可リストから削除される国を確認する警告モーダル。]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## 不正リスクの高い国 {#high-fraud-risk-countries}

特定の国では、SMS、MMS、およびRCSトラフィックポンピングのリスクが高くなっています。これらの国は、国のドロップダウンで**High Fraud Risk**タグによって示されます。

![アゼルバイジャンに「High Fraud Risk」タグが表示された国のドロップダウン。]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

これらの国への送信を許可する場合、その国が許可リストに追加される前に、リスクを承認する必要があります。

{% alert note %}
許可リストの国は、ビジネスニーズをサポートするために必要な国のみに制限してください。これにより、不正トラフィックの可能性を最小限に抑えることができます。SMS、MMS、およびRCSトラフィックポンピングの防止に関する詳細なガイダンスについては、[SMSトラフィックポンピング詐欺FAQ]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud)をご覧ください。
{% endalert %}

## 許可リスト外の送信の表示 {#visibility-of-sends-outside-the-allowlist}

国の許可リストに含まれていない国への送信は中止されます。中止されたメッセージは[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)および[SMS中止メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)に記録されます。

許可リストに含まれていない国の受信者に対する中止メッセージは、**Aborted Message Errors** として表示され、「The recipient's phone number is in a blocked country」というメッセージが含まれます。

![電話番号の国が国の許可リストに含まれていないため、SMS、MMS、RCS の送信が中止されたことを示す中止ログ。]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## 高リスク詐欺国とトラフィックポンピング詐欺に関する重要なお知らせ {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### SMS、MMS、RCSトラフィックポンピングとは？ {#what-is-sms-mms-and-rcs-traffic-pumping}

SMS、MMS、RCSトラフィックポンピング（人為的トラフィック膨張とも呼ばれます）は、顧客に重大な財務リスクをもたらす可能性のある、拡大する詐欺スキームです。詐欺師は、保護されていない公開Webフォーム、認証フロー、またはAPIエンドポイントを悪用して、自分たちが管理または影響を及ぼす電話番号に対して大量のSMS、MMS、RCSの送信（オプトイン確認、ワンタイムパスワード、通知など）をトリガーすることがあります。攻撃者は、その人為的なトラフィックを生成することで、共謀している、または知らずに加担しているモバイルネットワークから収益の分配を受け取ります。この下流への影響は、重大な財務リスクをもたらします。

### 高リスク詐欺国とは？ {#what-are-high-fraud-risk-countries}

ある国や地域が高リスク詐欺として指定されるのは、小規模でプレミアムレートのローカルローミングキャリアの密度が異常に高い場合、または厳格な規制監督が欠如している場合です。悪意のある行為者は、メッセージごとの収益分配の支払いを最大化するため、これらの高料金キャリアネットワークを体系的に標的にします。

さらに、システムのルーティング制限は、受信者の実際の物理的な場所ではなく、宛先の国コードに基づいて適用されます。つまり、頻繁に旅行する顧客がいる場合でも、メッセージングは現在の物理的な場所ではなく元の宛先国コードに基づいてルーティングされるため、旅行先を国別許可リストに追加する必要はありません。たとえば、英国と+44の国コードを共有するジャージーやガーンジーなど、リスクの低い地域と国コードを共有している地域でも、キャリアの高料金リスクがあり、同じ高リスク詐欺フレームワークの条件下で管理されます。

### 顧客の責任と財務上の責任 {#customer-responsibility-and-financial-liability}

顧客は、SMS、MMS、RCSトラフィックポンピングによって生じたメッセージを含め、顧客に代わってサービスを通じて送信されたすべてのモバイルメッセージについて責任を負い、請求されます。国別許可リストなどのプラットフォームの保護機能は、信頼できる地域への配信を制限するのに役立ちます。ただし、最終的には、外部向けエンドポイントのセキュリティ確保と壊滅的な財務被害の防止は、顧客の唯一の責任です。

### トラフィックポンピングを防ぐには {#how-to-prevent-traffic-pumping}

メッセージの配信を、実際の顧客が居住する地理的地域に厳密に限定しない場合、詐欺や深刻な財務被害に対して即座に脆弱になります。会社を保護するために、国別許可リストを使用して配信地域を事前に制限する必要があります。さらに、最も重要なこととして、SMS、MMS、RCSの送信をトリガーするオンラインの電話番号リクエストフォームやAPIエンドポイントを、業界のベストプラクティスに従って保護する必要があります。詳しくは[SMS、MMS、RCSトラフィックポンピング詐欺の理解と防止]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/sms_traffic_pumping_fraud)をご覧ください。