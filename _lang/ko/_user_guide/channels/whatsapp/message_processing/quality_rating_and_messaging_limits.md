---
nav_title: 품질 등급 및 메시징 한도
article_title: 품질 등급 및 메시징 한도
description: "이 참조 문서에서는 Meta가 WhatsApp 채널의 품질 등급과 메시징 한도에 미치는 영향을 다룹니다."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
---

# 품질 등급 및 메시징 한도 {#quality-rating-and-messaging-limits}

> Meta는 WhatsApp 채널을 사용하기 시작하는 순간부터 품질 등급과 [메시징 한도](https://developers.facebook.com/docs/whatsapp/messaging-limits)에 영향을 미치며, WhatsApp 사용 현황에 따라 지속적으로 영향을 줍니다.

## 정의 {#definitions}

| 용어 | 정의 |
| --- | --- |
| 품질 등급 | 최근 7일 동안 고객이 수신한 메시지를 기반으로 한 등급입니다. 이 등급은 전화번호 차단 사유 및 기타 신고 문제 등 고객의 피드백에 의해 결정됩니다. [품질 등급에 대해](https://www.facebook.com/business/help/896873687365001) 자세히 알아보려면 Meta 설명서를 참조하세요.|
| 메시징 한도 | 24시간 롤링 기간 동안 각 전화번호로 시작할 수 있는 비즈니스 주도 대화의 최대 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definitions" }

## 온보딩 {#onboarding}

새 WhatsApp Business 계정이 생성되면 Meta는 다양한 요소를 사용하여 초기 발송 한도를 결정합니다. 이 한도는 WhatsApp Business Manager에서 확인할 수 있으며, 전화번호 인사이트 페이지에서 추가 세부 정보를 확인할 수 있습니다.

[한도 확인](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) 및 [전화번호 요구 사항](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers)에 대해 자세히 알아보려면 Meta 설명서를 참조하세요.

## 처리량 {#throughput}

Meta는 등록된 각 비즈니스 전화번호에 대해 초당 80개 메시지의 처리량으로 시작합니다. 초당 1,000개 메시지로의 업그레이드는 자동으로 또는 요청에 의해 이루어질 수 있습니다.

[처리량](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput)에 대해 자세히 알아보려면 Meta 설명서를 참조하세요.

## 템플릿 페이싱 {#template-pacing}

최근 생성된 마케팅 템플릿과 일시 중지 후 다시 활성화된 마케팅 템플릿은 페이싱의 대상이 될 수 있습니다. Meta의 페이싱 선택 기준은 주로 템플릿 품질 이력에 의해 결정됩니다. 최근 생성된 마케팅 템플릿이나 최근 다시 활성화된 마케팅 템플릿을 사용하면, 지정되지 않은 임계값에 도달할 때까지 메시지가 정상적으로 발송됩니다. 이 임계값에 도달하면, 해당 템플릿을 사용하는 후속 메시지는 고객 피드백을 위한 충분한 시간을 확보하기 위해 보류됩니다.

[템플릿 페이싱](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing)에 대해 자세히 알아보려면 Meta 설명서를 참조하세요.