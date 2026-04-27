링크 단축을 사용하면 SMS 또는 RCS 메시지에 포함된 URL을 자동으로 단축하고 클릭률 분석을 수집할 수 있어, 사용자가 캠페인에 어떻게 참여하고 있는지 이해하는 데 도움이 되는 추가 참여 측정기준을 제공합니다.

링크 단축은 Campaigns와 Canvases 모두에서 [메시지 배리언트 수준]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests/#step-1-create-your-campaign)에서 활성화할 수 있습니다. 링크 단축이 활성화되면 클릭 시 Currents를 통해 전송되는 [SMS 클릭 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/)가 생성됩니다.

링크는 공유 단축 도메인(`brz.ai`) 또는 커스텀 링크 단축 도메인을 사용하여 단축되며, 생성된 날짜로부터 9주 동안 유효합니다. 예시 URL은 `https://brz.ai/8jshX2dj`와 같은 형태입니다.

## 링크 단축 사용하기 {#using-link-shortening}

링크 단축을 사용하려면 메시지 작성기에서 링크 단축 체크박스가 선택되어 있는지 확인하세요.

{% tabs %}
{% tab SMS composer %}

![링크 단축 체크박스가 선택된 SMS 메시지 작성기.]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS composer %}

![링크 단축 체크박스가 선택된 RCS 메시지 작성기.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

Braze는 `http://` 또는 `https://`로 시작하는 URL만 인식합니다. URL이 인식되면 **미리보기** 섹션이 입력 안내 URL로 업데이트됩니다. Braze는 단축 후 메시지 길이를 추정하지만, 더 정확한 추정을 위해 테스트 사용자를 선택하고 메시지를 초안으로 저장하라는 경고가 표시됩니다.

!["메시지" 상자에 긴 URL이 있고 미리보기에 생성된 단축 링크가 표시된 메시지 작성기.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### UTM 매개변수 추가하기 {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## URL에서의 Liquid 개인화 {#liquid-personalization-in-urls}

Braze 작성기 내에서 직접 URL을 동적으로 구성하여 URL에 동적 UTM 매개변수를 추가하거나 사용자에게 고유한 링크를 보내는 방법에 대한 자세한 내용은 [URL에서 Liquid 개인화 사용하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/#use-liquid-personalization-in-urls)를 참조하세요.

## 테스트 {#testing}

Campaign이나 Canvas를 시작하기 전에 먼저 메시지를 미리보기하고 테스트하는 것이 좋습니다. 이를 위해 **테스트** 탭으로 이동하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#content-test-groups) 또는 개별 사용자에게 SMS 또는 RCS 메시지를 미리보기하고 보내세요.

이 미리보기는 관련 개인화 및 단축된 URL로 업데이트됩니다. 문자 수와 [청구 가능 세그먼트]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/)도 렌더링된 개인화 및 단축된 URL을 반영하여 업데이트됩니다.

테스트 메시지를 보내기 전에 Campaign이나 Canvas를 저장해야 메시지에 발송되는 단축 URL의 실제 형태를 확인할 수 있습니다. 테스트 발송 전에 Campaign이나 Canvas가 저장되지 않으면 테스트 발송에 입력 안내 URL이 포함됩니다.

{% alert important %}
활성 Canvas 내에서 초안이 생성된 경우 단축 URL이 생성되지 않습니다. 실제 단축 URL은 Canvas 초안이 활성화될 때 생성됩니다.
{% endalert %}

![테스트 수신자를 선택하는 필드가 있는 메시지 "테스트" 탭.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
Liquid 개인화 및 단축 URL은 사용자가 선택된 후 **테스트** 탭에서 템플릿화됩니다. 정확한 문자 수를 확인하려면 사용자를 선택하세요.
{% endalert %}

## 클릭 추적 {#click-tracking}

링크 단축이 활성화되면 **SMS/MMS/RCS 성과** 테이블에 배리언트별 클릭 이벤트 수와 관련 클릭률을 보여주는 **총 클릭 수** 열이 포함됩니다. 측정기준에 대한 자세한 내용은 [메시지 성과]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting/)를 참조하세요.

![SMS 및 MMS 성과 측정기준 테이블.]({% image_buster /assets/img/link_shortening/shortening4.png %})

**과거 성과** 및 **SMS/MMS/RCS 성과** 테이블에도 **총 클릭 수** 옵션이 있으며 클릭 이벤트의 일별 시계열을 보여줍니다. 클릭 수는 리디렉션 시(예: 사용자가 링크를 방문할 때) 증가하며, 사용자당 두 번 이상 증가할 수 있습니다.

## 사용자 리타겟팅 {#retargeting-users}

리타겟팅에 대한 안내는 [리타겟팅]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/#filter-by-advanced-tracking-links)을 참조하세요.

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### URL을 클릭한 개별 사용자를 알 수 있나요? {#do-i-know-which-individual-users-are-clicking-on-a-url}

네. [SMS 리타겟팅 필터]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting/) 또는 Currents에서 전송하는 SMS 클릭 이벤트(`users.messages.sms.ShortLinkClick`)를 사용하여 URL을 클릭한 사용자를 리타겟할 수 있습니다.

### 링크 단축은 딥링크 또는 유니버설 링크에서 작동하나요? {#does-link-shortening-work-with-deep-links-or-universal-links}

링크 단축은 딥링크에서는 작동하지 않습니다. 대안으로 Branch나 Appsflyer와 같은 서드파티 제공업체의 유니버설 링크를 단축할 수 있지만, 사용자가 짧은 리디렉션 또는 "깜빡임" 효과를 경험할 수 있습니다. 이는 단축 링크가 앱 열기를 지원하는 유니버설 링크로 해석되기 전에 먼저 웹을 통해 라우팅되기 때문입니다. 또한 Braze는 유니버설 링크를 단축할 때 발생할 수 있는 문제(예: 기여도 손상 또는 예기치 않은 리디렉션)를 해결할 수 없습니다.

{% alert note %}
유니버설 링크와 함께 링크 단축을 구현하기 전에 사용자 경험을 테스트하여 기대에 부합하는지 확인하세요.
{% endalert %}

### `send_ids`가 SMS 클릭 이벤트와 연결되나요? {#are-sendids-associated-with-sms-click-events}

아니요. 하지만 일반적으로 [쿼리 빌더]({{site.baseurl}}/query_builder/)를 사용하여 다음 쿼리로 Currents 데이터를 조회함으로써 `send_ids`를 클릭 이벤트와 연결할 수 있습니다:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```