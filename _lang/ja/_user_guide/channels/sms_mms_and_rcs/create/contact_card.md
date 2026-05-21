---
nav_title: 連絡先カード
article_title: 連絡先カード
page_order: 3
description: "このリファレンス記事では、MMSおよびSMSメッセージに含める連絡先カードの作成方法について説明します。"
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS

---

# 連絡先カード {#contact-cards}

> 連絡先カード（vCardまたはVirtual Contact Files（VCF）とも呼ばれます）は、ビジネス情報や連絡先情報を送信するための標準化されたファイル形式で、アドレス帳や連絡先帳に簡単にインポートできます。

{% alert note %}
連絡先カードの送信はMMSとして課金されます。連絡先カードを作成する際は、予想されるMMSの送信量とメッセージまたはアクションクレジットの使用量を確認し、Brazeの[請求ページ]({{site.baseurl}}/user_guide/administer/global/billing/)でコストを確認してください。
{% endalert %}

連絡先カードは[プログラムで](https://www.twilio.com/blog/send-vcard-twilio-sms)作成してBrazeの[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#media-library)にアップロードするか、組み込みの連絡先カードジェネレーターを使用して作成できます。これらのカードには、会社名、電話番号、住所、メール、小さな写真などの一般的なプロパティを割り当てることができます。連絡先カードの作成を始めるには、まずBrazeでMMSを使用するための設定が完了していることを確認してください。

## 連絡先カードジェネレーター {#contact-card-generator}

### ステップ 1:名前を割り当てる {#step-1-assign-name}

連絡先カードは、SMSおよびMMSの作成画面から作成できます。**連絡先カードジェネレーター**タブを選択して開始します。

次に、会社名またはニックネームの入力を求められます。これは、ユーザーがカードを保存する際に表示される名前です。ユーザーが連絡先やメッセージングアプリで会社名またはエイリアスの全体を確認できるように、20文字の制限が適用されます。

![連絡先カードジェネレータータブ。]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### ステップ 2:電話番号を割り当てる {#step-2-assign-phone-number}

利用可能なドロップダウンオプションからサブスクリプショングループと希望の電話番号を選択します。この番号は連絡先カードに記載され、保存後にテキストメッセージを送信するために電話で利用できるようになります。

英数字コードは双方向メッセージングと互換性がなく、連絡先カードではサポートされていません。

### ステップ 3:オプションフィールド {#step-3-optional-fields}

![連絡先カードジェネレーターのオプションフィールド。]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### 連絡先カードの連絡先写真をアップロードする {#upload-contact-card-contact-photo}

連絡先カードにオプションのサムネイル連絡先写真をアップロードできます。240 x 240&nbsp;pxのJPEGまたはPNG画像を推奨します。アップロードされた高解像度画像は、メッセージの配信性を確保するために240 x 240&nbsp;pxにリサイズされます。5&nbsp;MBを超えるMMSメッセージは送信に失敗する場合があります。

#### 追加情報を入力する {#add-more-information}

その他のフィールドでは、名前、サブヘッダー、住所、およびユーザーが利用したいその他の連絡先情報を挿入できます。

### ステップ 4:連絡先カードを保存する {#step-4-saving-your-contact-card}

必要なフィールドをすべて入力したら、**連絡先カードを生成**をクリックすると、キャンペーンまたはキャンバスに自動的に添付されます。ここからメッセージを追加し、連絡先カードをテストして、キャンペーンまたはキャンバスを起動できます。

連絡先カードは[メディアライブラリ]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/#media-library)にも保存され、今後のキャンペーンやキャンバスで簡単に再利用できます。

## 既存の連絡先カードを追加する {#adding-an-existing-contact-card}

既存の連絡先カードを追加するには、キャンペーンまたはキャンバスを作成し、希望のサブスクリプショングループを選択します。次に、メッセージ作成画面に**メディアを追加**オプションが表示されます。ここで、既存の連絡先カードファイルをアップロードするか、メディアライブラリから検索できます。