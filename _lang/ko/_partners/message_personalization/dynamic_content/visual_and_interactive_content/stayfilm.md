---
nav_title: Stayfilm
article_title: Stayfilm
description: "웹훅 Campaign, 연결된 콘텐츠, 데이터 변환을 사용하여 Stayfilm 개인화 비디오 렌더링을 Braze와 통합하는 방법을 알아보세요."
alias: /partners/stayfilm/
page_type: partner
search_tag: Partner
---

# Stayfilm

> [Stayfilm](https://www.stayfilm.com/)은 대규모 자동화된 개인화 비디오 제작을 위한 REST API입니다. 이 플랫폼은 데이터, 이미지, 텍스트, 사운드트랙, 내레이션, 시각 효과를 통합하여 이커머스, 마켓플레이스, CRM 워크플로, 마케팅 Campaign을 위한 맞춤형 비디오 콘텐츠를 생성합니다.
>
> 이 통합은 Braze에서 Stayfilm API로 렌더 작업을 전송하고, 비디오가 준비되면 콜백을 수신하며, Campaign 및 Canvases에서 사용할 수 있도록 비디오 URL과 상태를 고객 프로필에 저장합니다.

_이 통합은 Stayfilm에서 유지 관리합니다._

## 사용 사례 {#use-cases}

Stayfilm은 고객 생애주기 전반에 걸쳐 개인화된 비디오 전달을 지원하며, 다음과 같은 사용 사례를 포함합니다:

- **온보딩 및 환영 여정:** 프로필이나 가입 상황에 맞게 개인화된 비디오로 신규 사용자를 환영합니다
- **제품 및 마켓플레이스 콘텐츠:** 카탈로그 또는 사용자가 제공한 미디어로 제품 중심 비디오를 생성합니다
- **전환 및 활성화:** 상황별 비디오 메시징으로 핵심 행동을 강화합니다
- **로열티 및 업셀:** 개인화된 오퍼 또는 사용 마일스톤을 비디오 형식으로 강조합니다
- **윈백 및 고객이탈 방지:** 맞춤형 비디오 콘텐츠로 비활성 사용자의 재참여를 유도합니다

## 사전 요구 사항 {#prerequisites}

시작하기 전에 다음 사항을 확인하세요:

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Stayfilm API 액세스 | Stayfilm에 연락하여 `idproject`, `Subscription-Key`, OAuth 클라이언트 자격 증명, Stayfilm API 기본 URL을 포함한 프로젝트 자격 증명을 받으세요. 인증 및 엔드포인트 세부 정보는 [Stayfilm API 설명서](https://apidoc.stayfilm.com)를 참조하세요. |
| Braze 데이터 변환 | [Braze 데이터 변환]({{site.baseurl}}/user_guide/data/unification/data_transformation)을 사용하여 Stayfilm 콜백을 수신하고 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통해 Braze 고객 프로필에 매핑하세요. |
| Braze 사용자 식별자 | 이 가이드에서는 `external_id`를 사용하여 Stayfilm 작업을 Braze 고객 프로필과 연결합니다. `CallbackRelayData`에 전달하는 값은 Braze에서 해당 사용자의 `external_id`와 일치해야 합니다. |
| Braze 샌드박스 (권장) | 프로덕션에 배포하기 전에 Braze 샌드박스 워크스페이스에서 통합을 테스트하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 통합 작동 방식 {#how-the-integration-works}

이 통합은 양방향 웹훅 흐름을 사용합니다:

1. **아웃바운드:** Braze [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks)이 Stayfilm `POST /Job` 엔드포인트로 렌더 작업을 전송합니다. 요청에는 사용자 미디어, 템플릿 구성 및 Braze 사용자의 `external_id`로 설정된 `CallbackRelayData`가 포함됩니다.
2. **인바운드:** Stayfilm이 렌더링을 완료하면, Braze 데이터 변환 웹훅 URL로 콜백을 전송합니다. 변환은 응답을 일치하는 고객 프로필의 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) 및 커스텀 이벤트에 매핑합니다.
3. **전달:** 저장된 `stayfilm_video_url` 속성을 커스텀 HTML이 포함된 [인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages)와 같은 메시징 채널에서 사용합니다.

이 안내에서 데이터 변환은 다음과 같은 커스텀 속성을 기록합니다:

| 속성 | 설명 |
| --------- | ----------- |
| `stayfilm_video_status` | 렌더링 성공 시 `ready`, Stayfilm이 오류를 보고할 때 `failed` |
| `stayfilm_video_url` | 렌더링된 MP4 비디오의 URL |
| `stayfilm_job_id` | Stayfilm 작업 식별자 |
| `stayfilm_render_error` | 렌더링 실패 시 오류 메시지 |
| `stayfilm_callback_received_at` | 콜백의 ISO 타임스탬프 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 속성" }

이 변환은 `stayfilm_video_ready` 또는 `stayfilm_video_failed`라는 커스텀 이벤트도 기록합니다.

## 통합 {#integration}

다음 단계에서는 개념 증명을 위한 과정을 안내합니다. 흐름을 검증한 후, 작업 페이로드, 속성, 메시징을 사용 사례에 맞게 조정하세요.

### 1단계: 테스트 사용자 만들기 {#step-1-create-a-test-user}

통합을 구축하고 검증하는 동안 사용할 테스트 사용자 프로필을 만듭니다. 자세한 내용은 [사용자 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)를 참조하세요.

1. **오디언스** > **사용자 가져오기**로 이동합니다.
2. **빠른 사용자 추가**를 선택합니다.
3. `external_id`와 기타 필수 필드를 입력한 후 **새 사용자 만들기**를 선택합니다.

{% alert important %}
이메일, 전화번호, 성명, 정부 발급 ID, 주소, 주문 세부 정보 등 개인 데이터를 `external_id`로 사용하지 마세요. 이 통합 전체에서 `external_id`는 대소문자를 구분하는 것으로 취급하세요.
{% endalert %}

이 안내에서는 `stayfilm-poc-001`을 예시 `external_id`로 사용합니다. 이후 단계에서 사용하게 되므로 선택한 값을 기록해 두세요.

### 2단계: 데이터 변환 만들기 {#step-2-create-a-data-transformation}

Stayfilm 콜백을 수신하고 사용자 프로필을 업데이트할 데이터 변환을 만듭니다.

1. **데이터 설정** > **데이터 변환**으로 이동합니다.
2. **변환 만들기**를 선택합니다.
3. `Stayfilm Callback Data Transformation`과 같은 이름을 입력합니다.
4. **편집 환경**에서 **처음부터 시작**을 선택합니다.
5. **대상 선택** > **대상**에서 **POST: Track users**를 선택합니다.
6. **변환 만들기**를 선택합니다.
7. 기본 변환 코드를 다음으로 바꿉니다:

```javascript
const brazeExternalId = payload.RelayedData;
if (!brazeExternalId) {
  throw new Error("Missing RelayedData. Expected Stayfilm callback to relay the Braze external_id from CallbackRelayData.");
}

const idJob = payload.IdJob || null;
const producedFiles = payload.ProducedFiles || {};
const videoUrl = producedFiles?.Videos?.VideoMP4?.Url || null;
const errorMessage = payload.ErrorMessage || null;
const hasError = payload.HasError === true || Boolean(errorMessage);
const isReady = !hasError && Boolean(videoUrl);
const now = new Date().toISOString();

let brazecall = {
  attributes: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      stayfilm_video_status: isReady ? "ready" : "failed",
      stayfilm_video_url: videoUrl || null,
      stayfilm_job_id: idJob,
      stayfilm_render_error: errorMessage,
      stayfilm_callback_received_at: now
    }
  ],
  events: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      name: isReady ? "stayfilm_video_ready" : "stayfilm_video_failed",
      time: now,
      properties: {
        stayfilm_job_id: idJob,
        stayfilm_video_url: videoUrl || null,
        stayfilm_render_error: errorMessage,
        stayfilm_status: payload.Status || payload.status || null
      }
    }
  ]
};

return brazecall;
```

{: start="8"}
8. **저장**을 선택한 후 생성된 웹훅 URL을 복사합니다.
9. 다음 샘플 Stayfilm 콜백 JSON으로 웹훅 URL에 테스트 `POST` 요청을 보냅니다. `RelayedData`를 1단계에서 만든 테스트 사용자의 `external_id`로 설정합니다.

```json
{
  "IdJob": "debug-job-001",
  "HasError": false,
  "Status": "DRAFT_DONE",
  "ProducedFiles": {
    "Videos": {
      "VideoMP4": {
        "Url": "https://example.com/stayfilm-poc-video.mp4"
      }
    }
  },
  "RelayedData": "stayfilm-poc-001"
}
```

cURL, Postman 또는 유사한 도구로 요청을 보냅니다. 성공적인 응답은 HTTP 상태 `201`과 함께 `{"message": "success"}`를 반환합니다.

{: start="10"}
10. **데이터 설정** > **데이터 변환**으로 이동하고, 변환이 목록에 나타나지 않으면 페이지를 새로고침합니다.
11. 변환을 열고 **유효성 검사**를 선택합니다. **출력**에서 유효성 검사가 성공했는지 확인합니다.
12. **활성화**를 선택합니다.
13. 복사한 웹훅 URL을 콜백 URL로 Stayfilm에 제공합니다.

{% alert note %}
Braze `external_id` 외에 추가 데이터를 `CallbackRelayData`에 저장하는 경우, `RelayedData`를 적절히 파싱하도록 변환 코드를 업데이트하세요.
{% endalert %}

### 3단계: Stayfilm에 작업을 전송하는 웹훅 Campaign 만들기 {#step-3-create-a-webhook-campaign-to-send-jobs-to-stayfilm}

Stayfilm에 렌더링 작업을 제출하는 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks)을 만듭니다.

{% alert important %}
Campaign을 테스트하기 전에, Stayfilm이 2단계의 데이터 변환 콜백 URL로 프로젝트를 구성했는지 확인하세요.
{% endalert %}

1. **메시징** > **Campaigns**로 이동합니다.
2. **Campaign 만들기** > **웹훅**을 선택합니다.
3. `Stayfilm Webhook Integration`과 같은 Campaign 이름을 입력합니다.
4. **웹훅 작성** > **처음부터 시작**을 선택합니다.
5. **웹훅 작성** > **웹훅 URL**에 Stayfilm이 제공한 Stayfilm `POST /Job` 엔드포인트 URL을 입력합니다. 다음 예시에서 *`{BASE_URL}`*을 교체합니다: `https://{BASE_URL}/stg/v3/job`
6. **HTTP 메서드**를 **POST**로 설정합니다.
7. **요청 본문**에서 **Raw Text**를 선택한 후, Stayfilm이 제공하는 작업 페이로드를 붙여넣습니다. [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)를 사용하여 본문을 동적으로 만들 수 있습니다.

`CallbackRelayData`를 Braze 사용자의 `external_id`로 설정합니다. Stayfilm은 콜백에서 이 값을 `RelayedData`로 반환합니다.

{% raw %}
```json
{
  "SmartTags": ["Setup-Template"],
  "Medias": [
    {
      "Group": "userMedia",
      "URL": "https://{BASE_URL}/some_media.png"
    }
  ],
  "Videos": [{}],
  "CallbackRelayData": "stayfilm-poc-001"
}
```
{% endraw %}

다음 요청 헤더를 추가합니다:

| 키 | 값 |
| --- | ----- |
| `idproject` | Stayfilm이 제공한 `idproject` 값 |
| `Subscription-Key` | Stayfilm이 제공한 `Subscription-Key` |
| `Content-Type` | `application/json` |
| `Authorization` | 연결된 콘텐츠를 통해 검색된 OAuth 베어러 토큰(다음 예시 참조) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요청 헤더" }

다음 연결된 콘텐츠 블록에서 *`{TENANT_ID}`*, *`{CLIENT_ID}`*, *`{CLIENT_SECRET_URL_ENCODED}`*, *`{SCOPE_URL_ENCODED}`*를 Stayfilm이 제공하는 값으로 교체합니다. *`{CLIENT_SECRET_URL_ENCODED}`*와 *`{SCOPE_URL_ENCODED}`*는 블록에 붙여넣기 전에 URL 인코딩하세요. OAuth 요구 사항에 대해서는 [Stayfilm API 문서](https://apidoc.stayfilm.com)를 참조하세요.

{% raw %}
```
{% connected_content https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
  :method post
  :body grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET_URL_ENCODED}&scope={SCOPE_URL_ENCODED}
  :content_type application/x-www-form-urlencoded
  :cache_max_age 3000
  :save stayfilm_auth
%}Bearer {{stayfilm_auth.access_token}}
```
{% endraw %}

{: start="8"}
8. **초안 저장**을 선택합니다.

{% alert note %}
Campaigns 페이지를 떠났다가 돌아오는 경우, **상태**를 **전체**로 설정하면 아직 **초안** 상태인 Campaign을 찾을 수 있습니다.
{% endalert %}

### 4단계: 웹훅 Campaign 테스트 {#step-4-test-the-webhook-campaign}

1. 웹훅 작성기에서 **테스트** 탭을 선택합니다.
2. **사용자로 메시지 미리보기**에서 **기존 사용자 선택**을 선택한 후, 테스트 사용자를 검색합니다(예: `stayfilm-poc-001`).
3. **테스트 전송**을 선택합니다.

성공적인 응답은 HTTP 상태 `201`과 함께 다음과 유사한 JSON 본문을 반환합니다:

```json
{
  "IdJob": "4557a77e-f56c-48be-81f7-2d8c5e558cb1",
  "Videos": [
    {
      "IdVideo": "87287b25-7814-4fa1-ad1a-f2ea89822d0f",
      "IdGenre": "f07a1334-5904-420a-9f31-92644f245c5a",
      "IdVideoTemplate": "7b77c3df-12a1-4636-a9b4-bc227f4c233f",
      "IdProject": "73ea3e73-b41e-4676-b674-51731d3bf49c",
      "Status": "DRAFT_RENDERING_PENDING",
      "DurationInSeconds": null,
      "URL": null,
      "ErrorMessage": null,
      "CreatedAt": "2026-06-16T00:35:28.7736263Z",
      "UpdatedAt": "2026-06-16T00:35:28.7736264Z",
      "IdVideoFather": null,
      "IdVideoSon": null,
      "ProducingStatus": "PENDING"
    }
  ],
  "Images": []
}
```

### 5단계: Stayfilm 콜백 확인 {#step-5-confirm-the-stayfilm-callback}

Stayfilm은 비디오를 비동기적으로 렌더링하고, 처리가 완료되면 데이터 변환에 콜백을 보냅니다. [Stayfilm API 문서](https://apidoc.stayfilm.com)에 설명된 Stayfilm API 엔드포인트를 통해 작업 상태를 모니터링하세요.

1. **데이터 설정** > **데이터 변환**으로 이동합니다.
2. 변환의 **로그** 탭을 선택합니다.
3. **성공** 상태의 콜백이 나타나는지 확인합니다.

### 6단계: 인앱 메시지에 비디오 표시 {#step-6-display-the-video-in-an-in-app-message}

사용자 프로필에 `stayfilm_video_url`이 설정되면, Campaign 또는 Canvas에서 렌더링된 비디오를 표시합니다.

1. **메시징** > **Campaigns**로 이동합니다.
2. **Campaign 만들기** > **인앱 메시지**를 선택합니다.
3. `Stayfilm Video Show`와 같은 Campaign 이름을 입력합니다.
4. 메시지 작성기에서 **전통 편집기**를 선택합니다.
5. **전송 대상**에서 **웹 브라우저**를 선택합니다.
6. **메시지 유형**을 **커스텀 코드**로 설정합니다.
7. 다음 HTML을 **HTML** 필드에 붙여넣습니다:

{% raw %}
```html
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<div id="stayfilm-video-url" style="display: none;">{{custom_attribute.${stayfilm_video_url}}}</div>
<video id="stayfilm-video" controls preload="metadata" playsinline style="width: 100%; max-width: 420px; border-radius: 12px; background: #000;">
Your browser does not support HTML5 video.
</video>
<script>
(function () {
  var urlElement = document.getElementById("stayfilm-video-url");
  var video = document.getElementById("stayfilm-video");
  var videoUrl = urlElement ? urlElement.textContent.trim() : "";
  if (!videoUrl || videoUrl.indexOf("http") !== 0) {
    return;
  }
  var source = document.createElement("source");
  source.src = videoUrl;
  source.type = "video/mp4";
  video.appendChild(source);
  video.load();
})();
</script>
</body>
</html>
```
{% endraw %}

{: start="8"}
8. **초안 저장**을 선택합니다.
9. **테스트** 탭을 선택합니다.
10. **사용자로 메시지 미리보기**에서 **기존 사용자 선택**을 선택한 후, 테스트 사용자의 `external_id`를 검색합니다.

프로필에 `stayfilm_video_url`이 설정되어 있으면, 미리보기에서 렌더링된 비디오가 나타나고 재생됩니다.

## 통합 확장 {#extend-the-integration}

이 안내에서는 Stayfilm API의 일부만 다루고 있습니다. 작업 템플릿, 미디어 입력 또는 후속 메시징을 조정하려면 [Stayfilm API 설명서](https://apidoc.stayfilm.com)를 참조하고, 웹훅 페이로드, 데이터 변환 매핑 및 Campaign 로직을 필요에 맞게 업데이트하세요.

## 고려 사항 {#considerations}

- **비동기 렌더링:** 비디오 생성은 즉시 이루어지지 않습니다. 웹훅과 동일한 플로우에서 인앱 메시지를 전송하는 대신, `stayfilm_video_ready` 커스텀 이벤트에서 후속 메시징을 트리거하거나 `stayfilm_video_status`를 기준으로 Segment를 활용하세요.
- **식별자 일관성:** `CallbackRelayData`의 값은 Braze 사용자의 `external_id`와 정확히 일치해야 합니다.
- **OAuth 토큰 캐싱:** 연결된 콘텐츠 예시에서는 OAuth 토큰을 3000초 동안 캐싱합니다. Stayfilm에서 토큰 수명 요구 사항을 변경하는 경우 `cache_max_age`를 조정하세요.
- **샌드박스 테스트:** 프로덕션 출시 전에 Braze 샌드박스에서 전체 콜백 루프를 검증하세요.
- **커스텀 속성 용량:** 이 통합에서 생성하는 Stayfilm 커스텀 속성 및 이벤트를 수용할 수 있는 워크스페이스 용량이 충분한지 확인하세요.

## 문제 해결 {#troubleshooting}

Stayfilm 통합에 문제가 발생하면 다음 표를 참조하세요.

| 문제 | 해결 방법 |
| ----- | ---------- |
| 데이터 변환 유효성 검사 실패 | 테스트 페이로드의 `RelayedData`가 유효한 Braze `external_id`와 일치하는지 확인한 후, **Data Transformation** 페이지를 새로고침하고 **Validate**를 선택하세요. |
| 웹훅 테스트에서 201이 아닌 응답이 반환됨 | 요청 헤더에서 Stayfilm 자격 증명을 확인하고, OAuth 연결된 콘텐츠 블록이 URL 인코딩된 값을 사용하는지 확인하며, `POST /Job` URL이 올바른지 점검하세요. |
| 콜백이 변환 로그에 표시되지 않음 | Stayfilm에 활성 상태의 데이터 변환 웹훅 URL이 등록되어 있는지 확인하고, 비디오 렌더링이 완료될 때까지 시간을 두고 기다리세요. |
| 인앱 미리보기에 비디오가 표시되지 않음 | 테스트 사용자 프로필에 `stayfilm_video_url`이 설정되어 있는지, 그리고 인앱 메시지가 **Custom Code**를 사용하여 **Web Browsers**를 타겟팅하고 있는지 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="문제 해결" }