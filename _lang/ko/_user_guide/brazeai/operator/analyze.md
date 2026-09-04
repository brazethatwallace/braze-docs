---
nav_title: 분석
article_title: Operator 분석
page_order: 100
description: "채널 참여, 기여 매출, 업계 벤치마크 대비 성과에 대해 자연어로 질문하세요. 차트, 비교, 유용한 인사이트를 몇 초 만에 확인할 수 있습니다."
page_type: reference
hidden: true
---

# Operator 분석 {#operator-analyze}

> Operator 분석은 BrazeAI Operator<sup>TM</sup>에서 자연어 성과 질문에 답변합니다. 응답에는 차트, 비교, 간단한 인사이트가 포함됩니다. 대시보드를 구축하거나 전체 보고서를 먼저 가져올 필요가 없습니다.

{% alert important %}
Operator 분석은 현재 베타 버전입니다. 기능과 지원되는 분석은 계속 발전하고 있습니다. 계정 액세스를 요청하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## Operator Analyze를 사용하는 이유 {#why-use-operator-analyze}

대부분의 성능 관련 질문에는 여전히 도구를 전환하거나, 뷰를 구성하거나, 다른 사람의 도움을 기다려야 합니다. 예를 들어 "지난주 성과는 어땠나요", "벤치마크 대비 추적이 잘 되고 있나요", "어떤 Campaign이 가장 강력한 결과를 이끌고 있나요?" 등이 있습니다.

Operator Analyze는 인게이지먼트 측정기준, *기여 매출*, 업계 벤치마크를 다룹니다. 이는 보고서나 대시보드에 직접 가져와야 했던 것과 동일한 데이터입니다. Operator 패널에서 자유롭게 질문하세요. 차트, 순위 비교, 또는 표와 함께 1~5개의 유용한 인사이트를 받을 수 있습니다.

## Operator Analyze에 액세스하기 {#access-operator-analyze}

Operator Analyze는 Operator 대화 패널에서 실행됩니다.

1. Braze 대시보드의 아무 페이지에서 사용자 프로필 옆에 있는 **BrazeAI<sup>TM</sup> Operator**를 선택합니다.
2. 채널 인게이지먼트 또는 벤치마크 비교에 대해 질문합니다([질문 예시](#example-questions) 참조).
3. Operator가 답변을 반환하며, 도움이 되는 경우 차트나 표와 함께 간략한 인사이트 목록을 제공합니다.

Operator 채팅 패널에 대한 자세한 내용은 [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)를 참조하세요.

## 질문 예시 {#example-questions}

알고 싶은 내용을 설명하세요. 정해진 문구는 필요하지 않습니다. 탭을 선택하여 샘플 프롬프트를 확인하세요.

{% tabs %}
{% tab 벤치마크 비교 %}

* "지난 30일간 이메일 *열람율*이 업계 벤치마크와 비교하여 어떤가요?"
* "이번 분기 SMS *클릭률*이 벤치마크보다 높은가요, 낮은가요?"
* "채널 구성 전반에서 업계 대비 실적이 저조한 부분은 어디인가요?"

{% endtab %}
{% tab 채널 개요 %}

* "FY26 현재까지 가장 성능이 좋은 채널은 어디인가요?"
* "지난 90일간 채널별 인게이지먼트를 분석해 주세요."
* "지난 분기 각 마케팅 채널이 창출한 *기여 매출*은 얼마인가요?"

{% endtab %}
{% tab Campaign 및 Canvas 상세 분석 %}

* "이번 회계 분기에 *클릭률* 기준 상위 10개 이메일 Campaigns는 무엇인가요?"
* "지난달 가장 많은 *클릭*을 유도한 Canvases는 무엇인가요?"
* "FY26 Q1에서 가장 많은 *기여 매출*을 창출한 Campaigns는 무엇인가요?"
* "지난 30일간 가장 성능이 낮은 푸시 Campaigns를 보여 주세요."

{% endtab %}
{% tab 트렌드 분석 %}

* "FY26 푸시 인게이지먼트의 월별 추이는 어떤가요?"
* "지난 1년간 이메일 *클릭률*이 분기별로 어떻게 변화했나요?"
* "지난 12개월간 *기여 매출* 추이는 어떤가요?"
* "지난 90일간 인앱 메시지의 주간 인게이지먼트 추이를 보여 주세요."

{% endtab %}
{% tab 매출 및 전환 %}

*기여 매출*과 *전환*에 대해 Campaign, Canvas, 채널, 또는 프로그램 수준으로 집계된 정보를 질문하세요.

* "최근 분기와 이전 분기의 *기여 매출* 및 *전환*을 비교해 주세요."
* "지난 90일간 가장 많은 *기여 매출*을 창출한 Campaigns는 무엇인가요?"
* "FY26 현재까지 채널별 *기여 매출*을 분석해 주세요."

{% endtab %}
{% tab 종합 검토 %}

* "인게이지먼트 프로그램에 대한 전체 검토와 권장 사항을 알려 주세요."
* "현재 채널 전반에서 가장 큰 기회와 리스크는 어디에 있나요?"

{% endtab %}
{% endtabs %}

## 시각화 {#visualizations}

Operator는 데이터가 지원하는 경우 차트를 추가합니다. **꺾은선형 차트**는 시계열에, **막대 차트**는 카테고리 비교에, **테이블**은 기타 경우에 적합합니다. 테이블은 백분율을 소수점 둘째 자리까지 표시하며, 큰 숫자에는 쉼표를 사용합니다.

응답에 여러 측정기준이 포함된 경우, Operator는 원시 수치보다 참여율(*열람율*, *클릭률*, *푸시 열람율*)을 우선적으로 표시합니다.

## 지원되는 채널 및 측정기준 {#supported-channels-and-metrics}

*기여 매출*과 *전환*은 **매출 및 전환** 탭의 [질문 예시](#example-questions)에 표시된 것과 동일한 Campaign, Canvas, 채널 및 프로그램 집계를 사용합니다.

| 채널 | 측정기준 | 업계 벤치마크 |
| --- | --- | --- |
| 이메일 | *발송*, *전달*, *고유 열람*, *고유 클릭*, *탈퇴* | 예 |
| 푸시 (iOS, Android, 웹) | *발송*, *전달*, *열람* | 예 |
| SMS | *발송*, *전달*, *링크 클릭* | 예 |
| In-App Messages | *노출 횟수*, *클릭* | 예 |
| Content Cards | *발송*, *노출 횟수*, *클릭* | 예 |
| WhatsApp | *발송*, *전달*, *읽음*, *클릭* | 아직 미지원 |
| RCS | *발송*, *전달*, *읽음*, *클릭* (텍스트 URL, 버튼, 액션, 답장 액션, 답장 버튼 하위 유형 포함) | 아직 미지원 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="지원되는 채널, 측정기준, 벤치마크 사용 가능 여부" }

{% alert tip %}
Operator는 비율 계산 시 고유 수를 사용합니다(예: *이메일 열람율*의 경우 *고유 열람*을 *전달*로 나눔). 수치가 대시보드와 다를 경우 기여 기간, 시간 범위, 정의를 비교해 보세요. Operator는 각 응답에 이 세 가지를 모두 표시합니다.
{% endalert %}

## 기간 및 기여도 분석 기간 {#time-periods-and-attribution-windows}

### 회계연도 vs. 역년 {#fiscal-year-vs-calendar-year}

Operator Analyze는 기본적으로 2월 1일부터 1월 31일까지 운영되는 **Braze 회계연도**를 사용합니다.

| 회계 분기 | 월 |
| --- | --- |
| FQ1 | 2월 – 4월 |
| FQ2 | 5월 – 7월 |
| FQ3 | 8월 – 10월 |
| FQ4 | 11월 – 1월 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze 회계 분기 및 달력 월" }

역년 기준 질문의 경우, "CY", "calendar year" 또는 "standard year"를 포함하세요. "last year"와 같이 모호한 표현을 사용하면 Operator가 어떤 캘린더를 의미하는지 확인을 요청합니다.

`Q4 2025` 또는 `2025-03-01 to 2025-05-31`과 같은 ISO 형식 범위도 사용할 수 있습니다.

### 기여도 분석 기간 {#attribution-windows}

Operator Analyze는 기본적으로 **7일**을 사용합니다. 기본값을 변경하려면 질문에 기간을 명시하세요.

* **1일** — 빠른 참여 확인용
* **3일** — 단기 사이클 Campaign용
* **7일** — 일반 개요 및 Campaign 분석용(기본값)
* **30일** — 전략적 또는 장기적 관점용
* **전체 기간** — 1일 / 3일 / 7일 / 30일 비교 분석용

기간별 결과가 50% 이상 차이나는 경우, Operator는 네 가지 기간을 나란히 표시합니다.

## 데이터 최신성 {#data-freshness}

데이터는 매일 갱신됩니다. 당일 활동은 다음 갱신 이후에 반영됩니다. 각 응답에는 데이터셋의 최신 날짜가 표시됩니다. 해당 날짜가 오래된 것으로 보이면 고객 성공 매니저에게 문의하세요.

## 범위 외 항목 {#whats-out-of-scope}

* **제품 수준의 성능 분석.** *기여 매출*과 인게이지먼트는 Campaign, Canvas, 채널 또는 프로그램 수준까지 집계됩니다. 제품이나 SKU별로 세분화되지 않습니다. 제품 또는 SKU 수준의 질문은 지원되지 않습니다. 해당 분석이 필요한 경우 고객 성공 매니저에게 문의하세요.
* **WhatsApp 및 RCS 업계 벤치마크.** 두 채널의 인게이지먼트 측정기준은 지원됩니다. 벤치마크는 아직 제공되지 않습니다.

범위 외 질문에 대해서는 직접적인 답변, 가능한 경우 대안 제안, 또는 고객 성공 매니저 안내가 제공됩니다.

## 더 나은 결과를 위한 팁 {#tips-for-better-results}

* **시간 범위:** 정밀도가 필요한 경우 "지난 분기"와 같은 모호한 표현보다 명시적인 범위("FY26 Q2", "지난 90일")를 사용하세요.
* **측정기준:** 관심 있는 비율을 구체적으로 명시하세요(*열람율*, *클릭률*, *클릭 대비 열람율*). Operator는 사용한 공식을 보고합니다.
* **후속 질문:** 결과를 자세히 살펴보거나, 기간을 변경하거나, 채널을 전환하세요. Operator는 스레드 전체에서 컨텍스트를 유지합니다.
* **채널별 용어:** WhatsApp과 RCS는 *읽음률*(*열람율*이 아님)을 사용합니다. SMS는 *링크 클릭률*을 사용합니다.
* **복합 요청:** 벤치마크와 추세를 하나의 프롬프트에서 함께 요청할 수 있습니다.

## 데이터 프라이버시 및 보안 {#data-privacy-and-security}

Operator Analyze는 BrazeAI Operator<sup>TM</sup>와 동일한 프라이버시 및 보안 모델을 따릅니다. 자세한 내용은 [데이터 프라이버시 및 보안]({{site.baseurl}}/user_guide/brazeai/operator/data_privacy_security)을 참조하세요.

## 다음 단계 {#next-steps}

{% article_tiles %}
- name: BrazeAI Operator
  link: /docs/user_guide/brazeai/operator
  description: Operator에 액세스하고 대시보드 기능을 살펴보세요.
- name: 액션 검토
  link: /docs/user_guide/brazeai/operator/reviewing_actions
  description: Operator가 제안한 변경 사항을 검토하고 승인하세요.
{% endarticle_tiles %}