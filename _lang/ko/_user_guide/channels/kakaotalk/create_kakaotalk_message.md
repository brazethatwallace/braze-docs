---
nav_title: KakaoTalk 메시지 만들기
article_title: KakaoTalk 메시지 만들기
description: "이 참조 문서에서는 KakaoTalk 메시지를 만드는 방법을 설명합니다."
page_order: 1
alias: /create_kakaotalk_message/
channel:
  - KakaoTalk
---

# KakaoTalk 메시지 만들기 {#create-a-kakaotalk-message}

> [KakaoTalk 메시징 채널]({{site.baseurl}}/kakaotalk)을 사용하여 KakaoTalk 플랫폼을 통해 사용자에게 직접 도달하세요. Liquid 및 기타 동적 콘텐츠를 활용하여 브랜드와 함께 풍부한 사용자 경험을 촉진하고 향상시키는 개인화된 사용자 경험을 구축하세요.<br><br>KakaoTalk 메시징 채널을 설정하려면 [KakaoTalk 설정]({{site.baseurl}}/kakaotalk_setup)을 참조하세요.

## 1단계: 메시지를 작성할 위치 선택 {#step-1-choose-where-to-build-your-message}

KakaoTalk은 Campaigns와 Canvas 모두에서 지원됩니다. Campaigns는 단일 메시징 캠페인에 가장 적합하며, Canvases를 사용하면 다단계, 다채널 사용자 여정을 오케스트레이션할 수 있습니다.

{% tabs local %}
{% tab Campaign %}

1. **메시징** > **Campaigns**로 이동하여 **캠페인 만들기**를 선택합니다.
2. 단일 채널 캠페인의 경우 **KakaoTalk**을, 다채널 캠페인의 경우 **멀티채널 캠페인**을 선택합니다.

![메시징 채널 선택 옵션이 있는 패널.]({% image_buster /assets/img/kakaotalk/kakaotalk_campaign.png %}){: style="max-width:30%" }

3. 캠페인에 추가 배리언트를 추가하여 다양한 메시지 유형과 레이아웃을 선택할 수 있습니다. 자세한 내용은 [다변량 및 A/B 테스트]({{site.baseurl}}/user_guide/messaging/ab_testing)를 참조하세요.

{% endtab %}
{% tab Canvas %}

1. [Canvas를 만듭니다]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas).
2. Canvas 빌더에서 메시지 단계를 추가하고 **KakaoTalk**을 선택합니다.

![Canvas 메시징 채널 선택 화면.]({% image_buster /assets/img/kakaotalk/kakaotalk_canvas.png %})

{% endtab %}
{% endtabs %}

## 2단계: KakaoTalk 메시지 작성하기 {#step-2-compose-your-kakaotalk-message}

1. **KakaoTalk 채널** 드롭다운을 선택하면 기술 파트너 페이지를 통해 설정한 KakaoTalk 채널 목록이 표시됩니다. 메시지를 보내는 데 사용할 KakaoTalk 채널을 선택합니다.
2. 보낼 메시지 유형을 선택합니다:
   - 텍스트
   - 이미지
       - 좁은 이미지
       - 넓은 이미지
   - 리스트 항목
   - 캐러셀

{% tabs local %}
{% tab 텍스트 %}

KakaoTalk 텍스트 메시지는 가장 간단한 커뮤니케이션 형태로, 표준 텍스트 메시지입니다.

### 사양 {#specifications}

| 영역 | 사양 |
| --- | --- |
| 콘텐츠 | 이모지 및 Liquid 개인화를 포함한 텍스트 콘텐츠 |
| 텍스트 용량 | 최대 1,000자 |
| 버튼 | 최대 5개의 선택적 버튼. 현재 클릭 시 URL을 여는 용도로만 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사양" }

![작성기에서의 KakaoTalk 텍스트 메시지.]({% image_buster /assets/img/kakaotalk/kakaotalk_text.png %})

{% endtab %}
{% tab 이미지 %}

이미지는 시각적 요소와 보조 텍스트를 결합한 메시지입니다. Braze는 KakaoTalk 서버로의 이미지 업로드를 자동으로 처리합니다.

### 일반 사양 {#general-specifications}

| 영역 | 사양 |
| --- | --- |
| 콘텐츠 | 이미지 1개와 보조 텍스트 |
| 허용 파일 형식 | JPEG 또는 PNG |
| 권장 너비 | 500px |
| 파일 크기 | 최대 500kb |
| 종횡비 | 2:1(넓은 이미지)에서 3:4(세로 이미지) 사이여야 합니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="일반 사양" }

좁은 이미지와 넓은 이미지 메시지는 각각 글자 수 및 버튼 관련 고려 사항이 다릅니다.

{% subtabs %}
{% subtab 좁은 이미지 %}

#### 좁은 이미지 {#narrow-image}

좁은 이미지 메시지는 약간 더 세로로 긴 좁은 이미지와 더 많은 텍스트 및 버튼 옵션을 제공합니다.

##### 사양

| 영역 | 사양 |
| --- | --- |
| 콘텐츠 | 이미지 1개와 보조 텍스트 |
| 텍스트 용량 | 최대 500자 |
| 버튼 | 최대 5개의 선택적 버튼 |
| 이미지 소스 | Braze 미디어 라이브러리 또는 직접 URL을 사용하여 이미지를 추가할 수 있습니다 |
| 커스터마이징 | 이미지의 클릭 시 동작을 지정할 수 있습니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사양" }

![KakaoTalk 좁은 이미지 메시지.]({% image_buster /assets/img/kakaotalk/narrow_image.png %})

{% endsubtab %}
{% subtab 넓은 이미지 %}

#### 넓은 이미지 {#wide-image}

넓은 이미지 메시지는 시각적 임팩트가 높은 커뮤니케이션에 적합한 넓은 이미지를 중심으로, 최소한의 보조 텍스트를 포함합니다.

##### 사양

| 영역 | 사양 |
| --- | --- |
| 콘텐츠 | 이미지 1개와 보조 텍스트 |
| 텍스트 용량 | 최대 76자 |
| 버튼 | 최대 2개의 선택적 버튼 |
| 이미지 소스 | Braze 미디어 라이브러리 또는 직접 URL을 사용하여 이미지를 추가할 수 있습니다 |
| 커스터마이징 | 이미지의 클릭 시 동작을 지정할 수 있습니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사양" }

![KakaoTalk 넓은 이미지 메시지.]({% image_buster /assets/img/kakaotalk/wide_image.png %})

{% endsubtab %}
{% endsubtabs %}

### 이미지 추가하기 {#add-images}

Braze 미디어 라이브러리를 통해 이미지를 추가하거나 JPEG 또는 PNG 파일을 호스팅하는 URL을 붙여넣어 이미지를 추가할 수 있습니다. 또한 이미지의 클릭 시 동작을 지정하여 이미지를 클릭한 사용자를 특정 URL로 리디렉션할 수 있습니다.

Braze는 KakaoTalk의 모든 이미지 업로드 요구 사항을 자동으로 처리하므로, 메시지를 보내기 전에 KakaoTalk 제공업체에 이미지를 업로드할 필요가 없습니다. 이미지를 업로드하고 Braze에서 직접 메시지를 보내면 됩니다!

![좁은 이미지를 추가하기 위한 아이콘이 선택된 섹션.]({% image_buster /assets/img/kakaotalk/add_image.png %})

{% endtab %}
{% tab 리스트 항목 %}


KakaoTalk 항목 리스트 메시지는 콘텐츠 항목 목록을 깔끔한 세로 형식으로 표시하도록 설계되었습니다.

리스트 항목 메시지는 헤더, 항목 리스트 섹션, 그리고 선택적 버튼 영역으로 구성됩니다.

#### 사양

| 영역 | 사양 |
| --- | --- |
| 항목 수 | 최소 2개 또는 3개의 항목이 필요합니다 |
| 헤더 | 최대 250자 |
| 항목 제목 | 최대 25자 |
| 웹사이트 URL(항목별, 행 탭) | 필수. 최대 250자. 사용자가 해당 항목의 이미지 또는 제목을 탭하면 열립니다. |
| 버튼(메시지 수준) | 최대 5개의 선택적 버튼(각각 고유한 URL 또는 액션 포함) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사양" }

![KakaoTalk 리스트 항목 메시지.]({% image_buster /assets/img/kakaotalk/item_list.png %})

{% endtab %}
{% tab 캐러셀 %}

KakaoTalk 캐러셀 메시지는 최대 6개의 스크롤 가능한 카드를 포함합니다. 각 카드에는 이미지, 헤더, 메시지, 선택적 **웹사이트 URL**, 그리고 최소 1개의 버튼이 있습니다.

카드와 버튼 모두 작성기에서 **웹사이트 URL**이라는 레이블이 지정된 필드를 사용하지만, 서로 다른 탭 대상에 적용됩니다:

- **카드 웹사이트 URL:** (선택 사항) 사용자가 카드 이미지를 탭하면 열립니다. 이 필드를 비워두면 이미지를 탭할 수 없습니다.
- **버튼 웹사이트 URL:** 사용자가 해당 버튼을 탭하면 열립니다. 각 웹 버튼에는 고유한 URL이 필요하며, 카드 이미지와 다른 대상을 가리킬 수 있습니다.

클릭 추적이 활성화되면 카드 및 버튼 URL은 독립적으로 단축 및 추적됩니다.

Braze는 이미지 메시지와 마찬가지로 메시지를 보낼 때 카드 이미지를 KakaoTalk 서버에 자동으로 업로드합니다.

{% alert note %}
**캐러셀** 메시지 유형은 계정에서 활성화될 때까지 워크스페이스에 표시되지 않을 수 있습니다.
{% endalert %}

### 사양

| 영역 | 사양 |
| --- | --- |
| 카드 | 2~6개의 스크롤 가능한 카드 |
| 헤더(카드별) | 최대 20자 |
| 메시지(카드별) | 최대 180자 |
| 이미지(카드별) | 필수 |
| 허용 파일 형식 | JPG 또는 PNG |
| 최소 너비 | 500px |
| 종횡비 | 2:1, 16:10, 3:2, 4:3, 1:1 또는 3:4 |
| 웹사이트 URL(카드별, 이미지 탭) | (선택 사항) 최대 250자. 사용자가 카드 이미지를 탭하면 열립니다. |
| 버튼(카드별) | 최소 1개, 최대 2개 |
| 버튼 텍스트(카드별) | 최대 8자 |
| 버튼 유형 | 웹 URL 열기, 앱 링크 또는 텍스트 답장 |
| 버튼 웹사이트 URL(**웹 URL 열기** 버튼별) | 필수. 최대 500자. 사용자가 해당 버튼을 탭하면 열립니다. |
| 개인화 | 카드 필드 및 URL에서 Liquid 지원 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사양" }

![KakaoTalk 캐러셀 메시지.]({% image_buster /assets/img/kakaotalk/carousel_message.png %})

{% endtab %}
{% endtabs %}

## 3단계: 클릭 추적 설정 {#step-3-set-up-click-tracking}

카카오톡 클릭 추적이 켜져 있으면, Braze가 자동으로 URL을 단축하고, 추적 메커니즘을 추가하며, 실시간으로 클릭을 기록합니다. 이 데이터를 통해 클릭 행동에 따라 사용자를 세분화하거나 특정 클릭에 대한 응답으로 메시지를 트리거하는 등 보다 타겟팅된 세분화 및 리타겟팅 전략을 수립할 수 있습니다.

클릭 추적은 텍스트, 이미지, 리스트 항목, 캐러셀 메시지에서 지원됩니다. 버튼 내 링크와 이미지 클릭 액션을 지원합니다. 또한 Liquid 및 커스텀 도메인을 사용하여 URL을 개인화할 수도 있습니다.

클릭 추적을 활성화하려면 작성기의 **링크 옵션** 섹션에서 **클릭 추적**을 선택합니다. URL은 기본 Braze 도메인(`https://brz.ai`) 또는 구독 그룹에 지정된 커스텀 도메인을 사용하여 단축되며, 사용자별로 개인화됩니다.

클릭 추적, 커스텀 도메인, URL 내 Liquid 개인화, 리포팅 및 리타겟팅에 대한 자세한 내용은 [카카오톡 클릭 추적]({{site.baseurl}}/kakaotalk_click_tracking)을 참조하세요.

### 사용자 리타겟팅 {#retargeting-users}

다음 세분화 필터 및 트리거를 사용하여 카카오톡 메시지에서 URL을 클릭한 사용자를 리타겟할 수 있습니다.

- 실행 기반 트리거
    - Campaign과 상호작용
    - 단계와 상호작용

- 세분화 필터
    - Campaign 클릭/열람
    - 태그가 있는 Campaign 또는 Canvas 클릭/열람
    - 단계 클릭/열람

## 4단계: KakaoTalk 메시지 미리보기 및 테스트 {#step-4-preview-and-test-your-kakaotalk-message}

KakaoTalk 메시지를 작성하면 메시지 미리보기가 자동으로 업데이트됩니다. 테스트할 준비가 되면 **테스트** 탭으로 이동하여 콘텐츠 테스트 그룹이나 개별 사용자에게 테스트 메시지를 보내거나, Braze에서 직접 기존 사용자 또는 커스텀 사용자로 메시지를 미리 볼 수 있습니다.

테스트 사용자를 선택한 후 **테스트 보내기**를 선택합니다. 테스트 전송 결과를 알려주는 알림이 표시됩니다. CJ OliveNetworks의 경우 "C100" 응답을 받게 됩니다. 다른 오류가 표시되면 [CJ KakaoTalk 사용자 설명서](https://developers.kakao.com/docs/latest/en/index)를 참조하세요.

![KakaoTalk 메시지 미리보기 창.]({% image_buster /assets/img/kakaotalk/preview_message.png %})

{% alert note %}
기존 사용자에게 테스트 메시지를 미리 보고 보내려면 "PII 보기" 권한이 있어야 합니다. 해당 권한 없이도 커스텀 사용자에게 테스트 메시지를 미리 보고 보낼 수 있습니다.
{% endalert %}

전송 결과를 확인하거나 문제를 해결하려면 **설정** > **메시지 활동 로그**로 이동하세요. 자세한 내용은 [메시지 활동 로그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)를 참조하세요.

## 5단계: Campaign 또는 Canvas의 나머지 부분 구성하기 {#step-5-build-the-remainder-of-your-campaign-or-canvas}

KakaoTalk 메시지를 작성하기 위해 도구를 가장 효과적으로 사용하는 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

### 전달 스케줄 또는 트리거 선택하기 {#choose-delivery-schedule-or-trigger}

KakaoTalk 메시지는 예약된 시간, 실행 또는 API 트리거를 기반으로 전달할 수 있습니다. 스케줄 및 트리거 옵션에 대한 자세한 내용은 [Campaign 스케줄 설정]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) 또는 [항목 스케줄 유형]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#entry-schedule-types)(Canvas의 경우)을 참조하세요.

사용자가 Campaign을 다시 수신할 수 있도록 재자격 부여를 허용하거나 최대 게재빈도 설정 규칙을 활성화하는 등 전달 제어를 지정할 수 있습니다. 실행 기반 전달의 경우 Campaign의 기간과 [방해금지 시간]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)도 설정할 수 있습니다.

{% alert important %}
KakaoTalk은 한국 표준시(KST) 기준 약 20:50부터 08:00까지 방해금지 시간을 적용합니다. 이 시간대에 예약된 메시지는 방해금지 시간이 종료될 때까지 발송되지 않습니다. 이 제한은 KakaoTalk 전달 공급자(CJ OliveNetworks 및 Infobip)에 의해 적용되며, Braze의 선택적 방해금지 시간 설정과는 독립적으로 모든 KakaoTalk 메시지 유형에 적용됩니다.
{% endalert %}

### 타겟 사용자 선택하기 {#choose-users-to-target}

Segment 또는 필터를 선택하여 오디언스를 좁혀 사용자를 타겟팅하세요. 현재 KakaoTalk은 채널 친구에게만 메시지를 보낼 수 있습니다. 채널 친구를 나타내는 커스텀 속성을 설정하여 사용자를 적절히 세분화하고, KakaoTalk 메시지를 수신할 수 없는 사용자에게 메시지를 보내는 것을 방지하는 것을 권장합니다.

### 전환 이벤트 선택하기 {#choose-conversion-events}

Braze에서는 Campaign을 수신한 후 사용자가 특정 행동(전환 이벤트)을 수행하는 빈도를 추적할 수 있습니다. 사용자가 지정된 행동을 취할 경우 전환으로 집계되는 최대 30일의 기간을 설정할 수 있습니다.

전환 이벤트는 Campaign의 성공을 측정하는 데 도움이 됩니다. 예를 들어, 사용자가 앱을 사용하도록 유도하려는 경우 전환 이벤트를 **Starts Session**으로 설정하세요.

특정 사용 사례에 맞는 커스텀 전환 이벤트를 설정할 수도 있습니다. 창의적으로 생각하고 Campaign의 성공을 어떻게 측정할지 고민해 보세요.

## 6단계: 검토 및 배포 {#step-6-review-and-deploy}

Campaign 또는 Canvas의 마지막 구성을 완료한 후, 세부 사항을 검토하고 테스트한 다음 전송합니다!