---
nav_title: "ユーザーリターゲティング"
article_title: "ユーザーリターゲティング"
description: "このリファレンス記事では、ユーザーのSMSおよびRCSインタラクションに基づいてメッセージをリターゲティングする方法について説明します。"
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - キャンペーン
channel:
  - SMS
  - MMS
  - RCS

---

# ユーザーリターゲティング {#user-retargeting}

> Brazeは、ユーザーのサブスクリプション状態の変更や受信キーワードに基づく自動応答の送信に加えて、ユーザープロファイルにインタラクションを記録し、メッセージのフィルタリングやトリガーに活用できるようにします。<br><br>これらのフィルターとトリガーにより、SMS、MMS、RCSのキャンペーンを送信されたユーザーや応答したユーザーに基づいてアクションをフィルタリングしたり、短縮URLをクリックしたユーザーにさらにエンゲージしたりすることができます。

{% alert tip %}
カスタムキーワードの詳細や、これらのリターゲティングオプションを活用するための双方向メッセージングの設定方法については、[カスタムキーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/)の記事をご覧ください。
{% endalert %}

## リターゲティングオプション {#retargeting-options}

{% alert note %}
ユーザーリターゲティングでオーディエンスを構築する際、ユーザーの設定に基づいて特定のユーザーを含めたり除外したりすることや、CUPAに基づく「販売または共有の禁止」権利などのプライバシー法に準拠することが必要になる場合があります。マーケターは、キャンバスやキャンペーンのエントリ条件内で、ユーザーの適格性に関する関連フィルターを実装する必要があります。
{% endalert %}

### SMS、MMS、RCSでユーザーをフィルタリングする {#filter-users-by-sms-mms-and-rcs}

ユーザーは、最後にSMS、MMS、RCSを受信した日時や、特定のキャンペーンからSMS、MMS、RCSを受信したかどうかでフィルタリングできます。フィルターは、キャンペーンビルダーの**ターゲットオーディエンス**ステップで設定できます。

{% alert note %}
メッセージが受信、開封、またはクリックされると、Brazeはインタラクションを記録したプロファイルと同じ電話番号を共有するすべてのプロファイルのデータを更新します。メッセージを受信、開封、またはクリックした人と電話番号を共有しているユーザーは、元々キャンペーンに含まれていなかったり、直接メッセージを送信されていなかったりしても、このフィルターに一致する場合があります。
{% endalert %}

#### 最後にSMS/MMS/RCSを受信した日時でフィルタリング {#filter-by-last-received-smsmmsrcs}

![セグメンテーションフィルター「最後にSMSを受信」が2020年12月8日以降。]({% image_buster /assets/img/sms/filter2.png %})

#### SMS/MMS/RCS キャンペーンからの受信メッセージでフィルタリング {#filter-by-received-messages-from-smsmmsrcs-campaign}

特定のキャンペーンからメッセージを受信したユーザーをフィルタリングします。このフィルターでは、キャンペーンからメッセージを受信していないユーザーを除外するオプションもあります。

![セグメンテーションフィルター「キャンペーンからメッセージを受信」で「SMSリターゲティング」キャンペーン。]({% image_buster /assets/img/sms/filter1.png %})

### ユーザーがSMS、MMS、RCSを受信した際にメッセージをトリガーする {#trigger-messages}

ユーザーが特定のキャンペーンからSMS、MMS、RCSメッセージを受信した際にメッセージをトリガーするには、アクションベースのキャンペーンのトリガーアクションとして**キャンペーンとのインタラクション**を選択します。次に、**SMSを受信**と使用したいSMS、MMS、RCSのキャンペーンを選択します。

![]({% image_buster /assets/img/sms/trigger.png %})

### 高度なトラッキングリンクでフィルタリング {#filter-by-advanced-tracking-links}

[高度なトラッキングリンク]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/)を含むキャンペーンをクリックしたユーザーをリターゲティングします。
高度なトラッキングが有効になっているキャンペーンのみが、以下のドロップダウンに表示されます。

#### 特定のSMS、MMS、RCS キャンペーンをクリックしたユーザーをリターゲティング {#retarget-users-who-have-clicked-a-specific-sms-mms-or-rcs-campaign}

1. **クリック/開封したキャンペーン**フィルターを使用してセグメントを作成します。
2. **短縮SMSリンクをクリック**を選択します。
3. 目的のキャンペーンを選択します。

![]({% image_buster /assets/img/sms/retargeting5.png %})

#### 特定のキャンバスステップをクリックしたユーザーをリターゲティング {#retarget-users-who-have-clicked-a-specific-canvas-step}

1. **クリック/開封したステップ**フィルターを使用してセグメントを作成します。
2. **短縮SMSリンクをクリック**を選択します。
3. 目的のキャンバスとキャンバスステップを選択します。

![]({% image_buster /assets/img/keyword_example1.jpg %})

## キーワードカテゴリ別リターゲティング {#keyword-category-specific-retargeting}

3つのデフォルトキーワードカテゴリ（オプトイン、オプトアウト、ヘルプ）に加えて、最大25個の独自キーワードカテゴリを作成でき、任意のキーワードと応答を識別できます。これらのカテゴリは、フィルタリングとリターゲティングに使用できます。グローバルキーワードカテゴリとその設定方法の詳細については、[キーワード処理]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/)を参照してください。

### 最新性でフィルタリング {#filter-by-recency}

ユーザーがSMS、MMS、RCSプログラムに応答した最新性でフィルタリングします。このフィルターは、ユーザーがキーワードカテゴリのいずれかに該当する受信メッセージを最後に送信した日付を評価します。

![セグメンテーションフィルター「最後にSMSを送信」でサブスクリプショングループ「マーケティングSMS」、キーワード「オプトイン」が2020年8月11日以降。]({% image_buster /assets/img/sms/retargeting1.png %})

### キャンペーンまたはキャンバスアトリビューションでフィルタリング {#filter-by-campaign-or-canvas-attribution}

特定のSMS、MMS、RCSのキャンペーンまたはキャンバスコンポーネント、キーワードカテゴリ、またはタグに応答したユーザーをフィルタリングします。

#### 特定のキャンペーンにキーワードカテゴリで応答したユーザーをフィルタリング {#filter-by-replied-to-a-specific-campaign-with-keyword-category}

![フィルター「SMSに応答」でキャンペーン「SMS-283」「プロモーション」を使用したキャンペーン。フィルターの下に「このフィルターは、アクティブなキャンペーンで使用されていない場合、「プロモーション」から最後のメッセージが送信されてから25か月後に期限切れになります。」と記載されています。]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

#### 特定のタグを持つキャンペーンまたはキャンバスに応答したユーザーをフィルタリング {#filter-by-replied-to-a-campaign-or-canvas-with-a-specific-tag}

![フィルター「SMSに応答」でキャンペーンまたはキャンバスのタグ「Curbside Messaging Service C」を使用したキャンペーン。]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

#### 特定のステップに応答したユーザーをフィルタリング {#filter-by-replied-to-a-specific-step}

![フィルター「SMSに応答」でステップ「SMS Double Opt」「Step - Help」を使用したキャンペーン。]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### キーワードによるメッセージのトリガー {#trigger-messages-by-keyword}

メッセージは、キーワードカテゴリ（ユーザーがいずれかのキーワードを送信した場合）またはその他のキーワード（ユーザーが既存のカテゴリに該当しないキーワードを送信した場合）に基づいて、ユーザーが受信メッセージを送信した際にトリガーできます。これらのトリガーは、キャンペーンビルダーの配信ステップで設定します。

受信メッセージが定義されたトリガーイベントに一致するかどうかを評価する際、先頭と末尾のスペースは評価開始前に削除されます。

{% alert tip %}
受信SMSまたはMMSメッセージによってアクションベースのキャンバスがトリガーされた場合、次のアクションパスまでの任意のキャンバスステップで[サポートされているSMS Liquidプロパティ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)を参照できます。
{% endalert %}

#### 受信キーワードカテゴリによるトリガー {#trigger-by-inbound-keyword-category}

![アクションベースのSMS キャンペーンでセグメンテーションフィルター「キーワードを送信」で「オプトイン」をサブスクリプショングループ「マーケティングSMS」に送信。]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

#### 任意のキーワードによるトリガー {#trigger-by-arbitrary-keywords}

「その他」のキーワード応答でメッセージをトリガーする場合、キーワード本文を完全一致テキストで評価する機会があります。この一致は前述と同じルールに従います。**正確な単一単語のメッセージ**のみが処理されます（大文字小文字は*区別しません*）。`Hello Braze!` というキーワードを送信しても、以下の例に示す条件には一致しません。

![アクションベースのSMS キャンペーンでキーワードカテゴリが「その他」、メッセージ本文が正確に「Hello」または「Hey」。]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

#### テンプレートキーワード {#template-keywords}

受信SMSまたはMMSでキャンペーンまたはキャンバスコンポーネントをトリガーする際、ユーザーが送信したテキストやメディア添付ファイルをLiquidを使用してキャンペーンまたはキャンバスの本文にオプションでテンプレート化できます。これにより、ユーザーの応答にアクセスし、返信に含めたり、条件付きロジックを適用したり、Liquidで可能なその他の処理を行ったりすることができます。

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

`````````liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}