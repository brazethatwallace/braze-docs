---
nav_title: 메시지 및 이미지 형식
article_title: WhatsApp 메시지 및 이미지 형식
description: "이 참조 문서에서는 WhatsApp 메시지 및 템플릿을 만들기 위한 메시지 구조, 구성요소 제한, 미디어 자산 요구 사항을 다룹니다."
alias: /whatsapp_media_formats/
page_order: 9
channel:
  - WhatsApp
---

# WhatsApp 메시지 및 이미지 형식 {#whatsapp-message-and-image-formats}

> WhatsApp 메시지 및 템플릿을 만들기 위한 메시지 구조, 구성요소, 미디어 자산에 대한 요구 사항은 다음과 같습니다.

Braze에는 두 가지 유형의 WhatsApp 메시지가 있습니다: [템플릿 메시지](#template-messages)와 [응답 메시지](#response-messages).

| 메시지 유형 | 사용 시점 | Meta 승인 |
|---|---|---|
| 템플릿 메시지 | 비즈니스에서 시작하는 아웃리치; 언제든지 발송 가능 | 필수; 템플릿은 발송 전에 Meta에 제출하여 승인을 받아야 합니다. |
| 응답 메시지 | 사용자가 시작한 메시지에 대한 답장; 24시간 대화 기간 내에서만 가능 | 필수 아님 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="WhatsApp message and image formats" }

템플릿 메시지는 Meta에 제출하여 승인을 받아야 하며, 최대 24시간이 소요될 수 있습니다. 승인 후에는 언제든지 발송할 수 있습니다. 응답 메시지(Meta 설명서에서는 "세션 메시지"라고 함)는 활성 대화 기간이 열려 있는 동안에만 발송할 수 있으며, 사용자의 마지막 인바운드 메시지로부터 24시간 이내에만 가능합니다.

## 템플릿 메시지 {#template-messages}

WhatsApp 템플릿 메시지는 비즈니스에서 시작하는 아웃리치에 사용되는 사전 승인된 메시지 형식입니다. Braze에서는 Meta에 제출하기 전에 정의하는 구성요소로 빌드됩니다. 모든 템플릿 메시지는 카테고리 기반입니다: 마케팅, 유틸리티 또는 인증.

### 마케팅 템플릿 {#marketing-templates}

마케팅 템플릿은 Braze에서 가장 일반적으로 사용되는 유형입니다. 최대 4개의 구성요소로 이루어져 있습니다:

| 구성요소 | 필수 | 참고 |
|---|---|---|
| 헤더 | 아니요 | 텍스트, 이미지, 동영상, 문서 또는 위치를 지원합니다. 파일 유형, 크기 및 치수 요구 사항은 [미디어 사양](#media-specifications)을 참조하세요. |
| 본문 | 예 | 주요 메시지 콘텐츠 |
| 푸터 | 아니요 | 본문 아래에 표시되는 보충 텍스트 |
| 버튼 | 아니요 | 최대 10개의 버튼 포함(모든 버튼 유형 지원) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Marketing templates" }

#### 문자 길이 {#character-length}

| 구성요소 | 최대 문자 길이 |
|---|---|
| 본문 | 1,024자 |
| 푸터 | 60자 |
| 버튼 레이블(URL, 전화, 빠른 답장) | 25자 |
| 전화번호(전화 버튼 내) | 20자 |
| 템플릿 이름 | 512자(소문자, 영숫자 및 밑줄만 가능) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Character length" }

#### 버튼 유형 {#button-types}

| 버튼 유형 | 동작 | 참고 |
|---|---|---|
| 빠른 답장 | 대화에서 버튼 레이블 텍스트를 답장으로 전송 | |
| URL | 사용자의 기본 브라우저에서 URL을 열며, URL 끝에 1개의 변수를 추가할 수 있음(최대 2,000자) | |
| 전화번호 | 지정된 전화번호로 통화를 시작 | |
| 쿠폰 코드 복사 | 사용자의 클립보드에 쿠폰 코드를 복사 | 항상 Meta 승인 필요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Button types" }

#### 매개변수 형식 {#parameter-formatting}

템플릿 변수는 이름 지정 매개변수(예: {% raw %}`{{first_name}}`{% endraw %}) 또는 위치 매개변수(예: {% raw %}`{{1}}`{% endraw %})를 사용할 수 있습니다. Braze에서 변수는 Liquid 또는 일반 텍스트로 대체할 수 있습니다. Liquid 변수에는 항상 기본값을 포함하세요. 변수 값이 누락된 메시지는 발송되지 않습니다.

### 미디어 카드 캐러셀 템플릿 {#media-card-carousel-templates}

캐러셀 템플릿은 메시지 본문 뒤에 2~10개의 가로 스크롤 가능한 제품 카드를 표시하며, 각 카드에는 자체 미디어 자산과 버튼이 있습니다. 마케팅 템플릿 메시지에서만 사용할 수 있습니다.

#### 최상위 메시지 {#top-level-message}

| 구성요소 | 필수 | 최대 속성 | 참고 |
|---|---|---|---|
| 본문 텍스트 | 예 | 1,024자 | 변수 지원 |
| 카드 | 예 | 2~10개 카드 | 카드 수는 템플릿 생성 시 고정됩니다. 승인된 캐러셀 템플릿은 생성 시 정의된 정확한 카드 수로만 발송할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Top-level message" }

#### 카드별 사양 {#per-card-specifications}

| 구성요소 | 필수 | 참고 |
|---|---|---|
| 헤더(이미지 또는 동영상) | 예 | 모든 카드는 동일한 형식을 사용해야 합니다(모두 이미지 또는 모두 동영상). 여기에는 동일한 구성요소 구조가 포함되며, 본문 텍스트나 버튼이 있는 카드와 없는 카드를 혼합할 수 없습니다.<br><br> 카드 헤더 자산은 사용자의 기기에 따라 와이드 비율로 자동 잘립니다. |
| 본문 텍스트 | 아니요 | 카드 중 하나라도 본문 텍스트를 포함하면 모든 카드에 본문 텍스트가 포함되어야 합니다 |
| 버튼 | 아니요 | 카드당 최대 2개 버튼 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Per-card specifications" }

#### 카드별 문자 길이 {#per-card-character-lengths}

| 구성요소 | 최대 문자 길이 | 참고 |
|---|---|---|
| 카드 본문 텍스트 | 160자 | |
| 버튼 레이블 | 25자 | |
| 전화번호(전화 버튼 내) | 20자 | |
| URL(URL 버튼 내) | 2,000자; 끝에 1개의 변수를 추가할 수 있음 | URL 버튼은 WhatsApp 외부의 사용자 기본 브라우저에서 열립니다. 해당 시점부터 주문 또는 전환 웹훅은 트리거되지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Per-card character lengths" }

## 응답 메시지 {#response-messages}

응답 메시지(Meta에서는 "세션 메시지"라고도 함)는 24시간 대화 기간 내에서만 발송할 수 있습니다. 사용자가 비즈니스에 메시지를 보내면 대화 기간이 열리고 초기화됩니다.

Braze Campaign 또는 Canvas 편집기에서 직접 작성된 응답 메시지는 Meta 승인이 필요하지 않습니다.

Braze는 7가지 응답 메시지 레이아웃을 지원합니다:

| 메시지 레이아웃 | 설명 |
|---|---|
| 텍스트 | 일반 메시지 본문 텍스트 |
| 미디어 | 이미지, 동영상, 오디오 또는 문서 첨부가 포함된 메시지 |
| 빠른 답장 | 최대 3개의 탭 가능한 답장 버튼이 포함된 메시지 |
| 행동 유도(CTA) 버튼 | URL 버튼 또는 전화번호 버튼이 포함된 메시지 |
| 목록 메시지 | 선택 가능한 옵션의 구조화된 스크롤 가능 목록이 포함된 메시지 |
| 플로우 메시지 | 사용자에게 WhatsApp에서 양식 또는 대화형 작업을 완료하도록 안내하며, 출력이 Braze로 반환되는 메시지 |
| Meta 제품 메시지 | 연결된 Meta 카탈로그에서 단일 제품, 여러 제품 또는 전체 카탈로그를 강조하는 메시지 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Response messages" }

### 목록 메시지 구성요소 {#list-message-components}

| 구성요소 | 최대 속성 |
|---|---|
| 본문 텍스트 | 4,096자 |
| 버튼 레이블(목록 열기용) | 20자 |
| 섹션 수 | 최대 10개 |
| 섹션당 행 수 | 최대 10개 |
| 섹션 제목 | 24자 |
| 행 제목 | 24자 |
| 행 설명 | 72자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="List message components" }

### 빠른 답장 구성요소 {#quick-reply-components}

| 구성요소 | 최대 속성 |
| --- | --- |
| 버튼 | 최대 3개 |
| 버튼 레이블 | 버튼당 20자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Quick reply components" }

## 미디어 사양 {#media-specifications}

다음 사양은 WhatsApp 템플릿 헤더, 응답 메시지 또는 독립형 미디어 메시지의 모든 미디어에 적용됩니다.

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

### 이미지 {#images}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp images' %}

### 동영상 {#video}

{% multi_lang_include channels/image_specs.md variable_name='WhatsApp videos' %}

#### Android 호환성 {#android-compatibility}

B-프레임으로 인코딩된 H.264 "High" 프로필은 Android WhatsApp 클라이언트에서 지원되지 않습니다. 가장 넓은 호환성을 위해 B-프레임 없는 H.264 "Main" 프로필 또는 "Baseline" 프로필을 사용하세요. ffmpeg로 재인코딩하는 경우 `-movflags faststart` 플래그를 사용하여 `moov` 박스를 `mdat` 박스 앞에 배치하세요.

### 오디오 {#audio}

다음 사양은 응답 미디어 메시지 및 오디오 메시지에 적용되며, 오디오 유형에 따라 다릅니다: 음성 메시지 또는 기본 오디오 메시지.

#### 음성 메시지 {#voice-message}

음성 메시지는 녹음된 음성 메모처럼 작동하며, 재생 컨트롤과 텍스트 변환을 지원합니다.

| 속성 | 사양 |
|---|---|
| 필수 형식 | OGG만 |
| 필수 코덱 | OPUS만(모노 입력) |
| 파일 크기 | 최대 16 MB |
| 재생 아이콘 | 이 아이콘은 파일이 512 KB 이하인 경우에만 표시되며, 더 큰 파일은 다운로드 아이콘이 표시됩니다 |
| 텍스트 변환 | 사용자가 WhatsApp 음성 텍스트 변환을 활성화한 경우 자동으로 표시됩니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Voice message" }

#### 기본 오디오 메시지 {#basic-audio-message}

다음 사양은 표준 오디오 파일 공유(음악 클립, 오디오 광고 및 사운드 파일)에 적용됩니다.

| 형식 | 확장자 | 최대 파일 크기 | 참고 |
|---|---|---|---|
| AAC | .aac | 16 MB | |
| AMR | .amr | 16 MB | |
| MP3 | .mp3 | 16 MB | |
| MP4 Audio | .m4a | 16 MB | |
| OGG(OPUS 코덱) | .ogg | 16 MB | OGG 파일은 OPUS 코덱을 사용해야 합니다. OPUS 없는 기본 `audio/ogg`는 지원되지 않습니다.<br><br> 기본 오디오 메시지로 전송된 OGG/OPUS 파일은 음악 아이콘 대신 마이크 아이콘(음성 메시지와 동일)이 표시됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Basic audio message" }

#### 고려 사항 {#considerations}

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- 오디오 메시지에는 캡션을 지원하지 않습니다.
- 일반적인 오류는 MIME 유형 불일치입니다. 발송 전에 파일의 MIME 유형이 확장자와 일치하는지 확인하세요.

### 문서 {#documents}

다음 사양은 템플릿 헤더(문서 형식), 응답 미디어 메시지 및 문서 메시지에 적용됩니다.

| 문서 유형 | 파일 유형 | 최대 파일 크기 |
|---|---|---|
| PDF | PDF | 100 MB |
| Microsoft Word | DOC, DOCX | 100 MB |
| Microsoft Excel | XLS, XLSX | 100 MB |
| Microsoft PowerPoint | PPT, PPTX | 100 MB |
| 일반 텍스트 | TXT | 100 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Documents" }

#### 고려 사항

{% multi_lang_include alerts/important_alerts.md alert='WhatsApp audio and documents' %}

- 캡션은 선택 사항이며 최대 1,024자까지 가능합니다.
- 파일 이름은 선택 사항입니다. WhatsApp은 파일 확장자를 사용하여 대화에서 표시할 문서 아이콘을 결정합니다.
- 나열된 형식만 공식적으로 지원됩니다. 다른 파일 유형은 전송될 수 있지만 WhatsApp에서 올바르게 렌더링되는 것이 보장되지 않습니다.

## 빠른 참조: WhatsApp 미디어 사양 {#quick-reference-whatsapp-media-specifications}

| 미디어 유형 | 파일 유형 | 최대 파일 크기 | 캡션 가용성 |
|---|---|---|---|
| 이미지 | JPEG, PNG | 5 MB | 예(최대 1,024자) |
| 동영상 | MP4, 3GPP | 16 MB | 예(최대 1,024자) |
| 오디오(음성) | OGG(OPUS) | 16 MB | 아니요 |
| 오디오(기본) | AAC, AMR, MP3, M4A, OGG | 16 MB | 아니요 |
| 문서 | PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX, TXT | 100 MB | 예(최대 1,024자) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Quick reference: WhatsApp media specifications" }