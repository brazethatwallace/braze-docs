---
nav_title: "RCS 메시지 만들기"
article_title: "RCS 메시지 만들기"
permalink: /create_rcs_message/
description: "이 문서에서는 RCS 메시지를 만드는 방법을 다룹니다."
hidden: true
---

# RCS 메시지 만들기 {#creating-an-rcs-message}

> RCS Campaign은 고객에게 직접 도달하고 프로그래밍 방식으로 대화하는 데 적합합니다. Liquid 및 기타 동적 콘텐츠를 사용하여 사용자와 개인화된 경험을 만들고, 브랜드와의 자연스러운 사용자 경험을 촉진하고 향상시키는 환경을 구축할 수 있습니다.

## RCS 메시지 만들기

### 1단계: 메시지를 작성할 위치 선택 {#step-1-choose-where-to-build-your-message}

메시지를 Campaign으로 보낼지 Canvas로 보낼지 확실하지 않으신가요? Campaign은 단순한 단일 메시징에 적합하고, Canvas는 다단계 사용자 여정에 더 적합합니다.

{% tabs %}
{% tab Campaign %}
1. **메시징** > **Campaigns**로 이동하여 **캠페인 생성**을 선택합니다.
2. **SMS/MMS/RCS**를 선택하거나, 여러 채널을 타겟팅하는 Campaign의 경우 **멀티채널**을 선택합니다.
3. Campaign에 명확하고 의미 있는 이름을 지정합니다.
4. 필요에 따라 [Teams](https://braze.com/docs/user_guide/administrative/app_settings/manage_your_braze_users/teams/) 및 [태그](https://braze.com/docs/user_guide/administrative/app_settings/tags/)를 추가합니다.
   * 태그를 사용하면 Campaign을 더 쉽게 찾고 보고서를 작성할 수 있습니다. 예를 들어, [보고서 빌더](https://braze.com/docs/user_guide/analytics/reporting/report_builder/)를 사용할 때 특정 태그로 필터링할 수 있습니다.

{: start="5"}
5. Campaign에 필요한 만큼 배리언트를 추가하고 이름을 지정합니다. 추가된 각 배리언트에 대해 다른 플랫폼, 메시지 유형 및 레이아웃을 선택할 수 있습니다. 이 주제에 대한 자세한 내용은 [다변량 및 A/B 테스트](https://braze.com/docs/user_guide/engagement_tools/testing/multivariant_testing/)를 참조하세요.
- **SMS 및 RCS 배리언트 테스트**: Braze에서는 단일 Campaign 내에 SMS와 RCS 배리언트를 모두 포함할 수 있어 각각의 성과를 비교할 수 있습니다. 메시지 작성의 첫 번째 단계에서 SMS 및 RCS 배리언트를 추가할 수 있습니다.

{: start="6"}
6. RCS가 활성화된 [구독 그룹](https://braze.com/docs/sms_rcs_subscription_groups/)을 선택합니다. 구독 그룹을 선택하면 Braze가 자동으로 세분화 필터를 추가하여 구독한 사용자만 Campaign을 수신하도록 합니다. 해당 구독 그룹에 속한 긴 코드와 짧은 코드만 타겟 사용자에게 SMS를 보내는 데 사용됩니다.
- **SMS 대체**: Braze는 RCS 발신자를 포함하는 모든 구독 그룹에 대체용 SMS 코드를 하나 이상 포함할 것을 강력히 권장합니다. 이는 RCS 메시지 전달에 실패하는 경우 전달 가능성을 위해 중요합니다. 실패 원인으로는 사용자 기기 비호환성, 특정 국가 또는 지역의 불완전한 통신사 커버리지 등이 있을 수 있습니다. SMS 대체를 활성화하면 메시지가 여전히 사용자에게 전달되어 연결 기회를 놓치지 않습니다.

{: start="7"}
7. SMS와 RCS 중에서 선택합니다. RCS 메시지를 작성하기 전에 전송할 채널을 선택합니다. 일반적으로 SMS보다 사용자 참여 측면에서 상당한 이점이 있으므로 가능한 한 RCS를 사용하는 것을 권장합니다. 그러나 최대한의 유연성과 제어를 위해 항상 SMS로 전송하는 옵션도 제공합니다.

![RCS 또는 SMS/MMS 메시지 유형을 선택하는 옵션.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Campaign의 모든 메시지가 유사하거나 동일한 콘텐츠를 가질 경우, 추가 배리언트를 추가하기 전에 메시지를 작성하세요. 그런 다음 **배리언트 추가** 드롭다운에서 **배리언트에서 복사**를 선택할 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. Canvas 작성기를 사용하여 [Canvas를 생성](https://braze.com/docs/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)합니다.
2. Canvas를 설정한 후 Canvas 빌더에서 **SMS/MMS/RCS** 메시지 단계를 추가합니다.
3. 단계에 명확하고 의미 있는 이름을 지정합니다.
4. RCS가 활성화된 [구독 그룹](https://braze.com/docs/sms_rcs_subscription_groups/)을 선택합니다. 구독 그룹을 선택하면 Braze가 자동으로 세분화 필터를 추가하여 구독한 사용자만 Campaign을 수신하도록 합니다. 해당 구독 그룹에 속한 긴 코드와 짧은 코드만 사용자를 타겟팅하는 데 사용됩니다.
- **SMS 대체**: Braze는 RCS 발신자를 포함하는 모든 구독 그룹에 대체용 SMS 코드를 하나 이상 포함할 것을 강력히 권장합니다. 이는 RCS 메시지 전달에 실패하는 경우 전달 가능성을 위해 중요합니다. 실패 원인으로는 사용자 기기 비호환성, 특정 국가 또는 지역의 불완전한 통신사 커버리지 등이 있을 수 있습니다. SMS 대체를 활성화하면 메시지가 여전히 사용자에게 전달되어 연결 기회를 놓치지 않습니다.

{: start="5"}
5. SMS와 RCS 중에서 선택합니다. RCS 메시지를 작성하기 전에 전송할 채널을 선택합니다. 일반적으로 SMS보다 사용자 참여 측면에서 상당한 이점이 있으므로 가능한 한 RCS를 사용하는 것을 권장합니다. 그러나 최대한의 유연성과 제어를 위해 항상 SMS로 전송하는 옵션도 제공합니다.

![RCS 또는 SMS/MMS 메시지 유형을 선택하는 옵션.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### 2단계: RCS 메시지 유형 선택 {#step-2-select-your-rcs-message-type}

Campaign 및 Canvas 생성 시 목표에 가장 적합한 메시지를 구성하기 위해 세 가지 RCS 메시지 유형(텍스트, 미디어, 리치 카드) 중에서 선택합니다.

![텍스트, 미디어 또는 카드 메시지 유형을 선택하는 옵션.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs local %}
{% tab 텍스트 %}
이름에서 알 수 있듯이 RCS 텍스트 메시지는 텍스트를 매체로 사용합니다. 160자 이내로 입력하면 RCS 메시지는 텍스트 전용(또는 "기본") 메시지로 과금됩니다. 160자를 초과하거나 리치 요소를 사용하면 리치(또는 "단일") RCS 메시지로 과금됩니다(문자 제한이 3072자로 증가합니다).

#### 기능 {#features}

- 텍스트 메시지 유형에는 모든 SMS 기능이 포함됩니다. URL 클릭 추적에는 고급 추적만 가능하여 사용자 수준의 보고 세분화를 제공합니다.
- 또한 이제 랜딩 페이지 방문이나 주문과 같은 높은 참여도의 사용자 행동을 유도하는 매력적인 **추천 답장** 및 **추천 동작** 버튼을 포함할 수 있습니다.
    - **추천 답장**은 사용자가 클릭하여 텍스트 입력란에 미리 채울 수 있는 추천 응답이 포함된 버튼으로, 제한된 선택지를 제공하여 응답을 생각해야 하는 부담을 줄여줍니다.
    - **추천 동작**은 사용자의 기기에서 동작을 시작하는 버튼입니다. 일반적으로 한두 개의 설명 단어와 버튼의 기능을 이해하는 데 도움이 되는 시각적 아이콘으로 구성됩니다. Braze는 현재 OpenURL 추천 동작을 지원합니다. 이는 URL과 유사하게 작동하며, 버튼을 선택한 사용자는 웹페이지 또는 기타 URL로 식별되는 위치로 리디렉션됩니다.

![트렌디한 패션 스타일을 홍보하는 RCS 메시지의 세 가지 추천 동작 GIF: "동화 속 왕족", "엣지 있는 아카데미아", "다른 스타일 보여주세요".]({% image_buster /assets/unlisted_docs/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### 고려 사항 {#considerations}

- 텍스트 문자 제한의 경우, 텍스트 전용(기본) RCS 메시지는 최대 160자, 리치(단일) RCS 메시지는 최대 3072자까지 작성할 수 있습니다.
- 버튼 제한의 경우, 메시지당 최대 5개의 버튼을 추가할 수 있습니다. 이 버튼은 추천 동작 또는 추천 답장일 수 있습니다.
- 긴 텍스트 블록과 너무 많은 버튼은 사용자를 불편하게 할 수 있으므로, 가능한 한 간결함을 유지하는 것을 권장합니다.
- 경우에 따라 RCS를 통해 긴 텍스트 전용 메시지를 보내는 것이 SMS보다 비용 효율적일 수 있습니다. 긴 SMS 메시지는 여러 세그먼트로 분할되어 각각 과금되는 반면, RCS 메시지는 메시지당 과금되기 때문입니다. 자세한 내용과 안내는 Braze 계정 매니저에게 문의하세요.
{% endtab %}

{% tab 미디어 %}
RCS 미디어 메시지를 사용하면 SMS로는 불가능한 매력적인 미디어 형식을 사용할 수 있습니다. 여기에는 이미지, 동영상 및 문서 파일이 포함됩니다. 이러한 미디어 옵션은 오디언스를 더 깊이 참여시키고 완전히 새로운 사용 사례를 가능하게 합니다. 현재 [미디어 라이브러리](https://braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library/)를 통한 이미지 업로드만 지원됩니다.

#### 기능

- 미디어 메시지 유형은 텍스트 메시지 유형에서 사용 가능한 모든 기능(텍스트, 추천 답장, 추천 동작 포함)을 지원합니다.
- JPEG 및 PNG 파일 형식을 포함한 이미지 파일을 지원합니다. 이미지 파일은 미디어 라이브러리에서 업로드할 수 있습니다.
- MP4, MPEG 및 MV4 파일 형식을 포함한 동영상 파일을 지원합니다. 동영상 파일은 메시지 작성기에서 URL을 통해 직접 추가할 수 있습니다.
- PDF 형식의 문서 파일을 지원합니다. 문서 파일은 메시지 작성기에서 URL을 통해 직접 추가할 수 있습니다.

![미디어 파일을 업로드하는 옵션이 있는 RCS 작성기.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_type.png %})

#### 파일 사양 {#file-specifications}

| 파일 유형 | 사양 |
| --- | --- |
| 전체 | - 파일 크기는 100 MB로 제한됩니다 <br><br>- 파일 URL은 최대 2048자까지 가능합니다 |
| 이미지 파일 | 지원되는 파일 형식: JPG, JPEG, GIF |
| 동영상 파일 | 지원되는 파일 형식: H263, M4V, MP4, MPEG-4, MPEG, WEBM |
| 문서 파일 | 지원되는 파일 형식: PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### 고려 사항

RCS 메시지 수신 시 사용자 경험은 대상 국가의 통신사 커버리지, 모바일 기기 하드웨어, 모바일 기기 운영체제 등 여러 요인에 따라 약간 다를 수 있습니다.

일반적으로 RCS는 Android 기기와 더 자연스럽게 통합됩니다(이 방식은 주로 Google에 의해 구현되었으며, P2P RCS 메시징은 Android 커뮤니티에서 널리 채택되고 있습니다). 기기에 따라 경험이 다른 속도와 품질로 렌더링될 수 있습니다.
{% endtab %}

{% tab 리치 카드 %}

{% alert important %}
리치 카드는 얼리 액세스 중입니다. 이 얼리 액세스에 참여하려면 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

리치 카드는 미디어, 텍스트, 버튼을 하나의 메시지로 결합하여 고객에게 더 직관적이고 매력적인 경험을 제공합니다. 리치 카드의 두 가지 하위 유형인 텍스트와 미디어를 만들 수 있습니다.

{% subtabs %}
{% subtab 텍스트 %}
텍스트 리치 카드는 텍스트에 초점을 맞춘 간결한 메시지입니다. 다음 요소를 포함해야 합니다:

- **제목:** 최대 200자. Liquid로 개인화할 수 있습니다.
- **설명:** 최대 2,000자. Liquid로 개인화할 수 있습니다.
- **버튼:** 최소 하나의 버튼이 필요합니다. **추천 답장** 또는 **웹 URL 열기** 동작으로 최대 4개의 버튼을 추가할 수 있습니다.

{% endsubtab %}
{% subtab 미디어 %}

미디어 리치 카드는 이미지 또는 동영상을 포함하는 시각적 메시지입니다. 다음 요소를 포함해야 합니다:

- **미디어:** 이미지, GIF 또는 동영상.
    - 얼리 액세스에서는 커스텀 동영상 썸네일이 지원되지 않습니다. 얼리 액세스에서는 이미지 및 동영상 파일 모두에 대해 높은 미디어 높이의 세로 레이아웃만 지원됩니다.
- **버튼:** 최소 하나의 버튼이 필요합니다. **추천 답장** 또는 **웹 URL 열기** 동작으로 최대 4개의 버튼을 추가할 수 있습니다.

{% endsubtab %}
{% endsubtabs %}

### 기능
- **카드 버튼** 및 **추천:** 리치 카드 하단(버튼) 또는 메시지 화면 하단(추천)에 최대 4개의 버튼과 5개의 추천(각 최대 25자)을 추가할 수 있습니다. 사용자는 이러한 클릭-탭 옵션을 선택하여 특정 응답을 보내거나 특정 동작을 수행할 수 있습니다.
- **개인화:** Liquid를 사용하여 제목, 설명, 미디어, 버튼을 포함한 모든 리치 카드 요소를 개인화할 수 있습니다.
- **과금:** 리치 카드는 단일 리치(또는 "단일") RCS 메시지로 과금됩니다.
- **URL 안내:** 제목이나 설명에 일반 텍스트로 입력된 URL은 클릭할 수 없습니다. 사용자를 웹사이트로 안내하려면 **OpenURL 버튼**을 사용해야 합니다.

![미디어 또는 텍스트 리치 카드를 선택하는 옵션이 있는 패널.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_media_text.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### 3단계: RCS 메시지 작성 {#step-3-compose-your-rcs-message}

언어와 개인화([Liquid](https://braze.com/docs/user_guide/personalization_and_dynamic_content/liquid/), [연결된 콘텐츠](https://braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/), 이모지)를 필요에 따라 사용하여 메시지를 작성합니다. 초과 요금 발생 가능성을 줄이기 위해 메시지 문구 제한을 준수하세요.

{% alert important %}
진행하기 전에 [RCS 메시지 제한 가이드라인](#step-2-select-your-rcs-message-type)을 읽어보세요. RCS 메시지는 [메시지당 과금](https://braze.com/docs/sms_rcs_billing_calculators/)되므로, 각 RCS 메시지 유형에 포함할 수 있는 내용의 세부 사항을 이해하는 것이 좋습니다.
{% endalert %}

### 4단계: 메시지 미리보기 및 테스트 {#step-4-preview-and-test-your-message}

Braze는 항상 메시지를 보내기 전에 미리보기하고 테스트할 것을 권장합니다. **테스트** 탭으로 이동하여 콘텐츠 테스트 그룹이나 개별 사용자에게 테스트 RCS를 보내거나, Braze에서 직접 사용자로서 메시지를 미리볼 수 있습니다.

### 5단계: Campaign 또는 Canvas의 나머지 부분 구축 {#step-5-build-the-remainder-of-your-campaign-or-canvas}

다음으로 Campaign 또는 Canvas의 나머지 부분을 구축합니다. RCS 메시지를 구축하기 위한 도구 활용 방법에 대한 자세한 내용은 다음 섹션을 참조하세요.

#### 5.1단계: 전달 스케줄 또는 트리거 선택 {#step-51-choose-delivery-schedule-or-trigger}

RCS 메시지는 예약된 시간, 동작 또는 API 트리거를 기반으로 전달할 수 있습니다. 자세한 내용은 [Campaign 스케줄링](https://braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)을 참조하세요.

실행 기반 전달의 경우 Campaign의 기간과 방해금지 시간도 설정할 수 있습니다.

사용자가 Campaign을 다시 수신할 수 있도록 허용하거나 최대 게재빈도 설정 규칙을 활성화하는 등 전달 제어를 지정합니다.

#### 5.2단계: 타겟 사용자 선택 {#step-52-choose-users-to-target}

Segments 또는 필터를 선택하여 오디언스를 좁혀 사용자를 타겟팅합니다. 이미 구독 그룹을 선택했으므로, 사용자가 원하는 커뮤니케이션 수준이나 카테고리에 따라 사용자가 좁혀집니다.

{% multi_lang_include target_audiences.md %}

다음으로 Segments에서 더 큰 오디언스를 선택하고 선택적 [필터](https://braze.com/docs/user_guide/engagement_tools/segments/segmentation_filters/)로 해당 Segment를 더 좁힙니다. 현재 대략적인 Segment 인구가 어떻게 보이는지 자동으로 미리보기가 제공됩니다. 정확한 Segment 멤버십은 항상 메시지가 전송되기 직전에 계산된다는 점을 유의하세요.

{% alert tip %}
SMS 및 RCS 상호작용을 기반으로 사용자를 타겟팅하는 RCS 리타겟팅에 관심이 있으신가요? [리타겟팅](https://braze.com/docs/sms_mms_rcs_user_retargeting/)을 참조하세요.
{% endalert %}

#### 5.3단계: 전환 이벤트 선택 {#step-53-choose-conversion-events}

Braze를 사용하면 Campaign을 수신한 후 사용자가 특정 행동(전환 이벤트)을 수행하는 빈도를 추적할 수 있습니다. 사용자가 지정된 행동을 수행하면 전환이 집계되는 최대 30일의 기간을 설정할 수 있습니다.

전환 이벤트는 Campaign의 성공을 측정하는 데 도움이 됩니다. 예를 들어:
- 지오타겟팅을 사용하여 사용자의 구매를 최종 목표로 하는 RCS 메시지를 트리거하는 경우, 전환 이벤트를 **구매**로 설정합니다.
- 사용자를 앱으로 유도하려는 경우, 전환 이벤트를 **세션 시작**으로 설정합니다.

특정 사용 사례에 따라 커스텀 전환 이벤트를 설정할 수도 있습니다. Campaign의 성공을 측정하는 방법에 대해 창의적으로 생각해 보세요.

### 6단계: 검토 및 배포 {#step-6-review-and-deploy}

Campaign 또는 Canvas 구축을 완료한 후 세부 사항을 검토하고 테스트한 다음 전송합니다!

다음으로 [SMS, MMS 및 RCS 보고](https://braze.com/docs/sms_mms_rcs_reporting/)를 참조하여 RCS Campaign 결과에 액세스하는 방법을 알아보세요.

## 분석 및 보고 {#analytics-and-reporting}

Campaign 또는 Canvas 분석에는 다음이 포함됩니다:

- 버튼 클릭, 추천 답장 또는 동작 등 리치 카드와의 모든 상호작용을 포함하는 _총 클릭 수_ 통계.
- 이러한 상호작용에 대한 더 자세한 보기를 제공하는 분석 테이블.

{% alert note %}
얼리 액세스에는 사용자 수준의 클릭 추적이 포함되지 않습니다. _총 클릭 수_는 버튼이 클릭될 때마다 증가합니다. 예를 들어, 사용자가 같은 버튼을 세 번 클릭하면 클릭 수가 3 증가합니다.
{% endalert %}

## 팁 {#tips}

### 메시지 개인화를 위한 Liquid 사용 {#using-liquid-for-message-personalization}

Liquid를 사용할 계획이라면, 수신자의 사용자 프로필이 불완전한 경우 이름 대신 빈 입력 안내 `Hi, !`나 불완전한 문장을 받지 않도록 선택한 개인화에 기본값을 포함해야 합니다.

### AI 문구 생성 {#generating-ai-copy}

매력적인 문구를 작성하는 데 도움이 필요하신가요? [AI 카피라이팅 어시스턴트](https://braze.com/docs/user_guide/brazeai/generative_ai/copywriting/)를 사용해 보세요. 제품 이름이나 설명을 입력하면 AI가 메시징에 사용할 수 있는 사람이 작성한 것 같은 마케팅 문구를 생성합니다.

![AI 카피라이팅 어시스턴트를 여는 아이콘이 있는 메시지 작성기.]({% image_buster /assets/unlisted_docs/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## 자주 묻는 질문 {#frequently-asked-questions}

### RCS로 미리 녹음된 음성 메시지를 보낼 수 있나요? {#can-i-send-pre-recorded-voicemails-with-rcs}

네, 미디어 메시지를 사용하여 오디오 파일을 지원할 수 있습니다.