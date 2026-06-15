---
nav_title: 메시지 유형
article_title: LINE 메시지 유형
page_order: 0
description: "이 문서에서는 다양한 LINE 메시지 유형에 대해 설명합니다."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/message_types/
---

# LINE 메시지 유형 {#line-message-types}

> 이 문서에서는 작성할 수 있는 LINE 메시지 유형과 관련 사양 및 제한 사항을 다룹니다.

LINE 메시지를 작성할 때 메시지 유형을 작성기로 드래그 앤 드롭한 다음 커스터마이징할 수 있습니다.

![텍스트, 이미지, 리치 메시지, 카드 기반 메시지 등 작성기 편집기로 드래그할 수 있는 메시지 유형이 표시된 메시지 유형 패널.]({% image_buster /assets/img/line/line_message_types.png %}){: style="max-width:40%;"}

## 텍스트 {#text}

LINE 텍스트 메시지는 최대 5,000자까지 포함할 수 있으며 이모지와 Liquid 개인화를 지원합니다.

사용 사례:
- 재고 정리를 위한 한정 프로모션 안내
- 고유한 프로모션 카드와 함께 개인화된 생일 축하 메시지 발송
- 다가오는 이벤트에 대한 빠른 업데이트 공유

![블랙 프라이데이 파티를 잊지 말라는 내용과 자정 전까지 최대 80% 할인 가능성을 알리는 텍스트 메시지.]({% image_buster /assets/img/line/line_text_message.png %}){: style="max-width:40%;"}

## 이미지 {#image}

LINE 이미지 메시지는 [미디어 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/), URL 또는 Liquid를 통해 추가할 수 있습니다. 이러한 이미지는 독립형이며 클릭 가능한 링크를 포함하지 않습니다.

사용 사례:
- 휴가지를 소개하여 사용자가 항공권 구매를 고려하도록 유도
- 시즌 종료 프로모션을 강조하여 사용자가 좋은 가격에 내년 겨울 옷을 미리 구매하도록 유도
- 매장 전체 연간 세일에 대한 시각적 카운트다운 시작

![토스터 세일을 홍보하는 이미지 메시지.]({% image_buster /assets/img/line/line_image_message.png %}){: style="max-width:40%;"}

### URL 이미지 {#url-image}

URL 이미지는 다음과 같은 사용 사례에 활용합니다:
- 이미지 소스 속성에 Liquid를 포함하여 Liquid 동적 이미지를 사용합니다. 예를 들어, 이미지 URL로 {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %}를 삽입하여 이미지에 사용자의 이름을 포함할 수 있습니다.
- [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)를 사용하여 웹 서버 또는 공개적으로 접근 가능한 API에서 직접 이미지를 가져옵니다.
- [Braze 카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/)를 사용하여 가져온 CSV 파일 및 API 엔드포인트에서 이미지에 접근합니다.

| **사양** | **권장 속성** |
|--------------------------|----------------------------|
| 이미지 파일 URL 길이 | 최대 2,000자  |
| 이미지 형식          | PNG, JPEG             |
| 파일 크기     |  최대 10&nbsp;MB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URL image" }

## 리치 메시지 (이미지 맵) {#rich-messages-image-map}

LINE 리치 메시지는 이미지의 특정 영역을 선택하면 열리는 하나 이상의 링크를 포함하는 이미지입니다. 리치 메시지 템플릿을 선택하여 링크가 이미지에 매핑되는 방식을 지정합니다.

사용 사례:
- 새로 입고된 핸드백 그리드를 표시하고 각 가방의 제품 페이지로 연결
- 항목을 선택하여 콤보 주문을 시작하는 인터랙티브 메뉴 제공
- 사용자가 그리드 사각형을 선택하여 고를 수 있는 여러 프로모션 배치

![사용자가 탭하여 랜덤 오퍼를 받을 수 있는 흑백 그리드 사진이 포함된 6칸 리치 메시지.]({% image_buster /assets/img/line/line_rich_message.png %})

### 이미지 맵 {#image-map}

| **사양** | **권장 속성** |
|--------------------------|----------------------------|
| 이미지 파일 URL 길이 | 최대 2,000자  |
| 이미지 형식          | PNG(투명 가능), JPEG             |
| 종횡비          | 1:1 (너비:높이)
| 파일 크기     |  최대 10&nbsp;MB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image map" }

### URI 링크 {#uri-link}

| **사양** | **권장 속성** |
|--------------------------|----------------------------|
| 글자 수      | 최대 1,000 |
| 스킴              | HTTP, HTTPS, LINE, tel |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URI link" }

### 텍스트

텍스트 리치 메시지는 최대 400자까지 포함할 수 있습니다.

## 카드 기반 (캐러셀) {#card-based-carousel}

LINE 카드 기반 메시지를 사용하면 사용자가 캐러셀처럼 여러 메시지를 스크롤하며, 카드 또는 카드의 버튼을 선택하여 가장 관련성 높은 메시지에 대해 액션을 취할 수 있습니다.

사용 사례:
- 특정 메뉴 항목에 대한 프로모션 표시
- 이번 시즌 베스트셀러 재킷 강조
- 키트에 포함된 조리 도구 및 가젯 샘플링 제공

![작성기 편집기에서 샌드위치를 홍보하는 최소 두 장의 카드가 포함된 카드 기반 메시지.]({% image_buster /assets/img/line/line_card_message.png %})

### 메시지 {#message}

| **사양** | **권장 속성** |
|--------------------------|----------------------------|
| 열                  | 최대 10개 |
| 종횡비             | 직사각형: 1.51:1 <br> 정사각형: 1:1  |
| 제목                    | 최대 40자
{: .reset-td-br-1 .reset-td-br-2 aria-label="Message" }


### 이미지

| **사양** | **권장 속성** |
|--------------------------|----------------------------|
| 이미지 URL                 | 최대 2,000자 |
| 이미지 형식              | JPEG 또는 PNG |
| 너비                     | 1,024픽셀  |
| 파일 크기                 | 1 MB |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image" }


### 텍스트

| **사양** | **권장 속성** |
|-------------------------|----------------------------|
| 글자 수              | 최대 120자(이미지 또는 제목 없음) <br> 최대 60자(이미지 또는 제목이 포함된 메시지)  |
| 동작                 | 최대 3개 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Text" }