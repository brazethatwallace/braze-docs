---
nav_title: カレンダー追加リンク
article_title: カレンダー追加リンク
page_order: 1
page_type: tutorial
description: "この記事では、メールキャンペーンにカレンダー追加リンクを含める方法について説明します。"
channel: email

---

# カレンダー追加リンク {#add-to-calendar-links}

> イベント、セール、予約を宣伝する際、メールに「カレンダーに追加」リンクを追加することで、ユーザーが簡単にカレンダーにイベントを保存できるようになります。

メールの下書きを作成し、2つのカレンダーオプションを表示する場所を決めます。1つはGoogle カレンダー用のリンク、もう1つはその他のカレンダー（iCalやOutlookなど）用のリンクです。リンクテキストには「Google カレンダーに追加」や「iCalまたはOutlookに追加」のように記載します。

URLの設定方法は、使用するメールエディターによって異なります。

- **ドラッグ＆ドロップエディター：** **Paragraph**ブロックで、リンクにするテキストを選択し、ツールバーの**Link**コントロールを開いて、[URLフォーマット](#url-format)のURLを貼り付けます。または、**Button**ブロックを使用し、**Link type**を**Open web page**に設定して、**URL**にURLを貼り付けます。
- **HTMLエディター：** リンクテキストにはリッチテキストのリンクコントロールを使用するか、HTMLで各カレンダーURLに`<a href="...">`タグを追加します。

## URLフォーマット {#url-format}

リンクに以下のURLを追加し、プレースホルダーを置き換えてください。これら2つのURLの唯一の違いは、Googleカレンダーには追加パラメーター `&format=gcal` が必要な点です。

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCalまたはOutlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

以下を置き換えてください:

- `EVENT_SUBJECT`: イベントのタイトル
- `EVENT_LOCATION`: イベントの場所
- `START_TIME`: イベントの開始時刻（ISO 8601形式（YYYY-MM-DDTHH:MM:SSZ）、UTC）
- `END_TIME`: イベントの終了時刻（ISO 8601形式（YYYY-MM-DDTHH:MM:SSZ）、UTC）
- `EVENT_DESCRIPTION`: イベントの説明

スペースはHTMLエスケープコード `%20` に置き換えてください。たとえば、件名が「Meet Braze」の場合は「Meet%20Braze」となります。

以下は「Googleカレンダーに追加」URLの例です:

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### 追加パラメーター {#additional-parameters}

以下のパラメーターはオプションで、イベントの追加要素を定義するために使用できます。

- **主催者名:** `&organizer=name`
- **イベントに関連するURLを添付:** `&attach=http://www.example.com/`
- **期間:** `duration=30M`、イベント終了時刻（dtend）の代わりに、1Hや30Mのような期間を指定します
- **リマインダーアラーム時間（分単位）:** `&reminder=15`
- **終日イベント:** `&allday=1`
- **UID:** イベントの一意の識別子をハードコードするオプションパラメーターで、一部のカレンダーアプリがイベントを経時的に更新できるようにします。文字列 @ics.agical.io が値に自動的に追加されます。

繰り返しイベント用の追加パラメーターも指定できます:
- **毎週のイベント:** `&recur=weekly`
- **毎月のイベント:** `&recur=monthly`
- **繰り返しの終了:** `&recuruntil=END_DATE`、`END_DATE` は繰り返しが終了する日時（ISO 8601形式（YYYY-MM-DDTHH:MM:SSZ）、UTC）です

## リンクの動作 {#link-behavior}

ユーザーがリンクをクリックすると、カレンダーはURL内のUTCタイムスタンプを自動的に変換し、ユーザーのカレンダーに設定されたタイムゾーンを反映します。

たとえば、サンプルの「Googleカレンダーに追加」リンクを開き、カレンダーがCSTに設定されている場合、イベントの時刻は午後3時（UTC）をCSTに変換した時刻（午前10時）で自動入力されます。

### Googleカレンダー {#google-calendar}

クリックすると、Googleカレンダーが新しいタブまたはウィンドウで開き、イベントの詳細が招待に自動入力された状態で表示され、ユーザーはすぐに保存できます。これはモバイルとデスクトップの両方で動作します。

![イベントの詳細が追加され、保存可能な状態のGoogleカレンダーのイベント追加ダイアログ。]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCalまたはOutlook {#ical-or-outlook}

デスクトップでクリックすると、ICSファイルがブラウザのデフォルトのダウンロード場所（通常は**ダウンロード**フォルダ）にダウンロードされます。ユーザーはそのICSファイルを開く必要があり、開くとiCalまたはOutlookが起動し、カレンダーにイベントを追加するよう促されます。

![新しいイベントを追加するダイアログが表示されたiCalカレンダー。カレンダーの選択と確認を促しています。]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![イベントが追加されたiCalカレンダー。]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

モバイルでは、デバイスやメールアプリによって動作が異なります。

{% alert note %}
iPhoneでは、メールアプリおよびMicrosoft Outlookは、ユーザーがiCalリンクをタップするとICSファイルをデバイスにダウンロードしますが、リンクからカレンダーを開くことはありません。イベントを追加するには、**ファイル**、**ダウンロード**、または添付ファイルビュー（アプリによって異なります）からダウンロードしたファイルを開き、カレンダーでステップを完了してください。具体的な場所はメールアプリとiOSの設定によって異なります。
{% endalert %}

一部のモバイルメールアプリやブラウザでは、リンクを長押しするとカレンダーにイベントを追加するオプションが表示される場合があります。

![カレンダーリンクを長押しした際のiOSポップアップ。「カレンダーに追加」ボタンが含まれています。]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

詳細については、以下を参照してください。
* [Create events for Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Create an Add to calendar link in an email message](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)