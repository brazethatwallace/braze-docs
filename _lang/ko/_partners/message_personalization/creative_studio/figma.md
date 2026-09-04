---
nav_title: Figma
article_title: Figma
description: "이 참조 문서에서는 Braze와 Figma 간의 파트너십을 설명하며, 이미지 및 시각적 자산을 Braze 미디어 라이브러리로 전송할 수 있습니다."
alias: /partners/figma/
page_type: partner
search_tag: Partner
---

# Figma

> [Figma](https://www.figma.com/)는 제품을 구축, 디자인 및 프로토타이핑할 수 있는 협업 디자인 플랫폼입니다.

## 통합 소개 {#about-the-integration}

Braze와 Figma 통합을 사용하면 Figma에서 이미지 및 시각적 자산을 Braze 미디어 라이브러리로 직접 전송할 수 있습니다.

통합이 어떻게 작동하는지 개요를 보려면 다음 비디오를 시청하세요.

{% multi_lang_include video.html id="ab5ywsi72n" source="wistia" %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Figma 계정 | 이 파트너십을 활용하려면 Figma 계정이 필요합니다. |
| Braze 미디어 라이브러리 접근 권한 | Braze에서 미디어 라이브러리 자산을 추가, 편집 및 삭제하려면 "Manage Media Library Assets" 권한이 있어야 합니다. |
| Braze 워크스페이스 접근 권한 | Braze에서 Figma 이미지 및 시각적 자산을 업로드하려는 워크스페이스에 대한 접근 권한이 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

### 1단계: Figma to Braze Export 플러그인 설치 {#step-1-install-the-figma-to-braze-export-plugin}

Figma 커뮤니티에서 [Braze Export 플러그인](https://www.figma.com/community/plugin/1606726267245196698/figma-to-braze-export)에 접근합니다. **Open In**을 선택하여 Figma 파일에 플러그인을 로드합니다.

Figma에서는 **Plugins** 섹션에서도 Figma to Braze Export 플러그인을 찾을 수 있습니다.

### 2단계: Braze에 연결 {#step-2-connect-to-braze}

설치 후 **Connect to Braze**를 선택하여 Braze 계정을 연결한 다음 **Continue**를 선택합니다.

다음으로 **Braze workspace** 드롭다운에서 Braze 워크스페이스를 선택하거나 워크스페이스 이름을 입력합니다.

### 3단계: Figma 자산 선택 {#step-3-select-your-figma-assets}

Braze로 내보낼 이미지 및 시각적 자산을 선택합니다. 여러 자산을 선택하려면 <kbd>Shift</kbd>를 누르거나 자산 위로 커서를 드래그 앤 드롭하세요.

내보낸 이미지 또는 시각적 자산의 이름은 Figma에서 선택한 프레임의 이름을 사용합니다.

### 4단계: Braze로 내보내기 {#step-4-export-to-braze}

**Export to Braze**를 선택합니다. 이미지 및 시각적 자산이 Braze 미디어 라이브러리에 업로드됩니다. 이 통합을 사용하여 가져온 모든 이미지의 소스는 **Figma**로 설정됩니다.