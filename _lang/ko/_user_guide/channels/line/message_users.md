---
nav_title: 사용자에게 메시지 보내기
article_title: 사용자에게 메시지 보내기
page_order: 3
description: "이 참조 문서에서는 템플릿 기반 Campaigns와 Canvases를 사용하여 사용자와 대화하는 방법을 다룹니다."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# LINE 사용자에게 메시지 보내기 {#message-line-users}

> LINE은 양방향 소통 채널입니다. 단순히 사용자에게 메시지를 보내는 것을 넘어, 템플릿 기반 Campaigns와 Canvases를 사용하여 사용자와 대화할 수 있습니다. 이 문서에서는 인바운드 메시지의 트리거 단어 설정 방법과 인식되지 않는 응답 처리 등 사용자에게 메시지를 보내는 방법에 대한 세부 정보를 다룹니다.

LINE 트리거 단어를 사용하는 등 다양한 방법으로 LINE을 통해 사용자와 대화할 수 있습니다. 또한 콜투액션(CTA)을 사용하여 LINE 메시징에 대한 사용자 참여를 유도할 수 있습니다.

## 실행 기반 트리거 {#action-based-triggers}

인바운드 LINE 메시지(사용자가 보낸 메시지)에 트리거 단어가 포함되어 있을 때 시작되거나, 분기되거나, 중간에 변경되는 Campaigns와 Canvases를 생성할 수 있습니다. 사용자가 보낼 것으로 예상되는 내용과 일치하는 트리거 단어를 선택해야 합니다.

### Campaign

실행 기반 전달 Campaign을 예약할 때 트리거 단어를 설정합니다.

![실행 기반 트리거: "구독 그룹에 인바운드 LINE을 보낸 사용자에게 이 캠페인을 보내기, 메시지 본문이 다음인 경우"와 빈 필드.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canvas

Canvas의 [행동 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths/)에서 트리거 단어를 설정합니다.

![행동 경로 트리거: "구독 그룹에 인바운드 LINE을 보낸 사용자에게 이 캠페인을 보내기, 메시지 본문이 다음인 경우"와 빈 필드.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### 요구 사항 {#requirements}

Campaign 또는 Canvas를 구축할 때 트리거 단어의 각 글자는 대문자로 입력해야 합니다. 다만 Braze는 인바운드 트리거 단어가 대문자일 것을 요구하지 않습니다. 예를 들어, 트리거 단어가 "JOIN2023"인 경우 인바운드 메시지가 "jOin2023"이어도 Canvas 또는 Campaign이 트리거됩니다.

트리거 단어가 지정되지 않은 경우, Campaign 또는 Canvas는 *모든* 인바운드 LINE 메시지에 대해 실행됩니다. 여기에는 활성 Campaigns 및 Canvases에서 일치하는 문구가 있는 메시지도 포함되며, 이 경우 사용자는 두 개의 LINE 메시지를 받게 됩니다.

## 인식되지 않는 응답 {#unrecognized-responses}

인터랙티브 Canvases에는 인식되지 않는 응답에 대한 트리거 옵션을 포함해야 합니다. 이를 통해 사용자에게 사용 가능한 프롬프트(또는 트리거 단어)를 알리고 채널에 대한 기대치를 설정할 수 있습니다.

### 인식되지 않는 응답에 대한 트리거 생성 {#creating-a-trigger-for-unrecognized-responses}

커스텀 필터 문구에 대한 동작 그룹을 생성한 후, 행동 경로에 **LINE 메시지 보내기**에 대한 다른 동작 그룹을 추가하고 **메시지 본문이 다음인 경우**를 체크하지 마세요. 이렇게 하면 "else" 절과 유사하게 인식되지 않는 모든 사용자 응답을 포착합니다.

이 메시지에서는 해당 채널이 사람이 모니터링하지 않는다는 것을 사용자에게 알리는 LINE 메시지를 보내고, 필요한 경우 고객지원 채널로 안내해야 합니다.