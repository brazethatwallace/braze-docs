---
nav_title: 번역 접근 방식 비교
article_title: 다국어 번역 관리 접근 방식 비교
page_order: 1
page_type: reference
description: "수동 Liquid, Content Blocks, 카탈로그, 다국어 메시지, 번역 파트너, 연결된 콘텐츠를 비교하여 Kitchenerie가 현지화된 문구를 관리하는 방법을 선택합니다."
tool:
  - Campaigns
  - Canvas
---

# 다국어 번역 관리 접근 방식 비교 {#compare-approaches-for-managing-multi-language-translations}

> 현지화된 문구가 저장, 업데이트, 미리보기 및 전송되는 방식을 평가하여 QA 워크플로, 채널 구성, 업데이트 빈도에 맞는 현지화 접근 방식을 선택할 수 있습니다.

## 이 예제에 대하여 {#about-this-example}

가상의 주방용품 소매업체인 Kitchenerie는 이메일, 푸시, 인앱 메시지를 영어, 프랑스어, 독일어로 발송합니다. 마케팅팀과 엔지니어링팀은 Campaigns 전반에서 번역을 관리할 수 있는 반복 가능하고 확장 가능한 방법이 필요합니다.

Braze는 여러 가지 현지화 패턴을 지원합니다:

- **수동 조건 Liquid:** 메시지 본문에 언어별 콘텐츠를 직접 입력
- **Content Blocks:** 재사용 가능한 블록(다국어 번역 태그 포함 또는 미포함)
- **카탈로그:** 로케일을 키로 하는 구조화된 번역 행
- **다국어 메시지:** 번역 태그, CSV 업로드, 번역 API(얼리 액세스)
- **번역 파트너:** Smartling, Phrase, Lokalise 등
- **연결된 콘텐츠:** 발송 시점에 CMS 또는 API에서 가져오는 현지화된 문자열

이 예제에서는 각 방법의 장단점을 비교하여 QA 워크플로, 채널 구성, 업데이트 빈도, 팀 리소스에 맞는 접근 방식을 선택할 수 있도록 합니다. 이 문서는 특정 방법에 대한 단계별 설정 가이드를 대체하지 않습니다. 기능별 안내는 [현지화]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization) 및 [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 참조하세요.

## 고려 사항 {#considerations}

- 패턴을 선택하기 전에 대시보드 미리보기 및 QA, 전문 번역 워크플로, 고빈도 콘텐츠 업데이트, 또는 실시간 CMS 기반 카피가 필요한지 결정하세요.
- [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)는 이메일, 푸시, 배너, 인앱 메시지, Content Blocks를 지원합니다. 단문 메시지 서비스와 WhatsApp은 다른 현지화 패턴을 사용합니다. 수동 Liquid, Content Blocks, 카탈로그, 파트너, 연결된 콘텐츠는 해당 기능이 지원되는 채널 전반에 적용할 수 있습니다.
- Braze는 번역을 생성하지 않습니다. 대시보드, CSV, API, 카탈로그 가져오기, 파트너 워크플로 또는 외부 CMS를 통해 카피를 직접 제공해야 합니다.
- 수동 Liquid 및 조건문이 포함된 Content Blocks는 언어가 늘어남에 따라 명명 규칙과 검토 프로세스가 필요하며, 다국어 및 파트너 워크플로는 업데이트를 중앙 집중화하지만 CSV 또는 API 유지 관리가 필요할 수 있습니다.
- 연결된 콘텐츠 및 일부 파트너 플로는 외부 시스템에 의존합니다. 발송 시점에 API 또는 CMS를 사용할 수 없으면 현지화된 콘텐츠가 로드되지 않을 수 있습니다.
- 중복은 흔합니다. 예를 들어, 동일한 프로그램에서 이메일 본문에는 다국어 태그를, 공유 푸터에는 Content Blocks를, 제품 카피에는 카탈로그를 함께 사용할 수 있습니다.

## 설정 {#setup}

### 1단계: 현지화 요구 사항 파악 {#step-1-capture-your-localization-requirements}

| 요구 사항 | 답변해야 할 질문 |
| --- | --- |
| 미리보기 및 QA | 마케터가 발송 전에 Braze 작성기에서 각 로케일을 미리 볼 수 있어야 하나요? |
| 규모 | 몇 개의 언어를 지원하며, 문구가 얼마나 자주 변경되나요? |
| 워크플로 | 번역자 검토, 수정, 승인 과정이 필요한가요? |
| 데이터 형태 | 문구가 자유 형식의 마케팅 텍스트인가요, 아니면 구조화된 제품 필드(이름, 가격, URL)인가요? |
| 자동화 | CMS가 변경될 때 번역이 자동으로 업데이트되어야 하나요? |
| 팀 역량 | 팀에서 Liquid, CSV 업로드, API 또는 파트너 통합을 유지 관리할 수 있나요? |
{: .reset-td-br-1 .reset-td-br-2 aria-label="현지화 요구 사항 파악" }

### 2단계: 접근 방식 한눈에 비교 {#step-2-compare-approaches-at-a-glance}

| 차원 | 수동 Liquid | Content Blocks | 카탈로그 | 다국어 메시지 | 번역 파트너 | 연결된 콘텐츠 |
| --- | --- | --- | --- | --- | --- | --- |
| 대시보드 미리보기 / QA | 예 | 예 | 예 | 예 | 파트너에 따라 다름 | 제한적—가져온 콘텐츠 미리보기가 어려움 |
| 기본값(통합 없음) | 예 | 예 | 부분적—카탈로그 설정 필요 | 예 | 아니요—벤더 설정 필요 | 아니요—API 또는 CMS 필요 |
| 채널 지원 범위 | 모든 지원 채널 | 모든 지원 채널 | 모든 지원 채널 | 이메일, 푸시, 배너, 인앱 메시지, Content Blocks | 파트너에 따라 다름 | 모든 지원 채널 |
| 구현 노력 | 낮음 | 낮음–중간 | 중간 | 낮음 | 높음(파트너에 따라 다름) | 중간 |
| 지속적(BAU) 노력 | 높음—메시지별 편집 | 중간—블록 유지 관리 | 중간—CSV 또는 API 업데이트 | 중간—CSV 업로드 | 중간—플랫폼에서 관리 | 낮음—발송 시 가져옴 |
| 빈번한 업데이트 | 아니요 | 부분적 | 아니요 | 부분적 | 예 | 예 |
| 전문 번역 워크플로 | 아니요 | 아니요 | 아니요 | 아니요 | 예 | 아니요 |
| 구조화된 / 제품 데이터 | 제한적 | 제한적 | 예—키 기반 문구에 적합 | 제한적 | 다양함 | 예—외부 소스를 통해 |
| 외부 의존성 위험 | 없음 | 없음 | 없음 | 없음 | 중간 | 중간—소스 다운 시 발송 실패 |
| 적합한 사용 사례 | 소수 언어, 드문 업데이트 | 메시지 간 공유 구성 요소 | 구조화된 문자열의 다수 로케일 | 복사-붙여넣기 노력을 줄인 다국어 지원 | 승인 포함 엔터프라이즈 번역 | 동적 CMS 기반 현지화 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="접근 방식 한눈에 비교" }

### 3단계: Kitchenerie 스타일 시나리오를 접근 방식에 매칭 {#step-3-match-kitchenerie-style-scenarios-to-an-approach}

| Kitchenerie 시나리오 | 권장 시작점 |
| --- | --- |
| 3개 언어, 월 소수 Campaigns, 소규모 마케팅 팀 | 수동 조건 Liquid 또는 Liquid를 활용한 Content Blocks |
| 이메일과 인앱 메시지에서 공유하는 헤더, 푸터, 법무 블록 | Content Blocks—로케일이 확장될 때 [블록에 다국어 번역 저장]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#save-translations-in-content-blocks) 활용 |
| 로케일별로 키 지정된 제품명, 프로모션 문구, 이미지 URL | [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs) |
| 8개 이상 로케일의 이메일 및 푸시, 작성기 미리보기 포함 | [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) |
| 번역자 워크플로 및 승인이 포함된 중앙 TMS | [현지화 파트너]({{site.baseurl}}/partners/message_personalization/localization) (예: Smartling 또는 Phrase) |
| 매일 업데이트되는 CMS에서 관리하는 문구 | [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Kitchenerie 스타일 시나리오를 접근 방식에 매칭" }

### 4단계: 선택한 접근 방식 구현 {#step-4-implement-the-approach-you-selected}

1. **수동 조건 Liquid:** 프로필 `language` 또는 로케일 속성과 `if` / `elsif` / `else` Liquid를 사용합니다. [대안 접근 방식]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#alternative-approaches) 및 [조건 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic)을 참조하세요.
2. **Content Blocks:** 재사용 가능한 블록을 생성하고, 선택적으로 블록 내부에 조건 Liquid를 포함합니다. [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) 및 [번역된 메시지 발송]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages)의 Content Blocks 탭을 참조하세요.
3. **카탈로그:** 번역 행(예: `id`, `context`, `language`, `body`)을 가져오고 Liquid `catalog_items`로 참조합니다. [번역된 메시지 발송]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#sending-translated-messages)의 카탈로그 탭을 참조하세요.
4. **다국어 메시지:** [로케일을 추가]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)하고, 문구를 번역 태그로 감싼 다음 CSV를 업로드합니다. [번역 엔드포인트]({{site.baseurl}}/api/endpoints/translations)에 대한 얼리 액세스 권한이 있다면 API를 통해 번역을 업데이트할 수도 있습니다. 작성기에서 **Multi-language user**로 미리보기하세요.
5. **번역 파트너:** 워크스페이스 로케일을 구성한 다음 파트너 통합을 따릅니다(예: [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling) 또는 [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase)).
6. **연결된 콘텐츠:** 발송 시 CMS 또는 번역 API를 호출합니다. 철저히 테스트하세요. 미리보기에 실시간 API 응답이 반영되지 않을 수 있습니다. [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 참조하세요.

지역별 Canvas 및 Campaign 오케스트레이션(하나의 여정 대 국가별 여정)에 대해서는 현지화 페이지의 [번역 관리]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization#translation-management)를 참조하세요.

## 관련 문서 {#related-articles}

- [현지화]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)
- [다국어 메시지]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)
- [현지화 설정]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)
- [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)
- [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [현지화 파트너]({{site.baseurl}}/partners/message_personalization/localization)
- [현지화된 메시지의 접근성 언어 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility)