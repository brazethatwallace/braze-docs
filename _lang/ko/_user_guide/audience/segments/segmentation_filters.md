---
page_order: 3
nav_title: 세분화 필터
article_title: 세분화 필터
layout: glossary_page
glossary_top_header: "세분화 필터"
glossary_top_text: "Braze SDK는 특정 기능과 속성을 기반으로 사용자를 세분화하고 타겟팅할 수 있는 강력한 필터 모음을 제공합니다. 필터 카테고리별로 이러한 필터를 검색하거나 범위를 좁힐 수 있습니다.<br><br>사용자를 세분화하는 데 사용할 수 있는 다양한 커스텀 속성 데이터 유형에 대해 알아보려면 <a href=\"/docs/user_guide/data/activation/attributes/custom_attributes#custom-attribute-data-types\">커스텀 속성 데이터 유형</a> 을 참조하세요. 간격 필터는 100년으로 제한됩니다."

page_type: glossary
tool: Segments
description: "이 용어집에는 사용자를 세분화하고 타겟팅하는 데 사용할 수 있는 필터가 나열되어 있습니다."
search_rank: 2
glossary_tag_name: 필터 카테고리
glossary_filter_text: "카테고리를 선택하여 용어집 범위를 좁히세요:"

glossary_tags:
  - name: Segment or CSV membership
  - name: Custom attribute
  - name: Custom events
  - name: Sessions
  - name: Retargeting
  - name: Channel subscription behavior
  - name: Purchase behavior
  - name: eCommerce
  - name: Demographic attributes
  - name: App
  - name: Uninstall
  - name: Devices
  - name: Location
  - name: Cohort membership
  - name: Install attribution
  - name: Intelligence and predictive
  - name: Social activity
  - name: Other Filters
  - name: Advertising use cases
  - name: User Attributes

glossaries:
  - name: Segment Membership
    display_name: "Segment 멤버십"
    description: 필터가 사용되는 모든 곳(예&#58; Segments, Campaigns 등)에서 Segment 멤버십을 기준으로 필터링하고, 하나의 Campaign 내에서 여러 Segments를 타겟팅할 수 있습니다. <br><br>특정 시점의 Segment 멤버십을 캡처하려면, Campaign 또는 Canvas를 발송하기 전에 대시보드에서 Segment의 사용자를 내보내거나 [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/) 엔드포인트를 호출하세요. 자세한 내용은 [Segment 데이터를 CSV로 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/)를 참조하세요.<br><br>이 필터를 이미 사용하고 있는 Segments는 다른 Segments에 추가로 포함하거나 중첩할 수 없습니다. 이렇게 하면 Segment A가 Segment B를 포함하고, Segment B가 다시 Segment A를 포함하려는 순환이 발생할 수 있기 때문입니다. 이런 상황이 발생하면 Segment가 계속 자기 자신을 참조하게 되어 실제로 누가 해당 Segment에 속하는지 계산할 수 없게 됩니다. 또한 이러한 Segment 중첩은 복잡성을 높이고 처리 속도를 저하시킬 수 있습니다. 대신 포함하려는 Segment를 동일한 필터를 사용하여 다시 생성하세요.<br><br>Segment가 **Segment Membership** 필터 드롭다운에 표시되지 않으면, 동일한 필터로 다시 생성하고 새 Segment를 선택하거나, 순환을 만들 수 있는 방식으로 이 오디언스에 이미 의존하고 있지 않은지 확인하세요.
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    display_name: "Braze 세그먼트 확장"
    description: Braze 대시보드에서 세그먼트 확장을 생성한 후, 해당 확장을 Segment에 포함하거나 제외할 수 있습니다.
    tags:
      - Segment or CSV membership
  - name: Updated/Imported from CSV
    display_name: "CSV에서 업데이트/가져오기됨"
    description: 사용자가 CSV 업로드에 포함되었는지 여부를 기준으로 세분화합니다.
    tags:
      - Segment or CSV membership
  - name: Custom Attributes
    display_name: "커스텀 속성"
    description: 사용자가 커스텀으로 기록된 속성 값과 일치하는지 여부를 판단합니다. <br><br>시간대:<br>회사 시간대
    tags:
      - Custom attribute
  - name: Created At
    display_name: "생성 시점"
    description: 고객 프로필이 생성된 시점을 기준으로 사용자를 세분화합니다. 사용자가 CSV 또는 API를 통해 추가된 경우, 이 필터는 추가된 날짜를 반영합니다. 사용자가 CSV 또는 API를 통해 추가되지 않고 SDK에 의해 첫 번째 세션이 추적된 경우, 이 필터는 해당 첫 번째 세션의 날짜를 반영합니다.
    tags:
      - Other Filters
  - name: Created From
    display_name: "생성 출처"
    description: "고객 프로필이 생성된 출처를 기준으로 사용자를 세분화합니다.<br><br>다음 값이 지원됩니다:<br>- SDK (<code>sdk</code>): Braze SDK를 통해 생성된 고객 프로필.<br>- REST API (<code>rest</code>): Braze REST API를 통해 생성된 고객 프로필.<br>- 푸시 토큰 가져오기 (<code>pti</code>): 푸시 토큰 가져오기를 통해 생성된 고객 프로필.<br>- CSV (<code>csv</code>): CSV 가져오기를 통해 생성된 고객 프로필.<br>- 데모 (<code>demo</code>): 데모 데이터를 통해 생성된 고객 프로필.<br>- SMS (<code>sms</code>): SMS를 통해 생성된 고객 프로필.<br>- Shopify (<code>shopify</code>): Shopify를 통해 생성된 고객 프로필.<br>- WhatsApp (<code>whats_app</code>): WhatsApp을 통해 생성된 고객 프로필.<br>- 프로바이더 이벤트 (<code>provider_event</code>): 프로바이더 이벤트를 통해 생성된 고객 프로필.<br>- 프로바이더 동기화 (<code>provider_sync</code>): 프로바이더 동기화를 통해 생성된 고객 프로필.<br>- 랜딩 페이지 (<code>landing_page</code>): 랜딩 페이지를 통해 생성된 고객 프로필."
    tags:
      - Other Filters
  - name: Nested Custom Attributes
    display_name: "중첩 커스텀 속성"
    description: 커스텀 속성의 등록정보인 속성입니다.<br><br>중첩된 시간 커스텀 속성을 필터링할 때 "연중 일자" 또는 "시간"을 기준으로 필터링할 수 있습니다. "연중 일자"는 비교 시 월과 일만 확인합니다. "시간"은 연도를 포함한 전체 타임스탬프를 비교합니다.
    tags:
      - Custom attribute
  - name: Day of Recurring Event
    display_name: "반복 이벤트 일자"
    description: 이 필터는 "날짜" 데이터 유형의 커스텀 속성에서 월과 일을 확인하지만 연도는 확인하지 않습니다. 이 필터는 연간 이벤트에 유용합니다.<br><br>시간대&#58;<br>이 필터는 메시지가 현지 시간 예약 옵션을 사용하여 발송되는 한 사용자가 속한 시간대에 맞게 조정됩니다. 그렇지 않으면 회사 시간대를 사용합니다.
    tags:
      - Custom attribute
  - name: Custom Event
    display_name: "커스텀 이벤트"
    description: 사용자가 특별히 기록된 이벤트를 수행했는지 여부를 판단합니다.<br><br>예시:<br>activity_name 등록정보가 있는 활동 완료.<br><br>시간대:<br>UTC - 캘린더 일 = 1 캘린더 일은 24-48시간의 사용자 기록을 확인합니다
    tags:
      - Custom events
  - name: First Did Custom Event
    display_name: "커스텀 이벤트 최초 수행"
    description: 사용자가 특별히 기록된 이벤트를 수행한 가장 이른 시점을 판단합니다. (24시간 기간) <br><br>예시:<br> 유기한 장바구니 최초 발생이 1일 미만 전<br><br>시간대:<br>회사 시간대
    tags:
      - Custom events
  - name: Last Did Custom Event
    display_name: "커스텀 이벤트 최근 수행"
    description: 사용자가 특별히 기록된 이벤트를 수행한 가장 최근 시점을 판단합니다. 이 필터는 0.25시간과 같은 소수를 지원합니다. (24시간 기간) <br><br>예시:<br> 유기한 장바구니 최근 발생이 1일 미만 전<br><br>시간대:<br>회사 시간대
    tags:
      - Custom events
  - name: X Custom Event In Y Days
    display_name: "Y일 내 X 커스텀 이벤트"
    description: 사용자가 지정된 캘린더 일수(1~30일) 내에 특별히 기록된 이벤트를 0~50회 수행했는지 여부를 판단합니다. (캘린더 일 = 1 캘린더 일은 24-48시간의 사용자 기록을 확인합니다)<br> <a href="/docs/x-in-y-behavior/">X-in-Y 동작에 대해 자세히 알아보세요.</a> <br><br>예시:<br>유기한 장바구니가 지난 1 캘린더 일 내에 정확히 0회<br><br>시간대:<br>UTC - 모든 시간대를 고려하기 위해, 1 캘린더 일은 Segment가 평가되는 시점에 따라 24-48시간의 사용자 기록을 확인합니다. 2 캘린더 일의 경우 48-72시간의 사용자 기록을 확인하며, 이후도 마찬가지입니다.
    tags:
      - Custom events
  - name: X Custom Event Property In Y Days
    display_name: "Y일 내 X 커스텀 이벤트 등록정보"
    description: 사용자가 지정된 캘린더 일수(1~30일) 내에 특정 등록정보와 관련하여 특별히 기록된 이벤트를 0~50회 수행했는지 여부를 판단합니다. (캘린더 일 = 1 캘린더 일은 24-48시간의 사용자 기록을 확인합니다)<br><a href="/docs/x-in-y-behavior/">X-in-Y 동작에 대해 자세히 알아보세요.</a> <br><br>예시:<br> "event_name" 등록정보가 있는 즐겨찾기 추가가 지난 1 캘린더 일 내에 정확히 0회<br><br>시간대:<br>UTC - 모든 시간대를 고려하기 위해, 1 캘린더 일은 Segment가 평가되는 시점에 따라 24-48시간의 사용자 기록을 확인합니다. 2 캘린더 일의 경우 48-72시간의 사용자 기록을 확인하며, 이후도 마찬가지입니다.
    tags:
      - Custom events
  - name: Email Address
    display_name: "이메일 주소"
    description: 테스트를 위해 개별 이메일 주소로 Campaign 수신자를 지정할 수 있습니다. 또한 필터 내에서 "이메일 주소가 비어 있지 않음" 지정자를 사용하여 모든 사용자(탈퇴한 사용자 포함)에게 트랜잭션 이메일을 보내는 데 사용할 수 있으므로, 옵트인 상태에 관계없이 이메일 전달을 극대화할 수 있습니다. <br><br>이 필터는 고객 프로필에 이메일 주소가 있는지만 확인하는 반면, <a href="/docs/user_guide/audience/segments/segmentation_filters#email-available">이메일 사용 가능</a> 필터는 추가 기준을 확인합니다.
    tags:
      - Other Filters
  - name: External User ID
    display_name: "외부 사용자 ID"
    description: 테스트를 위해 개별 사용자 ID로 Campaign 수신자를 지정할 수 있습니다.
    tags:
      - Other Filters
  - name: "Random Bucket #"
    display_name: "무작위 버킷 번호"
    description: 무작위로 할당된 번호(0~9999 포함)로 사용자를 세분화합니다. A/B 및 다변량 테스트를 위해 진정한 무작위 사용자로 구성된 균일하게 분포된 Segments를 생성할 수 있습니다.
    tags:
      - Other Filters
  - name: Session Count
    display_name: "세션 수"
    description: 워크스페이스 내 앱에서 사용자가 가진 세션 수를 기준으로 세분화합니다.
    tags:
      - Sessions
  - name: Session Count For App
    display_name: "앱별 세션 수"
    description: 특정 지정된 앱에서 사용자가 가진 세션 수를 기준으로 세분화합니다.
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    display_name: "최근 Y일 내 X 세션"
    description: 지정된 캘린더 일수(1~30일) 내에 앱에서 사용자가 가진 세션 수(0~50회)를 기준으로 세분화합니다. <br> <a href="/docs/x-in-y-behavior/">X-in-Y 동작에 대해 자세히 알아보세요.</a>
    tags:
      - Sessions
  - name: First Used App
    display_name: "앱 최초 사용"
    description: 사용자가 앱을 연 가장 이른 기록 시점을 기준으로 세분화합니다. <em>이는 Braze SDK가 통합된 앱 버전을 사용한 첫 번째 세션을 캡처합니다.</em> (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Sessions
  - name: First Used Specific App
    display_name: "특정 앱 최초 사용"
    description: 워크스페이스 내 앱 중 하나를 사용자가 연 가장 이른 기록 시점을 기준으로 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Sessions
  - name: Last Used App
    display_name: "앱 최근 사용"
    description: 사용자가 앱을 연 가장 최근 시점을 기준으로 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Sessions
  - name: Last Used Specific App
    display_name: "특정 앱 최근 사용"
    description: 사용자가 특정 지정된 앱을 연 가장 최근 시점을 기준으로 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Sessions
  - name: Median Session Duration
    display_name: "세션 중간 길이"
    description: 앱에서 사용자의 세션 중간 길이를 기준으로 세분화합니다.
    tags:
      - Sessions
  - name: Received Message from Campaign
    display_name: "Campaign에서 메시지 수신"
    description: 사용자가 특정 Campaign을 수신했는지 여부를 기준으로 세분화합니다. <br><br>Content Cards, 배너, 인앱 메시지의 경우, 이는 사용자가 노출을 기록한 시점이며 카드나 인앱 메시지가 발송된 시점이 아닙니다.<br><br>푸시 및 웹훅의 경우, 이는 메시지가 사용자에게 발송된 시점입니다.<br><br>WhatsApp의 경우, 이는 마지막 메시지 API 요청이 WhatsApp에 전송된 시점이며 메시지가 사용자의 기기에 전달된 시점이 아닙니다.<br><br>이메일의 경우, 타겟팅된 고객 프로필은 이메일 요청이 이메일 서비스 제공업체에 전송될 때 이 필터와 일치합니다(실제로 전달되었는지 여부와 관계없이).<br><br>SMS 및 RCS의 경우, 사용자는 발송 시점에 메시지를 "수신"한 것으로 간주됩니다. 메시지가 사용자의 기기에 도달하지 못하더라도 사용자는 여전히 이 필터와 일치합니다.<br><br>메시지가 전달, 열림 또는 클릭되면, Braze는 동일한 채널 식별자(예&#58; 이메일 또는 전화번호)를 공유하는 모든 프로필의 데이터를 업데이트하므로, 메시지를 수신한 사람과 식별자를 공유하는 사용자는 자신의 프로필에 직접 Campaign이 발송되지 않았더라도 이 필터와 일치할 수 있습니다.
    tags:
      - Retargeting
  - name: Received Campaign Variant
    display_name: "Campaign 배리언트 수신"
    description: 사용자가 다변량 Campaign의 어떤 배리언트를 수신했는지를 기준으로 세분화합니다.<br><br>이 필터는 다변량 및 다변량 빠른 푸시 Campaigns에 적용됩니다. API Campaigns, 표준 멀티채널 Campaigns, 기능 플래그 실험 Campaigns는 Campaign 선택기에 표시되지 않습니다. 웹훅 전용 Campaigns는 Campaign 선택기에 표시되지 않습니다.<br><br>Content Cards, 배너, 인앱 메시지의 경우, 이는 사용자가 노출을 기록한 시점이며 카드나 인앱 메시지가 발송된 시점이 아닙니다.<br><br>푸시 및 웹훅의 경우, 이는 메시지가 사용자에게 발송된 시점입니다.<br><br>WhatsApp의 경우, 이는 마지막 메시지 API 요청이 WhatsApp에 전송된 시점이며 메시지가 사용자의 기기에 전달된 시점이 아닙니다.<br><br>이메일의 경우, 타겟팅된 고객 프로필은 이메일 요청이 이메일 서비스 제공업체에 전송될 때 이 필터와 일치합니다(실제로 전달되었는지 여부와 관계없이).<br><br>SMS 및 RCS의 경우, 사용자는 발송 시점에 메시지를 "수신"한 것으로 간주됩니다. 메시지가 사용자의 기기에 도달하지 못하더라도 사용자는 여전히 이 필터와 일치합니다.<br><br>메시지가 전달, 열림 또는 클릭되면, Braze는 동일한 채널 식별자(예&#58; 이메일 또는 전화번호)를 공유하는 모든 프로필의 데이터를 업데이트하므로, 메시지를 수신한 사람과 식별자를 공유하는 사용자는 자신의 프로필에 직접 Campaign이 발송되지 않았더라도 이 필터와 일치할 수 있습니다.
    tags:
      - Retargeting
  - name: Received Message from Canvas Step
    display_name: "캔버스 단계에서 메시지 수신"
    description: 사용자가 특정 Canvas 구성요소를 수신했는지 여부를 기준으로 세분화합니다.<br><br>Content Cards 및 인앱 메시지의 경우, 이는 사용자가 노출을 기록한 시점이며 카드나 인앱 메시지가 발송된 시점이 아닙니다.<br><br>푸시 및 웹훅의 경우, 이는 메시지가 사용자에게 발송된 시점입니다.<br><br>WhatsApp의 경우, 이는 마지막 메시지 API 요청이 WhatsApp에 전송된 시점이며 메시지가 사용자의 기기에 전달된 시점이 아닙니다.<br><br>이메일의 경우, 타겟팅된 고객 프로필은 이메일 요청이 이메일 서비스 제공업체에 전송될 때 이 필터와 일치합니다(실제로 전달되었는지 여부와 관계없이).<br><br>SMS 및 RCS의 경우, 사용자는 발송 시점에 메시지를 "수신"한 것으로 간주됩니다. 메시지가 사용자의 기기에 도달하지 못하더라도 사용자는 여전히 이 필터와 일치합니다.<br><br>메시지가 전달, 열림 또는 클릭되면, Braze는 동일한 채널 식별자(예&#58; 이메일 또는 전화번호)를 공유하는 모든 프로필의 데이터를 업데이트하므로, 메시지를 수신한 사람과 식별자를 공유하는 사용자는 자신의 프로필에 직접 Campaign이 발송되지 않았더라도 이 필터와 일치할 수 있습니다.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Canvas Step
    display_name: "특정 캔버스 단계에서 마지막 메시지 수신"
    description: 사용자가 특정 Canvas 구성요소를 수신한 시점을 기준으로 세분화합니다.<br><br>전달, 열림 또는 클릭이 발생할 때 동일한 채널 식별자(예&#58; 이메일 또는 전화번호)를 공유하는 모든 프로필의 데이터가 업데이트되므로, 메시지를 수신한 사람과 식별자를 공유하는 사용자는 명시적으로 메시지를 받지 않았더라도 이 필터와 일치할 수 있습니다. 중복 프로필에서 고객 프로필을 분리하려면 "Entered Canvas Variation"을 사용하세요.<br><br>이 필터는 사용자가 다른 Canvas 구성요소를 수신한 시점은 고려하지 않습니다.
    tags:
      - Retargeting
  - name: Last Received Message from Specific Campaign
    display_name: "특정 Campaign에서 마지막 메시지 수신"
    description: 사용자가 특정 Campaign을 수신했는지 여부를 기준으로 세분화합니다.<br><br>전달, 열림 또는 클릭이 발생할 때 동일한 채널 식별자(예&#58; 이메일 또는 전화번호)를 공유하는 모든 프로필의 데이터가 업데이트되므로, 메시지를 수신한 사람과 식별자를 공유하는 사용자는 명시적으로 메시지를 받지 않았더라도 이 필터와 일치할 수 있습니다.<br><br>이 필터는 사용자가 다른 Campaigns를 수신한 시점은 고려하지 않습니다.
    tags:
      - Retargeting
  - name: Received Message from Campaign or Canvas with Tag
    display_name: "태그가 있는 Campaign 또는 Canvas에서 메시지 수신"
    description: 사용자가 특정 태그가 있는 특정 Campaign 또는 Canvas를 수신했는지 여부를 기준으로 세분화합니다.<br><br>Content Cards, 배너(Campaigns만 해당), 인앱 메시지의 경우, 이는 사용자가 노출을 기록한 시점이며 카드나 인앱 메시지가 발송된 시점이 아닙니다.<br><br>푸시 및 웹훅의 경우, 이는 메시지가 사용자에게 발송된 시점입니다.<br><br>WhatsApp의 경우, 이는 마지막 메시지 API 요청이 WhatsApp에 전송된 시점이며 메시지가 사용자의 기기에 전달된 시점이 아닙니다.<br><br>이메일의 경우, 타겟팅된 고객 프로필은 이메일 요청이 이메일 서비스 제공업체에 전송될 때 이 필터와 일치합니다(실제로 전달되었는지 여부와 관계없이).<br><br>SMS 및 RCS의 경우, 사용자는 발송 시점에 메시지를 "수신"한 것으로 간주됩니다. 메시지가 사용자의 기기에 도달하지 못하더라도 사용자는 여전히 이 필터와 일치합니다.<br><br>메시지가 전달, 열림 또는 클릭되면, Braze는 동일한 채널 식별자(예&#58; 이메일 또는 전화번호)를 공유하는 모든 프로필의 데이터를 업데이트하므로, 메시지를 수신한 사람과 식별자를 공유하는 사용자는 자신의 프로필에 직접 Campaign이 발송되지 않았더라도 이 필터와 일치할 수 있습니다.
    tags:
      - Retargeting
  - name: Last Received Message from Campaign or Canvas With Tag
    display_name: "태그가 있는 Campaign 또는 Canvas에서 마지막 메시지 수신"
    description: 사용자가 특정 태그가 있는 특정 Campaign 또는 Canvas를 수신한 시점을 기준으로 세분화합니다. 이 필터는 사용자가 다른 Campaigns 또는 Canvases를 수신한 시점은 고려하지 않습니다. (24시간 기간)
    tags:
      - Retargeting
  - name: Has Never Received a Message from Campaign or Canvas Step
    display_name: "Campaign 또는 캔버스 단계에서 메시지를 수신한 적 없음"
    description: 사용자가 Campaign 또는 Canvas 구성요소를 수신한 적이 있는지 여부를 기준으로 세분화합니다.
    tags:
      - Retargeting
  - name: Last Received Email
    display_name: "마지막 이메일 수신"
    description: 사용자가 이메일 메시지를 마지막으로 수신한 시점을 기준으로 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Retargeting
  - name: Last Received Push
    display_name: "마지막 푸시 수신"
    description: 사용자가 푸시 알림을 마지막으로 수신한 시점을 기준으로 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Retargeting
  - name: Last In App Message Impression
    display_name: "마지막 인앱 메시지 노출"
    description: 사용자가 인앱 메시지를 마지막으로 본 시점을 기준으로 세분화합니다.
    tags:
      - Retargeting
  - name: Last Received SMS
    display_name: "마지막 SMS 수신"
    description: 마지막 SMS, MMS 또는 RCS 메시지가 SMS 또는 RCS 제공업체에 전달된 시점을 기준으로 사용자를 세분화합니다. 이는 메시지가 사용자의 기기에 전달되었음을 보장하지 않습니다. (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Retargeting
  - name: Last Received Webhook
    display_name: "마지막 웹훅 수신"
    description: Braze가 해당 사용자에 대해 웹훅을 마지막으로 발송한 시점을 기준으로 세분화합니다. (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Retargeting
  - name: Last Received WhatsApp
    display_name: "마지막 WhatsApp 수신"
    description: 사용자가 WhatsApp 메시지를 마지막으로 수신한 시점을 기준으로 세분화합니다. 이는 마지막 메시지 API 요청이 WhatsApp에 전송된 시점이며 메시지가 사용자의 기기에 전달된 시점이 아닙니다. (24시간 기간)<br><br>시간대:<br>회사 시간대
    tags:
      - Retargeting
  - name: Live Activities Push to Start Registered for App
    display_name: "앱에 대해 Live Activities 푸시 시작 등록됨"
    description: 사용자가 특정 앱에 대해 iOS 푸시 알림을 통해 Live Activity를 시작하도록 등록되어 있는지 여부를 기준으로 세분화합니다.
    tags:
      - Devices
  - name: Clicked/Opened Campaign
    display_name: "Campaign 클릭/열림"
    description: 특정 Campaign과의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우, 열림 이벤트에는 기계 열림과 비기계 열림이 모두 포함됩니다.<br><br>이메일의 경우, "모든 이메일 열림(기계 열림)" 및 "모든 이메일 열림(기타 열림)"으로 필터링하는 옵션도 포함됩니다. 탈퇴 링크 및 환경설정 센터 클릭은 이 필터에 포함되지 않습니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일이 열리거나 클릭되면, 동일한 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 원래 사용자가 메시지 발송 후 열림 또는 클릭 전에 이메일 주소를 변경하면, 열림 또는 클릭은 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 적용됩니다.<br><br>SMS 및 RCS의 경우, 상호작용은 다음과 같이 정의됩니다:<br>- 사용자가 주어진 키워드 카테고리와 일치하는 답장 SMS 또는 RCS를 마지막으로 보낸 시점. 이는 해당 전화번호를 가진 모든 사용자가 수신한 가장 최근 Campaign에 귀속됩니다. Campaign은 지난 4시간 이내에 수신되었어야 합니다.<br>- 사용자가 주어진 Campaign에서 사용자 클릭 추적이 활성화된 SMS 또는 RCS 메시지의 단축 링크를 마지막으로 선택한 시점.
    tags:
      - Retargeting
  - name: Clicked/Opened Campaign or Canvas With Tag
    display_name: "태그가 있는 Campaign 또는 Canvas 클릭/열림"
    description: 특정 태그가 있는 특정 Campaign과의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우, 열림 이벤트에는 기계 열림과 비기계 열림이 모두 포함됩니다.<br><br>이메일의 경우, "모든 이메일 열림(기계 열림)" 및 "모든 이메일 열림(기타 열림)"으로 필터링하는 옵션이 포함됩니다. 여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일이 열리거나 클릭되면, 동일한 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 원래 사용자가 메시지 발송 후 열림 또는 클릭 전에 이메일 주소를 변경하면, 열림 또는 클릭은 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 적용됩니다.<br><br>SMS 및 RCS의 경우, 상호작용은 다음과 같이 정의됩니다:<br>- 사용자가 주어진 키워드 카테고리와 일치하는 답장 SMS 또는 RCS를 마지막으로 보낸 시점. 이는 해당 전화번호를 가진 모든 사용자가 수신한 가장 최근 Campaign에 귀속됩니다. Campaign은 지난 4시간 이내에 수신되었어야 합니다.<br>- 사용자가 태그가 있는 주어진 Campaign 또는 캔버스 단계에서 사용자 클릭 추적이 활성화된 SMS 또는 RCS 메시지의 단축 링크를 마지막으로 선택한 시점.
    tags:
      - Retargeting
  - name: Clicked/Opened Step
    display_name: "단계 클릭/열림"
    description: 특정 Canvas 구성요소와의 상호작용을 기준으로 필터링합니다. 이메일 메시징의 경우, 열림 이벤트에는 기계 열림과 비기계 열림이 모두 포함됩니다.<br><br>이메일의 경우, "모든 이메일 열림(기계 열림)" 및 "모든 이메일 열림(기타 열림)"으로 필터링하는 옵션이 포함됩니다.<br><br>SMS 및 RCS의 경우, 상호작용은 다음과 같이 정의됩니다:<br>- 사용자가 주어진 키워드 카테고리와 일치하는 답장 SMS 또는 RCS를 마지막으로 보낸 시점. 이는 해당 전화번호를 가진 모든 사용자가 수신한 가장 최근 Campaign에 귀속됩니다. Campaign은 지난 4시간 이내에 수신되었어야 합니다. <br>- 사용자가 주어진 캔버스 단계에서 사용자 클릭 추적이 활성화된 SMS 또는 RCS 메시지의 단축 링크를 마지막으로 선택한 시점.
    tags:
      - Retargeting
  - name: Clicked Alias in Campaign
    display_name: "Campaign에서 별칭 클릭"
    description: 사용자가 특정 Campaign에서 특정 별칭을 클릭했는지 여부를 기준으로 필터링합니다. 이메일 메시지에만 적용됩니다. <br><br>여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일이 열리거나 클릭되면, 동일한 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 원래 사용자가 메시지 발송 후 열림 또는 클릭 전에 이메일 주소를 변경하면, 열림 또는 클릭은 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 적용됩니다.
    tags:
      - Retargeting
  - name: Clicked Alias in Canvas Step
    display_name: "캔버스 단계에서 별칭 클릭"
    description: 사용자가 특정 Canvas에서 특정 별칭을 클릭했는지 여부를 기준으로 필터링합니다. 이메일 메시지에만 적용됩니다. <br><br>여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일이 열리거나 클릭되면, 동일한 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 원래 사용자가 메시지 발송 후 열림 또는 클릭 전에 이메일 주소를 변경하면, 열림 또는 클릭은 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 적용됩니다.
    tags:
      - Retargeting
  - name: Clicked Alias in Any Campaign or Canvas Step
    display_name: "모든 Campaign 또는 캔버스 단계에서 별칭 클릭"
    description: 사용자가 모든 Campaign 또는 Canvas에서 특정 별칭을 클릭했는지 여부를 기준으로 필터링합니다. 이메일 메시지에만 적용됩니다. <br><br>여러 사용자가 동일한 이메일 주소를 공유하는 경우:<br>- 이메일이 열리거나 클릭되면, 동일한 이메일 주소를 가진 다른 모든 사용자의 프로필도 업데이트됩니다. <br>- 원래 사용자가 메시지 발송 후 열림 또는 클릭 전에 이메일 주소를 변경하면, 열림 또는 클릭은 원래 사용자 대신 해당 이메일 주소를 가진 나머지 모든 사용자에게 적용됩니다.
    tags:
      - Retargeting
  - name: Hard Bounced
    display_name: "하드바운스"
    description: 사용자의 이메일 주소가 하드바운스되었는지(예&#58; 이메일 주소가 유효하지 않음) 여부를 기준으로 세분화합니다. 유효하지 않은 이메일을 가진 사용자를 내보내려면 [`/email/hard_bounces`]({{site.baseurl}}/api/endpoints/email/get_list_hard_bounces/) 엔드포인트를 호출하거나, 이메일 주소가 비어 있지 않음, 이메일 사용 불가, 이메일 구독 상태가 탈퇴가 아님과 같은 필터로 Segment를 구성하세요.
    tags:
      - Retargeting
  - name: Soft Bounced
    display_name: "소프트바운스"
    description: 사용자가 Y일 내에 X회 소프트바운스되었는지 여부를 기준으로 세분화합니다. Segment 필터는 최대 30일까지만 조회할 수 있지만, 세그먼트 확장을 사용하면 더 이전까지 조회할 수 있습니다.<br><br>이 필터는 Currents의 소프트바운스 이벤트와 다르게 작동합니다. 소프트바운스 Segment 필터는 72시간 재시도 기간 동안 성공적인 전달이 없었을 경우 소프트바운스로 계산합니다. Currents에서는 모든 실패한 재시도가 소프트바운스 이벤트로 전송됩니다.
    tags:
      - Retargeting
  - name: Has Marked You As Spam
    display_name: "스팸으로 표시됨"
    description: 사용자가 메시지를 스팸으로 표시했는지 여부를 기준으로 세분화합니다.
    tags:
      - Retargeting
  - name: Invalid Phone Number
    display_name: "유효하지 않은 전화번호"
    description: 사용자의 전화번호가 유효하지 않은지 여부를 기준으로 세분화합니다.
    tags:
      - Retargeting
  - name: Last Sent Specific SMS Inbound Keyword Category
    display_name: "특정 SMS 인바운드 키워드 카테고리 마지막 발송"
    description: 사용자가 특정 구독 그룹 내 특정 키워드 카테고리로 SMS, MMS 또는 RCS를 마지막으로 보낸 시점을 기준으로 세분화합니다.
    tags:
      - Retargeting
  - name: Converted From Campaign
    display_name: "Campaign에서 전환"
    description: 사용자가 특정 Campaign에서 전환했는지 여부를 기준으로 세분화합니다. 이 필터에는 대조군에 속한 사용자가 포함되지 않습니다.
    tags:
      - Retargeting
  - name: Converted From Canvas
    display_name: "Canvas에서 전환"
    description: 사용자가 특정 Canvas에서 전환했는지 여부를 기준으로 세분화합니다. 이 필터에는 대조군에 속한 사용자가 포함되지 않습니다.
    tags:
      - Retargeting
  - name: In Campaign Control Group
    display_name: "Campaign 대조군에 속함"
    description: 사용자가 특정 다변량 Campaign의 대조군에 속했는지 여부를 기준으로 세분화합니다.
    tags:
      - Retargeting
  - name: In Canvas Control Group
    display_name: "Canvas 대조군에 속함"
    description: 사용자가 특정 Canvas의 대조군에 속했는지 여부를 기준으로 세분화합니다. 이 필터는 Canvas에 진입한 사용자만 평가하므로, Canvas에 진입하지 않은 사용자는 결과에서 완전히 제외됩니다.<br><br>예를 들어, Canvas의 대조군에 속하지 않은 사용자를 필터링하면, Canvas에 진입하여 비대조 배리언트에 할당된 사용자만 받게 됩니다. Canvas에 진입하지 않은 사용자는 포함되지 않습니다. Canvas 진입 여부에 관계없이 모든 사용자를 포함하려면 <code>Entered Canvas Variation</code> 필터를 대신 사용하세요.
    tags:
      - Retargeting
  - name: Last Enrolled in Any Control Group
    display_name: "마지막 대조군 등록"
    description: 사용자가 Campaign에서 대조군에 마지막으로 포함된 시점을 기준으로 세분화합니다. <br><br>시간대:<br>회사 시간대
    tags:
      - Retargeting
  - name: Entered Canvas Variation
    display_name: "Canvas 배리언트 진입"
    description: 사용자가 특정 Canvas의 배리언트 경로에 진입했는지 여부를 기준으로 세분화합니다. 이 필터는 모든 사용자를 평가합니다.<br><br>예를 들어, Canvas 배리언트 대조군에 진입하지 않은 사용자를 필터링하면, Canvas에 진입했는지 여부에 관계없이 대조군에 속하지 않은 모든 사용자를 받게 됩니다.
    tags:
      - Retargeting
  - name: Last Received Any Message
    display_name: "마지막 메시지 수신"
    description: 마지막으로 수신한 메시지를 판단하여 사용자를 세분화합니다. (24시간 기간)<br><br>Content Cards, 배너, 인앱 메시지의 경우, 이는 사용자가 마지막으로 노출을 기록한 시점이며 카드나 인앱 메시지가 마지막으로 발송된 시점이 아닙니다.<br><br>푸시 및 웹훅의 경우, 이는 메시지가 사용자에게 발송된 시점입니다.<br><br>WhatsApp의 경우, 이는 마지막 메시지 API 요청이 WhatsApp에 전송된 시점이며 메시지가 사용자의 기기에 전달된 시점이 아닙니다.<br><br>이메일의 경우, 타겟팅된 고객 프로필은 이메일 요청이 이메일 서비스 제공업체에 전송될 때 이 필터와 일치합니다(실제로 전달되었는지 여부와 관계없이).<br><br>SMS 및 RCS의 경우, 사용자는 발송 시점에 메시지를 "수신"한 것으로 간주됩니다. 메시지가 사용자의 기기에 도달하지 못하더라도 사용자는 여전히 이 필터와 일치합니다.<br><br>메시지가 전달, 열림 또는 클릭되면, Braze는 동일한 채널 식별자(예&#58; 이메일 또는 전화번호)를 공유하는 모든 프로필의 데이터를 업데이트하므로, 메시지를 수신한 사람과 식별자를 공유하는 사용자는 자신의 프로필에 직접 Campaign이 발송되지 않았더라도 이 필터와 일치할 수 있습니다.<br><br>예시:<br>마지막 메시지 수신이 1일 미만 전 = 24시간 미만 전<br><br>시간대:<br>회사 시간대
    tags:
      - Retargeting
  - name: Last Engaged With Message
    display_name: "마지막 메시지 참여"
    description: 사용자가 메시징 채널(배너, Content Cards, 이메일, 인앱, SMS, RCS, 푸시, WhatsApp) 중 하나를 마지막으로 클릭하거나 연 시점을 기준으로 세분화합니다.<br><br>Content Cards, 배너, 인앱 메시지의 경우, 이는 사용자가 노출을 기록한 시점이며 카드나 인앱 메시지가 발송된 시점이 아닙니다.<br><br>푸시 및 웹훅의 경우, 이는 메시지가 사용자에게 발송된 시점입니다.<br><br>WhatsApp의 경우, 이는 마지막 메시지 API 요청이 WhatsApp에 전송된 시점이며 메시지가 사용자의 기기에 전달된 시점이 아닙니다.<br><br>이메일 메시징의 경우, 열림 이벤트에는 기계 열림과 비기계 열림이 모두 포함됩니다. (24시간 기간)<br><br>이메일의 경우, 타겟팅된 고객 프로필은 이메일 요청이 이메일 서비스 제공업체에 전송될 때 이 필터와 일치합니다(실제로 전달되었는지 여부와 관계없이). 또한 "모든 이메일 열림(기계 열림)" 및 "모든 이메일 열림(기타 열림)"으로 필터링하는 옵션이 포함됩니다.<br><br>SMS 및 RCS의 경우, 이는 사용자가 사용자 클릭 추적이 활성화된 메시지의 단축 링크를 마지막으로 선택한 시점입니다.<br><br>메시지가 전달, 열림 또는 클릭되면, Braze는 동일한 채널 식별자(예&#58; 이메일 또는 전화번호)를 공유하는 모든 프로필의 데이터를 업데이트하므로, 메시지를 수신한 사람과 식별자를 공유하는 사용자는 자신의 프로필에 직접 Campaign이 발송되지 않았더라도 이 필터와 일치할 수 있습니다.<br><br>시간대:<br>회사 시간대
    tags:
      - Retargeting
  - name: Clicked card
    display_name: "카드 클릭"
    description: 사용자가 특정 콘텐츠 카드를 클릭했는지 여부를 기준으로 세분화합니다. 이 필터는 "Campaign 클릭/열림", "태그가 있는 Campaign 또는 Canvas 클릭/열림", "단계 클릭/열림"의 하위 필터로 사용할 수 있습니다.
    tags:
      - Retargeting
  - name: Feature Flags
    display_name: "기능 플래그"
    description: 특정 <a href="/docs/developer_guide/feature_flags/">기능 플래그</a> 가 현재 활성화된 사용자의 Segment입니다.
    tags:
      - Retargeting
  - name: Subscription Group
    display_name: "구독 그룹"
    description: 이메일, SMS, MMS, RCS 또는 WhatsApp에 대한 구독 그룹을 기준으로 사용자를 세분화합니다. 아카이브된 그룹은 표시되지 않으며 사용할 수 없습니다.
    tags:
      - Channel subscription behavior
  - name: Email Available
    display_name: "이메일 사용 가능"
    description: 사용자에게 유효한 이메일 주소가 있는지, 이메일에 가입 또는 옵트인했는지 여부를 기준으로 세분화합니다. 이 필터는 세 가지 기준을 확인합니다&#58; 사용자가 이메일을 탈퇴했는지, Braze가 하드바운스를 수신했는지, 이메일이 스팸으로 표시되었는지. 이러한 기준 중 하나라도 충족되거나 사용자에게 이메일이 존재하지 않으면, 해당 사용자는 포함되지 않습니다.<br><br>이메일 사용 가능이 <code>false</code>인 사용자는 Campaign 오디언스에서 제외되며 이메일을 수신하지 않습니다. 발송 설정이 모든 사용자(탈퇴한 사용자 포함)에게 발송하도록 구성되어 있더라도 마찬가지입니다.<br><br>옵트인 상태가 중요한 이메일의 경우, <a href="/docs/user_guide/audience/segments/segmentation_filters#email-address">이메일 주소</a> 대신 이메일 사용 가능을 사용하세요. 추가 기준이 이메일을 수신할 자격이 있는 사용자를 타겟팅하는 데 도움이 됩니다.
    tags:
      - Channel subscription behavior
  - name: Email Opt In Date
    display_name: "이메일 옵트인 날짜"
    description: 사용자가 이메일에 옵트인한 날짜를 기준으로 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Email Subscription Status
    display_name: "이메일 구독 상태"
    description: 이메일 구독 상태를 기준으로 사용자를 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Email Unsubscribed Date
    display_name: "이메일 탈퇴 날짜"
    description: 사용자가 향후 이메일을 탈퇴한 날짜를 기준으로 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled
    display_name: "포그라운드 푸시 활성화됨"
    description: 임시 푸시 승인을 받았거나 포그라운드 푸시가 활성화된 사용자를 세분화합니다. 구체적으로 이 수에는 다음이 포함됩니다:<br>1. 임시로 푸시가 승인된 iOS 사용자. <br>2. 포그라운드 푸시가 활성화되어 있고 푸시 구독 상태가 탈퇴가 아닌 사용자(모든 앱 대상). 이러한 사용자의 경우 포그라운드 푸시만 포함됩니다.<br><br>포그라운드 푸시 활성화됨에는 탈퇴한 사용자가 포함되지 않습니다. <br><br>이 필터로 세분화한 후, 하단 패널인 <em>도달 가능 사용자</em>에서 Android, iOS, 웹별로 해당 Segment에 속한 사용자의 분류를 확인할 수 있습니다.
    tags:
      - Channel subscription behavior
  - name: Foreground Push Enabled for App
    display_name: "앱에 대해 포그라운드 푸시 활성화됨"
    description: 사용자의 기기에서 앱에 대해 푸시가 활성화되어 있는지 여부를 기준으로 세분화합니다. 앱에 대해 포그라운드 푸시가 활성화된 사용자입니다. 푸시 구독 상태는 고려하지 않습니다. 이 수에는 포그라운드 및 백그라운드 푸시 토큰이 임시로 승인된 사용자가 포함됩니다.
    tags:
      - Channel subscription behavior
  - name: Background or Foreground Push Enabled
    display_name: "백그라운드 또는 포그라운드 푸시 활성화됨"
    description: 사용자에게 푸시 토큰이 있고 탈퇴하지 않았는지 여부를 기준으로 세분화합니다. 모든 앱에 대해 백그라운드 또는 포그라운드 푸시가 활성화된 사용자입니다.
    tags:
      - Channel subscription behavior
  - name: Push Opt In Date
    display_name: "푸시 옵트인 날짜"
    description: 사용자가 푸시에 옵트인한 날짜를 기준으로 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Push Subscription Status
    display_name: "푸시 구독 상태"
    description: 푸시에 대한 <a href="/docs/user_guide/channels/push/push_setup/push_subscription_states#push-subscription-state">구독 상태</a> 를 기준으로 사용자를 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Push Unsubscribed Date
    display_name: "푸시 탈퇴 날짜"
    description: 사용자가 향후 푸시 알림을 탈퇴한 날짜를 기준으로 세분화합니다.
    tags:
      - Channel subscription behavior
  - name: Purchased Product
    display_name: "구매한 제품"
    description: 앱에서 구매한 제품을 기준으로 사용자를 세분화합니다.
    tags:
      - Purchase behavior
  - name: Total Number of Purchases
    display_name: "총 구매 횟수"
    description: 앱에서 사용자가 수행한 구매 횟수를 기준으로 세분화합니다.
    tags:
      - Purchase behavior
  - name: X Product Purchased In Y Days
    display_name: "Y일 내 X 제품 구매"
    description: 특정 제품이 구매된 횟수를 기준으로 사용자를 필터링합니다.
    tags:
      - Purchase behavior
  - name: X Purchases in Last Y Days
    display_name: "최근 Y일 내 X 구매"
    description: 지정된 캘린더 일수(1~30일) 내에 사용자가 구매한 횟수(0~50회)를 기준으로 세분화합니다. <br> <a href="/docs/x-in-y-behavior/">X-in-Y 동작에 대해 자세히 알아보세요.</a>
    tags:
      - Purchase behavior
  - name: X Purchase Property In Y Days
    display_name: "Y일 내 X 구매 등록정보"
    description: 지정된 캘린더 일수(1~30일) 내에 특정 구매 등록정보와 관련하여 구매가 이루어진 횟수를 기준으로 사용자를 세분화합니다. <br> <a href="/docs/x-in-y-behavior/">X-in-Y 동작에 대해 자세히 알아보세요.</a>
    tags:
      - Purchase behavior
  - name: First Made Purchase
    display_name: "최초 구매"
    description: 사용자가 앱에서 구매한 가장 이른 시점을 기준으로 세분화합니다.
    tags:
      - Purchase behavior
  - name: First Purchase For App
    display_name: "앱 최초 구매"
    description: 사용자가 앱에서 구매한 가장 이른 시점을 기준으로 세분화합니다.
    tags:
      - Purchase behavior
  - name: Last Made Purchase
    display_name: "마지막 구매"
    description: 사용자가 마지막으로 구매한 시점을 기준으로 필터링합니다.
    tags:
      - Purchase behavior
  - name: Last Purchased Product
    display_name: "마지막 구매 제품"
    description: 사용자가 특정 제품을 마지막으로 구매한 시점을 기준으로 필터링합니다.
    tags:
      - Purchase behavior
  - name: Money Spent
    display_name: "지출 금액"
    description: 앱에서 사용자가 지출한 금액을 기준으로 세분화합니다.
    tags:
      - Purchase behavior
  - name: X Money Spent in Y Days
    display_name: "Y일 내 X 지출 금액"
    description: 지정된 캘린더 일수(1~30일) 내에 앱에서 사용자가 지출한 금액을 기준으로 세분화합니다. 이 금액에는 최근 50건의 구매 합계만 포함됩니다. <br> <a href="/docs/x-in-y-behavior/">X-in-Y 동작에 대해 자세히 알아보세요.</a>
    tags:
      - Purchase behavior
  - name: Last order placed (last 730 days)
    display_name: "마지막 주문 완료 (최근 730일)"
    description: 사용자가 마지막으로 주문한 시점을 기준으로 세분화하며, 이는 주문 완료에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 기반으로 합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 사용자는 하루에 한 번 이 필터에 대해 평가되며, 최대 조회 기간은 최근 2년입니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Total orders count (last 730 days)
    display_name: "총 주문 수 (최근 730일)"
    description: 최근 2년 내 사용자의 총 주문 수를 기준으로 세분화하며, 이는 주문 완료에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 기반으로 합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 이 수에는 취소된 주문이 제외되며, 취소된 주문은 주문 취소에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 사용하여 추적해야 합니다. 사용자는 하루에 한 번 이 필터에 대해 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Total orders count
    display_name: "총 주문 수"
    description: 사용자의 전체 기간에 걸친 총 주문 수를 기준으로 세분화하며, 이는 주문 완료에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 기반으로 합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 이 수에는 취소된 주문이 제외되며, 취소된 주문은 주문 취소에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 사용하여 추적해야 합니다. 사용자는 이 필터에 대해 실시간으로 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Total canceled orders count (last 730 days)
    display_name: "총 취소 주문 수 (최근 730일)"
    description: 최근 2년 내 사용자가 취소한 총 주문 수를 기준으로 세분화하며, 이는 주문 완료에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 기반으로 합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 사용자는 하루에 한 번 이 필터에 대해 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Customer lifetime value (last 730 days)
    display_name: "고객 생애주기 가치 (최근 730일)"
    description: 사용자가 브랜드와의 구매 이력에서 생성할 것으로 예상되는 총 매출을 기준으로 세분화합니다. 계산은 최근 730일을 고려하며, 평균 주문 금액(AOV)에 총 주문 수를 곱한 후 사용자의 활성 구매 기간(첫 번째 주문과 가장 최근 주문 사이의 기간)을 반영합니다. 이 필터는 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 에서 추적된 데이터를 사용합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 사용자는 하루에 한 번 이 필터에 대해 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Total refund value (last 730 days)
    display_name: "총 환불 금액 (최근 730일)"
    description: 최근 2년 동안 사용자에게 부여된 환불 금액을 기준으로 세분화하며, 이는 주문 환불에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 기반으로 합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 사용자는 하루에 한 번 이 필터에 대해 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Total refund value
    display_name: "총 환불 금액"
    description: 사용자의 전체 기간에 걸쳐 부여된 총 환불 금액을 기준으로 세분화하며, 이는 주문 환불에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 기반으로 합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 실시간으로 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Total revenue (last 730 days)
    display_name: "총 매출 (최근 730일)"
    description: 최근 2년 동안 사용자의 주문에서 발생한 총 매출을 기준으로 세분화하며, 주문 완료에 대한 eCommerce 이벤트의 매출에서 주문 환불에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 의 매출을 차감하여 계산합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 사용자는 하루에 한 번 이 필터에 대해 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Total revenue
    display_name: "총 매출"
    description: 사용자의 전체 기간에 걸쳐 주문에서 발생한 총 매출을 기준으로 세분화하며, 주문 완료에 대한 eCommerce 이벤트의 매출에서 주문 환불에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 의 매출을 차감하여 계산합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 사용자는 이 필터에 대해 실시간으로 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Average order value (last 730 days)
    display_name: "평균 주문 금액 (최근 730일)"
    description: 최근 2년 동안 사용자 주문의 평균(산술 평균) 금액을 기준으로 세분화하며, 이는 주문 완료에 대한 <a href="/docs/user_guide/data/activation/events/recommended_events/ecommerce_events">eCommerce 권장 이벤트</a> 를 기반으로 합니다(eCommerce 이벤트를 추적하지 않는 워크스페이스에는 이 필터에 대한 데이터가 없습니다). 사용자는 하루에 한 번 이 필터에 대해 평가됩니다.<br><br>이 필터는 베타 버전입니다. 이 필터를 사용하려면 Braze 계정 매니저에게 문의하세요.
    tags:
      - eCommerce
  - name: Country
    display_name: "국가"
    description: 사용자가 마지막으로 표시한 국가 위치를 기준으로 세분화합니다.
    tags:
      - Demographic attributes
  - name: City
    display_name: "도시"
    description: 사용자가 마지막으로 표시한 도시 위치를 기준으로 세분화합니다.
    tags:
      - Demographic attributes
  - name: Language
    display_name: "언어"
    description: 사용자의 선호 언어를 기준으로 세분화합니다.
    tags:
      - Demographic attributes
  - name: Age
    display_name: "나이"
    description: 앱 내에서 사용자가 표시한 나이를 기준으로 세분화합니다.
    tags:
      - Demographic attributes
  - name: Birthday
    display_name: "생일"
    description: 앱 내에서 사용자가 표시한 생일을 기준으로 세분화합니다. <br> 2월 29일이 생일인 사용자는 3월 1일을 포함하는 Segments에 포함됩니다.<br><br>12월 또는 1월 생일을 타겟팅하려면, 타겟팅하려는 연도의 12개월 범위 내에서만 필터 로직을 삽입하세요. 즉, 이전 연도의 12월이나 다음 연도의 1월을 참조하는 로직을 삽입하지 마세요. 예를 들어, 12월 생일을 타겟팅하려면 "12월 31일에", "12월 31일 이전에" 또는 "11월 30일 이후에"로 필터링할 수 있습니다.
    tags:
      - Demographic attributes
  - name: Gender
    display_name: "성별"
    description: 앱 내에서 사용자가 표시한 성별을 기준으로 세분화합니다.
    tags:
      - Demographic attributes
  - name: Unformatted Phone Number
    display_name: "형식 미지정 전화번호"
    description: 형식이 지정되지 않은 전화번호를 기준으로 사용자를 세분화합니다. 괄호, 대시 또는 기타 기호를 포함하지 않습니다.
    tags:
      - Demographic attributes
  - name: First Name
    display_name: "이름"
    description: 앱 내에서 사용자가 표시한 이름을 기준으로 세분화합니다.
    tags:
      - Demographic attributes
  - name: Last Name
    display_name: "성"
    description: 앱 내에서 사용자가 표시한 성을 기준으로 세분화합니다.
    tags:
      - Demographic attributes
  - name: Has App
    display_name: "앱 보유"
    description: 사용자가 앱을 설치한 적이 있는지 여부를 기준으로 세분화합니다. 현재 앱이 설치되어 있는 사용자와 과거에 삭제한 사용자가 모두 포함됩니다. 일반적으로 이 필터에 포함되려면 사용자가 앱을 열어야(세션을 시작해야) 합니다. 그러나 사용자가 Braze로 가져와져 앱에 수동으로 연결된 경우와 같은 일부 예외가 있습니다.
    tags:
      - App
  - name: Most Recent App Version Name
    display_name: "최신 앱 버전 이름"
    description: 사용자 앱의 최신 이름을 기준으로 세분화합니다.<br><br>"미만" 또는 "이하"를 사용할 때, 주요 앱 버전이 존재하지 않으면 이 필터는 사용자가 해당 앱 버전보다 오래되었기 때문에 `true`를 반환합니다. 즉, 사용자의 마지막 주요 앱 버전이 존재하지 않으면 자동으로 필터와 일치합니다.
    tags:
      - App
  - name: Most Recent App Version Number
    display_name: "최신 앱 버전 번호"
    description: 사용자 앱의 최신 앱 버전 번호를 기준으로 세분화합니다. 괄호 안의 버전 번호가 필터링에 사용되며, 그 앞의 번호는 참조용입니다. 예를 들어, "3.7.0(134.0.0.0)"에서 "134.0.0.0"이 필터링되는 버전 번호입니다.<br><br>"미만" 또는 "이하"를 사용할 때, 주요 앱 버전이 존재하지 않으면 이 필터는 사용자가 해당 앱 버전보다 오래되었기 때문에 `true`를 반환합니다. 즉, 사용자의 마지막 주요 앱 버전이 존재하지 않으면 자동으로 필터와 일치합니다.<br><br>현재 앱 버전이 채워지는 데 시간이 걸릴 수 있습니다. 고객 프로필의 앱 버전은 SDK에 의해 정보가 캡처될 때 업데이트되며, 이는 사용자가 앱을 열 때에 의존합니다. 사용자가 앱을 열지 않으면 현재 버전이 업데이트되지 않습니다. 이러한 필터는 소급 적용되지도 않습니다. 현재 및 미래 버전에 대해 "초과" 또는 "같음"을 사용하는 것이 좋지만, 과거 버전 필터를 사용하면 예상치 못한 동작이 발생할 수 있습니다.
    tags:
      - App
  - name: Uninstalled
    display_name: "삭제됨"
    description: 사용자가 현재 백엔드에서 삭제된 것으로 표시되어 있는지 여부를 기준으로 세분화합니다. 앱을 삭제한 후 나중에 다시 설치한 사용자는 포함되지 않습니다. 이 필터는 현재 삭제 상태를 반영하며, 모든 삭제 이벤트의 이력 로그가 아닙니다.
    tags:
      - Uninstall
  - name: Device Carrier
    display_name: "기기 통신사"
    description: 기기 통신사를 기준으로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Device Count
    display_name: "기기 수"
    description: 사용자가 앱을 사용한 기기 수를 기준으로 세분화합니다.
    tags:
      - Devices
  - name: Device Model
    display_name: "기기 모델"
    description: 휴대폰의 모델 버전을 기준으로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Device OS
    display_name: "기기 OS"
    description: 지정된 운영체제를 가진 기기가 하나 이상인 사용자를 세분화합니다. 운영체제 범위로 사용자를 세분화하려면 <a href="/docs/user_guide/audience/segments/segmentation_filters#device-os-version-number">기기 OS 버전 번호</a> 필터를 사용하세요.
    tags:
      - Devices
  - name: Device OS Version Number
    display_name: "기기 OS 버전 번호"
    description: 지정된 범위 내의 운영체제 버전을 가진 기기가 하나 이상인 사용자를 세분화합니다. 예를 들어, iOS 운영체제 버전이 26.0 이상인 사용자를 타겟팅할 수 있습니다.
    tags:
      - Devices
  - name: Most Recent Device Locale
    display_name: "최근 기기 로캘"
    description: 가장 최근에 사용한 기기의 <a href="/docs/user_guide/messaging/messaging_fundamentals/localization">로캘 정보</a> 를 기준으로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Most Recent Watch Model
    display_name: "최근 워치 모델"
    description: 가장 최근의 스마트워치 모델을 기준으로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Provisionally Authorized on iOS
    display_name: "iOS에서 임시 승인됨"
    description: 특정 앱에 대해 iOS 12에서 임시로 승인된 사용자를 찾을 수 있습니다.
    tags:
      - Devices
  - name: Web Browser
    display_name: "웹 브라우저"
    description: 웹사이트에 접속하는 데 사용하는 웹 브라우저를 기준으로 사용자를 세분화합니다.
    tags:
      - Devices
  - name: Device IDFA
    display_name: "기기 IDFA"
    description: 테스트를 위해 IDFA로 Campaign 수신자를 지정할 수 있습니다.
    tags:
      - Advertising use cases
  - name: Device IDFV
    display_name: "기기 IDFV"
    description: 테스트를 위해 IDFV로 Campaign 수신자를 지정할 수 있습니다.
    tags:
      - Advertising use cases
  - name: Device Google Ad ID
    display_name: "기기 Google 광고 ID"
    description: Google 광고 ID를 기준으로 사용자를 세분화합니다.
    tags:
      - Advertising use cases
  - name: Device Roku Ad ID
    display_name: "기기 Roku 광고 ID"
    description: Roku 광고 ID를 기준으로 사용자를 세분화합니다.
    tags:
      - Advertising use cases
  - name: Device Windows Ad ID
    display_name: "기기 Windows 광고 ID"
    description: Windows 광고 ID를 기준으로 사용자를 세분화합니다.
    tags:
      - Advertising use cases
  - name: Ad Tracking Enabled
    display_name: "광고 추적 활성화됨"
    description: 사용자가 광고 추적에 옵트인했는지 여부를 기준으로 필터링할 수 있습니다. 광고 추적은 Apple이 모든 iOS 기기에 할당하는 IDFA 또는 "광고주용 식별자"와 관련이 있으며, SDK에서 설정할 수 있습니다. 이 식별자를 통해 광고주는 사용자를 추적하고 타겟 광고를 제공할 수 있습니다.
    tags:
      - Advertising use cases
  - name: Most Recent Location
    display_name: "최근 위치"
    description: 사용자가 앱을 사용한 마지막 기록 위치를 기준으로 세분화합니다.
    tags:
      - Location
  - name: Location Available
    display_name: "위치 사용 가능"
    description: 사용자가 위치를 보고했는지 여부를 기준으로 세분화합니다. 이 필터를 사용하려면 앱에 <a href="/docs/search/?query=location%20tracking">위치 추적이 통합</a> 되어 있어야 합니다.
    tags:
      - Location
  - name: Amplitude Cohorts
    display_name: "Amplitude 코호트"
    description: Amplitude를 사용하는 고객은 Amplitude에서 코호트를 선택하고 가져와 Segments를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Census Cohorts
    display_name: "Census 코호트"
    description: Census를 사용하는 고객은 Census에서 코호트를 선택하고 가져와 Segments를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Heap Cohorts
    display_name: "Heap 코호트"
    description: Heap을 사용하는 고객은 Heap에서 코호트를 선택하고 가져와 Segments를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Hightouch Cohorts
    display_name: "Hightouch 코호트"
    description: Hightouch를 사용하는 고객은 Hightouch에서 코호트를 선택하고 가져와 Segments를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Kubit Cohorts
    display_name: "Kubit 코호트"
    description: Kubit을 사용하는 고객은 Kubit에서 코호트를 선택하고 가져와 Segments를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Mixpanel Cohorts
    display_name: "Mixpanel 코호트"
    description: Mixpanel을 사용하는 고객은 Mixpanel에서 코호트를 선택하고 가져와 Segments를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Segment Cohorts
    display_name: "Segment 코호트"
    description: Segment를 사용하는 고객은 Segment에서 코호트를 선택하고 가져와 Segments를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Tinyclues Cohorts
    display_name: "Tinyclues 코호트"
    description: Tinyclues를 사용하는 고객은 Tinyclues에서 코호트를 선택하고 가져와 Segments를 보완할 수 있습니다.
    tags:
      - Cohort membership
  - name: Install Attribution Ad
    display_name: "설치 기여도 광고"
    description: 설치가 귀속된 광고를 기준으로 사용자를 세분화합니다.
    tags:
      - User Attributes
  - name: Install Attribution Adgroup
    display_name: "설치 기여도 광고 그룹"
    description: 설치가 귀속된 광고 그룹을 기준으로 사용자를 세분화합니다.
    tags:
      - Install attribution
  - name: Install Attribution Campaign
    display_name: "설치 기여도 Campaign"
    description: 설치가 귀속된 광고 Campaign을 기준으로 사용자를 세분화합니다.
    tags:
      - Install attribution
  - name: Install Attribution Source
    display_name: "설치 기여도 소스"
    description: 설치가 귀속된 소스를 기준으로 사용자를 세분화합니다.
    tags:
      - Install attribution
  - name: Churn Risk Category
    display_name: "이탈 위험 카테고리"
    description: 특정 예측에 따른 이탈 위험 카테고리를 기준으로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Churn Risk Score
    display_name: "이탈 위험 점수"
    description: 특정 예측에 따른 이탈 위험 점수를 기준으로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Category
    display_name: "이벤트 가능성 카테고리"
    description: 특정 예측에 따라 이벤트를 수행할 가능성을 기준으로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Event Likelihood Score
    display_name: "이벤트 가능성 점수"
    description: 특정 예측에 따라 이벤트를 수행할 가능성을 기준으로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Intelligent Channel
    display_name: "인텔리전트 채널"
    description: 최근 3개월 동안 가장 활발한 채널을 기준으로 사용자를 세분화합니다.
    tags:
      - Intelligence and predictive
  - name: Message Open Likelihood
    display_name: "메시지 열림 가능성"
    description: 지정된 채널에서 <a href="/docs/user_guide/brazeai/intelligence_suite/intelligent_channel#individual-channels">메시지를 열 가능성</a> 을 0-100 척도로 기준으로 사용자를 필터링합니다. 채널에 대한 가능성을 측정하기에 충분한 데이터가 없는 사용자는 "비어 있음"을 사용하여 선택할 수 있습니다.<br><br>이메일의 경우, 기계 열림은 가능성 계산에서 제외됩니다.
    tags:
      - Intelligence and predictive
  - name: Number of Facebook Friends Using App
    display_name: "앱을 사용하는 Facebook 친구 수"
    description: 동일한 앱을 사용하는 Facebook 친구 수를 기준으로 사용자를 세분화합니다.
    tags:
      - Social activity
  - name: Connected Facebook
    display_name: "Facebook 연결됨"
    description: 사용자가 앱을 Facebook에 연결했는지 여부를 기준으로 세분화합니다.
    tags:
      - Social activity
  - name: Connected Twitter
    display_name: "Twitter 연결됨"
    description: 사용자가 앱을 X(구 Twitter)에 연결했는지 여부를 기준으로 세분화합니다.
    tags:
      - Social activity
  - name: Number of Twitter Followers
    display_name: "Twitter 팔로워 수"
    description: X(구 Twitter) 팔로워 수를 기준으로 사용자를 세분화합니다.
    tags:
      - Social activity
  - name: Phone Number
    display_name: "전화번호"
    description: E.164 형식의 전화번호 필드를 기준으로 사용자를 세분화합니다.<br><br>전화번호가 Braze에 전송되면, Braze는 SMS, RCS 및 WhatsApp 채널을 통해 발송하는 데 사용되는 <a href="/docs/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#importing-phone-numbers">e.164 형식</a> 으로 변환을 시도합니다. 번호가 올바르게 형식화되지 않으면 변환 프로세스가 실패할 수 있으며, 이 경우 고객 프로필에 형식이 지정되지 않은 전화번호는 있지만 발송용 전화번호는 없게 됩니다. 이 Segment 필터는 e.164 형식의 전화번호(사용 가능한 경우)를 기준으로 사용자를 반환합니다.<br><br>사용 사례:<br> - SMS, RCS 또는 WhatsApp 메시지를 발송할 때 가장 정확한 타겟 오디언스 규모를 파악하려면 이 필터를 사용하세요. <br>- 이 필터와 함께 정규표현식(regex)을 사용하여 특정 국가 코드의 전화번호를 기준으로 세분화하세요. <br>- e.164 변환 프로세스에 실패한 전화번호를 기준으로 사용자를 세분화하려면 이 필터를 사용하세요.
    tags:
      - Other Filters
---