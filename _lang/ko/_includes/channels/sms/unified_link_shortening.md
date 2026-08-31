링크 단축을 사용하면 SMS 또는 RCS 메시지에 포함된 URL을 자동으로 단축하고 클릭률 분석을 수집할 수 있어, 사용자가 Campaign에 어떻게 참여하고 있는지 이해하는 데 도움이 되는 추가 인게이지먼트 측정기준을 제공합니다.

링크 단축은 Campaigns와 Canvases 모두에서 [메시지 배리언트 수준]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-1-create-your-campaign)에서 활성화할 수 있습니다. 링크 단축이 활성화되면 클릭 시 Currents를 통해 전송되는 [SMS 클릭 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)가 생성됩니다.

{% multi_lang_include channels/sms/rcs_link_shortening_note.md %}

링크는 공유 단축 도메인(`brz.ai`) 또는 커스텀 링크 단축 도메인을 사용하여 단축되며, 생성된 날짜로부터 9주 동안 유효합니다. 예시 URL은 `https://brz.ai/8jshX2dj`와 같은 형태입니다.

## 링크 단축 사용하기 {#using-link-shortening}

링크 단축을 사용하려면 메시지 작성기에서 링크 단축 체크박스가 선택되어 있는지 확인하세요.

{% tabs %}
{% tab SMS 작성기 %}

![링크 단축 체크박스가 선택된 SMS 메시지 작성기.]({% image_buster /assets/img/link_shortening/shortening1.png %})

{% endtab %}
{% tab RCS 작성기 %}

![링크 단축 체크박스가 선택된 RCS 메시지 작성기.]({% image_buster /assets/img/link_shortening/shortening1_rcs.png %})

{% endtab %}
{% endtabs %}

Braze는 `http://` 또는 `https://`로 시작하는 URL만 인식합니다. URL이 인식되면 **미리보기** 섹션이 입력 안내 URL로 업데이트됩니다. Braze는 단축 후 메시지 길이를 추정하지만, 더 정확한 추정을 위해 테스트 사용자를 선택하고 메시지를 초안으로 저장하라는 경고가 표시됩니다.

![메시지 작성기에서 "메시지" 상자에 긴 URL이 있고 미리보기에 생성된 단축 링크가 표시된 모습.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### UTM 파라미터 추가하기 {#adding-utm-parameters}

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## URL에서의 Liquid 개인화 {#liquid-personalization-in-urls}

Braze 작성기에서 직접 URL을 동적으로 구성하여 URL에 동적 UTM 파라미터를 추가하거나 사용자에게 고유한 링크를 전송하는 방법에 대한 자세한 내용은 [URL에서 Liquid 개인화 사용]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#use-liquid-personalization-in-urls)을 참조하세요.

## 테스트 {#testing}

Campaign 또는 Canvas를 시작하기 전에 먼저 메시지를 미리보기하고 테스트하는 것이 좋습니다. 이를 위해 **테스트** 탭으로 이동하여 [콘텐츠 테스트 그룹]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#content-test-groups) 또는 개별 사용자에게 SMS 또는 RCS 메시지를 미리보기하고 전송할 수 있습니다.

이 미리보기는 관련 개인화 및 단축 URL로 업데이트됩니다. 문자 수와 [청구 가능 세그먼트]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator)도 렌더링된 개인화 및 단축 URL을 반영하여 업데이트됩니다.

테스트 메시지를 보내기 전에 Campaign 또는 Canvas를 저장하여 메시지에서 발송되는 단축 URL의 표현을 받을 수 있도록 하세요. Campaign 또는 Canvas가 테스트 전송 전에 저장되지 않으면, 테스트 전송에 입력 안내 URL이 포함됩니다.

{% alert important %}
활성 Canvas 내에서 초안이 생성되면 단축 URL이 생성되지 않습니다. 실제 단축 URL은 Canvas 초안이 활성화될 때 생성됩니다.
{% endalert %}

![테스트 수신자를 선택할 수 있는 필드가 있는 메시지 '테스트' 탭]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
Liquid 개인화 및 단축 URL은 사용자가 선택된 후 **테스트** 탭에서 템플릿 처리됩니다. 정확한 문자 수를 받으려면 사용자가 선택되어 있는지 확인하세요.
{% endalert %}

## 클릭 추적 {#click-tracking}

링크 단축이 켜져 있으면, **SMS/MMS/RCS 성능** 테이블에 **총 클릭 수**라는 제목의 열이 포함되어 배리언트별 클릭 이벤트 수와 관련 클릭률이 표시됩니다. 측정기준에 대한 자세한 내용은 [메시지 성능]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/reporting)을 참조하세요.

![SMS 및 MMS 성능 측정기준 테이블.]({% image_buster /assets/img/link_shortening/shortening4.png %})

**과거 성능** 및 **SMS/MMS/RCS 성능** 테이블에도 **총 클릭 수** 옵션이 포함되어 있으며, 클릭 이벤트의 일별 시계열을 보여줍니다. 클릭 수는 리디렉션 시(예: 사용자가 링크를 방문할 때) 증가하며, 사용자당 두 번 이상 증가할 수 있습니다.

## 사용자 리타겟팅 {#retargeting-users}

리타겟팅에 대한 안내는 [리타겟팅]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting#filter-by-advanced-tracking-links)을 참조하세요.

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### 어떤 사용자가 URL을 클릭했는지 알 수 있나요? {#do-i-know-which-individual-users-are-clicking-on-a-url}

네. [SMS 리타겟팅 필터]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/user_retargeting) 또는 Currents에서 전송하는 SMS 클릭 이벤트(`users.messages.sms.ShortLinkClick`)를 사용하여 URL을 클릭한 사용자를 리타겟할 수 있습니다.

### 링크 단축은 딥링크 또는 유니버설 링크에서 작동하나요? {#does-link-shortening-work-with-deep-links-or-universal-links}

링크 단축은 딥링크에서는 작동하지 않습니다. 대안으로 Branch나 Appsflyer와 같은 서드파티 제공업체의 유니버설 링크를 단축할 수 있지만, 사용자가 짧은 리디렉션 또는 "깜빡임" 효과를 경험할 수 있습니다. 이는 단축된 링크가 앱 열기를 지원하는 유니버설 링크로 전환되기 전에 먼저 웹을 거치기 때문에 발생합니다. 또한 Braze는 유니버설 링크를 단축할 때 발생할 수 있는 문제(예: 기여도 추적이 깨지거나 예기치 않은 리디렉션이 발생하는 경우)를 해결할 수 없습니다.

{% alert note %}
유니버설 링크와 함께 링크 단축을 구현하기 전에 사용자 경험을 테스트하여 기대에 부합하는지 확인하세요.
{% endalert %}

### `send_ids`가 SMS 클릭 이벤트에 연결되어 있나요? {#are-send_ids-associated-with-sms-click-events}

아니요. 하지만 일반적으로 [쿼리 빌더]({{site.baseurl}}/query_builder)를 사용하여 다음 쿼리로 Currents 데이터를 조회하면 `send_ids`를 클릭 이벤트에 연결할 수 있습니다:

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL;
```