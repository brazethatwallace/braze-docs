---
nav_title: OtherLevels
article_title: OtherLevels
alias: /partners/otherlevels/
description: "이 문서에서는 OtherLevels Experience Platform과 Braze 간의 통합에 대해 설명합니다."
page_type: partner
search_tag: OtherLevels

---

# OtherLevels

> [OtherLevels](https://www.otherlevels.com/) Experience Platform은 GenAI를 사용하여 스포츠 브랜드, 퍼블리셔 및 운영자가 기존 콘텐츠를 대규모의 브랜드 맞춤형 개인화 비디오 및 리치 미디어 경험으로 전환함으로써 고객과 연결하는 방식을 혁신합니다.

*이 통합은 OtherLevels에서 유지 관리합니다.*

## 개요 {#overview}

Braze와 OtherLevels의 통합을 통해 OtherLevels Experience Platform에 대한 API 호출을 통해 커스텀 GenAI 비디오를 만든 다음, [Braze 연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/)를 통해 이러한 비디오를 iOS 푸시 비디오로 사용자에게 전송할 수 있습니다.

OtherLevels의 AI 기반 경험으로 사용자에게 더 나은 경험을 제공하세요. 기존 콘텐츠와 타사 콘텐츠를 확장성이 뛰어난 비디오 및 리치 미디어로 변환하여 이미 다양한 방식으로 콘텐츠를 소비하고 상황별 개인화된 경험에 강력하게 반응하는 오디언스에게 제공할 수 있습니다.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항          | 설명                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| OtherLevels 계정   | 이 파트너십을 이용하려면 OtherLevels 계정이 필요합니다.                                                                     |
| Braze REST API 키  | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

이 통합을 위해서는 비디오 생성 프로세스의 일부로 OtherLevels Experience Platform API를 호출해야만 Braze에서 사용자에게 메시지를 보낼 수 있습니다. 이 설명서의 일부로 cURL 예제가 제공되지만, API 호출을 자동화하려면 Postman과 같은 API 클라이언트를 사용하는 것이 좋습니다.

## 활용 사례 {#use-cases}

OtherLevels Experience Platform으로 제작한 GenAI 비디오를 사용하여 다음을 수행할 수 있습니다:
- 스포츠 구단주 및 리그, 팬 참여, 스포츠 북, iGaming, 복권을 위한 더 나은 경험을 만들 수 있습니다.
- 텍스트 기반 콘텐츠를 리치 미디어와 비디오로 변환하여 인간적이고 참여도가 높은 경험을 만들어 고객 마케팅을 강화할 수 있습니다.
- 기존 Braze 통합을 재구축하지 않고 확장하여 고객 확보부터 유지까지 성과를 높일 수 있습니다.

## OtherLevels Experience Platform 통합하기 {#integrating-the-otherlevels-experience-platform}

### 1단계: OtherLevels Experience Platform API를 호출하여 비디오 생성하기 {#step-1}

통합의 첫 번째 단계는 OtherLevels Experience Platform API를 호출하여 새 비디오를 생성하는 것입니다. 비디오 생성은 즉시 이루어지지 않는다는 점에 유의하세요. 비디오의 길이와 복잡성에 따라 콘텐츠 제작에 최대 30분이 소요될 수 있습니다. 메시징 스케줄과 API 호출을 적절히 계획하여 비디오 생성을 위한 API 호출이 Braze 메시지 전송 예정 시간보다 충분히 앞서 이루어질 수 있도록 하세요.

{% alert important %}
다음 요청은 cURL을 사용합니다. 보다 효율적인 API 요청 관리를 위해 Postman과 같은 API 클라이언트를 사용하는 것이 좋습니다.
{% endalert %}

API 호출을 구조화하는 방법은 다음 예시를 참조하세요. 비디오 세부 사항을 커스터마이즈하고 API 호출을 구성하는 방법에 대한 자세한 내용은 [GenAI 비디오 커스터마이즈하기](#customizing-the-genai-video)를 참조하세요.

{% raw %}
```bash
curl --request POST \
  --url 'https://exp-platform-api.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media?=' \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/10.3.0' \
  --data '{
    "task": {
        "type": "tasks",
        "tasks": {
            "image_video_overlay": {
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''",
                "color": "255,255,255,0",
                "y_pos": "0",
                "x_pos": "0",
                "image_input": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_replace_bg.mp4",
                "type": "compose.ImageVideoOverlay"
            },
            "resize_image": {
                "media_input": "= tasks.bg_image.jpg ?? tasks.bg_image.png",
                "type": "compose.MediaResize",
                "width": "= .orientation == '\''portrait'\'' ? '\''1080'\'' : .orientation == '\''landscape'\'' ? '\''1920'\''",
                "height": "= .orientation == '\''portrait'\'' ? '\''1920'\'' : .orientation == '\''landscape'\'' ? '\''1080'\''"
            },
            "bg_image": {
                "type": "load",
                "url": "BACKGROUND_IMAGE_URL",
                "refresh_interval": "12h"
            },
            "talking_head": {
                "test": false,
                "title": "INSERT_TITLE",
                "caption": false,
                "templateId": "TALENT_TEMPLATE",
                "type": "TALENT_MODEL",
                "variables": {
                    "script": {
                        "name": "script",
                        "properties": {
                            "content": "= tasks.translate_text.text"
                        },
                        "type": "text"
                    }
                }
            },
            "translate_text": {
                "type": "translate_text",
                "source": "en",
                "target": "en",
                "text": "INSERT_SCRIPT"
            },
            "talking_talent_speed": {
                "type": "compose.VideoSetSpeed",
                "speed": "1.0",
                "video_input": "= tasks.talking_head.mp4"
            },
            "talking_talent_replace_bg": {
                "type": "compose.VideoReplaceBg",
                "video_background": "= tasks.resize_image.jpg ?? tasks.resize_image.png",
                "video_input": "= tasks.talking_talent_speed.mp4"
            }
        },
        "output": "image_video_overlay"
    }
}'
```
{% endraw %}

다음을 교체하세요:

| 플레이스홀더          | 설명                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| `OTHERLEVELS_PROJECT_KEY`   | OtherLevels 계정이 프로비저닝되면 OtherLevels 프로젝트 키가 제공됩니다.                                                                     |
| `BACKGROUND_IMAGE_URL`  | 비디오 배경에 대한 HTTPS URL입니다. |
| `INSERT_TITLE` | 비디오 제목으로, 내부 참조용이며 비디오에 표시되지 않습니다.                                                 |
| `TALENT_TEMPLATE` | 탤런트 템플릿 ID입니다. OtherLevels는 계정 프로비저닝 중에 탤런트(아바타)를 생성하기 위해 사용자와 협력합니다. 사용할 수 있는 탤런트 ID가 하나 또는 여러 개 제공됩니다.                                                 |
| `TALENT_MODEL` | 탤런트 모델 ID입니다. OtherLevels는 계정 프로비저닝 중에 탤런트(아바타)를 생성하기 위해 사용자와 협력합니다. 사용할 수 있는 탤런트 모델이 하나 또는 여러 개 제공됩니다.                                                 |
| `INSERT_SCRIPT` | 비디오에서 탤런트가 말하길 원하는 정확한 스크립트입니다.                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1: Call the OtherLevels Experience Platform API to generate a video" }

API 응답의 일부로 OtherLevels는 성공적인 API 호출을 나타내는 JSON 페이로드를 반환합니다. JSON에는 생성된 비디오를 식별할 수 있는 고유한 `recipe_id`가 포함됩니다. 다음 단계에서 `recipe_id`가 필요합니다.

다음은 API의 응답 예시입니다:

{% raw %}
```bash
{"$schema":"https://exp-platform-api.prod.awsotherlevels.com/schemas/GenerateMediaResBody.json","message":"success","recipe_id":"LMINHWXV2BBD6JGV5VF3ZNZV7BDDRR7FH5FJH6MMX4BVLTPRKTWQ","media_short_id":"LMINHWX","status":"triggered"}
```
{% endraw %}

### 2단계: `recipe_id`를 커스텀 속성으로 설정하기 {#step-2-setting-the-recipe_id-as-a-custom-attribute}

[1단계](#step-1)에서 받은 `recipe_id`를 비디오를 전송할 사용자의 Braze 커스텀 속성으로 설정합니다.

사용 사례에 따라 많은 오디언스를 대상으로 하는 단일 비디오를 생성했을 수 있으며, 이 경우 여러 사용자에게 동일한 `recipe_id`를 설정할 수 있습니다. 또는 각각 다른 사용자를 타겟팅하는 여러 개의 고유 비디오를 생성했을 수 있으며, 이 경우 각 사용자마다 고유한 `recipe_id`를 Braze 커스텀 속성으로 설정해야 합니다.

{% alert important %}
다음 요청은 cURL을 사용합니다. 보다 효율적인 API 요청 관리를 위해 Postman과 같은 API 클라이언트를 사용하는 것이 좋습니다.
{% endalert %}

{% raw %}
```bash
curl --location --request POST 'BRAZE_API_ENDPOINT/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer BRAZE_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "USER_ID",
      "olxpmedia": "RECIPE_ID"
    }
  ]
}'
```
{% endraw %}

다음을 교체하세요:

| 플레이스홀더             | 설명                                                                                                                                                                                     |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT`    | 현재 Braze 인스턴스의 Braze REST 엔드포인트 URL입니다. 자세한 내용은 [REST API 키]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)를 참조하세요. |
| `BRAZE_API_KEY`         | `users.track` 권한이 있는 Braze REST API 키입니다.                                                                                                                                      |
| `USER_ID`              | 이 특정 비디오를 수신할 사용자 ID입니다. 사용할 수 있는 식별자의 더 많은 예시는 [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#track-users)을 참조하세요.                                                                                                                                                  |
| `RECIPE_ID`       | [1단계](#step-1)의 OtherLevels API 응답에서 받은 `recipe_id`입니다.                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Setting the recipe_id as a custom attribute" }

### 3단계: Braze 연결된 콘텐츠를 통해 전송하기 {#step-3-sending-through-braze-connected-content}

GenAI 비디오를 iOS 푸시 메시지로 사용자에게 전송하려면 다음 단계를 따르세요:

1. Braze iOS 푸시 알림 Campaign을 생성합니다.
2. Campaign을 작성하는 동안 **자산** 섹션으로 이동하여 **Add from URL** 필드에 다음 연결된 콘텐츠 구문을 붙여넣습니다.

{% raw %}
```
{% connected_content https://exp-platform-api-external.prod.awsotherlevels.com/v1/app/OTHERLEVELS_PROJECT_KEY/media/{{custom_attribute.${olxpmedia}}} %}
```
{% endraw %}

그런 다음 `OTHERLEVELS_PROJECT_KEY`를 OtherLevels에서 제공한 프로젝트 키로 교체합니다.

{: start="3"}
3. **URL file format** 드롭다운에서 **MP4**를 선택합니다.
4. 원하는 기본 설정에 따라 나머지 Campaign(예: 메시지 콘텐츠, 전송 스케줄, 타겟 오디언스)을 구성합니다.

![연결된 콘텐츠의 자산 필드 예시.]({% image_buster /assets/img/otherlevels/1.png %})

## GenAI 비디오 커스터마이즈하기 {#customizing-the-genai-video}

### 비디오 크기 및 속성 {#video-size-and-attributes}

비디오 배경은 `bg_image` 키 내에서 지정할 수 있습니다.

| 매개변수             | 설명                  |
|-------------------------|----------------------------|
| `url`    | 배경 이미지의 HTTPS URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Video size and attributes" }

비디오 배경 크기는 `resize_image` 키 내에서 지정할 수 있습니다. 배경 이미지의 크기는 여기에서 구성한 것과 동일한 크기를 사용하는 것이 좋습니다.

| 매개변수             | 설명                  |
|-------------------------|----------------------------|
| `width`    | 배경 이미지의 너비로, 세로 및 가로 모드 모두에 대한 옵션이 있습니다. |
| `height`     | 배경 이미지의 높이로, 세로 및 가로 모드 모두에 대한 옵션이 있습니다.                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Video size and attributes" }

비디오 오버레이 옵션은 `image_video_overlay` 키 내에서 지정할 수 있습니다.

| 매개변수             | 설명                  |
|-------------------------|----------------------------|
| `width`    | 오버레이의 너비로, 세로 및 가로 모드 모두에 대한 옵션이 있습니다. |
| `height`         | 오버레이의 높이로, 세로 및 가로 모드 모두에 대한 옵션이 있습니다.                                              |
| `color`              | 투명도와 함께 RGB로 지정된 오버레이의 색상입니다.                                                                   |
| `y_pos`       | 중앙에서의 Y축 오프셋입니다.                                                              |
| `x_pos`    | 중앙에서의 X축 오프셋입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Video size and attributes" }

### 탤런트 및 스크립트 {#talent-and-script}

프로비저닝의 일환으로 OtherLevels는 사용자와 협력하여 비디오에 사용할 하나 또는 여러 개의 탤런트(아바타라고도 함)를 생성합니다. 사용 사례와 브랜드에 따라 기존 브랜드 홍보대사 중 한 명을 활용하거나 고유한 창작물을 제작할 수 있습니다.

이렇게 생성된 후에는 API에서 사용할 수 있는 `TALENT_TEMPLATE` 및 `TALENT_MODEL` ID가 제공됩니다.

입력 스크립트를 처리하는 데 사용되는 음성 모델은 사람이 읽을 수 있는 자연스러운 스크립트를 제공할 때 가장 잘 작동합니다. 대부분의 경우 스크립트를 수동으로 안내하기 위해 별도의 구두점이 필요하지 않습니다. 하지만 실제 오디언스에게 전송하기 전에 모든 스크립트를 테스트하는 것이 좋습니다. 탤런트가 스크립트를 읽는 속도는 `talking_talent_speed` 키 내에서 지정할 수 있습니다.

| 매개변수             | 설명                  |
|-------------------------|----------------------------|
| `speed`    | 탤런트가 스크립트를 읽는 속도를 지정합니다. 예: `1.5`.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Talent and script" }

## 추가 고려 사항 {#additional-considerations}

- iOS 푸시 알림 플랫폼만 기본적으로 비디오 미디어를 지원합니다. Android 푸시 알림은 기본적으로 비디오를 지원하지 않으므로 이 통합은 iOS 오디언스에서만 사용할 수 있습니다.
- iOS 기기에서 비디오 푸시 알림을 수신할 때, 사용자가 푸시 알림을 길게 누르면 비디오가 로드되고 재생됩니다. 이는 iOS 플랫폼의 표준 동작이며 커스터마이즈할 수 없습니다.