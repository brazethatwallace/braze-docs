---
nav_title: オプトインおよびオプトアウトキーワード
article_title: SMSオプトインおよびオプトアウトキーワード
page_order: 0
description: "このリファレンス記事では、BrazeがSMSメッセージングの基本的なオプトインおよびオプトアウトキーワードをどのように処理するかについて説明します。"
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# オプトインおよびオプトアウトキーワード {#opt-in-and-opt-out-keywords}

> 規制により、すべてのオプトイン、オプトアウト、およびヘルプ/情報キーワードの応答に対して返信が必要です。Brazeは以下の_完全一致、単一単語、大文字小文字を区別しない_メッセージを自動的に処理し、すべての受信リクエストに対してユーザーとその関連電話番号の[サブスクリプショングループの状態]({{site.baseurl}}/sms_rcs_subscription_groups/)を自動的に更新します。

## キーワードの概要 {#keyword-overview}

Brazeは以下のキーワードを自動的に処理し、すべての受信リクエストに対して電話番号のサブスクリプショングループの状態を更新します。これらのデフォルトキーワードと応答はカスタマイズすることもできます。

| タイプ | キーワード | 変更内容 |
|-|-------|---|
|オプトイン| `START`<br> `YES`<br> `UNSTOP` | これらの`Opt-In`キーワードのいずれかを含む受信リクエストにより、サブスクリプショングループの状態が`subscribed`に変更されます。さらに、そのサブスクリプショングループに関連付けられた送信者プールは、その顧客にSMS、MMS、またはRCSメッセージを送信できるようになります（送信者がサポートするメッセージングの種類に応じます）。<br><br>ユーザーには、定義済みのオプトイン自動応答が送信されます。 |
|オプトアウト| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | これらの`Opt-Out`キーワードのいずれかを含む受信リクエストにより、サブスクリプショングループの状態が`unsubscribed`に変更されます。さらに、そのサブスクリプショングループに関連付けられた番号プールは、その顧客にメッセージを送信できなくなります。<br><br>ユーザーには、定義済みのオプトアウト自動応答が送信されます。 |
| ヘルプ | `HELP`<br> `INFO` | ユーザーには、定義済みのヘルプ自動応答が送信されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**完全一致の単一単語メッセージ**のみが処理されます（大文字小文字は区別されません）。`STOP PLEASE`のようなキーワードは、[あいまいオプトアウト]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/)が有効になっていない限り無視されます。

受信者がキーワード`HELP`または`INFO`を使用した場合、応答が自動的にトリガーされます。これらの自動応答メッセージのデフォルト応答は、[オンボーディング]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/)および電話番号取得期間中に設定されます。初回のオンボーディング期間後もこれらの応答を引き続き更新できます。

{% alert tip %}
オプトアウト処理を拡張したいですか？[あいまいオプトアウト]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/fuzzy_opt_out/)をお試しください。この機能は、受信メッセージがオプトアウトキーワードと一致しないものの、オプトアウトの意図を示している場合にそれを認識しようとします。
{% endalert %}