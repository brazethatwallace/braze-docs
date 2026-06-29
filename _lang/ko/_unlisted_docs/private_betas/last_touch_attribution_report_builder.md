---
nav_title: "라스트 터치 기여도"
permalink: /last-touch_attribution_metrics/
hidden: true
---

# 라스트 터치 기여도 측정기준 {#last-touch-attribution-metrics}

> 보고서 빌더에서 보고서에 라스트 터치 기여도 측정기준을 추가하세요.

{% alert note %}
라스트 터치 기여도 측정기준은 얼리 액세스 중입니다. 얼리 액세스 참여에 관심이 있으시면 고객 성공 매니저에게 문의하세요.
{% endalert %}

라스트 터치 기여도(LTA)는 전환 전에 사용자가 마지막으로 상호작용한 메시지에 전환에 대한 전체 크레딧을 부여하는 전환 기여도 모델입니다. Campaign 수준의 전환 기간과 달리, LTA는 각 채널에 대해 업계 표준 기여도 기간을 사용합니다.

| 채널 | 기여도 기간 |
| --- | --- |
| 이메일 | 30일 |
| SMS | 7일 |
| WhatsApp | 7일 |
| 푸시 | 7일 |
| 인앱 메시지 | 3일 |
| Content Cards | 3일 |
| 웹훅 | 이 모델에서 제외 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
전환이 채널의 기여도 기간 외에 발생하면 이 모델에서 집계되지 않습니다.
{% endalert %}

## 이점 {#benefits}

라스트 터치 기여도는 표준 전환 추적에 비해 주요 이점을 제공합니다.

* 전환을 특정 터치포인트에 귀속시킬 수 있어, Campaign이나 Canvases뿐만 아니라 어떤 채널이 결과를 이끌어내는지 파악할 수 있습니다.
* 마지막으로 접촉한 메시지에만 크레딧이 부여되므로 각 전환은 한 번만 집계되며, 공유 전환 이벤트와 오디언스를 가진 Campaign 또는 Canvases 간의 중복 전환이 제거됩니다.

## 보고서에 라스트 터치 기여도 측정기준 추가하기 {#add-last-touch-attribution-metrics-to-your-report}

1. **Analytics** 아래의 **보고서 빌더**로 이동합니다.
2. **보고서 생성** > **커스텀 보고서 생성**을 선택합니다.
3. **행** 드롭다운에서 보고서를 생성할 항목을 선택합니다.
4. (선택 사항) **드릴다운 추가**를 선택한 다음, 보고서를 더 깊이 분석할 영역을 선택합니다.
5. **열** 아래에서 **측정기준 커스터마이즈**를 선택합니다.
6. **전환** 아래에서 **라스트 터치 기여도**를 선택한 다음 **모두 선택**을 선택합니다.

{% alert note %}
매출 및 구매 측정기준은 사용할 수 없습니다.
{% endalert %}

![라스트 터치 기여도 측정기준이 표시된 측정기준 커스터마이즈 패널.]({% image_buster /assets/unlisted_docs/img/report_builder_2/lta_report_builder.png %})

{: start="7" }
7. [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/) 페이지의 7~9단계를 따릅니다.

{% alert note %}
고객 성공 매니저에게 피드백을 보내거나 **피드백 보내기** 버튼을 선택하여 피드백을 제공하세요.
{% endalert %}