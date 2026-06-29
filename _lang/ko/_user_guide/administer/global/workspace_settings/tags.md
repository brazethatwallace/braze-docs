---
nav_title: 태그 관리
article_title: 태그 관리
page_order: 6
page_type: reference
description: "이 참조 문서에서는 Braze 대시보드에서 태그를 관리하는 방법을 다루며, Campaigns, Canvases, Segments 전반에 걸쳐 태그를 중첩하고, 이름을 변경하고, 정리하는 방법을 설명합니다."
---

# 태그 관리 {#managing-tags}

> Campaigns, Canvases, Segments 전반에서 사용하는 태그를 중앙 위치에서 관리할 수 있습니다. 태그의 이름을 변경하거나, 제거하거나, 추가하려면 **설정** > **태그 관리**로 이동하세요.

Campaigns, Canvases, Segments 및 커스텀 데이터에 태그를 추가하는 방법은 [태그]({{site.baseurl}}/user_guide/messaging/governance/tags)를 참조하세요.

## 태그 중첩 {#nesting-tags}

태그를 더 체계적으로 정리하려면 상위 태그 아래에 중첩할 수 있습니다. 예를 들어, 모든 휴일 태그를 상위 `Holidays` 태그 아래에 중첩하거나, 마케팅 퍼널의 특정 단계와 관련된 모든 태그를 상위 `Funnel` 태그 아래에 중첩할 수 있습니다.

- **새 태그 중첩:** 태그를 생성한 후 **Nest Tag Under**를 선택하고, 새 태그를 중첩할 기존 태그를 선택합니다.
- **기존 태그 중첩:** **태그 관리** 페이지로 이동하여 해당 태그가 있는 행에 마우스를 올린 후 **<i class="fas fa-pencil-alt"></i>편집**을 선택합니다. 그런 다음 **Nest Tag Under**를 선택하고 상위 태그를 선택합니다.

### 상위 태그가 사용 중이지만 **Nest Tag Under**에 표시되지 않는 경우 {#parent-tag-is-in-use-but-missing-from-nest-tag-under}

상위 태그가 대시보드에 적용되어 있지만 새 태그를 생성할 때 **Nest Tag Under** 드롭다운에 표시되지 않는 경우, 해당 상위 태그를 독립 태그로 다시 생성하면 목록에서 검색할 수 있게 됩니다. 이 동작은 상위 태그가 워크스페이스의 다른 곳에서 중첩 종속성으로만 존재하는 경우에 예상되는 동작입니다.

![Nest Tag Under 옵션이 선택된 새 태그 대화 상자.]({% image_buster /assets/img_archive/tag_nested.png %}){: style="max-width:70%;" }

## 모범 사례 {#tags-best-practices}

태그를 사용하여 Campaigns, Canvases, Segments를 비즈니스 목표, 퍼널 단계, 지역 등으로 정리하세요.

다음 표는 이커머스 앱에서 유용하게 사용할 수 있는 태그 예시를 보여줍니다.

<style>
table td {
    word-break: break-word;
}
</style>


<table aria-label="모범 사례">
  <caption>모범 사례</caption>
<thead>
  <tr>
    <th>퍼널</th>
    <th>비즈니스 목표</th>
    <th>지역</th>
    <th>Campaigns</th>
    <th>휴일</th>
    <th>트랜잭션</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>On-boarding<br>Re-engagement<br>Loyal<br>PowerUser<br>Churn<br>Lost</td>
    <td>HighSpender<br>ActiveUser<br>NewUsers<br>FacebookAttribution<br>FirstAction</td>
    <td>UnitedStates<br>Northeast<br>Midwest<br>South<br>West<br>LATAM<br>AP<br>WesternEurope<br>MiddleEast</td>
    <td>Sales<br>Coupons<br>Events</td>
    <td>MLK<br>SuperBowl<br>PiDay<br>StPatricksDay<br>MarchMadness<br>Easter<br>Passover<br>MothersDay<br>MemorialDay<br>FathersDay<br>FourthJuly<br>LaborDay<br>VeteransDay<br>ColumbusDay<br>PresidentsDay<br>Halloween<br>RoshHashanah<br>Thanksgiving<br>Christmas<br>Hanukkah<br>NewYears</td>
    <td>Transactional<br>Notification<br>ConnectedActionTaken</td>
  </tr>
</tbody>
</table>

## 활용 사례 {#use-cases}

다음은 메시징 라이프사이클을 관리하기 위해 태그를 사용하는 일반적인 활용 사례입니다.

{% tabs %}
{% tab 빈도 제한 %}

### 빈도 제한 {#throttling}

고객이 특정 유형의 Campaign을 받는 빈도를 제한합니다. 예를 들어, 프로모션 Campaign의 빈도를 제한하기 위해 다음과 같은 필터를 설정할 수 있습니다:

`Last received campaign` with tag `Promo` more than 5 days ago
<br>`OR`<br>
`Has not received campaign` with tag `Promo`

{% endtab %}
{% tab 보고서 %}

### 보고서 {#reporting}

특정 태그가 있는 모든 Campaign의 볼륨을 모니터링하기 위해 인게이지먼트 보고서를 설정합니다. 예를 들어, 모든 푸시 Campaign을 모니터링하려면 해당 Campaign에 `Push Reporting`과 같은 태그를 추가한 다음, 태그가 지정된 Campaign의 보고서를 매일 전송하도록 [인게이지먼트 보고서]({{site.baseurl}}/user_guide/analytics/reports/engagement_reports#automatically-select-campaigns-or-canvases)를 설정할 수 있습니다.

{% endtab %}
{% endtabs %}