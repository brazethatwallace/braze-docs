---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "이 참조 문서에서는 스프레드시트에서 가져온 데이터로 마케팅 캠페인을 개인화할 수 있는 서비스인 Sheetlabs와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/)는 스프레드시트를 강력하고 잘 문서화된 API로 변환할 수 있는 플랫폼입니다. Google Sheets 또는 Excel에서 데이터를 가져와 API로 변환한 다음, Braze와 같은 다른 애플리케이션에서 해당 API를 사용할 수 있습니다.
_이 통합은 Sheetlabs에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Sheetlabs와 Braze 통합을 통해 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)를 사용하여 Braze 마케팅 Campaign에 Sheetlabs API를 포함할 수 있습니다. 이 기능은 일반적으로 Google 스프레드시트(마케팅 팀이 직접 업데이트)와 Braze 템플릿 간의 브리지를 제공하는 데 사용됩니다. 이를 통해 번역이나 더 많은 커스텀 속성 세트 등 Braze 템플릿으로 더 많은 것을 달성할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Sheetlabs 계정 | 이 파트너십을 활용하려면 [Sheetlabs 계정](https://sheetlabs.com/)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

Braze와 Sheetlabs 통합을 통해 다음과 같은 활용 사례를 달성할 수 있습니다.

1. **마케터 접근 권한과 Braze Campaign 접근 권한 분리**: 일부 팀은 모든 직원에게 Braze 템플릿과 콘텐츠를 직접 구성할 수 있는 접근 권한을 부여하지 않기를 원합니다. 대신 직원이 스프레드시트에서 마케팅 콘텐츠를 업데이트하기를 원합니다. Sheetlabs는 스프레드시트와 Braze 간의 브리지를 제공하며 실시간으로 업데이트할 수 있습니다.
2. **번역**: Braze 템플릿은 기본적으로 번역을 지원하지 않습니다. 여러 언어를 지원하려면 여러 템플릿을 만들어야 합니다. Sheetlabs를 Braze와 함께 사용하면 하나의 Braze 템플릿으로 여러 언어로 번역할 수 있습니다.
3. **커스텀 속성 확장**: Braze는 구성할 수 있는 일정 수의 커스텀 속성을 제공합니다. Sheetlabs를 Braze와 함께 사용하면 이 초기 할당량을 초과하는 추가 커스텀 속성을 추가할 수 있습니다.

이러한 활용 사례에 대한 자세한 내용은 [Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/)를 참조하세요.

## 통합 {#integration}

### 1단계: Sheetlabs로 스프레드시트 가져오기 {#step-1-import-your-spreadsheet-into-sheetlabs}

Sheetlabs에서 Excel 스프레드시트를 업로드하거나 Google 계정을 연결하여 Google Sheet를 가져옵니다.

- Excel 스프레드시트를 가져오려면 메뉴 바에서 **Data Tables**를 클릭한 다음 **Import from CSV/Excel**을 클릭합니다.
- Google Sheets에서 가져오려면 메뉴 바에서 **Data Tables**를 클릭한 다음 **Import from Google**을 클릭합니다. 그런 다음 Google 로그인 자격 증명을 제공하고 시트를 가져와야 합니다.

Google Sheet를 동기화 상태로 유지하도록 선택할 수도 있습니다. 이렇게 하면 Google Sheet가 변경될 때 Sheetlabs가 자동으로 최신 데이터를 가져옵니다.

스프레드시트에 Braze 사용자 ID 또는 나중에 조회에 사용할 수 있는 다른 항목을 포함해야 합니다.

### 2단계: Sheetlabs에서 API 생성 {#step-2-create-an-api-in-sheetlabs}

다음으로 Sheetlabs에서 **APIs > Create API**로 이동하여 API에 이름을 지정합니다. Braze 사용자 ID와 같은 스프레드시트의 조회 필드를 통해 쿼리를 허용하는 것이 좋습니다.

이 시점에서 다음과 같은 링크로 API에 접근할 수 있어야 합니다.<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### 3단계: Braze 연결된 콘텐츠에서 API 사용 {#step-3-use-the-api-in-braze-connected-content}

이제 API에 접근할 수 있으므로 연결된 콘텐츠 호출에서 사용할 수 있습니다. 다음은 번역 템플릿의 예시입니다.

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Sheetlabs와의 통합에 대한 더 많은 예시와 조언은 [Sheetlabs 설명서](https://app.sheetlabs.com/docs/producers/braze/)를 참조하세요.
{% endalert %}