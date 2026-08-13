---
nav_title: "ユーザーの電話番号"
article_title: WhatsAppユーザーの電話番号
page_order: 3
description: "このリファレンス記事では、WhatsAppの電話番号のフォーマット、電話番号のインポート方法、およびWhatsApp購読グループへのユーザーの追加方法について説明します。"
page_type: reference
channel:
  - WhatsApp

---

# ユーザーの電話番号 {#user-phone-numbers}

> この記事では、ユーザーや顧客の電話番号に関するさまざまなトピックについて説明します。

電話番号はユーザープロファイルにローカル形式で表示されますが、番号をインポートする際に使用する形式（`(724) 123 4567`）とは異なります。

## 電話番号のインポート {#importing-phone-numbers}

電話番号は、[CSVをアップロード]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv)するか、[API経由]({{site.baseurl}}/api/endpoints/user_data/post_user_track)でユーザーを作成することでインポートできます。

### フォーマット {#formatting}

米国以外の番号は、「+」と国コードを含む[`E.164`](https://en.wikipedia.org/wiki/e.164)形式でインポートすることが重要です。この形式で提供されない電話番号は、米国の番号として解釈されます。

電話番号がE.164形式に変換されてもバリデーションに合格しない場合、Brazeはその番号にWhatsAppメッセージを送信できません。フォーマットできない電話番号を持つユーザーは、WhatsAppを含むキャンバスステップから自動的に退出します。

すべての米国番号は、有効な市外局番を持つ有効な10桁の電話番号である必要があります。`+`や国コードなしで入力できます。Brazeは有効な10桁の電話番号をすべて米国番号として想定しマッピングします。

すべての国際番号は`+`で始まり、その後に国コード、電話番号が続く必要があります。（例：`+442071838750`）

![フォーマットに関するスクリーンショット。]({% image_buster /assets/img/sms/e164.png %}){: style="max-width:50%;border: 0;"}

ただし、異なる国コードや市外局番を持つ複数の地域に送信する場合の正確性を確保するために、米国ベースの電話番号であっても`E.164`形式を使用することをお勧めします。

ローカル番号のフォーマットとユニバーサルな`E.164`フォーマットの違いは、以下の表で確認できます。

| 国 | ローカル | 国コード | `E.164` |
|---|---|---|---|
| 米国 | `4155552671` | 1 | `+14155552671` |
| 英国 | `02071838750` | 44 | `+442071838750` |
| ブラジル | `1155256325` | 55 | `+551155256325` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="フォーマット" }

### WhatsApp購読グループへのユーザーの追加 {#adding-users-to-whatsapp-a-subscription-group}

顧客がWhatsAppメッセージを受信するには、有効な電話番号を持ち、購読グループにオプトインしている必要があります。詳細については、[WhatsApp購読グループ]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/subscription_groups)を参照してください。


### 同じ電話番号を持つ複数のユーザー {#multiple-users-with-the-same-phone-number}

単一のキャンペーンまたはキャンバスステップのセグメント内で複数のユーザーが同じ電話番号を持っている場合、Brazeは送信の重複を排除し、その電話番号に1通のメッセージのみを送信します。