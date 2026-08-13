---
page_order: 10
nav_title: 알아두어야 할 용어
article_title: 알아두어야 할 Braze 용어

layout: glossary_page
glossary_top_header: "알아두어야 할 용어"
glossary_top_text: "이 용어들은 Braze와 함께 고객 및 사용자 관계를 개선하는 여정을 시작할 때 도움이 될 것입니다. 온보딩을 시작하기 전에 이 내용을 읽어보세요."
page_type: glossary
description: "이 용어집에서는 Braze 온보딩 과정을 진행하면서 알아야 할 중요한 용어에 대해 설명합니다."

glossaries:
  - name: Active user
    description: Campaign 타겟팅에서 Braze는 특정 기간 동안의 <a href="/docs/user_guide/messaging/campaigns/ideas_and_strategies/active_user_campaigns">활성 사용자</a> 를 해당 기간에 세션이 있는 모든 사용자로 정의합니다(API를 통해 업데이트된 사용자도 해당 기간에 포함됩니다). <a href="/docs/user_archival#active-users">사용자 아카이브</a> 및 도달 가능성 통계에서는 프로필 업데이트, 사용자에게 전송된 메시지, 메시지와의 상호작용도 포함하는 더 넓은 정의를 사용합니다.
    display_name: "활성 사용자"
  - name: Alloys
    description: Alloys는 Braze의 <a href="/docs/partners/home">기술 파트너</a> 입니다.
    display_name: "Alloys"
  - name: Anonymous users
    description: SDK를 통해 사용자 프로필이 인식되면 관련 <a href="/docs/api/basics#user-ids">Braze 사용자 ID</a> 와 함께 익명 사용자 프로필이 생성됩니다.
    display_name: "익명 사용자"
  - name: API campaigns
    description: <a href="/docs/api/api_campaigns">API 캠페인</a> 은 Braze 대시보드를 사용하여 <code>campaign_id</code>(및 변형 ID)를 생성하고, 카피, 오디언스, 스케줄, 자산은 <a href="/docs/api/endpoints/messaging">메시징 API</a> 를 통해 제공합니다. 이는 대시보드에서 완전히 구성된 캠페인을 API를 통해 트리거하는 <a href="/docs/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery">API 트리거 캠페인</a> 과 다릅니다.
    display_name: "API 캠페인"
  - name: Application program interface (API)
    description: <a href="/docs/api/basics">Braze API</a> 는 모바일 SDK를 통하지 않고 HTTP를 통해 사용자가 수행한 작업을 직접 기록할 수 있는 웹 서비스를 제공합니다. 예를 들어, 앱이나 웹사이트 내에서 추적되지 않는 사용자 데이터를 Braze에 전달할 수 있습니다.
    display_name: "애플리케이션 프로그램 인터페이스(API)"
  - name: App instance
    description: 앱 인스턴스는 워크스페이스에 수집된 다양한 사이트와 앱을 의미합니다.
    display_name: "앱 인스턴스"
  - name: Braze (the product)
    description: 대시보드라고도 하는 이 제품은 Braze 플랫폼의 핵심에 있는 모든 데이터와 상호작용을 제어합니다. Braze 고객은 알림을 관리하고, 타겟팅 메시징 캠페인을 설정하고, 분석을 확인하는 데 사용합니다. 개발자는 API 키 및 푸시 알림 자격 증명과 같은 앱 통합을 위한 설정을 관리하는 데 사용합니다.
    display_name: "Braze(제품)"
  - name: Team
    description: Braze 관리자는 대시보드 사용자의 하위 집합을 다양한 사용자 역할과 권한을 가진 <a href="/docs/user_guide/administer/global/user_management/teams">Teams</a> 로 나눌 수 있습니다. 이를 통해 Braze 관리자는 그룹 멤버십에 따라 특정 기능에 대한 액세스를 제한할 수 있습니다.
    display_name: "팀"
  - name: Campaign
    description: Campaign(캠페인)은 고객에게 개인화된 응답을 전달하기 위한 맞춤형 메시징 방법입니다. 다양한 메시징 채널을 사용하여 <a href="/docs/user_guide/messaging/campaigns">캠페인을 구축</a> 하고 고유한 메시지를 보낼 수 있습니다.
    display_name: "캠페인"
  - name: Canvas
    description: <a href="/docs/user_guide/messaging/canvas">Canvas</a> 는 마케터가 여러 메시지와 단계로 구성된 캠페인을 설정하여 일관된 여정을 구성할 수 있는 단일 통합 인터페이스입니다. Canvas를 사용하면 전체 사용자 경험에 대한 포괄적인 분석을 통해 이러한 경험을 비교하고 최적화할 수 있습니다.
    display_name: "Canvas"
  - name: Connected Content
    description: <a href="/docs/user_guide/messaging/design_and_edit/personalize/connected_content">Connected Content</a> 는 마케팅 개인화를 확장하여 고객 참여와 전환을 촉진합니다. API를 통해 액세스할 수 있는 모든 정보를 사용자에게 보내는 메시지에 직접 삽입할 수 있습니다. Connected Content를 사용하면 웹 서버 또는 공개적으로 액세스할 수 있는 API에서 직접 콘텐츠를 가져올 수 있습니다.
    display_name: "Connected Content"
  - name: Content Cards
    description: <a href="/docs/user_guide/channels/content_cards">Content Cards</a> 를 사용하면 고객의 경험을 방해하지 않으면서도 고객이 즐겨 사용하는 앱 내에서 바로 고도로 타겟팅된 풍부한 콘텐츠의 동적 스트림을 전송할 수 있습니다. Content Cards는 iOS, Android 및 웹 사용자에게 보낼 수 있습니다.
    display_name: "Content Cards"
  - name: Conversion event
    description: <a href="/docs/user_guide/messaging/messaging_fundamentals/conversion_events">전환 이벤트</a> 는 수신자가 메시지를 수신한 후(또는 Canvas나 대조군에 진입한 후, 채널 및 설정에 따라) 전환 기간 내에 높은 가치의 행동을 수행했는지 기록하는 성공 지표입니다. 전환 이벤트를 사용하여 단순 발송 이상의 Campaign 및 Canvas 성과를 측정할 수 있습니다.
    display_name: "전환 이벤트"
  - name: Currents
    description: 데이터 스트리밍 내보내기인 <a href="/docs/user_guide/data/distribution/braze_currents">Currents</a> 는 특정 Braze 패키지에 포함되어 있습니다. Braze 커런츠를 사용하면 플랫 파일을 사용하여 데이터 스토리지를 통해 통합하거나 지정된 엔드포인트에 일괄 처리된 JSON 페이로드를 사용하여 행동 분석 및 고객 데이터 파트너와 통합할 수 있습니다.
    display_name: "Currents"
  - name: Custom attributes
    description: <a href="/docs/user_guide/data/activation/attributes/custom_attributes">커스텀 속성</a> 은 사용자의 고유한 특성 모음입니다. 사용자에 대한 속성이나 애플리케이션 내에서 가치가 낮은 작업에 대한 정보를 저장하는 데 가장 적합합니다. 대시보드 내에서 사용자에게 커스텀 속성을 할당할 수 있습니다. <a href="/docs/developer_guide/analytics/setting_user_attributes?sdktab=swift">Swift</a> 및 <a href="/docs/developer_guide/analytics/setting_user_attributes?sdktab=android">Android</a> 캠페인 모두에서 이러한 속성에 따라 사용자를 필터링하고 세분화할 수 있습니다.
    display_name: "커스텀 속성"
  - name: Custom events
    description: <a href="/docs/user_guide/data/activation/events/custom_events">커스텀 이벤트</a> 는 사용자가 수행하는 작업으로, 애플리케이션과의 높은 가치의 사용자 상호작용을 추적하는 데 가장 적합합니다.
    display_name: "커스텀 이벤트"
  - name: Data point
    description: "데이터 포인트는 <a href=\"/docs/user_guide/data/activation/attributes/custom_attributes\">커스텀 속성</a> 이 설정되거나 업데이트될 때(동일한 값으로 업데이트하더라도), <a href=\"/docs/user_guide/data/activation/events/custom_events\">커스텀 이벤트</a> 또는 구매 이벤트가 기록될 때, 표준 데이터(예: <code>email</code>, <code>first_name</code>, <code>last_name</code>, <code>country</code>, <code>home_city</code>)가 기록될 때, 세션이 시작될 때, 세션이 종료될 때 카운트됩니다."
    display_name: "데이터 포인트"
  - name: Deep linking
    description: <a href="/docs/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls">딥링크</a> 는 고객을 다음 행동이나 참여로 안내하는 데 사용됩니다. 딥링크를 사용하면 메시지를 웹사이트 또는 모바일 앱 내의 타겟팅된 콘텐츠와 연결할 수 있습니다.
    display_name: "딥링킹"
  - name: Dormant users
    description: 사용자는 지난 12개월 동안 적격 활동이 없으면 <a href="/docs/user_archival#dormant-users">휴면</a> 상태로 간주됩니다. 워크스페이스 내 앱이나 웹사이트를 사용하지 않았고, 워크스페이스에서 메시지를 수신하지 않았으며, 12개월 이상 업데이트되지 않은 경우입니다. 기본적으로 Braze는 휴면 아카이브에 12개월 기간을 사용하며, 회사 설정에서 일수를 재정의할 수 있습니다.
    display_name: "휴면 사용자"
  - name: Endpoint
    description: API <a href="/docs/api/endpoints">엔드포인트</a> 라고도 하는 커뮤니케이션 채널의 끝은 메시지를 전송하고 예약하기 위해 Braze 메시징 API 내에서 사용됩니다.
    display_name: "엔드포인트"
  - name: Exception event
    description: Canvas에서 <a href="/docs/user_guide/messaging/canvas/create_a_canvas/exit_criteria#exception-events">예외 이벤트</a> 는 특정 행동이 발생했을 때(예&#58; 주문 완료) 사용자를 여정에서 제거하는 특정 작업입니다. 이를 통해 사용자가 목표를 완료한 후에도 후속 메시지의 관련성을 유지할 수 있습니다. 종료 기준이 어떻게 평가되고 시점이 결정되는지에 대해서는 <a href="/docs/user_guide/messaging/canvas/create_a_canvas/exit_criteria">종료 기준</a> 을 참조하세요.
    display_name: "예외 이벤트"
  - name: External ID
    description: "<code>external_id</code>는 Braze 사용자 프로필의 기본 사용자 식별자입니다. 자체 시스템에서 ID를 할당할 때 채널과 기기 전반에서 동일한 사람을 연결합니다. 익명 프로필은 사용자를 식별할 때까지 <code>external_id</code>가 없을 수 있습니다. 자세한 내용은 <a href=\"/docs/user_guide/get_started/users_and_segments\">사용자 및 Segments</a> 와 <a href=\"/docs/api/basics#user-ids\">사용자 ID</a> 를 참조하세요."
    display_name: "외부 ID"
  - name: Frequency capping
    description: <a href="/docs/user_guide/messaging/messaging_fundamentals/frequency_capping">최대 게재빈도 설정</a> 을 통해 오디언스를 압도하지 않으면서도 커뮤니케이션을 관리할 수 있습니다. 이는 사용자가 짧은 기간 내에 너무 많은 커뮤니케이션을 받지 않도록 메시지를 자동으로 제한하는 기능입니다.
    display_name: "최대 게재빈도 설정"
  - name: HIPAA
    description: HIPAA는 Health Insurance Portability and Accountability Act(건강보험 이동성 및 책임에 관한 법률)의 약자입니다. Braze는 <a href="/docs/developer_guide/disclosures/security_qualifications#hipaa">HIPAA를 준수합니다</a>. HIPAA 요건에는 관리적, 물리적, 기술적 보안이 포함됩니다.
    display_name: "HIPAA(미국의료정보보호법)"
  - name: In-app message
    description: <a href="/docs/user_guide/channels/in_app_messages">인앱 메시지</a> 는 애플리케이션 내에 표시되는 모바일 메시지입니다. 푸시 알림으로 사용자의 일과를 방해하지 않고 콘텐츠를 전달할 수 있습니다. 맞춤화된 인앱 메시지는 사용자 경험을 향상시키고 오디언스가 앱에서 최대한의 가치를 얻을 수 있도록 도와줍니다.
    display_name: "인앱 메시지"
  - name: Inactive users
    description: "사용자는 주요 메시징 채널(예: 이메일, SMS, 푸시, WhatsApp, LINE 등 구성에 따라)에서 도달할 수 없고, 워크스페이스 내 앱이나 웹사이트를 6개월 이상 사용하지 않았으며, 워크스페이스에서 6개월 이상 메시지를 수신하지 않았고, 6개월 이상 업데이트되지 않은 경우 <a href=\"/docs/user_archival#inactive-users\">비활성</a> 상태로 간주됩니다. 비활성 사용자는 휴면 사용자와 함께 아카이브 대상이 됩니다. 기본적으로 Braze는 비활성 아카이브에 6개월 기간을 사용하며, 회사 설정에서 일수를 재정의할 수 있습니다."
    display_name: "비활성 사용자"
  - name: IP warming
    description: <a href="/docs/user_guide/channels/email/email_setup/ip_warming">IP 워밍</a> 은 전용 IP에서 발송하는 메일 양을 점진적으로 늘리는 방법입니다. 이를 통해 인터넷 서비스 공급자와의 평판을 구축하여 메시지가 스팸으로 표시될 확률을 최소화할 수 있습니다.
    display_name: "IP 워밍"
  - name: Key-value pairs
    description: <a href="/docs/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs">키-값 페어</a> 는 키가 고유 식별자이고 값이 콘텐츠인 연결된 데이터 항목입니다. 사용자 기기에 추가 데이터 페이로드를 전송하는 데 사용할 수 있습니다.
    display_name: "키-값 페어"
  - name: Liquid
    description: Liquid는 Shopify에서 만들고 Ruby로 작성된 널리 사용되는 고객 대면 템플릿 언어입니다. <a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid">Liquid</a> 는 동적 콘텐츠를 로드하고 가져오는 데 사용됩니다. Liquid에서는 오브젝트, 태그 및 필터를 사용하여 <a href="/docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags">개인화 설정을 추가</a> 할 수 있습니다.
    display_name: "Liquid"
  - name: Messaging channel
    description: <a href="/docs/user_guide/channels">메시징 채널</a> 은 휴대폰이나 웹 브라우저의 푸시 알림, 이메일, 인앱 메시지 등을 통해 고객과 가상으로 소통할 수 있는 방법입니다!
    display_name: "메시징 채널"
  - name: Monthly active user (MAU)
    description: 지난 30일 이내에 세션이 있는 사용자입니다.
    display_name: "월간 활성 사용자(MAU)"
  - name: Multichannel messaging
    description: 이메일, 웹 푸시, 모바일 푸시 알림 등 다양한 매체를 통해 사용자에게 메시징을 전달합니다. <a href="/docs/developer_guide/getting_started/platform_overview#multichannel-messaging">메시징 채널</a> 은 이탈한 사용자를 다시 참여시키고, 활성 사용자를 유지하며, 브랜드 홍보대사에게 활력을 불어넣기 위해 정기적으로 함께 사용하는 것이 가장 좋습니다.
    display_name: "멀티 채널 메시징"
  - name: Multivariate testing
    description: <a href="/docs/user_guide/messaging/ab_testing">A/B 테스트</a> 는 소수의 메시지 버전을 비교하고, <a href="/docs/user_guide/messaging/ab_testing/create_tests">다변량 테스트</a> 는 여러 변수를 동시에 비교하여 어떤 조합이 가장 좋은 성과를 내는지 확인합니다. 지원되는 Campaign 유형에 대해 대시보드에서 두 가지 모두 구성할 수 있습니다.
    display_name: "다변량 테스트"
  - name: New user
    description: Braze는 신규 사용자를 앱을 새로 설치한 모든 사용자로 간주합니다. 또는 신규 사용자를 이전에 Braze 내에서 식별되지 않은 사용자 ID를 가진 사용자로 정의할 수도 있습니다.
    display_name: "신규 사용자"
  - name: Personalization
    description: 기술을 사용하여 각 사용자의 개별 선호도와 성향을 고려하여 소통합니다. <a href="/docs/user_guide/messaging/design_and_edit/personalize">개인화된 메시징</a> 은 고객의 선호도에 맞게 맞춤화하여 가치 있는 고객 경험을 구축하는 데 도움이 됩니다.
    display_name: "개인화"
  - name: Push message
    description: <a href="/docs/user_guide/channels/push">푸시 메시지</a> 또는 푸시 알림은 모바일 애플리케이션에서 표시되는 알림입니다. 푸시 알림은 iOS와 Android 모두에서 팝업 대화상자 및 배너로 표시되는 경우가 많습니다.
    display_name: "푸시 메시지"
  - name: Push token
    description: 푸시 토큰은 앱과 iOS, Android 또는 웹 기기 간의 연결을 생성하기 위해 Apple 또는 Google에서 생성 및 할당하는 고유 키입니다. <a href="/docs/api/objects_filters/user_attributes_object#migrate-push-tokens">푸시 토큰 마이그레이션</a> 은 이미 생성된 키를 Braze로 가져오는 것입니다.
    display_name: "푸시 토큰"
  - name: Push time to live (TTL)
    description: <a href="/docs/user_guide/administer/global/workspace_settings/push_settings">푸시 TTL</a> 이라고도 하는 유지 시간은 캠페인이 오프라인 사용자에게 계속 전달을 시도하는 기간을 의미합니다.
    display_name: "푸시 TTL"
  - name: Race condition
    description: <a href="/docs/user_guide/messaging/ab_testing/concepts/race_conditions">경합 조건</a> 은 시스템이 여러 작업을 동시에 수행하려고 할 때 발생하는 바람직하지 않은 상황을 설명하는 소프트웨어 엔지니어링 개념으로, 시스템의 특성상 작업이 올바른 순서로 수행되어야 올바르게 수행될 수 있습니다. <br><br>Braze 플랫폼에서 이벤트 발생 시점에 기록된 사용자 데이터로 트리거된 캠페인을 세분화하면 경합 조건이 발생할 수 있습니다. 이는 캠페인이 세분화되는 사용자 속성의 변경이 Segment 멤버십이 결정되고 캠페인이 전송되는 시점에 아직 처리되지 않아 사용자가 캠페인을 수신하지 못하는 경우에 발생합니다.
    display_name: "경합 조건"
  - name: Rate limiting
    description: "<a href=\"/docs/user_guide/messaging/messaging_fundamentals/frequency_capping\">사용량 제한</a> 은 메시지가 Braze에서 나가는 속도를 제어합니다(예: 분당 전달 속도 또는 Segment 필터를 사용한 사용자 중심 제한). 동일한 페이지에서 사용자가 일정 기간 내에 수신하는 메시지 수를 제한하는 최대 게재빈도 설정과 함께 작동합니다."
    display_name: "사용량 제한"
  - name: Segmentation
    description: 대시보드 <a href="/docs/user_guide/audience/segments">세분화</a> 를 사용하면 인앱 행동, 인구통계 데이터 등의 강력한 필터를 기반으로 사용자 그룹 또는 확장을 생성할 수 있습니다.
    display_name: "세분화"
  - name: Software development kit (SDK)
    description: <a href="/docs/developer_guide/getting_started/sdk_overview">SDK</a> 는 모바일 앱, 웹사이트 및 연결된 경험에 통합되며 마케팅, 메시징 및 분석 도구를 제공합니다. Braze는 <a href="/docs/developer_guide/sdk_integration?sdktab=swift">Swift</a> 및 <a href="/docs/developer_guide/sdk_integration?sdktab=android">Android</a> 등의 플랫폼에 대한 SDK 통합 가이드를 제공하며, 웹 및 기타 플랫폼은 SDK 개요에서 연결된 통합 경로를 따르세요.
    display_name: "소프트웨어 개발 키트(SDK)"
  - name: Subscription groups
    description: <a href="/docs/user_guide/channels/email/subscriptions#subscription-groups">구독 그룹</a> 은 글로벌 구독 상태 위에 계층화되어 세분화된 옵트인 선택(예&#58; 뉴스레터 대 프로모션)을 제공할 수 있습니다. SMS 및 WhatsApp과 같은 채널에도 유사한 패턴이 존재하며, 채널에서 요구하는 경우 항상 구독 그룹을 타겟팅하세요.
    display_name: "구독 그룹"
  - name: Sunsetting
    description: 서비스 종료란 참여하지 않는 사용자를 식별하고 해당 사용자가 아무런 조치를 취하지 않아도 해당 사용자에 대한 활성 메시징을 중단하는 프로세스를 말합니다. <a href="/docs/user_guide/channels/email/best_practices/sunset_policies">이메일</a> 및 <a href="/docs/user_guide/channels/push/best_practices#implement-a-sunset-policy-for-unresponsive-users">푸시</a> 메시지에 대한 서비스 종료 정책을 만들면 열람률에 미치는 영향을 억제하는 데 도움이 됩니다.
    display_name: "서비스 종료"
  - name: Tag
    description: <a href="/docs/user_guide/administer/global/workspace_settings/tags">태그</a> 는 하나 또는 여러 캠페인에 걸쳐 참여를 분류, 정리 및 정렬하는 데 도움이 되는 도구입니다.
    display_name: "태그"
  - name: User alias
    description: "<a href=\"/docs/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users#assigning-user-aliases\">사용자 별칭</a> 은 <code>external_id</code>가 존재하기 전에 익명 프로필에 할당할 수 있는 대체 식별자로, 사용자가 로그인할 때까지 기기나 채널 전반에서 동일한 사람을 참조할 수 있습니다."
    display_name: "사용자 별칭"
  - name: User archival
    description: <a href="/docs/user_archival">사용자 아카이브</a> 는 아카이브된 사용자를 의미합니다. Braze에서는 비활성 사용자와 휴면 사용자가 모두 여기에 포함됩니다. 아카이브는 Braze 서비스에서 비활성 및 휴면 규칙을 평가합니다(스케줄링, 사용자 수 임계값과 같은 워크스페이스 적격성, 회사 설정 또는 Canvas를 통한 기간 맞춤 설정 방법에 대해서는 사용자 아카이브를 참조하세요).
    display_name: "사용자 아카이브"
  - name: User profile
    description: <a href="/docs/user_guide/audience/manage_audience/user_profiles">사용자 프로필</a> 은 Braze에서 각 사람에 대한 중앙 기록으로, 식별자, 속성, 이벤트, 구매, 기기, 참여 이력 및 메시지 이력을 포함합니다. 프로필은 채널 전반에서 세분화, 개인화 및 규정 준수 워크플로를 지원합니다.
    display_name: "사용자 프로필"
  - name: Webhook
    description: <a href="/docs/user_guide/channels/webhooks">웹훅</a> 을 사용하면 SMS 문자 메시지 전송과 같은 앱 이외의 작업을 트리거할 수 있습니다. 웹훅을 사용하여 다른 시스템 및 애플리케이션에 실시간 정보를 제공할 수 있습니다. 이 기능의 유연성을 통해 모든 엔드포인트에 정보를 전송할 수 있습니다.
    display_name: "웹훅"
  - name: Workspace
    description: <a href="/docs/user_guide/get_started/workspaces">워크스페이스</a> 는 Braze가 데이터를 저장하고 팀이 Campaign, Canvases, Segments를 구축하는 컨테이너입니다. 각 워크스페이스에는 하나 이상의 <a href="/docs/user_guide/get_started/workspaces#understanding-workspaces">앱 인스턴스</a>(해당 워크스페이스로 데이터를 전송하는 개별 앱 및 사이트)가 포함됩니다.
    display_name: "워크스페이스"

---