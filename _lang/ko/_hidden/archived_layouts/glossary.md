---
nav_title: 용어 사전
article_title: 용어집 레이아웃
page_order: 0
noindex: true
---

# 레이아웃 예시: 용어 사전 {#example-layout-glossary}

> 용어집 레이아웃은 YAML로 되어 있습니다. 여기에는 여러 구성요소와 매개변수가 필요합니다. 용어집 레이아웃은 사전이나 특정 카테고리의 콘텐츠와 같이 현지화된 검색 가능한 콘텐츠에 적합합니다.

## 필수 구성요소 {#required-components}

1. YAML 열기 및 닫기 표기법. 즉, 콘텐츠 앞에는 `---`, 뒤에는 `---`를 입력합니다.
2. 특정 매개변수 내용을 따옴표로 묶습니다. (헤더 매개변수, 텍스트 매개변수, 하이픈 또는 기타 특수 문자가 포함된 콘텐츠)
3. 용어집 태그 표기법(필터 태그)

## 필수 매개변수 {#required-parameters}

| 매개변수 | 콘텐츠 유형 | 세부 정보 |
|---|---|---|
| `page_order` | 숫자 | 섹션 내에서 페이지 순서를 지정합니다. 이 순서는 왼쪽 탐색에 반영됩니다. |
| `nav-title` | 영숫자 | 왼쪽 탐색에 표시될 제목입니다. |
| `layout` | 영숫자 - 공백 없음 | 설명서의 [레이아웃 섹션](https://github.com/Appboy/braze-docs/tree/develop/_layouts)에서 레이아웃을 선택합니다. |
| `glossary_top_header` | 영숫자 | 큰따옴표가 필요합니다. 페이지 상단에 제목이 표시됩니다. |
| `glossary_top_text` | 문자열, 영숫자 | 용어집 페이지를 설명합니다. 검색창과 필터(필터를 선택한 경우) 위에 표시됩니다. 기본적으로 HTML로 작성되므로 ```<br>```을 사용하여 줄 바꿈을 만들 수 있습니다. |
| `glossary_tag_name` | 단일 단어, 영숫자 | 필터의 이름을 지정합니다. 검색창 아래의 체크박스와 아래 데이터에 표시됩니다. |
| `glossary_filter_text` | 문자열, 영숫자 | 필터에 대해 설명합니다. 일반적으로 안내 용도로 사용됩니다. |
| `glossary_tags` | 추가 YAML 및 콘텐츠 | 아래와 같이 포맷합니다: <br> glossary_tags: <br>  - name: Content Cards <br>  - name: Email |
| `glossaries` | 추가 YAML 및 콘텐츠 | 아래 [용어집 매개변수](#glossaries-parameters)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Required Parameters" }

### 용어집 매개변수 {#glossaries-parameters}

| 매개변수 | 콘텐츠 유형 | 세부 정보 |
|---|---|---|
| `name` | 영숫자 | 용어집 항목의 이름을 지정합니다. |
| `description` | 문자열, 영숫자 | 용어집 항목을 설명합니다. |
| `calculation` | 문자열 | (선택 사항) 용어집 항목의 계산 방법을 설명합니다(일반적으로 데이터 또는 측정기준을 설명할 때 사용됨). |
| `tags` | 영숫자 | `glossary_tags` 아래에 `name`으로 나열된 항목과 일치해야 합니다. 해당하는 만큼 나열합니다. `All`을 작성하면 모든 필터에 해당 항목이 포함됩니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Glossaries Parameters" }

## 예시 {#example}

```
---
page_order: 0
nav_title: Report Metrics Glossary
layout: glossary_page
glossary_top_header: "Report Metrics Glossary"
glossary_top_text: "These are terms you'll find in your reports in your Braze account. Search for the metrics you need, or filter by channel. <br>  <br> This glossary does not necessarily include metrics you might see in Currents or in other downloaded reports outside of your Braze account."

glossary_tag_name: Channels
glossary_filter_text: "Select Channels below to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Content Cards
  - name: Email
  - name: In-App Message
  - name: News Feed
  - name: Web Push
  - name: iOS Push
  - name: Android Push
  - name: Webhook

glossaries:
  - name: Variation
    description: Variation of a campaign, differing as defined by the creator.
    calculation: Count
    tags:
      - All
  - name: Audience
    description: Percentage of users who received a particular message. This number is received from Braze.
    calculation: (Number of Recipients in Variant) / (Unique Recipients)
    tags:
      - All
  - name: Unique Recipients
    description: Exact number of users who received a particular message. This number is received from Braze.
    calculation: Count
    tags:
      - Email
      - Web Push
      - iOS Push
      - Android Push
      - In-App Message
      - News Feed
  - name: Total Impressions
    description: The number of users whose devices reported that the in-app message has been delivered (if a user receives a message twice, they will be counted twice). This number is a sum of number of impression events that Braze receives from the SDKs.
    calculation: Count
    tags:
      - In-App Message
      - News Feed
      - Content Cards
---
```
