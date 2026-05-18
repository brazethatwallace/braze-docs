---
nav_title: カレンダー追加リンク
article_title: カレンダー追加リンク
page_order: 1
page_type: tutorial
description: "この記事では、メールキャンペーンにカレンダー追加リンクを含める方法について説明します。"
channel: email

---

# カレンダー追加リンク

> イベント、セール、予約を宣伝する際、メールに「カレンダーに追加」リンクを追加することで、ユーザーが簡単にカレンダーにイベントを保存できるようになります。

これを行うには、メールの下書きを作成し、リンクを配置する場所を決定します。次に、Google カレンダー用とその他のカレンダー（iCal や Outlook など）用の2つのオプションを追加します。例えば、「Google カレンダーに追加」と「iCal または Outlook に追加」のようにします。

![ダッシュボードでリンクを追加する際のリンクダイアログ。「Link Info」タブが選択されており、テキストは「Add to Google Calendar」に設定されています。]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## URL フォーマット

以下の URL をリンクに追加し、プレースホルダーを置き換えてください。これら2つの URL の唯一の違いは、Google カレンダーには追加のパラメーター `&format=gcal` が必要であることです。

{% tabs %}
{% tab Google Calendar %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION&format=gcal
```

{% endtab %}
{% tab iCal or Outlook %}

```
https://ics.agical.io/?subject=EVENT_SUBJECT&location=EVENT_LOCATION&dtstart=START_TIME&dtend=END_TIME&description=EVENT_DESCRIPTION
```

{% endtab %}
{% endtabs %}

以下を置き換えてください：

- `EVENT_SUBJECT`：イベントのタイトル
- `EVENT_LOCATION`：イベントのロケーション
- `START_TIME`：イベントの開始時刻（ISO 8601 形式（YYYY-MM-DDTHH:MM:SSZ）、UTC）
- `END_TIME`：イベントの終了時刻（ISO 8601 形式（YYYY-MM-DDTHH:MM:SSZ）、UTC）
- `EVENT_DESCRIPTION`：イベントの説明

スペースは HTML エスケープコード `%20` に置き換えてください。例えば、「Meet Braze」という件名は「Meet%20Braze」となります。

以下は「Google カレンダーに追加」URL の例です：

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### 追加パラメーター

以下のパラメーターはオプションで、イベントの追加属性を定義するために使用できます。

- **主催者名：** `&organizer=name`
- **イベントに関連する URL を添付：** `&attach=http://www.example.com/`
- **期間：** `duration=30M`、イベント終了時刻（dtend）の代わりに、1H や 30M のような期間を指定します
- **リマインダーアラーム時間（分）：** `&reminder=15`
- **終日イベント：** `&allday=1`
- **UID：** イベントのユニーク識別子をハードコードするオプションパラメーターで、一部のカレンダーアプリがイベントを経時的に更新できるようにします。文字列 @ics.agical.io が値に自動的に追加されます。

繰り返しイベント用の追加パラメーターも追加できます：
- **毎週のイベント：** `&recur=weekly`
- **毎月のイベント：** `&recur=monthly`
- **繰り返しの終了：** `&recuruntil=END_DATE`、`END_DATE` は繰り返しが終了する日時で、ISO 8601 形式（YYYY-MM-DDTHH:MM:SSZ）の UTC です

## リンクの動作

ユーザーがリンクをクリックすると、カレンダーは URL 内の UTC タイムスタンプを、カレンダーに設定されたユーザーのタイムゾーンに自動的に変換します。

例えば、「Google カレンダーに追加」のサンプルリンクを開き、カレンダーが CST に設定されている場合、イベントの時刻は UTC の午後3時が CST で何時になるか（午前10時）に従って自動入力されます。

### Google カレンダー

クリックすると、Google カレンダーが新しいタブまたはウィンドウで開き、イベントの詳細が招待に事前入力された状態で、ユーザーが保存できるようになります。これはモバイルとデスクトップの両方で動作します。

![イベントの詳細が追加され、保存の準備ができた状態の Google カレンダーのイベント追加ダイアログ。]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal または Outlook

デスクトップでクリックすると、ICS ファイルがダウンロードされます。ユーザーは ICS ファイルを開く必要があり、iCal または Outlook が開いてカレンダーにイベントを追加するよう促されます。

![新しいイベントを追加するダイアログが表示された iCal カレンダー。カレンダーの選択と確認を促しています。]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![イベントが追加された iCal カレンダー。]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

モバイルでは、ユーザーはリンクを長押しする必要があり、カレンダーに追加するよう促されます。

![カレンダーリンクを長押しした際の iOS ポップアップ。「カレンダーに追加」ボタンが含まれています。]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

詳細については、以下を参照してください：
* [Create events for Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Create an Add to calendar link in an email message](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)