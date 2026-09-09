---
nav_title: "ユーザーリターゲティング"
article_title: "ユーザーリターゲティング"
description: "このリファレンス記事では、ユーザーのSMSおよびRCSインタラクションに基づいてメッセージをリターゲティングする方法について説明します。"
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# ユーザーリターゲティング {#user-retargeting}

> Brazeは、ユーザーの購読状態の変更や受信キーワードに基づく自動応答の送信に加えて、ユーザープロファイルにインタラクションを記録し、メッセージのフィルタリングやトリガーに活用できるようにします。<br><br>これらのフィルターとトリガーにより、SMS、MMS、RCSキャンペーンを送信されたユーザーや応答したユーザーに基づいてアクションをフィルタリングしたり、短縮URLをクリックしたユーザーにさらにエンゲージしたりすることができます。

{% alert tip %}
カスタムキーワードの詳細や、これらのリターゲティングオプションを活用するための双方向メッセージングの設定方法については、[カスタムキーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling)の記事をご覧ください。
{% endalert %}

## リターゲティングオプション {#retargeting-options}

{% alert note %}
ユーザーリターゲティングでオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりすることや、CUPの「販売または共有の拒否」権利などのプライバシー法に準拠することが必要になる場合があります。マーケターは、キャンバスやキャンペーンのエントリ条件内で、ユーザーの適格性に関する適切なフィルターを実装する必要があります。
{% endalert %}

### SMS、MMS、RCSでユーザーをフィルタリングする {#filter-users-by-sms-mms-and-rcs}

ユーザーは、最後にSMS、MMS、またはRCSを受信した日時や、特定のキャンペーンからSMS、MMS、またはRCSを受信したかどうかでフィルタリングできます。フィルターは、キャンペーンビルダーの**ターゲットオーディエンス**ステップで設定できます。

{% alert note %}
メッセージが受信、開封、またはクリックされると、Brazeはインタラクションを記録したプロファイルと同じ電話番号を共有するすべてのプロファイルのデータを更新します。そのため、メッセージを受信、開封、またはクリックした人と電話番号を共有しているユーザーは、元々キャンペーンの対象外であったり、直接メッセージが送信されていなくても、このフィルターに一致する場合があります。
{% endalert %}

#### 最後にSMS/MMS/RCSを受信した日時でフィルタリング {#filter-by-last-received-smsmmsrcs}

![2020年12月8日以降にSMSを最後に受信したことによるセグメンテーションフィルター。]({% image_buster /assets/img/sms/filter2.png %})

#### SMS/MMS/RCSキャンペーンからの受信メッセージでフィルタリング {#filter-by-received-messages-from-smsmmsrcs-campaign}

特定のキャンペーンからメッセージを受信したユーザーをフィルタリングします。このフィルターでは、キャンペーンからメッセージを受信していないユーザーを除外するオプションもあります。

![「SMSリターゲティング」キャンペーンからメッセージを受信したかどうかによるセグメンテーションフィルター。]({% image_buster /assets/img/sms/filter1.png %})

### ユーザーがSMS、MMS、またはRCSを受信した際にメッセージをトリガーする {#trigger-messages}

特定のキャンペーンからユーザーがSMS、MMS、またはRCSメッセージを受信した際にメッセージをトリガーするには、アクションベースのキャンペーンのトリガーアクションとして**キャンペーンとのインタラクション**を選択します。次に、**SMSを受信**と使用するキャンペーンを選択します。

![特定のキャンペーンからユーザーがSMS、MMS、またはRCSメッセージを受信した際にメッセージをトリガーするには、アクションベースのキャンペーンのトリガーアクションとして「キャンペーンとのインタラクション」を選択します。次に、「SMSを受信」と使用するSMS、MMS、またはRCSキャンペーンを選択します。]({% image_buster /assets/img/sms/trigger.png %})

### 高度なトラッキングリンクでフィルタリング {#filter-by-advanced-tracking-links}

[高度なトラッキングリンク]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening)を含むキャンペーンをクリックしたユーザーをリターゲティングします。
高度なトラッキングが有効になっているキャンペーンのみが、以下のドロップダウンに表示されます。

#### 特定のSMS、MMS、またはRCSキャンペーンをクリックしたユーザーをリターゲティングする {#retarget-users-who-have-clicked-a-specific-sms-mms-or-rcs-campaign}

1. **Clicked/Opened キャンペーン**フィルターを使用してセグメントを作成します。
2. **clicked shortened sms link**を選択します。
3. 目的のキャンペーンを選択します。

![特定のSMS、MMS、またはRCSキャンペーンをクリックしたユーザーのリターゲティングに関するスクリーンショット。]({% image_buster /assets/img/sms/retargeting5.png %})

#### 特定のキャンバスステップをクリックしたユーザーをリターゲティングする {#retarget-users-who-have-clicked-a-specific-canvas-step}

1. **Clicked/Opened Step**フィルターを使用してセグメントを作成します。
2. **clicked shortened sms link**を選択します。
3. 目的のキャンバスとキャンバスステップを選択します。

![特定のキャンバスステップをクリックしたユーザーのリターゲティングに関するスクリーンショット。]({% image_buster /assets/img/keyword_example1.jpg %})

## キーワードカテゴリ固有のリターゲティング {#keyword-category-specific-retargeting}

3つのデフォルトキーワードカテゴリ（オプトイン、オプトアウト、ヘルプ）に加えて、最大25個の独自のキーワードカテゴリを作成することもでき、任意のキーワードと応答を識別できます。これらのカテゴリは、フィルタリングやリターゲティングに使用できます。グローバルキーワードカテゴリとその設定方法の詳細については、[キーワード処理]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing)を参照してください。

### 最新度でフィルタリング {#filter-by-recency}

ユーザーがSMS、MMS、またはRCSプログラムに応答した最新度でフィルタリングします。このフィルターは、ユーザーがいずれかのキーワードカテゴリ内のインバウンドメッセージを最後に送信した日付を評価します。

![セグメンテーションフィルター「購読グループ"Marketing SMS"にSMSを最後に送信した日」キーワード「オプトイン」2020年8月11日以降。]({% image_buster /assets/img/sms/retargeting1.png %})

### キャンペーンまたはキャンバスのアトリビューションでフィルタリング {#filter-by-campaign-or-canvas-attribution}

特定のSMS、MMS、またはRCSキャンペーンやキャンバスコンポーネント、キーワードカテゴリ、またはタグに返信したユーザーをフィルタリングします。

{% alert note %}
これらのフィルターは[メッセージングインタラクションデータ]({{site.baseurl}}/messaging_interaction_data)を使用します。停止されたキャンペーンやキャンバスの場合、そのデータはアクティブなリターゲティングフィルターで使用されない限り、3か月後に期限切れになります。期限切れのデータは復元できます。ワークスペースのリテンション期間はデフォルトと異なる場合があります。
{% endalert %}

#### キーワードカテゴリ付きの特定キャンペーンへの返信でフィルタリング {#filter-by-replied-to-a-specific-campaign-with-keyword-category}

![キャンペーン「SMS-283」「Promotion」に対して「SMSに返信した」フィルターを使用したキャンペーン。]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

#### 特定タグ付きのキャンペーンまたはキャンバスへの返信でフィルタリング {#filter-by-replied-to-a-campaign-or-canvas-with-a-specific-tag}

![タグ「Curbside Messaging Service C」が付いたキャンペーンまたはキャンバスに対して「SMSに返信した」フィルターを使用したキャンペーン。]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

#### 特定ステップへの返信でフィルタリング {#filter-by-replied-to-a-specific-step}

![ステップ「SMS Double Opt」「Step - Help」に対して「SMSに返信した」フィルターを使用したキャンペーン。]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### キーワードによるメッセージのトリガー {#trigger-messages-by-keyword}

メッセージは、キーワードカテゴリ（ユーザーがいずれかのキーワードを送信した場合）またはその他のキーワード（ユーザーが既存のカテゴリに該当しないキーワードを送信した場合）に基づいて、ユーザーがインバウンドメッセージを送信した際にトリガーできます。これらのトリガーは、キャンペーンビルダーの配信ステップで設定します。

インバウンドメッセージが定義されたトリガーイベントに一致するかどうかを評価する際、評価開始前に先頭と末尾のスペースが削除されます。

{% alert tip %}
アクションベースのキャンバスがインバウンドSMSまたはMMSメッセージによってトリガーされた場合、次のアクションパスまでの任意のキャンバスステップで[サポートされているSMS Liquidプロパティ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)を参照できます。
{% endalert %}

#### インバウンドキーワードカテゴリによるトリガー {#trigger-by-inbound-keyword-category}

![セグメンテーションフィルター「購読グループ"Marketing SMS"にキーワード"オプトイン"を送信」を使用したアクションベースのSMSキャンペーン。]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

#### 任意のキーワードによるトリガー {#trigger-by-arbitrary-keywords}

「その他」のキーワード応答でメッセージをトリガーする場合、キーワード本文を完全一致テキストで評価できます。この一致は前述と同じルールに従います。**正確な単一単語のメッセージ**のみが処理されます（大文字小文字は*区別しません*）。`Hello Braze!` というキーワードが送信された場合、以下の例に示す条件には一致しません。

![キーワードカテゴリが「その他」で、メッセージ本文が正確に「Hello」または「Hey」であるアクションベースのSMSキャンペーン。]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

#### キーワードのテンプレート化 {#template-keywords}

インバウンドSMSまたはMMSでキャンペーンやキャンバスコンポーネントをトリガーする場合、ユーザーが送信したテキストやメディア添付ファイルをLiquidを使用してキャンペーンやキャンバスの本文にオプションでテンプレート化できます。これにより、ユーザーの応答にアクセスし、返信に含めたり、条件付きロジックを適用したり、Liquidで可能なあらゆる処理を行うことができます。

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}