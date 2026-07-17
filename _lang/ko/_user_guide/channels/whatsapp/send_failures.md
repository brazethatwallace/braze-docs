---
nav_title: 전송 실패
article_title: WhatsApp 전송 실패 조사
page_order: 22
page_type: reference
description: "Campaign 분석, 메시지 활동 로그, Currents를 사용하여 WhatsApp 전송 실패 및 일반적인 Meta 오류 코드를 조사합니다."
tool:
  - Reports
channel:
  - WhatsApp
---

# WhatsApp 전송 실패 조사 {#investigate-whatsapp-send-failures}

> WhatsApp 전달 또는 읽음 수가 예상보다 낮거나, Campaign 분석에서 **실패** 수치가 높아 보일 때 이 페이지를 참고하세요.

## 조사 워크플로 {#investigation-workflow}

다음 단계를 순서대로 진행하세요.

1. **Campaign 또는 Canvas 분석에서 실패를 확인합니다.** 메시지 단계를 열고 **실패** 횟수와 실패율을 검토합니다. 전송 또는 전달 대비 실패가 높아 보이면 다음 단계로 진행합니다.
2. **메시지 활동 로그에서 오류 코드를 찾습니다.** 동일한 전송에 대해 [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)를 열고, 실패한 메시지로 필터링한 후 공급자 오류 코드를 확인합니다(예: 사용자별 마케팅 제한의 경우 `131049`). [일반적인 실패 코드](#common-failure-codes)를 참고하여 코드를 해석하고 다음 조치를 결정합니다.
3. **Currents를 통해 실패 데이터를 내보내 분석 또는 리타겟팅에 활용합니다.** 오류 코드를 파악한 후, Currents를 통해 WhatsApp 전송 실패 이벤트를 내보냅니다. 해당 데이터를 사용하여 데이터 웨어하우스에서 실패 추세를 분석하거나, Segment를 구축하여 다른 채널로 사용자를 리타겟팅할 수 있습니다.

## 일반적인 실패 코드 {#common-failure-codes}

| 오류 코드 | 일반적인 원인 | 다음 조치 |
|---|---|---|
| `131049` | Meta 사용자별 마케팅 빈도 제한 또는 미국 마케팅 일시 중지 | [Meta 리소스]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources) 및 [다른 Braze 채널에서 사용자 리타겟팅]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/optimized_delivery#retargeting-users-on-other-braze-channels)을 참고하세요 |
| `130472` | Meta 마케팅 실험 홀드아웃 | [Meta 리소스 FAQ]({{site.baseurl}}/user_guide/channels/whatsapp/meta_resources#faq)를 참고하세요 |
| `131026` | 다양한 미전달 사유(Meta에서 구체적인 내용을 공개하지 않음) | 즉시 재시도를 피하고, [Meta Cloud API 문제 해결](https://developers.facebook.com/docs/whatsapp/cloud-api/support#troubleshooting)을 검토하세요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="일반적인 WhatsApp 실패 코드" }