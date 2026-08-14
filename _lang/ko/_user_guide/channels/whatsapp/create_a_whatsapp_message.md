---
nav_title: WhatsApp 메시지 만들기
article_title: WhatsApp 메시지 만들기
page_order: 1
description: "이 참조 문서에서는 WhatsApp 메시지를 구축하고 만드는 단계를 다룹니다."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# WhatsApp 메시지 만들기 {#create-a-whatsapp-message}

> WhatsApp Campaign은 고객에게 직접 도달하고 프로그래밍 방식으로 대화하는 데 매우 유용합니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자와 개인화된 경험을 만들고, 브랜드와의 자연스러운 사용자 경험을 촉진하고 향상시키는 환경을 조성할 수 있습니다.

## 사전 요구 사항 {#prerequisites}

WhatsApp 메시지를 만들기 전에 [WhatsApp 개요]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup)에서 다음 사항을 검토하고 완료해야 합니다:
  - 정책, 제한 사항 및 콘텐츠 규칙 확인
  - WhatsApp 연결 설정
  - 메시지에 사용할 초기 템플릿을 Meta에서 작성

## 메시지 만들기 {#creating-a-message}

### 1단계: 메시지 작성 위치 선택 {#step-1-choose-where-to-build-your-message}

{% alert note %}
WhatsApp은 각 언어별로 서로 다른 [메시지 템플릿](#template-messages)을 생성합니다. 각 언어에 맞는 Campaign을 세분화하여 사용자에게 올바른 템플릿을 제공하거나, Canvas를 사용하세요.
{% endalert %}

메시지를 Campaign으로 보낼지 Canvas로 보낼지 확실하지 않으신가요? Campaigns는 단일 타겟팅 메시징 캠페인에 적합하고, Canvases는 다단계 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab Campaign %}

**단계:**

1. **Campaigns** 페이지로 이동하여 <i class="fas fa-plus"></i> **Create Campaign**을 클릭합니다.
2. **WhatsApp**을 선택하거나, 여러 채널을 타겟팅하는 캠페인의 경우 **Multichannel Campaign**을 선택합니다.
3. 캠페인에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams) 및 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가합니다.
   * 태그를 사용하면 캠페인을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더]({{site.baseurl}}/user_guide/analytics/reports/report_builder)를 사용할 때 특정 태그로 필터링할 수 있습니다.
5. 캠페인에 필요한 만큼 배리언트를 추가하고 이름을 지정합니다. 추가된 각 배리언트에 대해 서로 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% alert tip %}
캠페인의 모든 메시지가 유사하거나 동일한 콘텐츠를 가지고 있다면, 추가 배리언트를 추가하기 전에 먼저 메시지를 작성하세요. 그런 다음 **Add Variant** 드롭다운에서 **Copy from Variant**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**단계:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% alert tip %}
실행 기반 Canvas가 인바운드 WhatsApp 메시지에 의해 트리거되는 경우, 다음 행동 경로까지 모든 캔버스 단계에서 WhatsApp 속성을 참조할 수 있습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

### 2단계: WhatsApp 메시지 작성 {#step-2-compose-your-whatsapp-message}

사용 사례에 따라 WhatsApp [템플릿 메시지](#template-messages) 또는 응답 메시지를 만들지 선택합니다. 비즈니스에서 시작하는 모든 대화는 승인된 템플릿에서 시작해야 하며, 응답 메시지는 24시간 이내에 사용자의 인바운드 메시지에 대한 응답으로 사용할 수 있습니다.

![메시지 배리언트 섹션에서 구독 그룹과 두 가지 메시지 유형(WhatsApp 템플릿 메시지 및 응답 메시지) 중 하나를 선택할 수 있습니다.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab 템플릿 메시지 %}

[승인된 WhatsApp 템플릿 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup#step-3-create-whatsapp-templates
)를 사용하여 WhatsApp에서 사용자와 대화를 시작할 수 있습니다. 이러한 메시지는 콘텐츠 승인을 위해 WhatsApp에 사전 제출되며, 승인까지 최대 24시간이 소요될 수 있습니다. 문구를 수정하면 WhatsApp에 다시 편집하여 재제출해야 합니다.

비활성화된 텍스트 필드(회색으로 강조 표시)는 승인된 WhatsApp 템플릿의 일부이므로 편집할 수 없습니다. 비활성화된 텍스트를 업데이트하려면 템플릿을 편집하고 재승인을 받아야 합니다.

#### 언어 {#languages}

각 템플릿에는 지정된 언어가 있으므로, 사용자 매칭을 올바르게 설정하려면 각 언어에 대해 Campaign 또는 캔버스 단계를 만들어야 합니다. 예를 들어, 인도네시아어와 영어로 지정된 템플릿을 사용하는 Canvas를 구축하는 경우, 인도네시아어 템플릿용 캔버스 단계와 영어 템플릿용 캔버스 단계를 만들어야 합니다.

![메시지 미리보기, 지정된 언어 및 승인 상태를 포함한 템플릿 목록.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

오른쪽에서 왼쪽으로 쓰는 언어로 문구를 추가하는 경우, 오른쪽에서 왼쪽으로 쓰는 메시지의 최종 모양은 서비스 제공업체가 렌더링하는 방식에 크게 좌우됩니다. 가능한 한 정확하게 표시되는 오른쪽에서 왼쪽으로 쓰는 메시지를 작성하는 모범 사례는 [오른쪽에서 왼쪽으로 쓰는 메시지 만들기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)를 참조하세요.

#### 변수 {#variables}

Meta Business Manager에서 WhatsApp 템플릿을 만들 때 변수를 추가한 경우, 해당 변수는 메시지 작성기에서 빈 공간으로 표시됩니다. 이 빈 공간을 Liquid 또는 일반 텍스트로 대체하세요. 일반 텍스트를 사용하려면 이중 중괄호로 감싼 "여기에 텍스트" 형식을 사용합니다. 템플릿을 만들 때 이미지를 포함하도록 선택한 경우, 미디어 라이브러리에서 이미지를 업로드하거나 추가하거나 이미지 URL을 참조하여 이미지를 추가할 수 있습니다. 가능하면 일관성과 안정성을 보장하기 위해 미디어 라이브러리에 직접 이미지를 업로드하는 것을 권장합니다.

비활성화된 텍스트 필드(회색으로 강조 표시)는 승인된 WhatsApp 템플릿의 일부이므로 편집할 수 없습니다. 비활성화된 텍스트를 업데이트하려면 템플릿을 편집하고 재승인을 받아야 합니다.

{% alert tip %}
{% raw %}
Liquid를 사용할 계획이라면, 수신자의 사용자 프로필이 불완전한 경우에도 메시지를 받을 수 있도록 선택한 개인화에 기본값을 포함해야 합니다. Liquid 변수가 누락된 메시지는 WhatsApp에서 발송되지 않습니다.
{% endraw %}
{% endalert %}

![속성 'first_name'과 기본값 'you'가 있는 개인화 추가 도구.]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### 동적 링크 {#dynamic-links}

행동 유도 URL에는 변수가 포함될 수 있지만, Meta에서는 `{% raw %}https://example.com/{{variable}}{% endraw %}`와 같이 URL 끝에 위치해야 합니다. 이 변수는 Braze에서 Liquid로 대체할 수 있습니다. 링크는 템플릿의 일부로 본문 텍스트에도 포함할 수 있습니다. 이 두 가지 링크 모두 [클릭 추적]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/click_tracking)을 사용하여 단축하고 추적할 수 있습니다.

### 동적 이미지 {#dynamic-images}

미디어 라이브러리 또는 URL에서 이미지를 추가할 수 있습니다. URL을 사용하는 경우, URL의 어디에서나 전체 Liquid 로직을 포함하여 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)로 이미지를 개인화할 수 있습니다. 동적 이미지는 템플릿 메시지와 응답 메시지(미디어 메시지 및 빠른 답장 레이아웃)에서 지원됩니다.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab 응답 메시지 %}

응답 메시지를 사용하여 사용자의 인바운드 메시지에 답장할 수 있습니다. 이러한 메시지는 작성 과정에서 Braze 내에서 앱 내에서 빌드되며 언제든지 편집할 수 있습니다. Liquid를 사용하여 응답 메시지 언어를 적절한 사용자에게 매칭할 수 있습니다.

사용할 수 있는 응답 메시지 레이아웃은 다섯 가지입니다:
- 빠른 답장
- 텍스트 메시지
- 미디어 메시지
- 행동 유도 버튼
- 목록 메시지

![할인 코드로 신규 사용자를 환영하는 답장 메시지의 응답 메시지 작성기.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### 3단계: 메시지 미리보기 및 테스트 {#step-3-preview-and-test-your-message}

Braze는 항상 메시지를 보내기 전에 미리보기하고 테스트할 것을 권장합니다. **Test** 탭으로 전환하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) 또는 개별 사용자에게 테스트 WhatsApp 메시지를 보내거나, Braze에서 직접 사용자로서 메시지를 미리볼 수 있습니다.

![커스텀 사용자 Max에 대한 미리보기 메시지.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
응답 메시지(테스트 메시지 포함)를 보내려면 대화 창이 필요합니다. 대화 창을 시작하려면 이 메시지에 사용 중인 구독 그룹과 연결된 전화번호로 WhatsApp 메시지를 보내세요. 연결된 전화번호는 **Test** 탭의 알림에 나열되어 있습니다.
{% endalert %}

![WhatsApp 메시지를 보내 메시지 창을 열고, 테스트 사용자에게 메시지를 보내라는 알림.]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=whatsapp)를 참조하세요.

### 4단계: 테스트 발송 결과 확인 {#step-4-view-test-send-results}

테스트 WhatsApp 메시지를 보낸 후, 메시지 작성기에서 직접 상세한 전달 보고서를 확인할 수 있습니다. 이를 통해 메시지가 의도한 수신자에게 도달했는지 확인하고 출시 전에 실패를 해결할 수 있습니다.

**View test results** 버튼은 현재 Campaign 또는 캔버스 단계에 대한 테스트 발송 데이터가 있을 때 나타납니다. 이를 선택하여 결과 패널을 엽니다.

결과 패널은 메시지가 수신자에게 전달되는 과정에서 거친 각 단계를 보여줍니다:
- **Braze:** Braze가 메시지를 성공적으로 처리하고 발송했는지 여부
- **Meta:** Meta가 전달을 위해 메시지를 수락했는지 여부
- **사용자 기기:** 메시지가 수신자의 기기에 전달되었는지 여부

각 단계는 현재 상태를 표시합니다. 단계가 실패한 경우, 패널에 발생한 오류와 해결 방법에 대한 안내가 표시됩니다. 동일한 Campaign 또는 Canvas를 닫았다가 다시 열어도 결과는 유지됩니다.

![두 건의 성공적인 테스트 발송과 한 건의 실패한 테스트 발송을 보여주는 테스트 결과 패널.]({% image_buster /assets/img/whatsapp/whatsapp_test_results.png %}){: style="max-width:80%;"}

#### 재시도 및 이전 시도 {#retries-and-past-attempts}

테스트 발송이 실패하면 Braze는 최대 24시간 동안 자동으로 전달을 재시도합니다. 결과 패널에는 두 개의 탭이 표시됩니다:

- **Latest:** 재시도가 발생할 때 실시간으로 업데이트되는 가장 최근 전달 시도
- **Past attempts:** 각 단계 상태와 발생한 오류를 보여주는 이전 재시도 기록

최종 결과가 결정되면(성공적인 전달, 재시도 소진 또는 재시도로 해결할 수 없는 실패), 탭 이름이 각각 **Result**와 **Retry history**로 변경됩니다.

{% alert note %}
재시도가 최대 24시간 동안 계속될 수 있으므로, 발송 실패 직후에 최종 결과를 확인하지 못할 수 있습니다.
{% endalert %}

#### 실패 문제 해결 {#troubleshoot-failures}

단계에서 실패가 표시되면, 패널에 오류와 제안된 다음 단계가 표시됩니다. 테스트 발송이 실패할 수 있는 일반적인 이유는 다음과 같습니다:

- 메시지 템플릿이 Meta에서 일시 중지되었거나 아직 승인되지 않음
- 수신자의 전화번호가 속도 제한됨
- 메시지의 Liquid 변수가 선택한 테스트 사용자에 대해 채워지지 않음

지속적인 문제의 경우, Meta Business Manager에서 템플릿 상태를 확인하거나 테스트 수신자가 Braze에서 필요한 사용자 속성이 채워져 있는지 확인하세요.

### 5단계: 캠페인 또는 Canvas의 나머지 부분 구축 {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

다음으로, 캠페인의 나머지 부분을 구축합니다. WhatsApp 메시지를 구축하기 위한 도구 활용 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

#### 전달 스케줄 또는 트리거 선택 {#choose-a-delivery-schedule-or-trigger}

WhatsApp 메시지는 예약된 시간, 실행 또는 API 트리거를 기반으로 전달할 수 있습니다. 자세한 내용은 [캠페인 예약하기]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)를 참조하세요.

실행 기반 전달의 경우, 캠페인 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)도 설정할 수 있습니다.

이 단계에서는 사용자가 캠페인을 [재수신]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)할 수 있도록 허용하거나 [최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping) 규칙을 활성화하는 등의 전달 제어를 지정할 수도 있습니다.

#### 타겟 사용자 선택 {#choose-users-to-target}

다음으로, Segments 또는 필터를 선택하여 오디언스를 좁혀 [사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)해야 합니다. 이미 구독 그룹을 선택했어야 하며, 이를 통해 사용자가 원하는 커뮤니케이션 수준이나 카테고리별로 사용자를 좁힐 수 있습니다. 이 단계에서는 Segments에서 더 넓은 오디언스를 선택하고 필터를 사용하여 해당 Segment를 더 좁힙니다. 대략적인 Segment 인구의 스냅샷이 자동으로 표시됩니다. 정확한 Segment 멤버십은 항상 메시지가 발송되기 전에 계산된다는 점을 기억하세요.

{% multi_lang_include audience/target_audiences.md %}

#### 전환 이벤트 선택 {#choose-conversion-events}

Braze를 사용하면 캠페인을 수신한 후 사용자가 특정 행동([전환 이벤트]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events))을 수행하는 빈도를 추적할 수 있습니다. 사용자가 지정된 행동을 취하면 전환으로 집계되는 최대 30일의 기간을 설정할 수 있습니다.

특정 사용 사례에 따라 커스텀 전환 이벤트를 설정할 수도 있습니다. 창의적으로 생각하고 이 캠페인의 성공을 어떻게 측정하고 싶은지 고민해 보세요.

{% endtab %}

{% tab Canvas %}

아직 완료하지 않았다면, Canvas 구성요소의 나머지 섹션을 완료하세요. Canvas의 나머지 부분을 구축하고, 다변량 테스트 및 지능형 선택을 구현하는 방법 등에 대한 자세한 내용은 Canvas 설명서의 [Canvas 구축하기]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message) 단계를 참조하세요.

대화 창은 인바운드 메시지당 24시간만 지속될 수 있으므로, Braze는 인바운드 메시지와 응답 메시지 사이에 24시간을 초과하는 지연이 없는지 확인합니다.

{% endtab %}
{% endtabs %}

### 5단계: 검토 및 배포 {#step-5-review-and-deploy}

캠페인 또는 Canvas의 마지막 부분을 완성한 후, 세부 사항을 검토하고 테스트한 다음 발송하세요!

다음으로, [WhatsApp 보고]({{site.baseurl}}/user_guide/channels/whatsapp/reporting)를 확인하여 WhatsApp 캠페인의 결과에 액세스하는 방법을 알아보세요.

## 지원되는 WhatsApp 기능 {#supported-whatsapp-features}

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
| CTA 응답 메시지 | 콜투액션 버튼이 포함된 응답 메시지를 만듭니다. |
| [목록 응답 메시지]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/messaging_users#list-messages) | 사용자가 선택할 수 있는 최대 10개의 옵션 목록이 포함된 응답 메시지를 만듭니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="콜투액션 유형 #ctas" }