---
nav_title: Bynder
article_title: Bynder
description: "이 참고 문서에서는 디지털 자산 관리(DAM) 플랫폼인 Bynder와 Braze 간의 파트너십을 설명합니다. Universal Compact View Chrome 확장 프로그램을 통해 승인된 자산 URL을 검색하고 Braze Campaigns 및 Canvases에 삽입할 수 있습니다."
alias: /partners/bynder/
page_type: partner
search_tag: Partner
---

# Bynder

> [Bynder](https://www.bynder.com)는 고객이 승인된 디지털 자산(이미지, 비디오 및 기타 크리에이티브)을 단일 소스에서 생성, 관리, 검색 및 배포할 수 있도록 지원하는 디지털 자산 관리(DAM) 플랫폼입니다. Braze와 통합하면 Bynder의 Universal Compact View(UCV) Google Chrome 확장 프로그램을 통해 마케터가 Braze 대시보드를 벗어나지 않고도 Bynder 자산을 검색하고 선택할 수 있습니다. 해당 자산의 링크를 Campaigns 및 Canvases에 직접 삽입할 수 있습니다.

_이 통합은 Bynder에서 유지 관리합니다._

## 이 통합에 대하여 {#about-this-integration}

UCV Chrome 확장 프로그램을 통해 Bynder를 Braze에 연결하면 마케터가 Braze 콘텐츠 편집기 내에서 Bynder 자산 라이브러리에 접근할 수 있습니다. Braze 대시보드를 포함한 모든 브라우저 탭에서 Universal Compact View를 오버레이로 열 수 있습니다. 적합한 크리에이티브를 검색하거나 필터링한 다음, 자산의 URL을 Campaign에 붙여넣으세요.

이를 통해 Braze Campaigns가 Bynder의 단일 소스와 일치하게 유지됩니다. 올바른 권한, 최신 파일 버전, 올바른 사용 권한이 보장됩니다.

## 사용 사례 {#use-cases}

- Braze에서 이메일, 인앱 메시지 또는 콘텐츠 블록을 작성하는 마케터는 Bynder에서 직접 가져온 히어로 이미지, 배너 또는 프로모션 비디오 링크를 삽입하여 Campaigns에서 자산의 최신 승인 버전을 사용할 수 있습니다.
- Campaign 매니저는 Universal Compact View의 검색 및 필터 바를 사용하여 특정 오디언스 Segment에 맞는 승인된 지역별 또는 현지화된 크리에이티브를 찾은 후 캔버스 단계에 추가할 수 있습니다.
- 크리에이티브 팀은 Bynder의 Dynamic Asset Transformation을 적용하여 특정 채널에 맞게 자산의 크기를 조정하거나 형식을 변환한 후 링크를 Braze에 복사할 수 있습니다. 예를 들어, 푸시 알림에는 컴팩트 크롭을, 이메일에는 전체 크기 배너를 사용할 수 있습니다.

## 전제 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다.

| 요구 사항 | 설명 |
| --- | --- |
| Bynder 계정 | Braze에서 참조하려는 DAM 자산에 접근할 수 있는 Bynder 계정이 필요합니다. |
| Bynder Universal Compact View(UCV) Chrome 확장 프로그램 | Chrome 웹 스토어에서 설치하고 Bynder 포털에 연결해야 합니다. Google Chrome에서만 사용할 수 있습니다. |
| 공개 자산 및 파생물 | 링크하려는 자산과 특정 파생물은 Bynder에서 공개로 표시되어야 메시지 수신자에게 URL이 올바르게 표시됩니다. |
| Braze 계정 | 자산이 사용되는 메시징 채널(이메일, 콘텐츠 블록, 인앱 메시지, Canvas 등)에 대한 접근 권한이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: Bynder UCV Chrome 확장 프로그램 설치 및 연결 {#step-1-install-and-connect-the-bynder-ucv-chrome-extension}

1. Chrome 웹 스토어에서 [Bynder UCV 확장 프로그램](https://chromewebstore.google.com/detail/bynders-universal-compact/ilghhphnbdblpbdhmbdfiaidganphema)으로 이동합니다.
2. **Chrome에 추가**를 클릭하고, 요청된 권한을 검토한 다음 **확장 프로그램 추가**를 클릭합니다.
3. Chrome 도구 모음에서 Bynder UCV 아이콘을 선택합니다(아직 보이지 않는 경우 먼저 도구 모음에 고정하세요).
4. Bynder 포털 도메인을 입력하고(`https://` 제외) **Connect**를 클릭합니다.
5. 열리는 창에서 일반 자격 증명으로 Bynder 포털에 로그인합니다.

### 2단계: Bynder 자산 검색 및 선택 {#step-2-search-for-and-select-a-bynder-asset}

1. 확장 프로그램이 연결된 상태에서 Braze 대시보드를 포함한 모든 브라우저 탭에서 Universal Compact View를 엽니다.
2. 스마트 필터와 검색 바를 사용하여 필요한 이미지, 비디오, 문서 또는 오디오 자산을 찾습니다.
3. 자산을 선택한 다음, 사용하려는 파생물(또는 공개된 원본 파일)을 선택합니다.
4. **Add Asset**을 클릭하여 선택한 자산의 URL을 클립보드에 복사합니다.

### 3단계: Braze Campaign에 자산 URL 추가 {#step-3-add-the-asset-url-to-your-braze-campaign}

1. Braze에서 자산을 추가하려는 이메일, 콘텐츠 블록, 인앱 메시지 또는 캔버스 단계를 엽니다.
2. 복사한 Bynder 자산 URL을 관련 필드에 붙여넣습니다. 예를 들어, `<img src="">` 태그 또는 콘텐츠 블록의 이미지 URL 필드를 사용합니다.

   이미지 URL 예시:

   ```html
   <img src="https://your-portal.bynder.com/m/abcdef123456/original/campaign-banner.jpg" alt="Summer Campaign">
   ```

{: start="3"}
3. 메시지를 저장하고 미리보기하여 자산이 예상대로 렌더링되는지 확인합니다.

## 팁 {#tips}

### URL을 복사하기 전에 Dynamic Asset Transformation 적용 {#apply-dynamic-asset-transformations-before-copying-the-url}

Universal Compact View 내에서 사용 가능한 변환 옵션을 사용하여 타겟팅하는 채널에 맞게 자산의 크기를 조정하거나, 자르거나, 형식을 변환합니다. 이렇게 하면 별도로 잘린 버전을 Bynder에 업로드할 필요가 없습니다.

### 채널별 파생물 URL 생성 {#generate-channel-specific-derivative-urls}

각 변환 또는 파생물은 고유한 URL을 생성합니다. 이메일용, 푸시용, 인앱 메시지용으로 각각 크기가 조정된 버전을 생성한 다음, 해당하는 Braze 채널 또는 캔버스 단계에 각각 붙여넣으세요.

### 채널 간에 하나의 자산 URL 재사용 {#reuse-one-asset-url-across-channels}

붙여넣은 링크는 Bynder의 특정 자산과 파생물을 가리키므로, 동일한 URL 형식을 이메일, 콘텐츠 블록, 인앱 메시지 및 캔버스 단계에서 재사용할 수 있습니다. 이를 통해 Campaign에서 사용되는 모든 곳에서 크리에이티브의 일관성이 유지됩니다.

### Campaigns를 편집하지 않고 소스 자산 업데이트 {#update-the-source-asset-without-editing-your-campaigns}

Bynder에서 기본 파일이 동일한 공개 자산 및 파생물 설정을 유지한 채 교체되면, 해당 URL을 참조하는 모든 실시간 Braze 메시지에 업데이트가 자동으로 반영됩니다. Campaign 자체를 편집할 필요가 없습니다.

## 고려 사항 {#considerations}

- Bynder UCV Chrome 확장 프로그램은 Google Chrome에서만 사용할 수 있습니다. 다른 브라우저에서는 전체 Bynder 포털에서 직접 자산 URL을 복사하세요.
- Bynder에서 공개로 표시된 자산(및 링크되는 특정 파생물)만 Braze에 붙여넣었을 때 올바르게 표시됩니다. 비공개 자산은 수신자에게 접근 오류를 반환합니다.
- 팝업 창이 허용되지 않거나 포털이 이미 다른 탭에서 열려 있는 경우, 로그인 창이 올바르게 열리지 않을 수 있습니다. 연결하기 전에 팝업 창이 허용되어 있는지 확인하고, 포털이 열려 있는 다른 탭을 닫으세요.
- 확장 프로그램 내 접근 권한은 Bynder DAM에서 해당 회사 사용자의 기존 권한을 따르므로, 이미 접근이 승인된 자산만 보고 선택할 수 있습니다.

## 문제 해결 {#troubleshooting}

| 문제 | 해결 방법 |
| --- | --- |
| 확장 프로그램 아이콘이 보이지 않음 | 확장 프로그램 메뉴에서 Bynder UCV 확장 프로그램을 Chrome 도구 모음에 고정하세요. |
| **Connect**를 클릭해도 로그인 창이 열리지 않음 | Bynder 포털 도메인에 대해 Chrome 팝업이 허용되어 있는지 확인하고, 포털이 이미 열려 있는 다른 탭을 닫으세요. |
| 자산 URL이 Braze에서 렌더링되지 않음 | Bynder 포털에서 해당 자산과 사용된 특정 파생물이 공개로 표시되어 있는지 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }

자세한 내용은 Bynder의 [Universal Compact View 설명서](https://support.bynder.com/hc/en-us/sections/16936397091858-Universal-Compact-View-UCV)를 참조하거나 Bynder 지원팀에 문의하세요.