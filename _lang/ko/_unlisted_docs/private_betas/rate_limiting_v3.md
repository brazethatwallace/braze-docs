---
article_title: 푸시 Campaign 및 멀티채널 Canvases의 사용량 제한
permalink: /rate_limiting_v3/
page_type: reference
description: "이 문서에서는 푸시 Campaign 및 멀티채널 Canvases의 전달 속도 사용량 제한에 대해 설명합니다."
---

# 푸시 Campaign 및 멀티채널 Canvases의 사용량 제한 {#rate-limiting-for-push-campaigns-and-multichannel-canvases}

> 이 페이지에서는 푸시 Campaign 및 멀티채널 Canvases의 사용량 제한과 메시지를 조절할 때 유의해야 할 사항을 다룹니다.

푸시 Campaign 및 멀티채널 Canvases의 전달 속도 사용량 제한을 설정할 때, 이제 다음 중 하나를 선택할 수 있습니다:

- 채널별 사용량 제한
- 모든 메시지 채널에 공유되는 전체 사용량 제한

{% alert important %}
푸시 Campaign 및 멀티채널 Canvases의 사용량 제한은 얼리 액세스 단계에 있습니다. 이 얼리 액세스에 참여하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

다음 기능은 이 얼리 액세스에 **포함되지 않습니다**:

- 모든 유형의 멀티채널 Campaign 및 API 트리거 Canvases에 대한 채널별 사용량 제한 설정
- 글로벌 사용량 제한 설정
- Canvas에서 메시지 단계별 사용량 제한 설정

## 고려 사항 {#considerations}

- 이 사용량 제한 업데이트는 매우 낮은 사용량 제한을 설정하는 것을 방지하지 않습니다. 즉, 이러한 방지 기능이 없는 상태에서 사용량 제한을 설정하면 오디언스 규모에 따라 메시지가 매우 느린 속도로 발송될 수 있습니다.
- Campaign 및 Canvases의 **발송 설정** 요약에는 설정된 사용량 제한에 대한 부정확한 설명이 포함될 수 있습니다: <br><br>![사용자가 메시지를 수신하는 속도에 제한이 없는 Campaign의 발송 설정.]({% image_buster /assets/unlisted_docs/img/send_settings_example.png %}){: style="max-width:65%"}<br><br>
- 멀티채널 Campaign(Canvases 또는 푸시 Campaign 제외)의 사용량 제한은 [업데이트되지 않은 멀티채널 Campaign 사용량 제한 동작](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting)을 반영합니다. 이 얼리 액세스 단계에 참여하는 동안에는 사용량 제한이 적용된 멀티채널 Campaign을 생성하지 않는 것을 권장합니다.