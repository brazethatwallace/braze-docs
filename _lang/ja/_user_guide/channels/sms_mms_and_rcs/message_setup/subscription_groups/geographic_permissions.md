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

ドロップダウンを使用して許可リストに国を追加します。最も一般的なSMS、MMS、RCSの国が上部に表示され、その他の国はその下のセクションに表示されます。テキストフィールドに入力して国を検索することもできます。

![「Country allowlist」ドロップダウン。最も一般的な国が上部に表示されている。]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

以前に選択した国を削除するには、その横にあるチェックボックスをクリアします。

### 変更の保存 {#saving-your-changes}

変更は保存後に有効になります。許可リストから国を削除すると、それらの国のダイヤルコードを持つ電話番号へのすべてのSMS、MMS、RCSメッセージの送信が停止されます。

![許可リストから削除される国を確認する警告モーダル。]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## 不正リスクの高い国 {#high-fraud-risk-countries}

特定の国では、SMS、MMS、RCSトラフィックポンピングのリスクが高くなっています。これらの国は、国のドロップダウンで**High Fraud Risk**タグで示されます。

![国のドロップダウンでアゼルバイジャンに「High Fraud Risk」タグが表示されている。]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

これらの国への送信を許可する場合、その国が許可リストに追加される前に、まずリスクを承認する必要があります。

{% alert note %}
許可リストの国は、ビジネスニーズをサポートするために必要な国のみに制限してください。これにより、不正トラフィックの可能性を最小限に抑えることができます。SMS、MMS、RCSトラフィックポンピングの防止に関する詳細なガイダンスについては、[SMSトラフィックポンピング詐欺に関するFAQ]({{site.baseurl}}/sms_traffic_pumping_fraud)をご覧ください。
{% endalert %}

## 許可リスト外への送信の可視性 {#visibility-of-sends-outside-the-allowlist}

国の許可リストに含まれていない国への送信試行は中止されます。中止されたメッセージは[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)および[SMS中止メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)に記録されます。

許可リストに含まれていない国の受信者に対する中止メッセージは、**Aborted Message Errors**として表示され、「The recipient's phone number is in a blocked country」というメッセージが表示されます。

![SMS、MMS、RCSの送信が電話番号の国が許可リストにないため中止されたことを示す中止ログ。]({% image_buster /assets/img/sms/abort_log.png %}){: style="max-width:80%;"}

## 不正リスクの高い国とトラフィックポンピング詐欺に関する重要なお知らせ {#important-notice-for-high-fraud-risk-countries-and-traffic-pumping-fraud}

### SMS、MMS、RCSトラフィックポンピングとは？ {#what-is-sms-mms-and-rcs-traffic-pumping}

SMS、MMS、RCSトラフィックポンピング（人為的に膨張されたトラフィックとも呼ばれます）は、顧客に重大な財務的リスクをもたらす可能性のある、増加傾向にある詐欺スキームです。詐欺者は、保護されていない公開Webフォーム、認証フロー、またはAPIエンドポイントを悪用して、自分が管理または影響力を持つ電話番号に大量のSMS、MMS、RCS送信（オプトイン確認、ワンタイムパスワード、通知など）をトリガーすることができます。攻撃者は、その人為的なトラフィックを生成することで、共謀しているまたは関知していないモバイルネットワークから収益分配を受け取ります。その下流への影響は、重大な財務的リスクをもたらします。

### 不正リスクの高い国とは？ {#what-are-high-fraud-risk-countries}

ある国または地域が不正リスクが高いと指定されるのは、小規模なプレミアムレートのローカルローミングキャリアの密度が異常に高い場合、または厳格な規制監督が欠如している場合です。悪意のある行為者は、メッセージごとの収益分配の支払いを最大化するため、これらの高レートキャリアネットワークを体系的に標的にします。

さらに、システムルーティングの制限は、受信者の実際の物理的な場所ではなく、送信先の国コードに基づいて適用されます。つまり、頻繁に旅行する顧客がいる場合、メッセージングは現在の物理的な場所ではなく元の送信先国コードに基づいてルーティングされるため、旅行先の場所を国の許可リストに追加する必要はありません。たとえば、リスクの低い地域と国コードを共有する地域（ジャージーやガーンジーが英国と+44の国コードを共有しているなど）でも、高いキャリアレートのリスクがあり、同じ不正リスクの高いフレームワーク条件の下で管理されます。

### 顧客の責任と財務的責任 {#customer-responsibility-and-financial-liability}

顧客は、SMS、MMS、RCSトラフィックポンピングによるメッセージを含め、顧客に代わってサービスを通じて送信されたすべてのモバイルメッセージに対して責任を負い、請求されます。国の許可リストなどのプラットフォームのセーフガードは、信頼できる地域への配信を制限するのに役立ちます。ただし、最終的には、外部向けエンドポイントのセキュリティを確保し、壊滅的な財務的損害を防止することは、顧客の単独の責任です。

### トラフィックポンピングを防止する方法 {#how-to-prevent-traffic-pumping}

実際の顧客が居住する地理的地域にメッセージ配信を厳密に制限しないと、詐欺や深刻な財務的損害に対する脆弱性が即座に生じます。会社を保護するために、国の許可リストを使用して配信地域を積極的に制限する必要があります。さらに、最も重要なこととして、[SMS、MMS、RCSトラフィックポンピング詐欺の理解と防止]({{site.baseurl}}/sms_traffic_pumping_fraud)に記載されている業界のベストプラクティスに従って、SMS、MMS、RCS送信をトリガーするオンラインの電話番号リクエストフォームまたはAPIエンドポイントを保護する必要があります。