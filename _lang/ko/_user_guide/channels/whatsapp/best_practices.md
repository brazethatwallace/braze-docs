---
nav_title: 모범 사례
article_title: 모범 사례
page_order: 22
description: "이 문서에서는 높은 전화 품질 등급을 유지하고 높은 차단 및 신고율을 방지하는 방법을 포함하여 WhatsApp 메시징 채널 사용 시 권장되는 모범 사례를 설명합니다."
page_type: reference
channel:
  - WhatsApp

---
# WhatsApp 모범 사례 {#whatsapp-best-practices}

> WhatsApp 메시지를 발송하기 전에 높은 전화 품질 등급을 유지하고, 차단 및 신고를 방지하며, 사용자의 옵트인 및 옵트아웃을 관리하기 위한 권장 모범 사례를 참조하세요.

## 높은 전화 품질 등급 유지하기 {#maintain-a-high-phone-quality-rating}

WhatsApp은 메시지를 수신하는 사용자가 비즈니스를 차단하거나 신고하는 등의 행동을 기반으로 [전화 품질 등급](https://www.facebook.com/business/help/896873687365001)을 산정합니다. 높은 품질 등급을 유지하는 것이 중요합니다. 등급이 낮고 일정 기간 내에 개선되지 않으면 메시징 한도가 줄어들 수 있기 때문입니다.

WhatsApp에서 사용자에게 처음 메시지를 보내면 메시지 스레드 내에 다음과 같은 옵션이 표시됩니다.

![비즈니스를 차단하거나 신고할 수 있는 옵션이 있는 WhatsApp 메시지 스레드]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
차단 및 신고에 대한 측정기준을 확인하려면 WhatsApp Manager에서 [인사이트 탭](https://www.facebook.com/business/help/683499390267496)이 활성화되어 있는지 확인하세요.
{% endalert %}

높은 차단 및 신고 발생을 방지하기 위해 Braze는 높은 전화 품질 등급과 안정적인 메시징 한도를 유지하기 위한 다음 모범 사례를 권장합니다.

### WhatsApp 옵트인 요구 사항 및 가이드라인 준수하기 {#follow-whatsapp-opt-in-requirements-and-guidelines}

WhatsApp에서 사용자와 커뮤니케이션을 시작하기 전에 모든 사용자가 WhatsApp 메시지 수신에 적극적으로 동의했는지 확인하세요. 사용자에게 옵트인을 요청할 때, WhatsApp을 통해 비즈니스로부터 메시지를 수신하는 것에 구체적으로 동의하는 것임을 안내해야 합니다.

{% alert note %}
옵트인 요구 사항 및 유용한 팁에 대한 자세한 내용은 [WhatsApp 옵트인 받기](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)를 참조하세요.
{% endalert %}

### 메시징 모범 사례 준수하기 {#follow-messaging-best-practices}

- 사용자가 메시지가 스팸이 아닌 브랜드에서 보낸 것임을 인식할 수 있도록 채널 이름에 브랜드를 반영하세요.
- 사용자의 옵트인 동의를 수집한 후 확인 메시지를 발송하세요.
- 적절한 시간에 메시지를 발송하세요.

### 고객에게 옵트아웃 옵션 제공하기 {#give-customers-the-option-to-opt-out}

옵트아웃은 전화 품질 등급에 영향을 미치지 않으므로, 사용자가 차단하거나 신고하는 것보다 WhatsApp 커뮤니케이션 수신을 옵트아웃하는 것이 더 좋습니다.

권장 모범 사례는 사용자에게 보내는 첫 번째 메시지의 푸터에 옵트아웃 방법에 대한 안내를 제공하는 것입니다. 예를 들어, 옵트아웃 트리거 단어로 응답하면 WhatsApp 채널 구독을 취소할 수 있다고 안내할 수 있습니다. 또한 향후 Campaign에 옵트아웃 푸터를 정기적으로 포함할 수도 있습니다. 설정 방법에 대해 알아보려면 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs)을 참조하세요.

![채널 구독을 취소하려면 STOP으로 응답하라는 푸터가 있는 WhatsApp 메시지]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}

### 양방향 플로우의 응답 지연 시간 최소화하기 {#minimize-response-latency-for-two-way-flows}

[응답 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#response-messages)로 회신하는 인터랙티브 Canvas 플로우의 경우:

- 응답 메시지 단계를 인바운드 트리거 또는 행동 경로 평가 직후에 배치하세요.
- 회신 전에 구독 변경이 필요하지 않은 경우 사용자 업데이트 단계 대신 [웹훅]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)을 사용하세요.
- 인바운드 메시지와 응답 발송 사이에 긴 지연이나 며칠 간의 대기를 피하세요. WhatsApp 고객 서비스 창은 인바운드 메시지당 24시간입니다.