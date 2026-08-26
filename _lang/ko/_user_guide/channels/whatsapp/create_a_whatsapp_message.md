---
nav_title: WhatsApp 메시지 만들기
article_title: WhatsApp 메시지 만들기
page_order: 1
description: "이 참조 문서에서는 WhatsApp 메시지를 만들고 WhatsApp 관련 필드, 설정, 메시지 동작을 구성하는 방법을 다룹니다."
page_type: reference
tool:
  - Campaigns
  - Canvas
channel:
  - WhatsApp
search_rank: 1
---

# WhatsApp 메시지 만들기 {#create-a-whatsapp-message}

> WhatsApp Campaign을 사용하여 고객에게 직접 도달하세요. Liquid 및 기타 동적 콘텐츠를 사용하여 각 메시지를 개인화하고 일관된 브랜드 경험을 만들 수 있습니다.

## 사전 요구 사항 {#prerequisites}

시작하기 전에 다음 사항을 준비하세요:

| 요구 사항 | 설명 |
| --- | --- |
| Campaign 또는 Canvas | WhatsApp 메시지를 작성하기 전에 [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) 또는 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)를 설정하세요. |
| WhatsApp 채널 설정 | [WhatsApp 설정 플로우]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)를 완료하세요: 정책을 확인하고, 연결을 설정하고, 발송 인프라를 구성합니다. |
| 승인된 템플릿 | 비즈니스에서 시작하는 발송의 경우 Meta에서 템플릿을 만들고 승인받으세요. 자세한 내용은 [WhatsApp 설정의 3단계]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="WhatsApp 메시지 사전 요구 사항" }

## 메시지 유형 {#message-type}

WhatsApp은 Braze에서 두 가지 메시지 유형을 지원합니다:

- **템플릿 메시지:** 비즈니스에서 시작하는 대화에 사용합니다. 템플릿은 발송 전에 Meta에서 승인을 받아야 합니다.
- **응답 메시지:** 활성 24시간 대화 기간 내에서 인바운드 사용자 메시지에 답장할 때 사용합니다.

## 구독 그룹 {#subscription-group}

각 메시지 배리언트 또는 Canvas 메시지 단계에 대해 WhatsApp 구독 그룹을 선택합니다. 구독 그룹은 어떤 발신자 구성이 사용되는지, 어떤 사용자가 메시지를 수신할 자격이 있는지를 결정합니다.

## 템플릿 메시지 언어 {#languages-for-template-messages}

승인된 각 템플릿은 특정 언어에 연결되어 있습니다. 여러 템플릿 언어를 지원해야 하는 경우 별도의 배리언트 또는 캔버스 단계를 구성하세요.

오른쪽에서 왼쪽으로 쓰는 언어로 문구를 추가하는 경우 [오른쪽에서 왼쪽으로 쓰는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

## 작성 {#step-2-compose-your-whatsapp-message}

메시지 작성기에서 WhatsApp 콘텐츠를 작성합니다. WhatsApp 관련 설정 옵션은 아래 필드 참조를 사용하세요.

| 필드 또는 설정 | 제어 항목 | 참고 |
| --- | --- | --- |
| **구독 그룹** | WhatsApp 발신자 및 메시지의 대상 오디언스입니다. | 연결된 발신 전화번호는 **테스트** 탭 알림에 표시됩니다. |
| **메시지 유형** | 배리언트가 템플릿 메시지를 보낼지 응답 메시지를 보낼지 설정합니다. | 비즈니스에서 시작하는 발송에는 템플릿이 필요합니다. 응답 메시지에는 활성 대화 기간이 필요합니다. |
| **템플릿** (템플릿 메시지) | 메시지 발송에 사용되는 승인된 Meta 템플릿입니다. | 작성기에서 비활성화된 필드는 승인된 템플릿에서 가져온 것이며, Meta에서만 변경하고 재승인을 받을 수 있습니다. |
| **언어** (템플릿 메시지) | 배리언트 또는 단계에 대해 선택된 템플릿 언어입니다. | 수신자를 정확하게 매칭하려면 언어별로 캠페인 배리언트 또는 캔버스 단계를 생성하세요. |
| **변수** (템플릿 메시지) | 템플릿 변수 입력 안내에 삽입되는 값입니다. | 이중 중괄호에 Liquid 또는 일반 텍스트를 사용하세요. 프로필 데이터가 누락되었을 때 발송이 실패하지 않도록 Liquid에 기본값을 포함하세요. |
| **동적 링크** | 개인화된 행동 유도 URL입니다. | Meta에서는 변수가 CTA URL 끝에 위치해야 합니다. |
| **동적 이미지** | 템플릿 또는 응답 메시지에 사용되는 미디어 URL 또는 미디어 라이브러리 이미지입니다. | 동적 이미지는 URL에서 Liquid 및 연결된 콘텐츠를 지원합니다. |
| **응답 레이아웃** (응답 메시지) | 응답 콘텐츠의 형식입니다. | 지원되는 레이아웃은 빠른 답장, 텍스트 메시지, 미디어 메시지, 행동 유도 버튼, 목록 메시지, 플로우 메시지, Meta 제품 메시지, 캐러셀입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="WhatsApp 관련 필드 및 설정" }

{% tabs %}
{% tab 템플릿 메시지 %}

### 템플릿 메시지 {#template-messages}

[승인된 WhatsApp 템플릿 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates)를 사용하여 WhatsApp에서 대화를 시작합니다. 템플릿 승인은 Meta에서 처리하며 최대 24시간이 소요될 수 있습니다. 템플릿 문구를 수정하는 경우 Meta에서 업데이트하고 재승인을 위해 다시 제출하세요.

Campaign 또는 Canvas 작성기를 떠나지 않고 새 템플릿을 만들어 제출하려면 **새 템플릿 만들기**를 선택하세요. 카테고리, 유형 및 전체 빌드 프로세스에 대한 자세한 내용은 [WhatsApp 템플릿 빌더]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder)를 참조하세요.

비활성화된 텍스트 필드(회색으로 표시)는 승인된 WhatsApp 템플릿의 일부이므로 편집할 수 없습니다. 비활성화된 텍스트를 업데이트하려면 템플릿을 수정하고 재승인을 받아야 합니다.

#### 콘텐츠 필드 {#content-fields}

변수, 동적 링크 및 동적 이미지의 정의는 필드 참조 테이블을 사용하세요. 이 섹션에서는 템플릿별 동작 및 예시를 다룹니다.

![메시지 미리보기, 할당된 언어, 승인 상태가 표시된 템플릿 목록.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

{% alert tip %}
Liquid를 사용하는 경우 개인화 필드에 기본값을 포함하세요. 개인화 값이 누락된 메시지는 WhatsApp에서 발송되지 않습니다.
{% endalert %}

![속성 'first_name'과 기본값 'you'가 설정된 개인화 추가 도구.]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### 동적 이미지 {#dynamic-images}

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab 응답 메시지 %}

### 응답 메시지 {#response-messages}

응답 메시지를 사용하여 활성 24시간 대화 기간 동안 인바운드 사용자 메시지에 답장합니다. 이러한 메시지는 Braze에서 작성되며 언제든지 편집할 수 있습니다.

응답 메시지는 다음 레이아웃을 지원합니다:
- 빠른 답장
- 텍스트 메시지
- 미디어 메시지
- 행동 유도 버튼
- 목록 메시지
- 플로우 메시지
- Meta 제품 메시지
- 캐러셀

![할인 코드로 신규 사용자를 환영하는 답장 메시지의 응답 메시지 작성기.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

## WhatsApp 테스트 발송 결과 {#step-4-view-test-send-results}

WhatsApp 테스트 메시지를 발송한 후, 메시지 작성기에서 직접 상세한 전달 보고서를 확인할 수 있습니다. 이를 통해 메시지가 의도한 수신자에게 도달했는지 확인하고, 출시 전에 실패 원인을 해결할 수 있습니다.

테스트 발송 데이터가 현재 Campaign 또는 캔버스 단계에서 사용 가능한 경우 **테스트 결과 보기** 버튼이 표시됩니다. 이 버튼을 선택하면 결과 패널이 열립니다.

결과 패널에는 메시지가 수신자에게 전달되기까지 거치는 각 단계가 표시됩니다:
- **Braze:** Braze가 메시지를 성공적으로 처리하고 발송했는지 여부
- **Meta:** Meta가 메시지를 전달용으로 수락했는지 여부
- **사용자 기기:** 메시지가 수신자의 기기에 전달되었는지 여부

각 단계는 현재 상태를 표시합니다. 단계가 실패한 경우, 패널에 발생한 오류와 해결 방법에 대한 안내가 표시됩니다. 동일한 Campaign 또는 Canvas를 닫았다가 다시 열어도 결과는 유지됩니다.

![테스트 결과 패널에 두 건의 성공적인 테스트 발송과 한 건의 실패한 테스트 발송이 표시되어 있습니다.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

### 재시도 및 이전 시도 {#retries-and-past-attempts}

테스트 발송이 실패하면, Braze가 최대 24시간 동안 자동으로 전달을 재시도합니다. 결과 패널에는 두 개의 탭으로 이 내용이 반영됩니다:

- **최신:** 재시도가 발생할 때마다 실시간으로 업데이트되는 가장 최근의 전달 시도
- **이전 시도:** 이전 재시도 실행 이력으로, 각 단계의 상태와 발생한 오류가 표시됩니다

최종 결과가 결정되면(전달 성공, 재시도 소진, 또는 재시도로 해결할 수 없는 실패), 탭 이름이 각각 **결과**와 **재시도 이력**으로 변경됩니다.

{% alert note %}
재시도가 최대 24시간 동안 계속될 수 있으므로, 발송 실패 직후에는 최종 결과가 바로 표시되지 않을 수 있습니다.
{% endalert %}

### 실패 문제 해결 {#troubleshoot-failures}

단계에서 실패가 표시되면, 패널에 오류와 권장 조치가 표시됩니다. 테스트 발송이 실패하는 일반적인 원인은 다음과 같습니다:

- Meta에서 메시지 템플릿이 일시 중지되었거나 아직 승인되지 않은 경우
- 수신자의 전화번호가 속도 제한에 걸린 경우
- 메시지의 Liquid 변수가 선택한 테스트 사용자에 대해 채워지지 않은 경우

문제가 지속되는 경우, Meta Business Manager에서 템플릿 상태를 확인하거나 테스트 수신자에게 필요한 사용자 속성이 Braze에서 채워져 있는지 확인하세요.

## 알아두어야 할 사항 {#supported-whatsapp-features}

### 아웃바운드 메시지 {#outbound-messages}

Braze를 통해 발송하는 아웃바운드 WhatsApp 메시지에서 다음 기능이 지원됩니다:

| 기능 | 세부 사항 | 최대 크기 | 지원 형식 |
| ------- | ------- | ------------- | ---------------------- |
| 헤더 텍스트 | 문자열 및 변수 매개변수가 지원됩니다. | — | —
| 본문 텍스트 | 문자열 및 변수 매개변수가 지원됩니다. | — | — |
| 푸터 텍스트 | 문자열 및 변수 매개변수가 지원됩니다. | — | — |
| CTA 링크 | 다양한 콜투액션(CTA) 유형이 지원됩니다. 자세한 내용은 [콜투액션 유형](#ctas)을 참조하세요. | — | — |
| 이미지 | 이미지는 본문 텍스트 내에 삽입할 수 있습니다. 8비트여야 하며 RGB 또는 RGBA 색상 모델을 사용해야 합니다. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| 문서 | 문서는 본문 텍스트 내에 삽입할 수 있습니다. 파일은 URL을 통해 호스팅되어야 합니다. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| 비디오 | 비디오는 본문 텍스트 내에 삽입할 수 있습니다. 파일은 URL 또는 [Braze 미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library)를 통해 호스팅되어야 합니다. | < 16 MB | `.3gp`, `.mp4` |
| 오디오 | 오디오는 응답 메시징을 통해서만 지원됩니다. 파일은 URL을 통해 호스팅되어야 합니다. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="아웃바운드 메시지" }

{% multi_lang_include alerts/important_alerts.md alert='Meta MP4 video issue' %}

### 인바운드 메시지 {#inbound-messages}

Braze를 통해 수신하는 인바운드 WhatsApp 메시지에서 다음 기능이 지원됩니다:

| 기능 | 세부 사항 | 지원 형식 |
| ------- | ------- | ------------------ |
| 본문 텍스트 | 표준 문자열만 지원됩니다. | — |
| 이미지 | 이미지는 8비트여야 하며 RGB 또는 RGBA 색상 모델을 사용해야 합니다. 파일 크기는 5 MB 미만이어야 합니다. | `.jpg`, `.png` |
| 오디오 | Opus 코덱으로 인코딩된 Ogg 파일만 지원됩니다. 다른 Ogg 형식은 지원되지 않습니다. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| 문서 | 문서는 메시지 첨부를 통해 지원됩니다. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| 비디오 | H.264 비디오 코덱과 AAC 오디오 코덱만 지원됩니다. 비디오에는 단일 오디오 스트림이 있거나 오디오 스트림이 없어야 합니다. | `.mp4`, `.3gp` |
| CTA 링크 | 다양한 콜투액션(CTA) 유형이 지원됩니다. 자세한 내용은 [콜투액션 유형](#ctas)을 참조하세요. | — |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="인바운드 메시지" }

### 콜투액션 유형 {#ctas}

Braze를 통해 발송하는 WhatsApp 메시지에서 다음 콜투액션 유형이 지원됩니다:

| CTA 유형 | 세부 사항 |
| ----------- |---------------- |
| 웹사이트 방문 | 최대 1개의 버튼(변수 매개변수 포함). |
| 전화번호 호출 | 메시지 템플릿에서만 사용 가능합니다. <br>최대 1개의 버튼. |
| 커스텀 빠른 답장 버튼 | 최대 3개의 버튼. |
| 마케팅 옵트아웃 버튼 | 기본적으로 구독 상태는 자동으로 업데이트되지 않습니다. 전체 안내는 [옵트인 및 옵트아웃]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs#marketing-opt-out-selection)을 참조하세요. |
| 쿠폰 코드 메시지 템플릿 | 메시지 템플릿에서만 사용 가능합니다. <br>다른 메시지 템플릿처럼 열고 편집할 수 있으며, Liquid 및 Braze 프로모션 코드와 호환됩니다. |
| CTA 응답 메시지 | 콜투액션 버튼이 포함된 응답 메시지를 생성합니다. |
| [목록 응답 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | 사용자가 선택할 수 있는 최대 10개의 옵션 목록이 포함된 응답 메시지를 생성합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="콜투액션 유형 #ctas" }

## 다음 단계 {#next-steps}

WhatsApp 메시지를 작성한 후, 발송을 계속 구성하고 검증하세요:

- [Campaign 스케줄 설정]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) 또는 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) 구성 계속하기
- [사용자 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) 및 [전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) 설정
- [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp)
- [WhatsApp 리포팅]({{site.baseurl}}/user_guide/channels/whatsapp/reporting) 검토