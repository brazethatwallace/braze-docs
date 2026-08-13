---
nav_title: 현지화
article_title: 현지화
page_order: 8
description: "이 참조 문서에서는 현지화의 기본 사항을 다루고, Campaigns와 Canvases 전반에 걸친 다양한 오케스트레이션 접근 방식의 이점을 나열하며, 사용자가 메시징에서 개인화를 처리할 수 있는 다양한 방법을 소개합니다."
tool:
    - Campaigns
    - Canvas
---

# 현지화 {#localization}

> 여러 국가에 고객을 보유한 기업의 경우, Braze 여정 초기에 현지화를 처리하면 시간과 리소스를 절약할 수 있습니다.

## 작동 방식 {#how-it-works}

로캘 정보는 [Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration)(자동) 또는 [REST API]({{ site.baseurl }}/api/endpoints/user_data/post_user_track)를 사용하여 수집한 데이터를 기반으로 사용자 프로필에 저장됩니다. 로캘에는 언어와 지역 식별자가 포함됩니다. 이 정보는 Braze 세분화 툴의 **국가** 및 **언어** 아래에서 확인할 수 있습니다.

{% alert tip %}
SDK에서 로캘을 수집하는 방법에 대한 기술적 세부 사항은 공식 [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html), [Android](http://developer.android.com/reference/java/util/Locale.html) 및 [웹](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language) 설명서를 참조하세요.
{% endalert %}

## 번역 관리 {#translation-management}

번역을 관리하기 위해 다음 접근 방식을 고려하세요.

{% tabs local %}
{% tab campaign %}
### 모든 언어에 하나의 템플릿 {#one-template-for-all}

이 접근 방식에서는 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 사용하여 Braze의 단일 템플릿에 현지화를 적용합니다. 발송 후 대시보드에서 집계된 Campaign 분석을 제공합니다. 사용자 수준의 인게이지먼트는 커스텀 Segment 퍼널을 사용하여 측정할 수 있습니다. 예를 들어 **Country**와 **Received Campaign** 필터를 결합하는 방식입니다.

| 장점 | 고려 사항 |
| --- | --- |
| - 중앙 집중식 접근 방식<br>- 이메일 제작 시간 단축, 이메일을 여러 번 만들 필요 없음 | - 수동 보고서 작성 필요<br>- Campaign 보고서에 국가별 측정기준이 아닌 집계된 측정기준이 표시됨<br>- Liquid가 예상대로 채워지는지 철저히 테스트해야 함<br>- 국가 값을 가져오는 방식이나 설정된 국가 수에 따라 각 국가를 테스트하기 어려울 수 있음<br>- 시간대별로 특정 시간에 발송을 예약하기 어려움<br>- 국가별로 별도의 콘텐츠를 보내려는 경우 사용하기 어려움 |
| --- | --- | --- |
{: .reset-td-br-1 .reset-td-br-2 aria-label="모든 언어에 하나의 템플릿" }

### 국가별 하나의 템플릿 {#one-template-per-country}

이 접근 방식에서는 템플릿을 서로 다른 발송 로캘로 분리합니다. 발송 후 대시보드에서 각 국가별로 발송 분석을 별도로 보고하며, 다운스트림 사용자 수준의 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) 이벤트도 특정 Campaign에 연결됩니다.

- 템플릿은 유지 관리 및 추적 목적으로 [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 구현하면 유용합니다.
- Campaigns는 동일한 [Braze 템플릿]({{site.baseurl}}/user_guide/messaging/templates) 및 [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)(Liquid를 포함하는 [이메일 템플릿]({{site.baseurl}}/user_guide/messaging/templates/email_templates) 등)에서 구성을 상속받을 수 있습니다.
- 기존 Campaigns 및 템플릿을 [복제]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating)하여 더 빠르게 가치를 실현할 수 있습니다.

| 장점 | 고려 사항 |
| --- | --- |
| - 여러 지역으로 확장 가능<br>- Braze 내에서 국가별 매출 보고 가능(예: Campaign별)<br>- 국가별로 콘텐츠가 크게 다른 경우 유연하게 대응 가능 | - 전략적 구조화 필요<br>- 더 많은 제작 노력 필요(예: 각 국가별 별도 Campaign) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="국가별 하나의 템플릿" }
{% endtab %}

{% tab canvas %}
### 모든 언어에 하나의 여정 {#one-journey-for-all}

이 접근 방식에서는 [Canvas 기본 사항]({{site.baseurl}}/user_guide/messaging/canvas/canvas_basics#building-the-customer-journey)과 Liquid를 활용하여 각 사용자에 대한 메시징을 정의하고 현지화를 처리합니다.

Canvas가 발송된 후 대시보드에서 집계된 [Canvas 분석]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics)을 제공하며, 사용자 수준의 인게이지먼트는 커스텀 [Segment 퍼널]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size)을 통해 측정할 수 있습니다. 예를 들어 [**Country**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#country)와 [**Received Canvas Step**]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters#received-message-from-canvas-step) 필터를 결합하는 방식입니다.

| 장점 | 고려 사항 |
| --- | --- |
| - 중앙 집중식 접근 방식<br>- 이메일 제작 시간 단축 - 이메일을 여러 번 만들 필요 없음 | - 수동 보고서 작성 필요<br>- Canvas 보고서에 국가별 측정기준이 아닌 집계된 측정기준이 표시됨<br>- Liquid가 예상대로 채워지는지 철저히 테스트해야 함<br>- 국가 값을 가져오는 방식이나 설정된 국가 수에 따라 각 국가를 테스트하기 어려울 수 있음<br>- 시간대별로 특정 시간에 발송을 예약하기 어려움<br>- 국가별로 별도의 콘텐츠를 보내려는 경우 사용하기 어려움 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="모든 언어에 하나의 여정" }

### 국가별 하나의 여정 {#one-journey-per-country}

이 접근 방식에서는 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) 여정 빌더가 여러 [Canvas 구성 요소]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components)를 통해 사용자 여정을 만들 수 있는 유연성을 제공합니다. 이러한 구성 요소는 구성 요소 수준 및 전체 여정 수준에서 [복제]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/duplicating)할 수 있습니다.

현지화는 다음 방법으로 달성할 수 있습니다:

- 국가별 별도 Canvases를 사용하여 복잡한 사용자 여정이 오디언스 필터를 사용해 퍼널 상단에서 정의되도록 합니다.
- 국가별 맞춤 사용자 여정을 구현하며, [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)를 활용하여 각 여정에 대해 대규모로 사용자를 직관적으로 세분화하고 단일 Canvas 내에서 각 국가별로 별도의 메시지 스레드를 만듭니다.

발송 후 대시보드에서 고객의 현재 위치를 기반으로 국가별 동적 분석과 사용자 수준의 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents) 이벤트를 제공합니다.

| 장점 | 고려 사항 |
| --- | --- |
| - Braze 내에서 국가별 매출 보고 가능(예: Canvas, 배리언트 또는 단계별)<br>- 국가별로 콘텐츠가 크게 다른 경우 유연하게 대응 가능<br>- 향후 여정의 일부로 다른 채널을 추가할 수 있음 | - 전략적 구조화 필요<br>- 더 많은 제작 노력 필요(예: 각 국가별 별도 메시지 단계)<br>- 단일 Canvas 내에서 각 국가별로 커스텀 복잡한 여정이 있는 경우 Canvas가 커지고 읽기 어려워질 수 있음 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="국가별 하나의 여정" }
{% endtab %}
{% endtabs %}

## 번역된 메시지 보내기 {#sending-translated-messages}

사용자의 언어, 로캘 또는 커스텀 속성에 따라 개인화된 메시지를 보내려면 다음 방법 중 하나를 사용하세요.

### 번역 Liquid 태그(권장) {#translation-liquid-tag}

Braze는 {% raw %}`{% translation salutation %}Hello!{% endtranslation %}`{% endraw %} Liquid 태그를 지원하여 단일 메시지로 다양한 언어의 사용자를 타겟팅할 수 있습니다.

전체 안내는 [번역 태그 사용 가이드]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages)를 참조하세요.

### 대체 접근 방식 {#alternative-approaches}

{% tabs local %}
{% tab 커스텀 Liquid %}
메시지 본문에 콘텐츠를 수동으로 붙여넣고 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)를 사용하여 수신자에게 올바른 언어를 [조건부로]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#conditional-logic) 표시할 수 있습니다. 이를 위해:

1. 메시지를 작성한 다음 **Language**를 선택하여 선택한 각 언어에 대한 Liquid 조건 로직을 생성합니다.
2. 다음 Liquid 템플릿을 사용하여 메시지를 작성할 수 있습니다. 템플릿이 포함된 각 필드에 대해 괄호로 묶인 템플릿 세그먼트 뒤에 배리언트를 입력해야 합니다. 배리언트는 앞의 괄호에서 참조된 언어 코드에 해당해야 합니다.
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. 메시지를 보내기 전에 사용자의 ID 또는 이메일을 입력하여 언어에 따라 개인에게 메시지가 어떻게 표시되는지 확인하여 테스트합니다.

{% alert tip %}
메시징에 항상 {% raw %}`{% else %}`{% endraw %} 문을 포함하는 것을 권장합니다. 대부분의 사용자는 자신의 특정 언어에 맞는 메시지를 보게 되지만, 다음과 같은 사용자에게는 이 텍스트가 표시됩니다:
- 언어가 선택되지 않은 사용자
- Braze에서 지원하지 않는 언어를 사용하는 사용자
- 언어를 감지할 수 없는 기기를 사용하는 사용자
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Braze [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks)는 재사용 가능한 콘텐츠 블록입니다. 블록이 변경되면 해당 블록에 대한 모든 참조가 변경됩니다. 예를 들어, 이메일 헤더 또는 푸터에 대한 업데이트는 모든 이메일에 반영되거나 번역을 보관하는 데 사용됩니다. 이러한 블록은 REST API를 사용하여 [생성]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block) 및 [업데이트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)할 수도 있으며, 사용자는 프로그래밍 방식으로 번역을 업로드할 수 있습니다.

대시보드에서 Campaign을 작성할 때 {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %} 태그를 사용하여 Content Blocks를 참조할 수 있습니다. 이러한 블록에는 옵션 1에 표시된 것처럼 각 언어에 대한 조건 로직 내에 모든 번역이 포함될 수 있으며, 각 언어에 대해 별도의 블록을 사용할 수도 있습니다.

Content Blocks는 번역 관리 프로세스로도 활용할 수 있으며, 번역이 필요한 콘텐츠를 Content Block에 보관하고, 가져오고, 번역한 다음 업데이트합니다:
1. 대시보드에서 "Needs Translation" 태그가 있는 Content Block을 수동으로 생성합니다.
2. 서비스가 [`/content_blocks/list` 엔드포인트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks)를 사용하여 모든 Content Blocks를 야간에 가져옵니다.
3. 서비스가 [`/content_blocks/info` 엔드포인트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information)를 통해 각 Content Block의 세부 정보를 가져와 번역 태그가 지정된 블록을 확인합니다.
4. 번역 서비스가 모든 "Needs Translation" Content Blocks의 본문을 번역합니다.
5. 서비스가 [`/content_block/update` 엔드포인트]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block)를 호출하여 번역된 콘텐츠를 업데이트하고 태그를 "Translation Complete"로 업데이트합니다.
{% endtab %}

{% tab 카탈로그 %}
[카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)를 사용하면 API 및 CSV 파일을 통해 가져온 JSON 객체의 데이터에 액세스하여 커스텀 속성이나 커스텀 이벤트 속성정보와 유사하게 Liquid를 통해 메시지를 보강할 수 있습니다. 예를 들어:

{% subtabs local %}
{% subtab API %}

다음 API 호출을 통해 카탈로그를 생성합니다:
```bash
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

다음 API 호출을 통해 항목을 추가합니다:

```bash
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
다음 형식으로 CSV를 생성합니다:

| id | context | language | body |
| --- | --- | --- | --- |
| 1 | 1 | en | Hey |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hey |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hey |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="대체 접근 방식" }
{% endsubtab %}
{% endsubtabs %}

이러한 카탈로그 항목은 다음 예시에 표시된 것처럼 [개인화]({{site.baseurl}}/user_guide/data/activation/catalogs/create)를 사용하여 참조하거나, 데이터 그룹을 생성할 수 있는 [셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 통해 참조할 수 있습니다.

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}}
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Braze 파트너 %}
많은 Braze 파트너가 [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex#about-the-integration) 및 [Crowdin](https://crowdin.com/)을 포함한 현지화 솔루션을 제공합니다. 일반적으로 사용자는 내부 팀 및 번역 에이전시와 함께 플랫폼을 사용합니다. 이러한 번역은 해당 플랫폼에 업로드된 후 REST API를 통해 액세스할 수 있습니다. 이러한 서비스는 종종 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 활용하여 사용자가 API를 통해 번역을 가져올 수 있도록 합니다.

예를 들어, 다음 연결된 콘텐츠 호출은 Transifex와 Crowdin을 호출하여 번역을 가져오며, {% raw %}`{{${language}}}`{% endraw %}를 활용하여 특정 사용자에 대한 올바른 번역을 식별합니다. 이 번역은 JSON 블록 "strings"에 저장되고 참조됩니다.

{% subtabs local %}
{% subtab Transifex 예시 %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin 예시 %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 스프레드시트 %}
스프레드시트에 번역을 호스팅한 다음, 다음 방법 중 하나를 사용하여 해당 언어로 메시지를 보냅니다.

{% subtabs local %}
{% subtab 연결된 콘텐츠 %}
번역 에이전시와 협력하여 Google 스프레드시트에 번역을 저장한 다음, [Braze 연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 사용하여 이 콘텐츠를 쿼리할 수 있습니다. 메시지를 보낼 때 각 사용자에 대한 관련 번역이 선택한 언어에 따라 Campaign 본문에 가져와집니다.

{% alert note %}
Google Sheets API는 프로젝트당 100초에 500개의 요청 제한이 있습니다. 연결된 콘텐츠 호출은 캐시할 수 있지만, 이 솔루션은 트래픽이 많은 Campaign에는 확장성이 부족합니다.
{% endalert %}
{% endsubtab %}

{% subtab SheetDB를 통한 JSON API %}
이 옵션은 Google Sheets를 연결된 콘텐츠를 통해 쿼리할 수 있는 JSON 객체로 변환하는 대체 방법을 제공합니다. 스프레드시트를 SheetDB를 통해 JSON API로 변환하면 API 호출 빈도에 따라 [여러 구독 티어](https://sheetdb.io/pricing)에서 선택할 수 있습니다.

스프레드시트 구조는 옵션 4의 단계를 따르지만, SheetDB는 객체를 쿼리하기 위한 [추가 필터](https://docs.sheetdb.io/#sheetdb-api)도 제공합니다.

일부 사용자는 SheetDB의 [검색 메서드](https://docs.sheetdb.io/#get-search-in-document)를 GET 요청 호출에 구현하여 {% raw %}`{{${language}}}`{% endraw %} Liquid 태그를 기반으로 JSON 객체를 필터링함으로써 대규모 조건 블록을 작성하는 대신 단일 언어에 대한 결과를 자동으로 반환하도록 하여 Liquid 및 연결된 콘텐츠 블록 의존성을 줄이는 방식으로 SheetDB를 구현하는 것을 선호할 수 있습니다.

#### 1단계: Google 시트 형식 지정 {#step-1-format-the-google-sheet}

먼저 언어가 서로 다른 객체가 되도록 Google 시트를 구성합니다:

| language | title1 | body1 | title2 | body2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="1단계: Google 시트 형식 지정" }

#### 2단계: 연결된 콘텐츠 호출에서 언어 Liquid 태그 사용 {#step-2-use-the-language-liquid-tag-in-a-connected-content-call}

다음으로 연결된 콘텐츠 호출 내에서 {% raw %}`{{${language}}}`{% endraw %} Liquid 태그를 구현합니다. SheetDB는 스프레드시트를 생성할 때 `sheet_id`를 자동으로 생성합니다.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### 3단계: 메시지 템플릿 작성 {#step-3-template-your-messages}

마지막으로 Liquid를 사용하여 메시지를 템플릿화합니다:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### 고려 사항 {#considerations}

- {% raw %}`{{${language}}}`{% endraw %} 필드는 모든 사용자에 대해 정의되어야 합니다. 그렇지 않으면 언어가 없는 사용자를 위한 대체 핸들러로 Liquid 조건 블록이 포함되어야 합니다.
- Google Sheets 내의 데이터 모델링은 메시지 객체를 갖는 것과 달리 언어 중심의 수직 구조를 따라야 합니다.
- SheetDB는 제한된 무료 계정과 Campaign 전략에 따라 고려해야 할 여러 유료 옵션을 제공합니다.
- 연결된 콘텐츠 호출은 캐시할 수 있습니다. API 호출의 예상 빈도를 측정하고 검색 메서드를 사용하는 대신 기본 SheetDB 엔드포인트를 호출하는 대체 접근 방식을 조사하는 것을 권장합니다.
{% endsubtab %}
{% subtab Sheetlabs를 통한 JSON API %}

이 옵션은 Google Sheet를 연결된 콘텐츠로 쿼리할 수 있는 JSON API로 변환합니다. Sheetlabs는 대량 쿼리 볼륨을 지원하며 무료 및 유료 티어를 제공합니다.

#### 1단계: Google Sheets에서 번역 시트 준비 {#step-1-prepare-your-translations-sheet-in-google-sheets}

각 행이 하나의 언어가 되도록 Google Sheet를 구성합니다. 예를 들어:

| language | greeting | title1 | legal1 |
| ---- | ---- | ---- | ---- |
| en | Welcome! | Your exclusive offer is here | ... |
| fr | Bienvenue! | Votre offre exclusive est arrivée | ... |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="1단계: Google Sheets에서 번역 시트 준비" }

#### 2단계: Sheetlabs를 사용하여 시트를 가져오고 API 생성 {#step-2-use-sheetlabs-to-import-the-sheet-and-create-an-api}

1. [Sheetlabs](https://sheetlabs.com)에 가입합니다.
2. Sheetlabs 안내에 따라 Google Sheets에서 데이터를 가져옵니다.
3. 1단계에서 생성한 스프레드시트를 선택합니다.
4. **Create a matching API**를 선택합니다.

#### 3단계: Braze에 Sheetlabs 인증 토큰 추가(선택 사항) {#step-3-add-your-sheetlabs-authentication-token-to-braze-optional}

Sheetlabs API가 공개인 경우 이 단계를 건너뜁니다. 인증이 필요한 경우:

1. Sheetlabs의 **My Account** 페이지로 이동하여 API 토큰을 복사합니다.
2. [Braze Basic Auth 인증]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#using-basic-authentication) 단계에 따라 Braze에서 기본 인증 자격 증명을 생성합니다. Sheetlabs 사용자 이름(이메일 주소)과 복사한 API 토큰을 사용합니다.
3. `sheetlabs_creds`와 같은 이름으로 자격 증명을 저장합니다.

#### 4단계: 연결된 콘텐츠에서 Sheetlabs API 호출 {#step-4-call-the-sheetlabs-api-from-connected-content}

연결된 콘텐츠 호출을 Sheetlabs에 추가합니다. `/XXX/yourapi`를 2단계에서 생성한 API 경로로 바꿉니다.

{% raw %}
```liquid
{% connected_content https://sheetlabs.com/XXX/yourapi?language={{${language}}} :save translations :basic_auth sheetlabs_creds %}

```
{% endraw %}

#### 5단계: 메시지 템플릿 작성 {#step-5-template-your-messages}

Liquid를 사용하여 반환된 필드를 참조합니다. 예를 들어:

{% raw %}
```liquid
{{translations[0].greeting}} {{${first_name}}},
{{translations[0].body1}}
```
{% endraw %}

#### 고려 사항

- 매칭하려는 모든 사용자에 대해 {% raw %}`{{${language}}}`{% endraw %} 필드를 정의합니다. 사용자에게 언어가 설정되지 않은 경우 Liquid 대체를 포함합니다.
- 연결된 콘텐츠 호출은 캐시할 수 있습니다. Sheetlabs 플랜을 선택할 때 예상 API 빈도를 측정하세요.

자세한 내용은 [Braze에서 Sheetlabs 사용하기](https://app.sheetlabs.com/docs/producers/braze/)를 참조하세요.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}