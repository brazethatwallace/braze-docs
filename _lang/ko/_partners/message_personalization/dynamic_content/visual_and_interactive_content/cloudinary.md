---
nav_title: Cloudinary
article_title: Cloudinary
description: "이 참고 문서에서는 Braze와 Cloudinary의 파트너십에 대해 설명합니다."
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> [Cloudinary](https://www.cloudinary.com?utm_source=braze_partner_page)는 채널과 고객 여정 전반에 걸쳐 모든 캠페인에 이미지와 동영상을 대규모로 관리, 편집, 최적화 및 전달하는 데 사용되는 이미지 및 동영상 플랫폼입니다. 통합 및 활성화되면 Cloudinary의 미디어 관리 기능이 Braze Campaigns와 Canvases를 위한 동적이고 상황별로 개인화된 자산 전달을 지원합니다.

## 이 통합에 대하여 {#about-this-integration}

Cloudinary를 Braze에 연결하면 브랜드는 Cloudinary 자산에 저장된 시각적 미디어에 액세스하여 Braze 메시징 채널에서 사용할 수 있습니다. Cloudinary의 동적 링크를 사용하면 Braze 사용자 속성에 따라 이미지와 동영상을 실시간으로 선택하고 커스터마이즈할 수 있습니다. Cloudinary와 Braze는 함께 각 제품의 스토리를 전달하고 특별한 경험을 대규모로 제공하는 시각적으로 풍부하고 개인화된 캠페인을 제작할 수 있도록 지원합니다.

이 페이지에서는 Cloudinary와 Braze 간의 가능한 네 가지 통합 방법을 설명하지만, 이에 국한되지는 않습니다. 이러한 통합 방법은 주로 Cloudinary의 미디어 라이브러리에서 수동으로 복사한 자산 링크를 수정하는 방식에 의존합니다.

{% alert important %}
[연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)를 사용하여 Cloudinary의 [Admin API](https://cloudinary.com/documentation/admin_api#banner)를 호출하는 등 보다 고급 통합 방법도 가능하지만, 접근 방식은 고객마다 다를 수 있습니다. 안내가 필요하면 Cloudinary 및 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항     | 설명 |
|-----------------------|-----------------|
| Cloudinary 계정  | 이 파트너십을 이용하려면 [Cloudinary 계정](https://cloudinary.com/users/register_free?utm_source=braze+docs+page)이 필요합니다.  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합 방법 {#integration-methods}

{% alert tip %}
이러한 통합 방법 중 일부는 [이미지](https://cloudinary.com/documentation/image_transformations#banner) 및 [동영상](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner) 자산의 동작과 모양을 보다 심층적으로 커스터마이즈할 수 있는 `f_auto` 및 `q_auto` Cloudinary 변환을 사용합니다. 변환을 포함하도록 Cloudinary 자산 링크를 수정하는 방법에 대한 자세한 내용은 [변환 URL 구조](https://cloudinary.com/documentation/image_transformations#transformation_url_structure)를 참조하세요.
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## Cloudinary DAM을 통한 캠페인 자산 선택 {#select-campaign-assets-through-cloudinary-dam}

Braze Campaigns와 Canvases에서 Cloudinary의 DAM에 있는 이미지와 동영상을 직접 사용하는 가장 간단한 방법은 Cloudinary 미디어 라이브러리의 **Asset** 페이지에서 URL을 가져오는 것입니다.

![이미지 중 하나의 오른쪽 상단에 'Copy URL' 도구 설명이 강조 표시된 Cloudinary의 이미지 자산 라이브러리 그리드 보기]({% image_buster /assets/img/cloudinary/one.png %})

### 이미지 및 GIF 설정 {#images-and-gifs-setup}

1. **Assets** > **Media Library** > **Assets** > **Copy URL**로 이동하여 Cloudinary의 DAM에서 이미지 또는 GIF URL을 복사합니다.
2. HTML로 이미지 태그를 만든 다음 복사한 URL에 `f_auto,q_auto`를 추가하여 이미지 또는 GIF를 최적화합니다.

#### 이미지 URL 예시 {#example-image-url}

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### 동영상 설정 {#videos-setup}

1. **Assets** > **Media Library** > **Assets** > **Copy URL**로 이동하여 Cloudinary의 DAM에서 이미지 또는 GIF 링크를 복사합니다.
2. HTML로 동영상 태그를 만든 다음 복사한 URL에 `f_auto,q_auto`를 추가하면 동영상의 형식과 품질이 자동으로 최적화됩니다.

#### 동영상 URL 예시 {#example-video-url}

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

구체적인 Android 및 iOS 고려 사항은 [동영상]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/video_in_custom_html/)을 참조하세요.

{% endtab %}
{% tab 동영상을 GIF로 변환 %}

## 이메일을 위해 동영상을 GIF로 변환하기 {#convert-videos-to-gifs-for-emails}

`f_auto:animated` [Cloudinary 변환](https://cloudinary.com/documentation/image_transformations/)을 사용하여 동영상 자산을 GIF로 자동 변환할 수 있습니다. GIF는 이메일 페이로드를 줄이기 위해 최적화되어 있으며, 페이로드가 너무 크면 전달 가능성 문제를 일으킬 수 있으므로 Braze 이메일 채널을 사용하는 경우 특히 유용합니다.

### 변환 설정 {#conversion-setup}

1. Cloudinary DAM에서 동영상 URL을 복사합니다.
2. 이미지 태그를 생성하고 `f_auto:animated,fl_lossy`를 추가하여 GIF 크기를 줄이고 클라이언트에 가장 적합한 애니메이션 형식을 선택합니다.
3. 이메일 레이아웃에서 원하는 GIF 너비에 해당하는 `c_scale,w_nnn`을 추가합니다.
4. `e_loop`를 추가하여 애니메이션을 반복합니다.

#### GIF URL 예시 {#example-gif-url}

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab 타겟 속성 %}

## 타겟팅 속성에 따라 캠페인 자산을 동적으로 선택하기 {#dynamically-select-campaign-assets-based-on-targeting-attributes}

이 통합 방식은 사용자 속성을 기반으로 각 사용자에게 가장 적합한 자산을 실시간으로 지능적으로 선택함으로써 동적인 미디어 개인화를 가능하게 합니다.

Braze Campaign 메시지 내 Cloudinary 링크의 매개변수로 Liquid 태그를 포함하면, 메시지가 전송될 때 연결된 Braze 속성이 동적으로 Liquid 태그를 대체합니다. 이는 언어 또는 고객 등급과 같은 사용자별 데이터일 수 있습니다. 그런 다음 Cloudinary는 이러한 속성을 사용하여 해당 사용자에게 가장 적합한 캠페인 자산을 결정하고 올바른 이미지 또는 동영상을 자동으로 반환합니다. 따라서 수신자는 상황별로 관련성이 있고 브랜드가 승인한 자산만 수신하게 됩니다.

### 작동 방식 {#how-it-works}

Cloudinary는 [태그](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags)와 [구조화된 메타데이터(SMD)](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata)를 사용하여 캠페인 자산을 정리하고 검색할 수 있도록 합니다.

각 캠페인 자산은 캠페인 태그(예: `spring_launch`)로 그룹화되고 `language=en` 또는 `tier=gold`와 같은 Braze 속성에 해당하는 구조화된 메타데이터 필드로 보강됩니다. Braze가 Cloudinary 링크를 호출하면 [커스텀 함수](https://cloudinary.com/documentation/custom_functions#javascript_filters)가 들어오는 속성을 처리하고 태그와 메타데이터가 일치하는 자산을 검색한 다음 가장 적합한 항목을 반환합니다.

정확히 일치하는 항목을 찾을 수 없는 경우, 모든 경험의 연속성을 위해 대체 또는 "차선책" 옵션을 자동으로 선택합니다. 자산이 선택되면 Cloudinary의 변환 레이어(예: `f_auto` 또는 `q_auto`)가 전달할 미디어를 최적화합니다. 태그, 메타데이터, 커스텀 함수의 조합을 통해 개발자는 API 기반의 유연한 방식으로 개인화된 자산 전달을 자동화할 수 있습니다.

{% alert tip %}
커스텀 함수 생성 및 적용에 대한 지침과 특정 캠페인의 자산 선택 및 대체 옵션에 대한 커스텀 함수 예시는 Cloudinary의 [`braze-personalization` GitHub 리포지토리](https://github.com/cloudinary-devs/braze-personalization)를 참조하세요. 자세한 안내는 Cloudinary 지원팀에 문의하세요.
{% endalert %}

### 필수 조건

동적 자산 선택을 활성화하려면 Cloudinary가 태그와 메타데이터를 기반으로 자산 집합을 반환할 수 있어야 합니다. 목록 전달 유형이 제한되어 있는 경우, Cloudinary는 Braze Campaigns에서 개인화된 자산 선택에 필요한 동적 목록을 제공할 수 없습니다.
- 목록 전달 유형 제한 해제: Cloudinary 콘솔에서 보안 설정을 열고 제한된 이미지 유형 아래의 리소스 목록 항목을 선택 해제합니다.

### 동적 선택 설정 {#dynamic-selection-setup}

1. Cloudinary에서 자산에 대한 태그와 메타데이터를 설정합니다.
2. Cloudinary DAM에 커스텀 함수를 업로드합니다.
3. 원하는 태그의 Cloudinary URL을 만듭니다.
4. 태그 URL을 기본으로 사용하여 동적 이미지 Liquid 태그를 추가하여 Braze 속성과 커스텀 함수를 통합합니다.

#### URL 예시 {#example-url}

이 예시에서는 Cloudinary의 자산에 Braze 속성에 해당하는 예상 값으로 채워진 두 개의 정의된 SMD 필드("locale" 및 "audience")가 있다고 가정합니다. 또한 캠페인에 필요한 자산에 "samples" 태그를 부여하고, 커스텀 함수 `segmentedBanner.js`를 Cloudinary 계정에 업로드했습니다.

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %}
{% assign locale = {{${language}}}%}

// The URL for the "samples" tag used in the campaign is https://solutions-demo-res.cloudinary.com/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://solutions-demo-res.cloudinary.com/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner">
```
{% endraw %}

##### 출력 URL {#output-urls}

- 오디언스 `internal` 및 로캘 `en`을 가진 사용자를 위한 출력 URL:
```
https://solutions-demo-res.cloudinary.com/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- 오디언스 `external` 및 로캘 `es`을 가진 사용자를 위한 출력 URL:
```
https://solutions-demo-res.cloudinary.com/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- 대체 이미지 URL:
```
https://solutions-demo-res.cloudinary.com/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab 개인화된 이미지 생성 %}

## 개인화된 이미지 생성 {#personalized-image-generation}

Cloudinary의 [텍스트 오버레이 변환](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/)은 Cloudinary 자산 내에서 직접 Braze의 사용자 데이터를 사용합니다.

다음 예시는 `l_text` 변환을 사용하여 자산에 사용자 이름을 삽입하는 방법을 보여줍니다. Campaigns와 Canvases를 개발할 때 Liquid 태그를 활용하여 `l_text` 매개변수를 채울 텍스트를 결정하면 더욱 세밀하게 커스터마이즈할 수 있습니다.

변환 매개변수를 사용하여 자산을 디자인하는 방법에 대한 자세한 안내는 Cloudinary 지원팀에 문의하세요.

### `l_text` 변환 예시 {#example-l_text-transformation}

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%}
{% assign second_name = {{${last_name}}}%}

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### 출력 URL 예시 {#example-output-url}

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![바다가 내려다보이는 파란 지붕의 흰색 교회, 이미지 왼쪽 상단에 반투명한 어두운 직사각형 위에 'John Smith'라는 글자가 표시되어 있습니다.]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}