---
nav_title: 캘린더에 추가 링크
article_title: 캘린더에 추가 링크
page_order: 1
page_type: tutorial
description: "이 문서에서는 이메일 캠페인에 캘린더에 추가 링크를 포함하는 방법을 설명합니다."
channel: email

---

# 캘린더에 추가 링크

> 이벤트, 세일 또는 약속을 홍보할 때, 이메일에 "캘린더에 추가" 링크를 추가하면 사용자가 쉽게 캘린더에 이벤트를 저장할 수 있습니다.

이를 위해 이메일을 작성하고 링크를 배치할 위치를 결정합니다. 그런 다음 두 가지 옵션을 추가합니다: 하나는 Google 캘린더용이고 다른 하나는 기타 캘린더(iCal 또는 Outlook 등)용입니다. 예를 들어, "Google 캘린더에 추가"와 "iCal 또는 Outlook에 추가"입니다.

![대시보드에서 링크를 추가할 때 나타나는 링크 대화 상자. "Link Info" 탭이 선택되어 있고 텍스트가 "Add to Google Calendar"로 설정되어 있습니다.]({% image_buster /assets/img_archive/calendar_1.png %}){: style="max-width:50%"}

## URL 형식

다음 URL을 링크에 추가하고 플레이스홀더를 교체합니다. 이 두 URL의 유일한 차이점은 Google 캘린더에 추가 매개변수 `&format=gcal`이 필요하다는 것입니다.

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

다음을 교체합니다:

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

### 추가 매개변수

다음 매개변수는 선택 사항이며 이벤트의 추가 속성을 정의하는 데 사용할 수 있습니다.

- **주최자 이름:** `&organizer=name`
- **이벤트 관련 URL 첨부:** `&attach=http://www.example.com/`
- **기간:** `duration=30M`, 이벤트 종료 시간(dtend) 대신 1H 또는 30M과 같은 기간을 지정할 수 있습니다
- **알림 시간(분 단위):** `&reminder=15`
- **종일 이벤트:** `&allday=1`
- **UID:** 이벤트의 고유 식별자를 하드코딩하는 선택적 매개변수로, 일부 캘린더 앱에서 시간이 지남에 따라 이벤트를 업데이트할 수 있게 합니다. 문자열 @ics.agical.io가 값에 자동으로 추가됩니다.

반복 이벤트를 위한 추가 매개변수도 사용할 수 있습니다:
- **주간 이벤트:** `&recur=weekly`
- **월간 이벤트:** `&recur=monthly`
- **반복 종료:** `&recuruntil=END_DATE`, 여기서 `END_DATE`는 ISO 8601 형식(YYYY-MM-DDTHH:MM:SSZ)의 UTC 기준 반복 종료 날짜 및 시간입니다

## 링크 동작

사용자가 링크를 클릭하면, 캘린더가 URL의 UTC 타임스탬프를 사용자의 캘린더에 설정된 시간대에 맞게 자동으로 변환합니다.

예를 들어, "Google 캘린더에 추가" 예시 링크를 열고 캘린더가 CST로 설정되어 있다면, 이벤트 시간은 오후 3시 UTC가 CST에서 해당하는 시간(오전 10시)으로 미리 채워집니다.

### Google 캘린더

클릭하면 Google 캘린더가 새 탭 또는 창에서 열리며, 이벤트 세부 정보가 초대에 미리 채워져 사용자가 바로 저장할 수 있습니다. 이는 모바일과 데스크탑 모두에서 동일하게 작동합니다.

![이벤트 세부 정보가 추가되어 저장할 준비가 된 Google 캘린더 이벤트 추가 대화 상자.]({% image_buster /assets/img_archive/calendar_2.png %}){: style="max-width:75%"}

### iCal 또는 Outlook

데스크탑에서 클릭하면 ICS 파일이 다운로드됩니다. 사용자가 ICS 파일을 열면 iCal 또는 Outlook이 열리고 캘린더에 이벤트를 추가하라는 메시지가 표시됩니다.

![새 이벤트 추가 대화 상자가 있는 iCal 캘린더로, 사용자에게 캘린더를 선택하고 확인하라는 메시지가 표시됩니다.]({% image_buster /assets/img_archive/calendar_3.png %}){: style="max-width:75%"}

![이벤트가 추가된 iCal 캘린더.]({% image_buster /assets/img_archive/calendar_4.png %}){: style="max-width:81%"}

모바일에서는 사용자가 링크를 길게 누르면 캘린더에 추가하라는 메시지가 표시됩니다.

![캘린더 링크를 길게 누르면 나타나는 iOS 팝업으로, "Add to Calendar" 버튼이 포함되어 있습니다.]({% image_buster /assets/img_archive/calendar_5.png %}){: style="max-width:50%"}

자세한 내용은 다음을 참조하세요:
* [Create events for Google Calendar](https://developers.google.com/calendar/api/guides/create-events)
* [Create an Add to calendar link in an email message](https://support.microsoft.com/en-us/office/create-an-add-to-calendar-link-in-an-email-message-34f8ea28-322a-4867-b423-2998f9634e59)