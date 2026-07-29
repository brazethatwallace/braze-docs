---
nav_title: 홈
article_title: Braze의 새로운 기능
description: "Braze 릴리스 노트는 매월 게시되어 주요 제품 릴리스, 지속적인 제품 개선, Braze 파트너십, SDK 주요 변경 사항 및 기능 지원 중단에 대한 최신 정보를 확인할 수 있습니다."
page_order: 0
search_rank: 1
page_type: reference

---

# Braze의 새로운 기능 {#whats-new-in-braze}

{% alert tip %}
이 페이지에 나열된 업데이트에 대한 자세한 내용은 계정 매니저에게 문의하거나 [지원 티켓을 개설하세요]({{site.baseurl}}/user_guide/administer/personal/braze_support). 월간 SDK 릴리스, 개선 사항 및 주요 변경 사항에 대한 자세한 내용은 [SDK 체인지로그]({{site.baseurl}}/developer_guide/changelogs)에서 확인할 수 있습니다.
{% endalert %}

{% details 2026년 7월 23일 %}

## 2026년 7월 23일 릴리스 {#july-23-2026-release}

### 데이터 및 보고 {#data-reporting}

#### 메시징 진단 대시보드 {#messaging-diagnostics-dashboard}

{% multi_lang_include release_type.md release="General availability" %}

[메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)는 메시지 전송 결과에 대한 상위 수준 분석을 제공하여 메시징 설정의 트렌드를 파악하고 잠재적 문제를 진단할 수 있게 해줍니다. 이 대시보드는 Campaigns이나 Canvases의 메시지가 예상대로 전송되지 않은 이유를 이해하는 데 도움이 됩니다. 이 기능에 대한 액세스는 고객 성공 매니저에게 문의하세요.

#### CSV 커스텀 이벤트 매퍼 {#csv-custom-events-mapper}

{% multi_lang_include release_type.md release="General availability" %}

커스텀 이벤트를 위한 [CSV 가져오기 플로우]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#about-csv-import)에 이제 가져오기 전에 이벤트 이름과 이벤트 속성정보 헤더를 Braze 필드에 매핑할 수 있는 매퍼가 포함되었습니다. 이 업데이트는 커스텀 이벤트 경험을 커스텀 속성 플로우와 일치시키고 업로드 전 파일 재포맷의 필요성을 줄여줍니다. 이 플로우에는 CSV 업로드, 필수 필드 및 이벤트 매핑, 이벤트 속성정보 매핑, 가져오기 전 타겟팅 환경설정 선택이 포함됩니다. 파일이 이미 예상 형식과 일치하는 경우 매핑 변경 없이 플로우를 계속 진행할 수 있습니다.

#### 카탈로그 무료 스토리지가 이제 최대 500MB 지원 {#catalogs-free-storage-now-supports-up-to-500-mb}

{% multi_lang_include release_type.md release="General availability" %}

[카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers)의 무료 버전은 이제 모든 CSV 파일에 걸쳐 최대 500MB의 스토리지를 지원합니다.

### BrazeAI<sup>TM</sup>

#### Operator가 이제 설정 페이지를 직접 업데이트 가능 {#operator-can-now-update-settings-pages-for-you}

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities)가 이제 더 많은 설정 페이지에서 직접 변경할 수 있으므로 구성 화면을 클릭하는 대신 자연어로 변경 사항을 설명할 수 있습니다. 지원되는 페이지는 다음과 같습니다:

- 방해금지 시간
- 푸시 설정
- 메시징 사용량 제한
- 메시징 규칙 및 상시 승인 워크플로우
- 기타 식별자 및 API 제한
- 연락처 정보

예를 들어, 방해금지 시간 페이지에서 Operator에게 SMS에 대해 오후 9시부터 오전 8시까지 방해금지 시간을 설정하도록 요청할 수 있습니다.

#### 원격 Braze MCP 서버 {#remote-braze-mcp-server}

{% multi_lang_include release_type.md release="Early access" %}

[Braze MCP 서버]({{site.baseurl}}/user_guide/brazeai/mcp_server)는 Claude, ChatGPT, Cursor, VSCode, Codex, Google Antigravity, Claude Code와 같은 AI 에이전트를 Braze에 직접 연결할 수 있는 원격 호스팅 연결입니다. 자연어를 통해 에이전트는 Campaign, Canvas, Segment 분석, 커스텀 속성, 이벤트, KPI, 카탈로그를 읽고, 이메일 템플릿, Content Blocks, 미디어 라이브러리 자산을 생성하거나 업데이트할 수 있습니다. 사용자 프로필 PII는 노출되지 않습니다.

연결하려면 MCP 클라이언트에 단일 엔드포인트 URL을 붙여넣으세요. US의 경우 `https://mcp.braze.com/mcp`, EU의 경우 `https://mcp.braze.eu/mcp`입니다. 그런 다음 SSO를 포함한 OAuth로 로그인하면 서버가 사용 가능한 도구와 함께 시작됩니다.

### 오케스트레이션 {#orchestration}

#### 팀 오디언스 범위 지정 {#teams-audience-scoping}

{% multi_lang_include release_type.md release="General availability" %}

[팀]({{site.baseurl}}/user_guide/administer/global/user_management/teams) 오디언스 구성이 이제 여러 필터를 지원합니다.

### 채널 및 터치포인트 {#channels-touchpoints}

#### 인앱 메시지 및 랜딩 페이지를 위한 설문조사 평점 척도 {#survey-rating-scale-for-in-app-messages-and-landing-pages}

{% multi_lang_include release_type.md release="Early access" %}

[랜딩 페이지 설문조사]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale)와 [인앱 메시지 설문조사]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) 모두의 양식 블록에 숫자 평점 척도를 추가하여 커스텀 코드 없이 감정, 만족도, 추천 가능성을 캡처할 수 있습니다. 1~10, 1~5, 0~10(표준 NPS 범위)의 세 가지 범위가 지원됩니다.

#### WhatsApp 한정 시간 오퍼 템플릿 {#whatsapp-limited-time-offer-templates}

{% multi_lang_include release_type.md release="General availability" %}

[WhatsApp 한정 시간 오퍼 템플릿]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates)은 오퍼 만료가 가까워지면 선택적 카운트다운과 함께 시간 제한 프로모션 오퍼를 표시합니다. 시즌 세일이나 사용자 속성에 맞게 개인화된 오퍼와 같은 시간 제한 프로모션에 이 레이아웃을 사용하세요.

#### Shopify 셀프 서비스 SDK 버전 업그레이드 {#shopify-self-serve-sdk-version-upgrade}

{% multi_lang_include release_type.md release="General availability" %}

새로운 [Shopify]({{site.baseurl}}/partners/ecommerce/shopify) 고객은 설정 중에 최신 Braze Web SDK 및 JavaScript SDK 버전으로 프로비저닝됩니다. 기존 고객은 통합 설정에서 현재 SDK 버전을 확인하고, 새 버전이 사용 가능할 때 알림을 받으며, 통합 설정에서 셀프 서비스 업그레이드를 수행할 수 있습니다.

#### 배너용 HTML 편집기 {#html-editor-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

배너를 작성할 때 이제 [HTML 편집기를 사용하여]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner) 빌드할 수 있습니다. HTML 편집기는 이미 자체 HTML 템플릿을 유지하고 있거나 배너의 마크업과 스타일링을 완전히 제어하려는 팀에 가장 적합합니다. 편집기에 커스텀 HTML을 직접 작성하거나 붙여넣을 수 있습니다.

#### 미디어 라이브러리에서 파일 교체 {#replace-a-file-in-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

이제 URL과 자산 ID를 안정적으로 유지하면서 [기존 미디어 라이브러리 자산의 파일을 교체]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file)할 수 있습니다. URL이 변경되지 않으므로 해당 자산을 참조하는 모든 Campaign, Canvas, Content Block 또는 템플릿이 자동으로 업데이트된 파일을 반영하여 사용되는 모든 곳에서 수동으로 다시 업로드하거나 다시 연결할 필요가 없습니다.

#### 미디어 라이브러리의 그리드 뷰 {#grid-view-for-the-media-library}

{% multi_lang_include release_type.md release="General availability" %}

미디어 라이브러리와 일부 템플릿 라이브러리에서 이제 기존 목록 뷰와 함께 그리드 뷰를 제공합니다. 그리드 뷰는 자산을 주요 메타데이터(이름, 유형, 최종 수정일)와 함께 썸네일로 표시하여 파일 이름 대신 시각적으로 이미지와 크리에이티브를 더 빠르게 찾을 수 있습니다. 필터링과 검색은 두 뷰 모두에서 동일하게 작동합니다.

#### 더 많은 채널을 위한 공유 가능한 미리보기 지원 {#shareable-preview-support-for-more-channels}

{% multi_lang_include release_type.md release="General availability" %}

[공유 가능한 미리보기]({{site.baseurl}}/user_guide/channels/email/html_editor#step-3b-preview-and-test-your-message)가 이제 다음 추가 채널을 지원합니다:

- SMS, MMS, RCS
- WhatsApp
- 푸시
- Content Cards
- LINE

Campaign이나 메시지에서 링크를 생성하여 Braze 대시보드 액세스 권한이 없는 검토자(브랜드, 법무, 외부 에이전시 등)와 공유할 수 있습니다. 수신자는 모든 브라우저에서 링크를 열어 테스트 개인화를 포함하여 고객이 보는 것처럼 렌더링된 메시지를 볼 수 있습니다.

#### 푸시 자격 증명 업데이트 API {#push-credentials-update-api}

{% multi_lang_include release_type.md release="General availability" %}

이제 [푸시 자격 증명 업데이트 엔드포인트]({{site.baseurl}}/api/endpoints/apps/post_update_push_credential)를 사용하여 프로그래밍 방식으로 푸시 자격 증명을 업데이트할 수 있습니다. 각 요청은 하나의 앱과 하나의 플랫폼(`apple`, `firebase`, `huawei` 또는 `kindle`)을 업데이트하며 자격 증명 페이로드를 Base64 인코딩 값으로 수락합니다. 이를 통해 수동 대시보드 업로드에 의존하지 않고 대규모 앱 포트폴리오와 자격 증명 교체 정책을 관리할 수 있습니다.

### 파트너십 {#partnerships}

#### Refiner - 설문조사 {#refiner-surveys}

[Refiner](https://refiner.io)는 SaaS 및 모바일 앱을 위한 인앱 설문조사 플랫폼입니다. 제품 및 고객의 소리 팀이 타겟팅된 인앱 설문조사를 출시하고 NPS, CSAT, CES, 제품 피드백, 제로파티 사용자 데이터를 지속적으로 수집할 수 있습니다.

#### Stayfilm - 시각적 및 인터랙티브 콘텐츠 {#stayfilm-visual-and-interactive-content}

[Stayfilm](https://www.stayfilm.com/)은 대규모 자동화된 개인화 비디오 제작을 위한 REST API입니다. 이 플랫폼은 데이터, 이미지, 텍스트, 사운드트랙, 내레이션, 시각 효과를 통합하여 이커머스, 마켓플레이스, CRM 워크플로우, 마케팅 캠페인을 위한 맞춤형 비디오 콘텐츠를 생성합니다.

#### Validity - 데이터 및 분석 {#validity-data-and-analytics}

[Validity Everest](https://www.validity.com/everest/)는 받은편지함 배치를 측정하고 전송 평판을 보호하는 데 도움이 되는 이메일 전달 가능성 플랫폼입니다. Braze와 Validity 통합은 Everest 시드 목록을 Braze에 동기화하고, 적격 Campaigns과 Canvases에 자동으로 시드를 추가하며, 인게이지먼트 측정기준을 Validity Inbox로 다시 가져와 시드 기반 배치와 실제 구독자 인게이지먼트를 비교할 수 있습니다.

### SDK

다음 SDK 업데이트가 릴리스되었습니다. 자세한 내용은 [SDK 체인지로그]({{site.baseurl}}/developer_guide/changelogs)를 참조하세요.

#### SDK 주요 업데이트 {#sdk-breaking-updates}

최신 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 SDK 업데이트 섹션에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그에서 확인할 수 있습니다.

- [Android SDK 43.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v43.0.0)
    - `unregisterPush` 및 로그아웃 메서드를 추가합니다.
    - 이커머스 이벤트에 추가 필드를 추가합니다.
    - 푸시 알림 이미지 로딩에 지수 백오프를 추가합니다.
- [Swift SDK 17.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - 이커머스 이벤트에 추가 필드를 추가합니다.
    - 초기화 후 데이터 상태를 예측 가능하게 만듭니다.
    - 기기 및 사용자 식별자에 대한 비차단 접근자를 추가합니다.
    - `Braze.LiveActivities`에서 더 이상 사용되지 않는 push-to-start 업데이트 API를 제거합니다.
- [Web SDK 6.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - `unregisterPush` 및 로그아웃 메서드를 추가합니다.
    - 이커머스 이벤트에 추가 필드를 추가합니다.
    - 시작 시 중복 새로고침과 관련된 배너 및 Content Cards 문제를 수정합니다.
    - 배너 해제를 위한 공개 메서드를 추가합니다.
- [Flutter SDK 21.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/v21.0.0)
    - 네이티브 iOS 브리지를 업데이트합니다.
    - 더 이상 사용되지 않는 메서드를 제거합니다.
    - `changeUser`, `enableSDK`, `disableSDK` 핸들러를 완료 결과를 반환하도록 업데이트합니다.
- [Expo SDK 5.2.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/v5.2.0)
    - 샘플 앱을 Expo SDK 56으로 업데이트합니다.
- [React Native SDK 22.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/22.0.0)
    - 배너 해제 지원을 추가합니다.
    - 바인딩 업데이트를 포함합니다.

{% enddetails %}
{% details 2026년 6월 25일 %}

## 2026년 6월 25일 릴리스 {#june-25-2026-release}

### 데이터 및 보고

#### Content Cards 및 배너의 측정기준 이름 업데이트 {#metric-name-update-for-content-cards-and-banners}

Content Cards 및 배너의 _고유 수신자_ 측정기준이 _일일 고유 노출 횟수_로 이름이 변경되었습니다. _일일 고유 노출 횟수_는 Braze에서 수신한 수를 나타내며 `user_id`를 기반으로 합니다. 일일 고유 노출 횟수는 Campaign 또는 캔버스 단계 수준에서 집계됩니다. 자세한 내용은 [측정기준 용어집]({{site.baseurl}}/user_guide/analytics/metrics_glossary)을 참조하세요.

#### 사용자 삭제 {#user-deletion}

{% multi_lang_include release_type.md release="General availability" %}

[사용자 삭제]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)를 사용하면 더 이상 필요하지 않거나, 오류로 생성되었거나, 규정 준수(GDPR 또는 CCPA 등)를 위해 삭제해야 하는 프로필을 제거하여 데이터베이스를 관리할 수 있습니다.

#### 데이터 포인트 제외 {#data-point-exclusions}

{% multi_lang_include release_type.md release="General availability" %}

[이커머스 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)는 더 이상 청구 가능한 데이터 포인트에 포함되지 않습니다. 데이터 포인트 소비 없이 Braze 이커머스 이벤트(`ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`)를 도입할 수 있습니다.

#### 이벤트 기록 탭 {#event-history-tab}

{% multi_lang_include release_type.md release="General availability" %}

[고객 프로필]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)의 **이벤트 기록** 탭에는 최근 30일간의 사용자 커스텀 이벤트 및 구매 내역이 나열됩니다(최대 100개의 최근 항목). SDK 또는 API 통합이 예상대로 이벤트를 전송하고 있는지 확인하거나, 사용자가 이벤트 트리거 Campaign 또는 Canvas에 진입한(또는 진입하지 않은) 이유를 디버깅하거나, 특정 사용자에 대한 지원 에스컬레이션을 조사하는 데 사용할 수 있습니다.

#### 전달 가능성 센터에서 Amazon SES 고객을 위한 Microsoft SNDS 데이터 표시 {#deliverability-center-surfaces-microsoft-snds-data-for-amazon-ses-customers}

Amazon SES를 통해 이메일을 전송하는 워크스페이스의 경우, [전달 가능성 센터]({{site.baseurl}}/deliverability_center)에서 전용 전송 IP에 대한 Microsoft SNDS 측정기준을 표시합니다. 이 기능이 워크스페이스에 활성화되면 Braze는 최대 90일간의 과거 SNDS 데이터를 백필합니다.

### BrazeAI<sup>TM</sup>

#### Operator에서 통합된 BrazeAI 어시스턴트 {#unified-brazeai-assistants-in-operator}

대시보드 전반에 있던 독립형 BrazeAI 어시스턴트가 [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)로 통합되어, Operator가 대시보드 전반에서 마케터 대상 생성형 AI 지원을 위한 단일 AI 어시스턴트로 자리잡았습니다. 다음 어시스턴트가 이제 Operator를 통해 라우팅됩니다:

{% multi_lang_include releases/brazeai_operator_legacy_assistants.md %}

기존 진입점은 각 레거시 어시스턴트 버튼이 있던 위치에 그대로 유지됩니다. 독립형 어시스턴트를 여는 대신, 이러한 진입점은 이제 작업에 맞게 사전 범위가 지정된 동적 프롬프트와 함께 Operator 패널을 엽니다. 이러한 진입점은 기존 워크플로우를 조정하지 않고도 이러한 기능을 사용할 수 있도록 Operator로의 직접 경로를 제공합니다.

#### Campaign 생성 및 편집을 위한 Operator 지원 {#operator-support-for-campaign-creation-and-editing}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator)는 이제 메시지 작성뿐만 아니라 전체 Campaign을 생성하고 편집할 수 있습니다. 단일 자연어 프롬프트 또는 Campaign 브리프에서 Operator는 메시지 작성, 전달 예약, 오디언스 타겟팅, 전환 이벤트 할당 등 검토 준비가 된 Campaign을 처음부터 끝까지 구축한 다음 검토 단계에서 구축한 내용을 요약합니다. 이전에는 Operator가 메시지 작성(Campaign 생성 5단계 중 하나)만 할 수 있었지만, 이제 나머지 예약, 타겟, 할당 및 검토 단계에 대한 가시성과 제어 권한을 갖게 되었습니다.

이 기능은 **Campaigns** 페이지 또는 기존 Campaign 내에서 사용할 수 있습니다. 결과적으로 Operator는 다음을 수행할 수 있습니다:

{% multi_lang_include releases/brazeai_operator_campaign_creation_prompts.md %}

#### Content Blocks를 위한 Operator 지원 {#operator-support-for-content-blocks}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator)는 이제 자연어 프롬프트에서 직접 [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)—한 번 구축하고 여러 메시지에서 참조하는 재사용 가능한 스니펫—를 생성하고 편집할 수 있습니다. **Content Blocks** 페이지에서 Operator에게 처음부터 새 Content Block을 생성하거나 기존 것을 편집하도록 요청하면 Operator가 검토할 콘텐츠를 생성하거나 업데이트합니다.

#### Operator로 구축된 에이전트 콘솔 템플릿 {#agent-console-templates-built-with-operator}

**에이전트 콘솔**에서 에이전트를 구축할 때 커스텀 에이전트를 생성하거나 **Operator로 에이전트 생성**에서 옵션을 선택하여 BrazeAI Operator를 사용하여 시작 템플릿을 적용할 수 있습니다. Operator는 다음 에이전트 콘솔 시작 템플릿에 대한 지침, 출력 필드 및 컨텍스트를 사전 구성할 수 있습니다.

자세한 내용은 [커스텀 에이전트 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)을 참조하세요.

#### 에이전트 콘솔 개선 사항 {#agent-console-enhancements}

[에이전트 콘솔]({{site.baseurl}}/user_guide/brazeai/agents)에서 다음을 수행할 수 있습니다:

{% multi_lang_include releases/brazeai_agent_console_enhancements.md %}

#### 출시된 콘텐츠 최적화 프로그램 단계 편집 {#edit-a-launched-content-optimizer-step}

{% multi_lang_include release_type.md release="Beta" %}

Canvas가 출시된 후 이제 [콘텐츠 최적화 프로그램 단계를 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step#edit-a-launched-step)하여 다음을 수행할 수 있습니다:

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

### 채널 및 터치포인트

#### 배너의 사용자 해제 {#user-dismissals-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

해제 동작을 구성할 때 **배너를 해제할 수 있음**을 선택하여 사용자가 배너를 수동으로 해제할 수 있도록 허용할 수 있습니다. 이 옵션은 모든 앱 사용자에게 한정 세일을 홍보하되 관심이 없는 경우 메시지를 해제할 수 있도록 하려는 시나리오에서 유용합니다.

해제 활성화 및 해제 버튼 커스터마이징에 대한 자세한 내용은 [해제 동작 구성]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#dismiss-behavior)을 참조하세요.

#### 배너의 커스텀 클릭 추적 {#custom-click-tracking-for-banners}

{% multi_lang_include release_type.md release="General availability" %}

배너에 대한 더 세분화된 클릭 추적을 위해 속성 패널의 **보고용 식별자** 필드를 사용하여 각 인터랙티브 요소에 [커스텀 식별자를 할당]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#step-32-define-on-click-behavior-optional)할 수 있습니다.

#### 배너의 재자격 {#re-eligibility-for-banners}

배너 Campaign에 재자격이 활성화되면 배너를 해제한 사용자는 해제 시점부터 시작되는 구성 가능한 쿨다운 기간 후에 다시 자격을 얻을 수 있습니다. 재자격이 활성화되지 않은 경우 해제한 사용자는 자격이 없는 상태로 유지됩니다. 재자격을 구성하려면 [재자격 구성]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#re-eligibility)을 참조하세요. Canvas 배너 단계는 대신 Canvas 재진입 설정을 사용합니다.

#### Quick Push A/B 테스트 {#quick-push-ab-testing}

{% multi_lang_include release_type.md release="General availability" %}

Quick Push A/B 테스트는 이제 배리언트 그룹을 통해 멀티 플랫폼 푸시 Campaign 및 캔버스 단계를 지원하므로 하나의 워크플로우에서 정렬된 iOS 및 Android 메시지 배리언트를 테스트할 수 있습니다. 자세한 내용은 [멀티 플랫폼 푸시 메시지]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push#use-cases)를 참조하세요.

#### BrazeAI<sup>TM</sup> 배리언트 선택 {#brazeai-variant-selection}

{% multi_lang_include release_type.md release="Early access" %}

BrazeAI<sup>TM</sup> 배리언트 선택은 여러 푸시 배리언트를 추가할 때 자동으로 활성화되며, 추천 실험 기본값을 적용하고, 인게이지먼트를 개선하기 위해 가장 성과가 좋은 배리언트로 최적화합니다. 즉시 전송해야 하는 경우 끌 수 있습니다. 자세한 내용은 [BrazeAI<sup>TM</sup> 배리언트 선택]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection)을 참조하세요.

#### WhatsApp 테스트 전송 결과 {#whatsapp-test-send-results}

테스트 WhatsApp 메시지를 전송한 후 메시지 작성기에서 직접 [상세 전달 보고서]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message#step-4-view-test-send-results)를 볼 수 있습니다. 이를 통해 메시지가 의도한 수신자에게 도달했는지 확인하고 출시 전에 실패를 문제 해결할 수 있습니다.

### 파트너십

#### Convercus - 데이터 및 분석 - 로열티 {#convercus-data-and-analytics-loyalty}

[Convercus]({{site.baseurl}}/partners/data_and_analytics/loyalty/convercus)는 브랜드와 소매업체가 옴니채널 로열티 프로그램과 개인화된 쿠폰 캠페인을 통해 고객 빈도, 장바구니 가치 및 재구매율을 높일 수 있도록 돕는 SaaS 로열티 및 쿠폰 플랫폼입니다.

#### Copy Pastd - 메시지 오케스트레이션 - 템플릿 {#copy-pastd-message-orchestration-templates}

[Copy Pastd]({{site.baseurl}}/partners/copy_pastd) Building Blocks는 Liquid 기반 Content Blocks와 전체 템플릿을 Braze 워크스페이스에 직접 푸시하는 드래그 앤 드롭 이메일 빌더입니다. 한 번 디자인하고 Braze에 동기화한 다음 매번 HTML을 다시 빌드하지 않고도 Campaigns, Canvases 및 트리거 플로우에서 동일한 구성요소를 재사용할 수 있습니다.

#### Databricks Mosaic - AI 모델 제공업체 {#databricks-mosaic-ai-model-providers}

[Databricks Mosaic]({{site.baseurl}}/partners/databricks_mosaic)은 Databricks Data Intelligence Platform에서 AI 및 머신 러닝 모델을 대규모로 구축, 배포 및 관리하기 위한 Databricks의 통합 플랫폼입니다.

#### DinMo - 데이터 및 분석 - 리버스 ETL {#dinmo-data-and-analytics-reverse-etl}

[DinMo]({{site.baseurl}}/partners/dinmo)는 리버스 ETL을 통해 클라우드 데이터 웨어하우스를 Braze에 연결하는 구성 가능한 고객 데이터 플랫폼(CDP)입니다. 마케팅 팀은 웨어하우스 데이터에서 오디언스 세그먼트를 구축하고, 사용자 속성 및 이벤트를 Braze에 동기화하며, CSV 업로드나 엔지니어링 지원 없이 구독 상태를 최신으로 유지할 수 있습니다.

#### EmailShepherd - 메시지 오케스트레이션 - 템플릿 {#emailshepherd-message-orchestration-templates}

[EmailShepherd]({{site.baseurl}}/partners/emailshepherd)는 이메일 디자인 시스템을 기반으로 구축된 에이전트 기반 이메일 제작 플랫폼으로, 전체 마케팅 팀과 AI 에이전트가 병목 현상 없이 브랜드에 맞는 프로덕션 준비 이메일을 제작할 수 있도록 합니다. Braze 통합은 승인된 이메일을 Braze 워크스페이스에 직접 게시하므로 마케터가 브랜드 일관성을 희생하지 않고 Braze에서 이메일 제작을 확장할 수 있습니다.

#### Talkable - 메시지 개인화 - 추천 {#talkable-message-personalization-referrals}

[Talkable]({{site.baseurl}}/partners/talkable)은 소비자 브랜드가 만족한 고객을 확장 가능한 추천 채널로 전환하는 데 도움을 줍니다. Braze 통합을 통해 Talkable 추천 캠페인에서 캡처된 마케팅 이메일 옵트인이 실시간으로 Braze에 유입되어 팀이 모든 새로운 옹호자와 친구를 환영하고, 세분화하고, 참여시키는 데 필요한 동의, 컨텍스트 및 캠페인 데이터를 제공합니다.

### SDK

#### SDK 주요 업데이트

최신 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 SDK 업데이트 섹션에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그에서 확인할 수 있습니다.

{% multi_lang_include releases/sdk/2026_6_25_26_updates.md %}

{% enddetails %}

{% details 2026년 5월 28일 %}

## 2026년 5월 28일 릴리스 {#may-28-2026-release}

### 데이터 및 보고

#### 푸시 성과 대시보드 {#push-performance-dashboard}

[푸시 성과 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard)는 구성 가능한 시간 범위에 걸쳐 전송, 반송, 전달, 직접/영향/총 열람률을 포함한 푸시 인게이지먼트에 대한 단일 채널 수준 뷰를 제공합니다. 개별 Campaigns이나 Canvases의 데이터를 집계하지 않고도 푸시 채널의 전반적인 상태를 파악하는 데 사용할 수 있습니다.

#### 카탈로그 선택에서의 지리 위치 필드 {#geolocation-fields-in-catalog-selections}

{% multi_lang_include release_type.md release="General availability" %}

카탈로그는 이제 새로운 지리 위치 필드 유형과 카탈로그 선택 연산자를 사용한 거리 기반 필터링을 지원합니다. 이를 통해 각 사용자에게 가장 가까운 레스토랑을 표시하거나, 부동산 캠페인을 위해 50km 이내의 매물을 필터링하거나, 특정 이벤트 근처의 매장을 타겟팅하는 등 더 관련성 높은 위치 인식 경험을 만들 수 있습니다. 도시 또는 지역 코드로 지리적 타겟팅을 근사하는 대신, 사용자의 가장 최근 위치와 같은 Liquid 사용자 속성을 포함하여 중심점에 대한 근접성으로 카탈로그 항목을 필터링할 수 있습니다. 자세한 내용은 [선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 참조하세요.

#### 보고서 빌더에 배너 및 RCS 추가 {#banner-and-rcs-for-report-builder}

[보고서 빌더]({{site.baseurl}}/report_builder)는 배너를 채널로, RCS를 SMS의 하위 카테고리로 지원하므로 다른 모든 Braze 채널과 함께 커스텀 보고서에서 두 가지 모두의 성과를 직접 측정할 수 있습니다.

#### `ecommerce.cart_updated` 이벤트 액션 {#ecommercecart_updated-event-actions}

[`ecommerce.cart_updated` 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples)는 `replace`와 함께 `add` 및 `remove` 액션을 지원하여 매번 업데이트할 때마다 전체 장바구니 스냅샷 대신 증분 장바구니 변경 사항을 전송할 수 있습니다.

### BrazeAI<sup>TM</sup>

#### SMS, MMS 및 RCS 메시지를 위한 콘텐츠 최적화 프로그램 {#content-optimizer-for-sms-mms-and-rcs-messages}

{% multi_lang_include release_type.md release="Beta" %}

[콘텐츠 최적화 프로그램]({{site.baseurl}}/user_guide/brazeai/content_optimizer)을 사용하여 SMS, MMS 및 RCS 메시지의 훅, 본문 및 CTA를 최적화할 수 있습니다. 콘텐츠 최적화 프로그램은 AI를 사용하여 대량의 콘텐츠 배리언트를 자동으로 생성하고 평가하여 메시지 콘텐츠를 대규모로 테스트하고 최적화하는 데 도움이 됩니다.

### 오케스트레이션

#### 워크스페이스 시간대 {#workspace-time-zones}

{% multi_lang_include release_type.md release="General availability" %}

[워크스페이스 시간대]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone)를 사용하여 개별 워크스페이스에 대한 특정 시간대를 정의할 수 있습니다. 이를 통해 예약된 Campaigns과 Canvases(현지 시간 또는 Intelligent Timing을 사용하지 않는 경우)가 전체 회사 시간대가 아닌 워크스페이스의 지정된 시간대에 따라 전송됩니다.

메시지 전송을 위한 워크스페이스 시간대는 점진적으로 출시되고 있으므로 대시보드에서 아직 이러한 설정이 표시되지 않을 수 있습니다.

### 채널 및 터치포인트

#### WhatsApp `inbound_profile_name`

Meta의 인바운드 메시징 웹훅에서 사용자의 WhatsApp 표시 이름을 자동으로 캡처하여 사용자의 Braze 프로필에 기록할 수 있습니다. 인바운드 WhatsApp 메시지가 수신되면 Braze는 프로필 이름을 새로운 WhatsApp Liquid 속성인 [{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)으로 노출하며, 이를 Canvas 사용자 업데이트 단계에서 참조하여 프로필 필드에 저장할 수 있습니다.

#### 고아 SMS 구독 상태 {#orphaned-sms-subscription-states}

Braze는 [고아 구독 상태 레코드를 자동으로 관리]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#how-braze-handles-orphaned-subscription-states)합니다(사용자 프로필에 연결되지 않은 전화번호 또는 이메일 주소에 저장된 구독 데이터). 이를 통해 의도하지 않은 구독 상태 상속을 방지합니다. 이는 새로 생성된 사용자 프로필이 이전에 삭제되었거나 관련 없는 사용자의 구독 상태를 잘못 상속하는 시나리오로부터 사용자를 보호합니다.

### 파트너십

#### Chord - 고객 데이터 플랫폼 {#chord-customer-data-platform}

[Chord](https://www.chord.co/)는 이커머스 스토어프론트에서 이벤트를 캡처하고 표준화하는 고객 데이터 플랫폼을 제공합니다. Chord를 Braze에 연결하면 구매 활동, 행동 이벤트 및 ID 업데이트가 Braze로 유입되어 파이프라인을 직접 구축하지 않고도 Campaign을 트리거하고 프로필을 최신 상태로 유지할 수 있습니다.

자세한 내용은 [Chord]({{site.baseurl}}/partners/chord)를 참조하세요.

#### Better Email - 템플릿 {#better-email-templates}

[Better Email](https://www.betteremail.dev)은 이메일 디자인 시스템을 중심으로 구축된 협업 이메일 제작 플랫폼입니다. 팀은 공유 블록 및 스타일 시스템에서 프로덕션 준비가 된 이메일을 디자인, 관리 및 내보낼 수 있어 개발자나 에이전시에 의존하지 않고도 대규모로 브랜드 일관성을 보장할 수 있습니다.

자세한 내용은 [Better Email]({{site.baseurl}}/partners/better_email)을 참조하세요.

#### DailyPlay - 동적 콘텐츠 {#dailyplay-dynamic-content}

[DailyPlay](https://dailyplay.ai/)는 게임화 플랫폼입니다. 개인화된 브랜드 게임과 내장 보상 시스템을 출시하여 인게이지먼트를 심화하고 유지율을 개선하는 데 사용할 수 있습니다.

자세한 내용은 [DailyPlay]({{site.baseurl}}/partners/dailyplay)를 참조하세요.

### SDK

#### SDK 주요 업데이트

최신 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 SDK 업데이트 섹션에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그에서 확인할 수 있습니다.

{% multi_lang_include releases/sdk/2026_5_28_26_updates.md %}

{% enddetails %}
{% details 2026년 4월 30일 %}

## 2026년 4월 30일 릴리스 {#april-30-2026-release}

### 데이터 및 보고

#### 개별 프로필 생성을 위한 빠른 사용자 추가 {#quick-user-add-for-individual-profile-creation}

{% multi_lang_include release_type.md release="General availability" %}

이제 **사용자 가져오기**에서 **빠른 사용자 추가**를 선택하고 이메일 또는 외부 ID를 입력하여 개별 사용자 프로필을 생성할 수 있습니다.

이전에는 이 워크플로우에서 사용자를 생성하려면 CSV 업로드 또는 자동화된 수집 방법이 필요했습니다.

자세한 내용은 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)를 참조하세요.

#### Canvas 트리거를 위한 제로 카피 CDI 동기화 {#zero-copy-cdi-syncs-for-canvas-triggers}

{% multi_lang_include release_type.md release="General availability" %}

CDI는 이제 제로 카피 개인화를 위한 `Canvas triggers` 데이터 유형을 지원합니다. 웨어하우스 또는 S3 데이터에서 Canvases를 트리거하고 Braze 사용자 프로필에 해당 필드를 유지하지 않고도 컨텍스트 필드를 전달할 수 있습니다.

이전에는 CDI 동기화에서 이러한 유형의 개인화 워크플로우를 위해 데이터를 Braze 프로필에 기록해야 했습니다.

자세한 내용은 [CDI를 사용한 제로 카피 개인화]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)를 참조하세요.

#### 이커머스 추천 이벤트 {#ecommerce-recommended-events}

{% multi_lang_include release_type.md release="General availability" %}

[이커머스 추천 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events)는 구매 여정의 6단계를 다룹니다: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled`, `order_refunded`. 이러한 이벤트를 성공적으로 전송하면 Braze가 데이터를 검증하고 점점 늘어나는 플랫폼 기능 세트에서 사용할 수 있도록 합니다.

### Currents 및 데이터 공유 {#currents-and-datashare}

#### 새로운 배너 및 WhatsApp Currents 업데이트 {#new-banner-and-whatsapp-currents-updates}

{% multi_lang_include release_type.md release="General availability" %}

Currents 및 데이터 공유에 새로운 `Banner.Dismiss` 이벤트와 기존 WhatsApp 이벤트에 대한 추가 필드가 포함되었습니다.

이전에는 이러한 배너 해제 이벤트와 WhatsApp 필드를 내보내기 데이터에서 사용할 수 없었습니다.

자세한 내용은 [Currents 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)를 참조하세요.

### 오케스트레이션

#### 다국어 번역 {#multi-language-translations}

{% multi_lang_include release_type.md release="General availability" %}

복잡한 코드 없이 빠른 일회성 로캘 설정으로 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 작성하여 모든 시장에 자신 있게 전송할 수 있습니다.

#### 세분화된 권한 마이그레이션 {#granular-permissions-migration}

{% multi_lang_include release_type.md release="General availability" %}

계정에 액세스하고 특정 작업을 수행할 수 있는 사람을 관리하는 것은 보안과 운영 효율성 모두에 중요합니다. 더 많은 제어를 제공하기 위해 Braze는 계정 전반에서 사용자 액세스를 관리하는 더 유연하고 정밀한 방법인 [세분화된 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/granular_permissions_migration)을 도입합니다.

#### 대상으로 보내기 Canvas 구성요소 {#send-to-destination-canvas-component}

{% multi_lang_include release_type.md release="General availability" %}

[대상으로 보내기 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination)를 사용하면 한 Canvas에서 다른 Canvas로 사용자를 보낼 수 있습니다. 예를 들어, 프로모션 오퍼에 대한 메시징을 공유하는 두 개의 Canvases가 있는 경우 대상으로 보내기를 사용하여 이러한 Canvases를 연결할 수 있습니다.

#### Canvas 컨텍스트 개선 사항 {#canvas-context-enhancements}

{% multi_lang_include release_type.md release="General availability" %}

Canvas에서 이제 컨텍스트 변수를 참조하여 다음을 설정할 수 있습니다:

- Content Cards의 제거 이벤트
- Content Cards의 만료

자세한 내용은 [카드 생성]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas)을 참조하세요.

#### 메시지 단계의 전달 유효성 검사 진행 동작 {#delivery-validation-advancement-behavior-for-message-steps}

{% multi_lang_include release_type.md release="General availability" %}

[전달 유효성 검사]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations)는 메시지 전송 시 오디언스가 전달 기준을 충족하는지 확인하기 위한 추가 검사를 제공합니다. 사용자가 메시지 단계에 대해 설정된 전달 유효성 검사를 충족하지 않는 경우 **전달 유효성 검사 진행 동작** 설정을 사용하여 사용자가 다음 단계로 진행할지 Canvas를 종료할지 결정할 수 있습니다.

#### 워크스페이스 메시징 사용량 제한 {#workspace-messaging-rate-limits}

{% multi_lang_include release_type.md release="General availability" %}

[워크스페이스 메시징 사용량 제한]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits)을 사용하여 플랫폼에서 발신 메시지의 전달 속도를 조절하여 사용자가 필요한 메시지를 받을 수 있도록 합니다. 워크스페이스 메시징 사용량 제한은 점진적으로 출시되고 있으므로 대시보드에서 아직 이러한 설정이 표시되지 않을 수 있습니다.

### 채널 및 터치포인트

#### WhatsApp 템플릿 빌더 {#whatsapp-template-builder}

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp 템플릿 빌더]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization)를 사용하면 Braze에서 직접 WhatsApp 메시지 템플릿을 생성하고 제출할 수 있어 Braze와 Meta 비즈니스 매니저 사이를 전환할 필요가 없습니다. Meta가 템플릿을 승인하면 원하는 만큼 많은 Campaigns과 Canvases에서 사용할 수 있습니다.

#### Shopify 제품 태그, 메타필드 및 컬렉션 {#shopify-product-tags-metafields-and-collections}

{% multi_lang_include release_type.md release="General availability" %}

이제 Shopify 스토어에서 [Shopify 제품 태그, 컬렉션 및 메타필드를 동기화]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs)하여 Braze 카탈로그에 저장할 수 있습니다. 이를 통해 커스텀 해결 방법 없이 개인화, 세분화 및 카탈로그 기반 메시징을 위한 더 풍부한 제품 데이터를 제공합니다.

### 파트너십

#### GRAVITY - 데이터 및 분석 - 로열티 {#gravity-data-and-analytics-loyalty}

{% multi_lang_include release_type.md release="General availability" %}

[GRAVTY®](https://www.lji.io/)는 Loyalty Juggernaut Inc.(LJI)의 엔터프라이즈급 로열티 플랫폼으로, 소매, 여행, 레스토랑(퀵서비스 레스토랑 포함) 및 금융 서비스 전반의 브랜드가 차세대 프로그램을 설계, 관리 및 확장할 수 있도록 지원하여 개인화된 데이터 중심 경험을 통해 인게이지먼트, 유지 및 고객 생애주기 가치에서 측정 가능한 성장을 이끌어냅니다.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
### SDK

다음 SDK 업데이트가 릴리스되었습니다. 자세한 내용은 [SDK 체인지로그]({{site.baseurl}}/releases/sdk_changelogs)를 참조하세요.

#### SDK 주요 업데이트

{% multi_lang_include release_type.md release="General availability" %}

최신 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 SDK 업데이트 섹션에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그에서 확인할 수 있습니다.

{% multi_lang_include releases/sdk/2026_4_30_26_updates.md %}

{% enddetails %}
{% details 2026년 4월 2일 %}

## 2026년 4월 2일 릴리스 {#april-2-2026-release}

### 데이터 및 보고

#### Currents 및 데이터 공유 이벤트의 새로운 배너 채널 필드 {#new-banner-channel-fields-in-currents-and-datashare-events}

Braze는 Currents 및 데이터 공유 내보내기의 기존 배너 채널 이벤트에 필드를 추가했습니다. 이러한 이벤트 및 필드 업데이트 목록은 [버전 7의 변경 사항]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-for-storage)을 참조하세요.

#### Currents를 위한 Mixpanel EU 및 인도 데이터 센터 지원 {#mixpanel-eu-and-india-data-center-support-for-currents}

Currents Mixpanel 통합은 이제 Mixpanel의 EU 및 인도 데이터 센터를 지원합니다. Mixpanel 통합을 구성할 때 Braze가 데이터를 전송할 Mixpanel 리전을 선택할 수 있습니다. 이 업데이트는 상호 고객을 위한 Mixpanel의 성장하는 국제적 인프라를 지원합니다. 자세한 내용은 [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel)을 참조하세요.

#### 재사용 가능한 클라우드 데이터 수집(CDI) 소스 및 동기화 {#reusable-cloud-data-ingestion-cdi-sources-and-syncs}

{% multi_lang_include release_type.md release="Early access" %}

클라우드 데이터 수집(CDI)에 소스와 동기화를 분리하는 새로운 디자인이 적용되어 하나의 소스를 여러 동기화에서 재사용할 수 있습니다. 기존 동기화는 중단 시간 없이 새로운 소스 및 동기화 모델로 자동 마이그레이션됩니다. **클라우드 데이터 수집** > **소스**로 이동하여 소스를 보거나 편집하거나 생성한 다음, 동기화를 생성할 때 드롭다운에서 소스를 선택하세요. 이 변경으로 반복적인 설정이 줄어들고 향후 개선을 위한 기반이 마련됩니다. 자세한 내용은 [데이터 웨어하우스 통합 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations)을 참조하세요.

### BrazeAI<sup>TM</sup>

#### BrazeAI Operator<sup>TM</sup>에서 지원 티켓 제출 {#file-support-tickets-from-brazeai-operatortm}

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)에 대시보드를 떠나지 않고 Braze 지원 티켓을 제출할 수 있는 플로우가 포함되었습니다. 단계, 자동 포함 컨텍스트 및 빠른 해결을 위한 팁은 [BrazeAI Operator로 지원 티켓 제출]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets)을 참조하세요.

### 오케스트레이션

#### 다국어 번역

{% multi_lang_include release_type.md release="General availability" %}

워크스페이스에 로캘을 추가한 후 [다국어 번역]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales)을 사용하여 단일 푸시, 이메일, 배너, 인앱 메시지 또는 Content Block 내에서 다양한 언어의 사용자를 타겟팅할 수 있습니다.

![로캘 미리보기]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Canvas 컨텍스트 개선 사항

{% multi_lang_include release_type.md release="General availability" %}

Canvas에서 이제 컨텍스트 변수를 참조하여 다음을 설정할 수 있습니다:

- 메시지 단계에서 배너 및 인앱 메시지의 [만료]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#set-an-expiration)
- 행동 경로 단계의 [개인화된 지연]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables#action-path-delays)

컨텍스트 변수 이름 필드에서 컨텍스트 변수 이름을 직접 입력하거나 단계 편집기의 드롭다운에서 선택할 수도 있습니다. 자세한 내용은 [컨텍스트]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) 및 [컨텍스트 변수]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables)를 참조하세요.

### 채널 및 터치포인트

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk)은 브로드캐스트 메시징과 사용자와의 1:1 채팅을 가능하게 하는 메시징 채널입니다. Liquid 및 기타 동적 콘텐츠를 사용하여 브랜드와의 풍부한 사용자 경험을 촉진하고 향상시키는 개인화된 사용자 경험을 만들 수 있습니다.

![KakaoTalk 리스트 아이템 메시지.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Canvas의 배너 {#banners-in-canvas}

{% multi_lang_include release_type.md release="General availability" %}

Canvas [메시지 단계]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step)에서 [배너]({{site.baseurl}}/user_guide/message_building_by_channel/banners)를 메시징 채널로 사용할 수 있습니다. 배너를 사용하면 앱 또는 웹사이트 콘텐츠를 동적으로 개인화하여 실시간 사용자 자격 및 행동을 반영할 수 있습니다.

### 파트너십

#### CataBoom - 메시지 개인화 - 시각적 및 인터랙티브 콘텐츠 {#cataboom-message-personalization-visual-and-interactive-content}

[CataBoom]({{site.baseurl}}/partners/cataboom)은 게임화 플랫폼입니다. 브랜드는 이를 사용하여 스핀 투 윈 게임, 퀴즈, 즉석 당첨 게임 등 인터랙티브 디지털 경험을 구축하고 출시합니다. 이러한 경험은 인게이지먼트를 심화하고 퍼스트파티 데이터를 수집합니다.

#### Denada - 메시지 오케스트레이션 - 템플릿 {#denada-message-orchestration-templates}

[Denada]({{site.baseurl}}/partners/denada)는 주제 전문가가 자연스러운 대화를 통해 브랜드에 맞는 마케팅 자료를 만들 수 있게 해주는 AI 기반 마케팅 크리에이티브 플랫폼입니다. Denada를 사용하면 팀이 디자인 전문 지식 없이도 아이디어 구상에서 완성된 이메일 콘텐츠까지 진행할 수 있습니다.

#### Poq - 이커머스 - 모바일 앱 플랫폼 {#poq-ecommerce-mobile-app-platform}

[Poq]({{site.baseurl}}/partners/poq)는 기업이 완전한 네이티브 iOS 및 Android 앱을 신속하게 출시, 관리 및 확장할 수 있도록 지원하여 커머스를 촉진하고 브랜드 약속을 실현하는 고성능 모바일 경험을 제공합니다.

#### The Trade Desk – Canvas 오디언스 동기화 {#the-trade-desk-canvas-audience-sync}

[Braze 오디언스 동기화를 The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync)에 사용하면 Braze에서 퍼스트파티 사용자 데이터를 The Trade Desk로 직접 동적으로 동기화하여 광고 리타겟팅, 유사 모델링 및 억제에 활용할 수 있습니다.

### SDK

#### 통합 개발 환경(IDE)을 Docs MCP에 연결 {#connect-your-integrated-development-environment-ide-to-the-docs-mcp}

AI 코딩 어시스턴트를 사용하여 Context7을 통해 통합 개발 환경(IDE)을 Braze Docs MCP에 연결하여 Braze 통합 워크플로우를 가속화하세요. 이를 통해 어시스턴트가 최신 Braze 설명서에 직접 액세스할 수 있어 개발 환경에서 더 정확한 SDK 가이드, 코드 예제 및 문제 해결 도움을 생성할 수 있습니다. Cursor, Claude Desktop 및 VS Code에서의 설정 단계는 [LLM으로 빌드하기]({{site.baseurl}}/developer_guide/getting_started/build_with_llm#connecting-to-the-braze-docs-mcp)를 참조하세요.

#### SDK 주요 업데이트

최신 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 SDK 업데이트 섹션에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그에서 확인할 수 있습니다.

{% multi_lang_include releases/sdk/2026_4_2_26_updates.md %}

{% enddetails %}

{% details 2026년 3월 5일 %}

## 2026년 3월 5일 릴리스 {#march-5-2026-release}

### 데이터 및 보고

#### 새로운 데이터 센터 {#new-data-center}

{% multi_lang_include release_type.md release="General availability" %}

Braze가 새로운 [데이터 센터]({{site.baseurl}}/user_guide/data/infrastructure/data_centers)를 출시했습니다: JP-01. Braze 계정을 설정할 때 리전별 데이터 센터에 가입할 수 있습니다.

#### 컨텍스트 변수 {#context-variables}

{% multi_lang_include release_type.md release="General availability" %}

[컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)는 특정 Canvas를 통한 사용자 여정 내에서 생성하고 사용할 수 있는 임시 데이터입니다. 사용자가 Canvas에 진입할 때마다(이전에 진입한 적이 있더라도) 컨텍스트 변수는 최신 진입 데이터와 Canvas 설정을 기반으로 재정의됩니다. 이 접근 방식을 통해 각 Canvas 진입이 자체적인 독립 컨텍스트를 유지할 수 있어 사용자가 동일한 여정 내에서 여러 활성 상태를 가지면서 각 상태에 대한 특정 컨텍스트를 유지할 수 있습니다.

#### 클라우드 데이터 수집 소스 {#cloud-data-ingestion-sources}

{% multi_lang_include release_type.md release="Early access" %}

[클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze)에 소스와 동기화를 분리하는 새로운 UI가 적용되어 단일 소스를 여러 동기화에서 재사용할 수 있습니다. 이를 통해 중복 구성이 줄어들고 여러 동기화가 있을 때 설정이 간소화됩니다. 기존 동기화가 있는 경우 중단 시간 없이 새로운 소스 및 동기화 구조로 자동 마이그레이션됩니다. 시작하려면 **클라우드 데이터 수집** > **소스**로 이동하여 소스를 보거나 편집하거나 생성한 다음, 동기화를 생성할 때 드롭다운에서 소스를 선택하세요.

#### Currents 및 데이터 공유 이벤트의 추가 필드 {#additional-fields-for-currents-and-data-share-events}

{% multi_lang_include release_type.md release="General availability" %}

[Currents 및 데이터 공유 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)에 분석 및 다운스트림 시스템에서 사용할 수 있는 데이터를 심화하기 위해 다음과 같은 새로운 필드가 포함되었습니다:

{% multi_lang_include releases/currents/2026_3_5_26_field_changes.md %}

#### Snowflake 데이터 공유를 위한 Campaign 및 Canvas 필드 {#campaign-and-canvas-fields-for-snowflake-data-share}

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake 데이터 공유]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs)에 66개의 기존 테이블에 걸쳐 Campaign 및 Canvas 정보를 반영하는 추가 필드가 포함되었습니다:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSV 사전 가져오기 유효성 검사 및 오류 보고 {#csv-pre-import-validation-and-error-reporting}

{% multi_lang_include release_type.md release="General availability" %}

[CSV 사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)에서 이제 사전 가져오기 유효성 검사 및 상세 오류 보고를 지원합니다. 가져오기 전에 **사용자 가져오기** 페이지에서 **가져오기 전 파일 유효성 검사**를 선택하면 Braze가 파일을 스캔하고 완전히 실패할 행(오류)과 일부 값이 건너뛰어지면서 성공할 행(경고)을 식별하는 보고서를 생성합니다. 보고서를 다운로드하고 CSV를 수정하여 다시 업로드하거나 그대로 진행할 수 있습니다. 가져오기가 완료된 후에도 실패한 행에 대한 다운로드 가능한 보고서가 제공되며, 각 문제에 대한 정확한 이유가 포함됩니다.

#### 메시징 진단 대시보드

{% multi_lang_include release_type.md release="Early access" %}

[메시징 진단 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard)는 메시지 전송 결과에 대한 상위 수준 분석을 제공하여 메시징 설정의 트렌드를 파악하고 잠재적 문제를 진단할 수 있게 해줍니다. 이 대시보드는 Campaigns이나 Canvases의 메시지가 예상대로 전송되지 않은 이유를 이해하는 데 도움이 됩니다.

### BrazeAI<sup>TM</sup>

#### 에이전트 콘솔의 Braze 에이전트 {#braze-agents-in-agent-console}

{% multi_lang_include release_type.md release="General availability" %}

[Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents)는 Braze 내에서 생성할 수 있는 AI 기반 도우미입니다. 에이전트는 콘텐츠를 생성하고, 지능적인 의사 결정을 내리고, 데이터를 보강하여 더욱 개인화된 고객 경험을 제공할 수 있습니다. 에이전트를 생성할 때 목적을 정의하고 동작 방식에 대한 가드레일을 설정합니다. 에이전트가 활성화되면 Braze에서 [배포]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)하여 개인화된 카피를 생성하거나, 실시간 의사 결정을 내리거나, 카탈로그 필드를 업데이트할 수 있습니다.

### 오케스트레이션

#### 세분화된 사용자 권한 {#granular-user-permissions}

{% multi_lang_include release_type.md release="Early access" %}

Braze는 사용자 액세스를 관리하는 더 유연한 방법인 [세분화된 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 도입합니다. 레거시 권한이 세분화된 권한에 어떻게 매핑되는지를 포함한 마이그레이션 프로세스에 대해 알아보려면 [세분화된 권한으로 마이그레이션]({{site.baseurl}}/granular_permissions_migration)을 참조하세요.

#### 채널 기반 사용량 제한 {#channel-based-rate-limiting}

{% multi_lang_include release_type.md release="General availability" %}

멀티채널 Campaign 또는 Canvas에 대한 전달 속도 사용량 제한을 설정할 때 공유 사용량 제한 또는 [채널 기반 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#multichannel-campaigns-and-canvases)을 설정할 수 있습니다. 멀티채널 Campaign 또는 Canvas가 채널 기반 사용량 제한을 사용하면 선택한 각 채널에 사용량 제한이 적용됩니다. 예를 들어, Campaign 또는 Canvas에서 분당 최대 5,000개의 웹훅과 2,500개의 SMS 메시지를 전송하도록 설정할 수 있습니다.

#### Canvas 컨텍스트 단계 {#canvas-context-step}

{% multi_lang_include release_type.md release="General availability" %}

[Canvas 컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)를 사용하면 사용자가 Canvas를 이동할 때 하나 이상의 변수를 생성하고 업데이트할 수 있습니다. 예를 들어, 시즌 할인을 관리하는 Canvas가 있는 경우 컨텍스트 변수를 사용하여 사용자가 Canvas에 진입할 때마다 다른 할인 코드를 저장할 수 있습니다.

### 채널 및 터치포인트

#### Content Blocks에서 로캘 번역 {#translate-locales-in-content-blocks}

{% multi_lang_include release_type.md release="Early access" %}

워크스페이스에 로캘을 추가한 후 Content Block 내에서 [다양한 언어의 사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)할 수 있습니다.

### 파트너십

#### Algolia - 검색 추천 {#algolia-search-recommendations}

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia)는 개발자가 빠르고 관련성 높으며 확장 가능한 검색 경험을 구축할 수 있도록 돕는 검색 및 디스커버리 플랫폼입니다. 강력한 API 우선 접근 방식으로 Algolia는 고급 랭킹 알고리즘과 AI 기반 인사이트를 결합하여 원활한 사이트 검색, 내비게이션 및 개인화된 콘텐츠 디스커버리를 제공합니다.

#### Anthropic - AI 모델 제공업체 {#anthropic-ai-model-provider}

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic)은 다양한 언어 작업에 유용하고 정직하며 안전하도록 설계된 차세대 AI 어시스턴트 Claude를 개발하는 AI 안전 및 연구 회사입니다.

#### Canva - 메시지 개인화 - 크리에이티브 스튜디오 {#canva-message-personalization-creative-studio}

[Canva]({{site.baseurl}}/partners/canva)는 Canva의 이미지를 Braze 미디어 라이브러리에 직접 동기화하여 크리에이티브 워크플로우를 간소화하고 모든 메시징 채널에서 시각적 자산을 최신 상태로 유지합니다.

#### DOTS.ECO - 리워드 {#dotseco-rewards}

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco)를 사용하면 추적 가능한 디지털 인증서를 통해 실제 환경에 미치는 영향에 대해 사용자에게 보상할 수 있습니다. 각 인증서에는 공유 가능한 인증서 URL 및 이미지 URL과 같은 메타데이터가 포함될 수 있어 사용자가 자신의 영향력 증명을 보고 다시 방문할 수 있습니다.

#### Figma - 메시지 개인화 - 크리에이티브 스튜디오 {#figma-message-personalization-creative-studio}

[Figma]({{site.baseurl}}/partners/figma)는 제품을 빌드, 디자인 및 프로토타입할 수 있는 협업 디자인 플랫폼입니다. 이 통합을 사용하여 Figma에서 Braze 미디어 라이브러리로 이미지와 시각적 자산을 직접 전송할 수 있습니다.

#### Flybuy - 메시지 개인화 - 위치 {#flybuy-message-personalization-location}

Radius Networks의 [Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy)는 AI 기반 기술을 활용하여 픽업, 배달, 드라이브스루 및 매장 내 식사 전반에 걸쳐 서비스 속도를 최적화하는 선도적인 옴니채널 위치 플랫폼입니다. 통합 마케팅 스위트를 통해 Flybuy는 브랜드가 하이퍼 타겟팅된 순간 기반 메시지를 전달하여 인게이지먼트를 유도하고 주문 금액을 늘리며 더 넓은 로열티 이니셔티브를 지원할 수 있도록 합니다.

#### Google Gemini - AI 모델 제공업체 {#google-gemini-ai-model-provider}

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini)는 텍스트, 코드 및 이미지 전반에 걸친 고급 추론을 결합하여 브랜드가 더 스마트하고 개인화된 경험을 제공할 수 있도록 돕는 Google의 AI 모델 제품군입니다.

#### Limbik - 메시지 개인화 - 개인화 엔진 {#limbik-message-personalization-personalization-engines}

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik)은 AI 공명 레이어로, 실제 오디언스가 메시지, 개념 및 AI 출력을 시장에 도달하기 전에 어떻게 해석하고 반응하는지 예측합니다. 60개 이상의 국가와 25개 이상의 언어에 걸친 지속적인 1차 연구를 기반으로 Limbik은 인간이 검증한 합성 오디언스를 제공합니다. 이는 기계 속도와 연구 수준의 정확도(95% 신뢰도, 1.5%~3% 오차 범위)로 실제 오디언스 반응을 시뮬레이션하는 디지털 인구입니다. Limbik은 메시징이 타겟 오디언스가 믿고 느끼는 것과 공명하는지 즉시 확인할 수 있는 능력을 제공합니다.

#### Linkrunner - 메시지 오케스트레이션 - 기여도 {#linkrunner-message-orchestration-attribution}

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner)는 사용자 획득 캠페인을 추적하고 분석하는 데 도움이 되는 모바일 기여도 및 분석 플랫폼입니다.

#### Mailizio - 메시지 오케스트레이션 - 템플릿 {#mailizio-message-orchestration-templates}

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio)는 직관적인 시각적 편집기를 사용하여 재사용 가능하고 브랜드에 안전한 콘텐츠를 쉽게 디자인할 수 있는 이메일 제작 및 관리 플랫폼입니다. Mailizio를 Braze에 통합하면 콘텐츠 블록과 이메일 템플릿을 내보낸 다음 동일한 자산에서 인앱 메시지를 자동으로 생성하여 빠르고 완벽하게 제어되는 캠페인 배포를 할 수 있습니다.

#### Open Loyalty - 데이터 및 분석 - 로열티 {#open-loyalty-data-and-analytics-loyalty}

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty)는 고객 로열티 및 보상 프로그램을 구축하고 관리할 수 있는 클라우드 기반 로열티 프로그램 플랫폼입니다. Braze와 Open Loyalty 통합은 포인트 잔액, 등급 변경, 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화합니다. 이를 통해 사용자의 로열티 상태가 변경되면 개인화된 메시지(이메일, 푸시, SMS)를 트리거할 수 있습니다.

#### OpenAI - AI 모델 제공업체 {#openai-ai-model-provider}

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai)는 자연어 이해 및 생성을 가능하게 하는 GPT와 같은 고급 AI 모델을 만들어 브랜드가 의미 있는 고객 상호작용을 구축하고 확장할 수 있도록 지원합니다.

#### Shopgate - 채널 {#shopgate-channels}

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate)는 상인이 쇼핑 앱을 만들고 풀필먼트 도구와 클라이언텔링(고객 데이터를 기반으로 한 개인화된 매장 내 고객 지원)을 통해 오프라인 매장의 효율성을 개선할 수 있도록 돕는 모바일 커머스 및 옴니채널 플랫폼입니다.

#### Splio - 데이터 및 분석 - 코호트 가져오기 {#splio-data-and-analytics-cohort-import}

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio)는 고객 경험을 해치지 않으면서 캠페인 수와 매출을 늘릴 수 있는 오디언스 구축 도구이며, 온라인 및 오프라인 CRM 캠페인의 성과를 추적하는 분석을 제공합니다.

### SDK

#### SDK 주요 업데이트

최신 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 SDK 업데이트 섹션에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그에서 확인할 수 있습니다.

{% multi_lang_include releases/sdk/2026_3_5_26_updates.md %}

{% enddetails %}

{% details 2026년 2월 5일 %}

## 2026년 2월 5일 릴리스 {#february-5-2026-release}

### BrazeAI<sup>TM</sup>

#### 콘텐츠 최적화 프로그램 {#content-optimizer}

{% multi_lang_include release_type.md release="Beta" %}

[콘텐츠 최적화 프로그램]({{site.baseurl}}/user_guide/brazeai/content_optimizer)은 자동화된 인게이지먼트 최적화를 제공하는 지속적인 고배리언트 콘텐츠 테스트 캔버스 단계입니다. 메시지 단계와 유사한 드래그 앤 드롭 인터페이스를 사용하여 테스트할 구성요소를 정의하고, AI를 사용하여 배리언트를 생성하거나 수동으로 입력한 다음, Liquid 태그를 사용하여 이러한 구성요소를 메시지 콘텐츠에 매핑할 수 있습니다.

비상황별 멀티암드 밴딧 옵티마이저를 기반으로 구축된 콘텐츠 최적화 프로그램은 사용자당 단일 메시지를 전송하며, 예측 추천을 기반으로 전달할 구성요소 배리언트 조합을 결정합니다. 단계가 시간이 지남에 따라 데이터를 수집하면서 성과가 우수한 배리언트는 자연스럽게 전송 할당이 증가하고 성과가 낮은 배리언트는 감소합니다. 콘텐츠 최적화 프로그램은 지속적인 최적화를 위해 일일 사용자 수가 일정한(하루 최소 수천 명) 반복 전송 Canvases에서 가장 잘 작동합니다.

### 데이터 및 보고

#### 이커머스 추천 이벤트

{% multi_lang_include release_type.md release="Early access" %}

이커머스 추천 이벤트와 기존 구매 이벤트를 일치시키기 위해 "구매하기"와 유사한 ["주문하기" 전환 이벤트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases#conversions-dashboard)를 추가했습니다.

### 채널 및 터치포인트

#### 배너의 로캘 번역 {#translate-locales-in-banners}

{% multi_lang_include release_type.md release="Early access" %}

워크스페이스에 로캘을 추가한 후 단일 배너 내에서 [다양한 언어의 사용자를 타겟팅]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#use-locales)할 수 있습니다.

#### 드래그 앤 드롭 Content Blocks의 너비 구성 {#configure-width-for-drag-and-drop-content-blocks}

탐색 메뉴에서 버튼을 선택하여 [Content Block의 너비를 조정]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email)합니다. 이메일 글로벌 스타일 설정에서 지정하지 않은 경우 기본 너비는 100%이며, 그렇지 않은 경우 글로벌 설정이 적용됩니다.

![너비를 편집할 수 있는 양면 화살표.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### 자동화된 IP 워밍 사용 {#use-automated-ip-warming}

{% multi_lang_include release_type.md release="Early access" %}

[자동화된 IP 워밍]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#automated-ip-warming)을 사용하여 일일 전송량을 점진적으로 늘려 받은편지함 제공업체가 전송 패턴을 학습하고 신뢰할 수 있도록 합니다. Braze는 인게이지먼트가 가장 높은 구독자에게 먼저 전송하므로 일일 볼륨이 모범 사례에 맞는 속도로 증가할 수 있습니다.

### 파트너십

#### LinkedIn – Canvas 오디언스 동기화 {#linkedin-canvas-audience-sync}

[Braze 오디언스 동기화를 LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync)에 사용하면 Braze 통합의 사용자 데이터를 LinkedIn 고객 목록에 추가하여 행동 트리거, 세분화 등을 기반으로 광고를 게재할 수 있습니다. 일반적으로 사용자 데이터를 기반으로 Braze Canvas에서 메시지(푸시, 이메일, SMS, 웹훅 등)를 트리거하는 데 사용했던 모든 기준을 이제 LinkedIn 고객 목록에서 해당 사용자에게 광고를 트리거할 수 있습니다.

#### Oracle CrowdTwist - 데이터 및 분석 {#oracle-crowdtwist-data-analytics}

[Oracle CrowdTwist]({{site.baseurl}}/partners/crowdtwist)는 브랜드가 개인화된 고객 경험을 제공할 수 있도록 지원하는 선도적인 클라우드 네이티브 고객 로열티 솔루션입니다. 이 솔루션은 100개 이상의 즉시 사용 가능한 인게이지먼트 경로를 제공하여 마케터가 고객에 대한 보다 완전한 시각을 개발할 수 있도록 빠른 가치 창출 시간을 제공합니다.

#### Fullstory - 동적 콘텐츠 {#fullstory-dynamic-content}

[Fullstory의]({{site.baseurl}}/partners/fullstory) 행동 데이터 플랫폼은 기술 리더가 더 나은 정보에 기반한 의사 결정을 내릴 수 있도록 지원합니다. 디지털 행동 데이터를 분석 스택에 주입하여 Fullstory의 특허 기술은 양질의 행동 데이터를 대규모로 활용함으로써 모든 디지털 방문을 유용한 인사이트로 전환합니다.

#### Open Loyalty - 데이터 및 분석 {#open-loyalty-data-analytics}

[Open Loyalty]({{site.baseurl}}/partners/openloyalty)는 고객 로열티 및 보상 프로그램을 구축하고 관리할 수 있는 클라우드 기반 로열티 프로그램 플랫폼입니다. Braze와 Open Loyalty 통합은 포인트 잔액, 등급 변경, 만료 경고와 같은 로열티 데이터를 실시간으로 Braze에 직접 동기화합니다. 이를 통해 사용자의 로열티 상태가 변경되면 개인화된 메시지(이메일, 푸시, SMS)를 트리거할 수 있습니다.

#### DOTS.ECO - 확장 {#dotseco-extensions}

[DOTS.ECO]({{site.baseurl}}/partners/dots.eco)를 사용하면 추적 가능한 디지털 인증서를 통해 실제 환경에 미치는 영향에 대해 사용자에게 보상할 수 있습니다. 각 인증서에는 공유 가능한 인증서 URL 및 이미지 URL과 같은 메타데이터가 포함될 수 있어 사용자가 자신의 영향력 증명을 보고 다시 방문할 수 있습니다.

#### Mailizio - 메시지 오케스트레이션 {#mailizio-message-orchestration}

[Mailizio]({{site.baseurl}}/partners/mailizio)는 직관적인 시각적 편집기를 사용하여 재사용 가능하고 브랜드에 안전한 콘텐츠를 쉽게 디자인할 수 있는 이메일 제작 및 관리 플랫폼입니다. Mailizio를 Braze에 통합하면 콘텐츠 블록과 이메일 템플릿을 내보낸 다음 동일한 자산에서 인앱 메시지를 자동으로 생성하여 빠르고 완벽하게 제어되는 캠페인 배포를 할 수 있습니다.

### API {#apis}

#### 미디어 라이브러리 POST API {#media-library-post-apis}

{% multi_lang_include release_type.md release="General availability" %}

이제 API를 통해 미디어 라이브러리 자산을 추가할 수 있어 고객, 파트너, 대행사가 메시지 제작 워크플로우를 더 많이 자동화할 수 있습니다. [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create)를 사용하여 자산 파일을 직접 업로드하거나 기존 URL에서 파일을 복사할 수 있습니다. 이 기능을 통해 통합 및 자동화 기능을 사용할 수 있습니다.

### Currents 및 데이터 공유

#### 스토리지 대상 및 데이터 공유를 위한 에이전트 콘솔 이벤트 {#agent-console-events-for-storage-destinations-and-datashare}

{% multi_lang_include release_type.md release="General availability" %}

이제 스토리지 대상(AWS S3, GCS, Azure Blob Storage) 및 Snowflake 데이터 공유를 위한 두 가지 새로운 [이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)(`agentconsole.AgentExecuted` 및 `agentconsole.ToolInvocation`)를 사용할 수 있습니다. 이러한 이벤트를 통해 다운스트림 시스템에서 에이전트 콘솔 사용량과 세부 정보를 분석하여 에이전트 사용량을 이해하고 최대한 활용할 수 있습니다. 에이전트를 사용하면 Canvases 또는 카탈로그에서 콘텐츠를 생성하고 지능적인 의사 결정에 따라 사용자를 다른 경로로 라우팅하는 등 Braze 전반에서 특정 작업을 수행할 수 있는 지능형 에이전트를 만들고 배포할 수 있습니다. 자세한 내용은 [Currents 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### 개별 채널에 대한 새로운 '재시도' 이벤트 {#new-retry-events-for-individual-channels}

{% multi_lang_include release_type.md release="General availability" %}

이제 이메일, LINE, 푸시 알림, SMS, 웹훅, WhatsApp 채널에 새로운 [재시도 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events)를 사용할 수 있습니다. 이러한 이벤트는 최대 게재빈도 설정으로 인해 예약된 메시지가 중단되지 않고 지연되는 경우에 대한 가시성을 제공합니다. 메시지의 우선순위가 낮아지거나 게재빈도가 제한되는 경우 이제 구성된 재시도 기간 내에 재시도할 수 있어 메시지 전달 패턴과 최대 게재빈도 제한의 영향에 대해 더 나은 인사이트를 얻을 수 있습니다. 자세한 내용은 [Currents 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### TokenStateChange 이벤트에 새로운 'time_ms' 필드 추가 {#add-new-time_ms-field-to-tokenstatechange-event}

{% multi_lang_include release_type.md release="General availability" %}

[`users.behaviors.pushnotification.TokenStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) 이벤트에 새로운 `time_ms` 필드가 추가되어 푸시 토큰 상태 변화를 추적하기 위한 밀리초 수준의 세분성을 제공합니다. 이 향상된 정밀도는 같은 초 내에 여러 변경 사항이 발생할 때 푸시 토큰의 최신 상태를 파악하는 데 도움이 되며, 다운스트림 시스템에서 올바른 구독 상태를 유지하고 있다는 확신을 줍니다. 자세한 내용은 [Currents 체인지로그]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04)를 참조하세요.

#### Tealium 대상으로 익명 사용자 보내기 {#send-anonymous-user-to-tealium-destinations}

{% multi_lang_include release_type.md release="General availability" %}

이제 외부 사용자 ID가 정의되지 않은 이벤트도 [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1) 대상으로 스트리밍할 수 있습니다. Currents 통합에서 "익명 사용자의 이벤트 포함" 확인란을 선택하면 외부 사용자 ID가 없는 이벤트가 억제되지 않고 대상에게 전송됩니다. 이 기능은 비식별 및 익명 사용자와 관련된 다운스트림 분석 및 사용 사례에 매우 중요합니다.

##### CustomHTTP 대상으로 익명 사용자 보내기 {#send-anonymous-user-to-customhttp-destinations}

{% multi_lang_include release_type.md release="Beta" %}

이제 외부 사용자 ID가 정의되지 않은 이벤트도 CustomHTTP 대상으로 스트리밍할 수 있습니다. Currents 통합에서 "익명 사용자의 이벤트 포함" 확인란을 선택하면 외부 사용자 ID가 없는 이벤트가 억제되지 않고 대상에게 전송됩니다. 이 기능은 비식별 및 익명 사용자와 관련된 다운스트림 분석 및 사용 사례에 매우 중요합니다.

#### 이메일 열기 이벤트 — "machine_open" 필드 {#email-open-event-machine_open-field}

[이메일 열기 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events)는 이제 "machine_open" 필드 값을 생성하여 [_머신 열기_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens) 측정기준을 보고할 수 있습니다.

### SDK

다음 SDK 업데이트가 릴리스되었습니다. Swift SDK v14.0.1에서 유니버설 링크 처리 관련 문제가 수정되었습니다. Android SDK v40.2.0은 잠재적인 메모리 누수를 수정하고 투명 활동이 있을 때 여러 세션이 열리는 문제를 해결합니다. Expo SDK v3.2.0에는 네이티브 Swift SDK의 유니버설 링크 처리를 구성할 수 있는 `forwardUniversalLinks` 옵션(기본값: false)이 추가되었습니다.

#### SDK 주요 업데이트

최신 SDK 업데이트가 릴리스되었습니다. 주요 업데이트는 SDK 업데이트 섹션에 나열되어 있으며, 그 외의 모든 업데이트는 해당 SDK 체인지로그에서 확인할 수 있습니다.

{% multi_lang_include releases/sdk/2026_2_5_26_updates.md %}

{% enddetails %}