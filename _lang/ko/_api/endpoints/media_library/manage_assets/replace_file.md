---
nav_title: "PUT: 미디어 라이브러리의 자산 교체"
article_title: "PUT: 미디어 라이브러리의 자산 교체"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "이 문서에서는 `PUT /media_library/replace_file` 엔드포인트에 대한 세부 정보를 설명합니다."
---

{% api %}
# 미디어 라이브러리의 자산 교체 {#replace-an-asset-in-the-media-library}
{% apimethod put %}
/media_library/replace_file
{% endapimethod %}

> 이 엔드포인트를 사용하여 [Braze 미디어 라이브러리]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/)에 있는 기존 자산의 파일을 자산 ID와 URL을 유지하면서 교체할 수 있습니다. 외부에서 호스팅되는 URL(`asset_url`) 또는 요청 본문에 포함된 바이너리 파일 데이터(`asset_file`)를 사용하여 교체 파일을 제공할 수 있습니다.

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `media_library.replace` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='media_library' %}

## 요청 본문 {#request-body}

`asset_url`을 포함하면 엔드포인트가 해당 URL에서 파일을 다운로드합니다. `asset_file`을 포함하면 엔드포인트가 요청 본문의 바이너리 데이터를 사용합니다.

`asset_url`에 대한 요청 본문 예시:

```json
{
  "asset_id": "your-asset-id",
  "asset_url": "https://cdn.example.com/assets/cat.jpg"
}
```

`asset_file`에 대한 요청 본문 예시:

```json
{
  "asset_id": "your-asset-id",
  "asset_file": <BINARY FILE DATA>
}
```

요청 본문에는 다음 매개변수가 포함됩니다:

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | -------- | --------- | ----------- |
| `asset_id` | 필수 | 문자열 | 교체할 자산의 ID입니다. |
| `asset_url` | 선택 사항 | 문자열 | 교체 파일에 대한 공개적으로 접근 가능한 URL입니다. |
| `asset_file` | 선택 사항 | 바이너리 | 교체 파일의 바이너리 파일 데이터입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request body" }

{% alert important %}
`asset_url`과 `asset_file`은 상호 배타적이므로 API 요청에 둘 중 하나만 포함해야 합니다.
{% endalert %}

### 교체 파일 요구 사항 {#replacement-file-requirements}

- 교체 파일의 확장자는 기존 자산의 확장자와 정확히 일치해야 합니다. 예를 들어, `.png` 자산을 `.jpg` 파일로 교체할 수 없습니다.
- 이미지, SVG, 문서, 글꼴, 연락처 카드 및 코드 파일에 대해 파일 교체가 지원됩니다. 동영상 자산은 교체할 수 없습니다.

## 요청 예시 {#example-request}

이 섹션에는 URL을 사용하여 자산을 교체하는 것과 바이너리 파일 데이터를 사용하는 것, 두 가지 `curl` 요청 예시가 포함되어 있습니다.

이 요청은 `asset_url`을 사용하여 미디어 라이브러리의 자산을 교체하는 예시를 보여줍니다.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_url": "https://cdn.example.com/assets/cat.jpg"}'
```

이 요청은 `asset_file`을 사용하여 미디어 라이브러리의 자산을 교체하는 예시를 보여줍니다.

```
curl -X PUT --location 'https://rest.iad-01.braze.com/media_library/replace_file' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_id": "your-asset-id", "asset_file":<BINARY FILE DATA>}'
```

### 오류 응답 {#error-responses}

이 섹션에서는 잠재적인 오류와 해당 메시지 및 설명을 나열합니다.

#### 유효성 검사 오류 {#validation-errors}

유효성 검사 오류는 다음과 같은 구조를 반환합니다:

```json
{
  "message": (String) Human-readable error description
}
```

이 표에는 가능한 유효성 검사 오류가 나열되어 있습니다.

| HTTP 상태 | 메시지 | 설명 |
| --- | --- | --- |
| 400 | "asset_id is required." | 요청에 자산 ID가 제공되지 않았습니다. |
| 400 | "Either file or asset_url is required." | `asset_file` 또는 `asset_url`이 제공되지 않았습니다. 둘 중 하나가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Validation errors" }

#### 처리 오류 {#processing-errors}

처리 오류는 오류 코드가 포함된 다른 응답을 반환합니다:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

이 표에는 가능한 처리 오류가 나열되어 있습니다.

| 오류 코드 | HTTP 상태 | 설명 |
| --- | --- | --- |
| `ASSET_NOT_FOUND` | 404 | 이 워크스페이스에 지정된 `asset_id`를 가진 자산이 없습니다. `meta` 오브젝트에 `asset_id`가 포함됩니다. |
| `INVALID_ASSET_URL` | 400 | `asset_url` 값이 유효한 URI가 아닙니다. `meta` 오브젝트에 `asset_url`이 포함됩니다. |
| `EXTENSION_MISMATCH` | 400 | 교체 파일의 확장자가 기존 자산의 확장자와 일치하지 않습니다. `meta` 오브젝트에 `expected_extension`과 `received_extension`이 포함됩니다. |
| `UNSUPPORTED_ASSET_TYPE_FOR_REPLACE` | 400 | 이 자산 유형(예: 동영상)에 대해서는 파일 교체가 지원되지 않습니다. `meta` 오브젝트에 `asset_type`이 포함됩니다. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | 파일이 허용되는 최대 크기를 초과합니다. `meta` 오브젝트에 `size_limit_bytes`와 `file_size_bytes`가 포함됩니다. |
| `CORRUPT_FILE` | 400 | 이미지 파일이 손상되었거나 읽을 수 없습니다. `meta` 오브젝트에 `file_name`이 포함됩니다. |
| `GENERIC_ERROR` | 500 | 파일 교체 중 예기치 않은 오류가 발생했습니다. `meta` 오브젝트에 디버깅을 위한 `original_error`가 포함됩니다. 다시 시도하거나 [고객지원]({{site.baseurl}}/support_contact/)에 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Processing errors" }

## 응답 {#response}

이 엔드포인트에 대한 상태 코드 응답은 `200`, `400`, `404`, `429`, `500` 다섯 가지입니다.

다음 JSON은 예상되는 응답 형태를 보여줍니다.

```json
{
  "info": "Asset file updated successfully.",
  "new_image_asset": {
    "name": (String) the name of the asset,
    "size": (Integer) the byte size of the asset,
    "url": (String) the URL to access the asset,
    "ext": (String) the file extension (e.g., "png", "jpg", "gif")
  }
}
```

{% endapi %}