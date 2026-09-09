---
nav_title: GPI
article_title: Globalization Partners International
date_published: "2026-09-09"
description: "이 참조 문서에서는 번역 서비스 제공업체인 Globalization Partners International(GPI)과 Braze 간의 파트너십에 대해 설명합니다. GPI Translation Services 커넥터는 번역을 위해 Braze 콘텐츠를 추출하고, 완료된 번역을 Braze의 Translation API를 통해 다시 가져옵니다."
alias: /partners/gpi/
page_type: partner
search_tag: Partner
---

# Globalization Partners International

> [Globalization Partners International](https://www.globalizationpartners.com/)(GPI)은 Braze용 GPI Translation Services 커넥터를 제공합니다. 이 커넥터는 Campaigns, Canvases, 이메일 템플릿, Content Blocks에서 번역할 콘텐츠를 추출한 후, 완료된 번역을 Translation API를 통해 Braze로 다시 가져옵니다. GPI는 200개 이상의 언어에 대해 전문 번역, 인공지능 기반 번역, 전문가 사후 편집을 포함한 인공지능 번역을 지원합니다.

_이 통합은 Globalization Partners International에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

GPI Translation Services 커넥터는 Braze의 기본 다국어 모델 및 Translation API와 통합됩니다. GPI Translation Portal에서 번역 가능한 콘텐츠를 추출하고, GPI에 번역을 의뢰한 후, 완료된 번역을 수동 복사/붙여넣기 없이 Braze로 다시 가져올 수 있습니다. GPI는 워크플로 전체에서 Liquid 태그와 개인화를 유지합니다.

## 사용 사례 {#use-cases}

### 글로벌 캠페인 출시 {#global-campaign-launch}

Braze에서 Campaigns, Canvases 또는 이메일 템플릿을 선택하고, 소스 언어와 대상 언어를 설정한 다음, 전문 번역을 위해 GPI에 콘텐츠를 제출합니다. GPI는 출시 전 초안 미리보기에서 현지화 및 품질 보증을 처리합니다.

### 시간에 민감하거나 대량인 현지화 {#time-sensitive-or-high-volume-localization}

반짝 세일, 긴급 라이프사이클 메시지 또는 대량의 Content Blocks를 커넥터를 통해 전달하면, 번역이 자동으로 Braze에 가져와집니다. 처리 시간은 선택한 워크플로에 따라 수 주에서 수 분까지 다양합니다.

### 국제화 지원 {#internationalization-support}

GPI는 아랍어, 히브리어, 페르시아어와 같은 오른쪽에서 왼쪽(RTL) 언어를 포함하여 Braze 현지화에 대한 서식 및 모범 사례 가이드를 제공합니다.

### 대규모 지속적 현지화 {#ongoing-localization-at-scale}

GPI는 번역 메모리를 사용하여 이전 번역을 재활용함으로써 용어 및 스타일 일관성을 유지하고, 정확 일치, 반복 일치, 유사 일치에 대한 비용을 절감합니다. Braze에서 소스 언어 캠페인을 업데이트하고, 수정된 콘텐츠를 GPI에 전송하여 해당 번역을 갱신합니다.

## 전제 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다.

| 전제 조건 | 설명 |
| --- | --- |
| Globalization Partners International 계정 | 이 통합을 사용하려면 GPI 계정이 필요합니다. |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키:<br>- `campaigns.list`<br>- `campaigns.details`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `canvas.list`<br>- `canvas.details`<br>- `canvas.translations.get`<br>- `canvas.translations.update`<br>- `content_blocks.list`<br>- `content_blocks.info`<br>- `content_blocks.translations.get`<br>- `content_blocks.translations.update`<br>- `templates.email.list`<br>- `templates.email.info`<br>- `templates.email.translations.get`<br>- `templates.email.translations.update`<br><br>이 키는 Braze 대시보드에서 **설정** > **API 및 식별자** > **API 키**로 이동하여 생성합니다. 자세한 내용은 [REST API 키 생성]({{site.baseurl}}/api/basics#creating-rest-api-keys)을 참조하세요. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze 다국어 설정 | 대상 로케일은 Braze에서 **설정** > **현지화 설정**에서 구성되어야 합니다. 자세한 내용은 [다국어 설정]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: Braze REST API 키 생성 {#step-1-create-a-braze-rest-api-key}

1. Braze에서 **설정** > **API 및 식별자** > **API 키**로 이동합니다.
2. [전제 조건](#prerequisites)에 나열된 권한으로 REST API 키를 생성합니다.
3. API 키를 복사하고 인스턴스 REST 엔드포인트를 기록합니다.

### 2단계: GPI에 설정 정보 전송 {#step-2-send-settings-to-gpi}

1. API 키와 REST 엔드포인트를 GPI 계정 매니저에게 전송합니다.
2. 커넥터에 접근해야 하는 사용자 목록을 전송하여 GPI가 해당 사용자를 활성화할 수 있도록 합니다.
3. GPI가 자격 증명으로 커넥터를 구성하고 연결을 검증합니다.

### 3단계: Braze에서 현지화 설정 구성 {#step-3-configure-localization-settings-in-braze}

1. Braze에서 **설정** > **현지화 설정**으로 이동하여 대상 로케일이 활성화되어 있는지 확인합니다.
2. 번역을 위해 전송하는 콘텐츠에 필요한 로케일이 활성화되어 있는지 확인합니다. 로케일이 활성화되지 않은 콘텐츠는 가져온 번역을 수신할 수 없습니다.
3. 번역이 필요한 콘텐츠에 [번역 Liquid 태그]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 추가합니다.
4. RTL 언어의 경우 언어에 따른 콘텐츠 방향을 지원하기 위해 Liquid 태그를 추가합니다. 정렬 스타일 지시문은 RTL 렌더링에 영향을 미치지 않는지 확인한 후에만 사용합니다.

## Braze에서 GPI 사용 {#use-gpi-with-braze}

Braze에서는 초안 또는 출시 후 초안 상태의 콘텐츠만 번역할 수 있습니다.

### 1단계: 번역을 위해 콘텐츠 내보내기 {#step-1-export-content-for-translation}

1. [GPI Translation Portal](https://www.translationportal.com)에서 **Braze** 커넥터를 열고 **New Request**를 선택합니다.
2. **Information** 탭을 완성한 다음 **Content** 탭을 엽니다. **Categories**에서 **Campaign**, **Canvas**, **Email Template** 또는 **Content Block**을 선택한 다음 내보낼 항목을 선택합니다.
3. **Submit**을 선택하여 GPI에 견적 요청을 보냅니다. 견적이 검토 및 승인 준비가 되면 GPI 계정 매니저가 연락합니다.

### 2단계: Braze에 번역 가져오기 {#step-2-import-translations-into-braze}

1. **Braze** 커넥터에서 가져오려는 프로젝트를 찾습니다.
2. **Actions** 열에서 **Import** 아이콘을 선택합니다.
3. 가져오기 확인 메시지를 기다립니다. **Jobs** 페이지에서 가져오기 작업 상태를 확인합니다.

### 3단계: 번역 요청 상태 확인 {#step-3-check-translation-request-status}

1. [GPI Translation Portal](https://www.translationportal.com)로 이동합니다.
2. **Sign In**을 선택하고 자격 증명을 입력합니다.
3. GPI Translation Portal 내비게이션에서 **Braze**를 선택하여 커넥터 대시보드를 엽니다. **Quotes** 및 **Projects** 테이블에서 요청 및 프로젝트 상태를 확인합니다.

### 4단계: Braze에서 번역 미리보기 {#step-4-preview-translations-in-braze}

번역을 가져온 후 Braze에서 미리보기합니다.

1. 번역한 캠페인 또는 메시지의 **편집** 화면을 엽니다.
2. **메시지 작성기**에서 **미리보기 및 테스트** 또는 **테스트** 탭으로 이동합니다.
3. **사용자로 메시지 미리보기**에서 **다국어 사용자**를 선택한 다음 보려는 로케일을 선택합니다.
4. 대상 언어로 미리보기를 확인합니다. 외부 검토자와 공유하려면 미리보기 링크를 생성합니다.

## 참고 사항 {#considerations}

- Braze용 GPI Translation Services 커넥터는 무료로 배포됩니다.

## 문제 해결 {#troubleshooting}

Braze용 GPI Translation Services 커넥터 또는 GPI 번역 프로젝트에 대한 도움이 필요하면 GPI 프로젝트 매니저에게 연락하거나, +1-866-272-5874로 전화하거나, [support@globalizationpartners.com](mailto:support@globalizationpartners.com)으로 이메일을 보내세요.