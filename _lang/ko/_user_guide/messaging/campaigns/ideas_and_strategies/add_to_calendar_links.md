---
nav_title: 캘린더에 추가 링크
article_title: 캘린더에 추가 링크
page_order: 1
page_type: tutorial
description: "이 문서에서는 이메일 Campaign에 캘린더에 추가 링크를 포함하는 방법을 설명합니다."
channel: email

---

# 캘린더에 추가 링크 {#add-to-calendar-links}

> 이벤트, 세일 또는 약속을 홍보할 때, 이메일에 "캘린더에 추가" 링크를 추가하면 사용자가 쉽게 캘린더에 이벤트를 저장할 수 있습니다.

이메일을 작성하고 두 가지 캘린더 옵션이 표시될 위치를 선택합니다. 하나는 Google 캘린더용 링크이고 다른 하나는 기타 캘린더(iCal 또는 Outlook 등)용 링크입니다. "Google 캘린더에 추가"와 "iCal 또는 Outlook에 추가"와 같은 링크 텍스트를 사용합니다.

URL을 연결하는 방법은 사용하는 이메일 편집기에 따라 다릅니다.

- **드래그 앤 드롭 편집기:** **Paragraph** 블록에서 링크할 텍스트를 선택하고 도구 모음에서 **Link** 컨트롤을 열어 [URL 형식](#url-format)의 URL을 붙여넣습니다. 또는 **Button** 블록을 사용하여 **Link type**을 **Open web page**로 설정하고 **URL**에 URL을 붙여넣습니다.
- **HTML 편집기:** 링크 텍스트에는 리치 텍스트 링크 컨트롤을 사용하거나, HTML에서 각 캘린더 URL에 대해 `<a href="...">` 태그를 추가합니다.

## URL 형식 {#url-format}

링크에 다음 URL을 추가하고 입력 안내 부분을 교체합니다. 이 두 URL의 유일한 차이점은 Google 캘린더에 추가 매개변수 `&format=gcal`이 필요하다는 것입니다.

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

다음 항목을 교체합니다:

- `EVENT_SUBJECT`: 이벤트 제목
- `EVENT_LOCATION`: 이벤트 위치
- `START_TIME`: ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)의 UTC 기준 이벤트 시작 시간
- `END_TIME`: ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)의 UTC 기준 이벤트 종료 시간
- `EVENT_DESCRIPTION`: 이벤트 설명

공백은 HTML 이스케이프 코드 `%20`으로 교체합니다. 예를 들어, "Meet Braze"라는 제목은 "Meet%20Braze"가 됩니다.

다음은 "Google 캘린더에 추가" URL의 예시입니다:

```
https://ics.agical.io/?subject=Meet%20Braze&location=114%20Sansome%20Street&dtstart=2021-06-24T15:00:00Z&dtend=2021-06-24T16:00:00Z&description=Braze%20Party&format=gcal
```

### 추가 매개변수 {#additional-parameters}

다음 매개변수는 선택 사항이며 이벤트의 추가 속성을 정의하는 데 사용할 수 있습니다.

- **주최자 이름:** `&organizer=name`
- **이벤트 관련 URL 첨부:** `&attach=http://www.example.com/`
- **기간:** `duration=30M`, 이벤트 종료 시간(dtend) 대신 1H 또는 30M과 같은 기간을 지정합니다
- **알림 시간(분 단위):** `&reminder=15`
- **종일 이벤트:** `&allday=1`
- **UID:** 이벤트의 고유 식별자를 하드코딩하는 선택적 매개변수로, 일부 캘린더 앱에서 시간이 지남에 따라 이벤트를 업데이트할 수 있도록 합니다. 문자열 @ics.agical.io가 값에 자동으로 추가됩니다.

반복 이벤트를 위한 추가 매개변수도 사용할 수 있습니다:
- **주간 이벤트:** `&recur=weekly`
- **월간 이벤트:** `&recur=monthly`
- **반복 종료:** `&recuruntil=END_DATE`, 여기서 `END_DATE`는 ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)의 UTC 기준 반복 종료 날짜 및 시간입니다

## 링크 동작 {#link-behavior}

사용자가 링크를 클릭하면, 캘린더가 URL의 UTC 타임스탬프를 사용자의 캘린더에 설정된 시간대에 맞게 자동으로 변환합니다.

예를 들어, "Google 캘린더에 추가" 예시 링크를 열고 캘린더가 CST로 설정되어 있다면, 이벤트 시간은 UTC 오후 3시가 CST에서 해당하는 시간(오전 10시)으로 미리 채워집니다.

### Google 캘린더 {#google-calendar}

클릭하면 Google 캘린더가 새 탭 또는 창에서 열리며, 이벤트 세부 정보가 초대에 미리 채워져 사용자가 바로 저장할 수 있는 상태가 됩니다. 이 동작은 모바일과 데스크톱 모두에서 동일합니다.

![이벤트 세부 정보가 추가되어 저장할 준비가 된 Google 캘린더 이벤트 추가 대화 상자.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal 또는 Outlook {#ical-or-outlook}

데스크톱에서 클릭하면 ICS 파일이 다운로드됩니다. 사용자가 ICS 파일을 열면 iCal 또는 Outlook이 열리고, 캘린더에 이벤트를 추가하라는 메시지가 표시됩니다.

![새 이벤트 추가 대화 상자가 표시된 iCal 캘린더로, 사용자에게 캘린더를 선택하고 확인하라는 메시지가 표시됩니다.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![이벤트가 추가된 iCal 캘린더.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

모바일에서의 동작은 기기와 이메일 앱에 따라 다릅니다.

{% alert note %}
iPhone에서 Mail 앱과 Microsoft Outlook은 사용자가 iCal 링크를 탭하면 ICS 파일을 다운로드하지만, 해당 앱에서 링크를 통해 캘린더를 직접 열지는 않습니다. 이벤트를 추가하려면 **파일**, **다운로드** 또는 첨부 파일 보기(앱에 따라 다름)에서 다운로드된 파일을 열고, 캘린더에서 나머지 단계를 완료하세요.
{% endalert %}

일부 다른 모바일 이메일 앱이나 브라우저에서는 링크를 길게 누르면 캘린더에 이벤트를 추가하는 옵션이 표시될 수 있습니다.

![캘린더 링크를 길게 눌렀을 때 나타나는 iOS 팝업으로, '캘린더에 추가' 버튼이 포함되어 있습니다.]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

자세한 내용은 다음을 참조하세요:
* [Google 캘린더 이벤트 만들기](https://developers.google.com/calendar/api/guides/create-events)
* [이메일 메시지에 캘린더에 추가 링크 만들기](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)