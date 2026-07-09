---
nav_title: "POST: 푸시 자격 증명 업데이트"
article_title: "POST: 푸시 자격 증명 업데이트"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 푸시 자격 증명 업데이트 Braze 엔드포인트에 대해 설명합니다."
---

{% api %}
# 푸시 자격 증명 업데이트 {#update-push-credentials}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/apps/push_credential/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 단일 앱의 푸시 자격 증명을 프로그래밍 방식으로 업데이트할 수 있으므로, 대시보드 UI를 사용하지 않고도 자격 증명을 관리할 수 있습니다.

각 요청은 하나의 앱과 하나의 푸시 플랫폼에 대한 푸시 자격 증명을 업데이트합니다. iOS 인증 키 또는 Firebase 서비스 계정과 같은 자격 증명 파일은 JSON 요청 본문 내에서 [Base64](https://en.wikipedia.org/wiki/Base64) 인코딩된 문자열로 전달됩니다.

이 엔드포인트는 다음 푸시 플랫폼을 지원합니다:

| 플랫폼 | 자격 증명 |
|---|---|
| iOS (APNs) | `.p8` 인증 키만 지원됩니다. `.p12` 및 `.pem` 인증서는 이 엔드포인트에서 지원되지 않습니다. |
| Android (Firebase Cloud Messaging) | 서비스 계정 JSON |
| Android (Huawei Mobile Services) | 앱 ID 및 앱 시크릿 |
| Kindle (Amazon Device Messaging) | 클라이언트 ID 및 클라이언트 시크릿 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="지원되는 푸시 플랫폼" }

## 전제 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `apps.push_credential` 권한이 있는 [API 키]({{site.baseurl}}/api/basics#rest-api-key)가 필요합니다.

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

요청당 하나의 플랫폼 객체를 포함합니다: `apple`, `firebase`, `huawei` 또는 `kindle`.

{% tabs %}
{% tab iOS (APNs) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "apple": {
    "certificate": (required, string) the Base64-encoded .p8 authentication key,
    "jwt_key_id": (required, string) the key ID for the .p8 authentication key,
    "jwt_team_id": (required, string) your Apple Developer team ID,
    "jwt_bundle_id": (required, string) your app's bundle ID,
    "apns_gateway": (required, string) either "prod" or "dev"
  }
}
```
{% endtab %}
{% tab Android (Firebase Cloud Messaging) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "firebase": {
    "credential": (required, string) the Base64-encoded Firebase service account JSON
  }
}
```
{% endtab %}
{% tab Android (Huawei Mobile Services) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "huawei": {
    "app_id": (required, string) your Huawei app ID,
    "app_secret": (required, string) your Huawei app secret
  }
}
```
{% endtab %}
{% tab Kindle (Amazon Device Messaging) %}
```json
{
  "app_id": (required, string) the app identifier API key found under Settings > App Settings,
  "kindle": {
    "client_id": (required, string) your Amazon Device Messaging client ID,
    "client_secret": (required, string) your Amazon Device Messaging client secret
  }
}
```
{% endtab %}
{% endtabs %}

## 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| [`app_id`]({{site.baseurl}}/api/identifier_types#app-identifier) | 필수 | 문자열 | 업데이트하려는 앱의 앱 식별자 API 키입니다. 대시보드에서 **설정** > **앱 설정**의 **API 키** 필드 옆에서 확인할 수 있습니다. |
| `apple` | 필수* | 객체 | iOS (APNs) 자격 증명입니다. |
| `firebase` | 필수* | 객체 | Android (Firebase Cloud Messaging) 자격 증명입니다. |
| `huawei` | 필수* | 객체 | Android (Huawei Mobile Services) 자격 증명입니다. |
| `kindle` | 필수* | 객체 | Kindle (Amazon Device Messaging) 자격 증명입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="요청 매개변수" }

\* 요청당 정확히 하나의 플랫폼 객체를 포함해야 합니다.

### iOS (APNs) 매개변수 {#ios-apns-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `certificate` | 필수 | 문자열 | Base64 인코딩된 `.p8` 인증 키입니다. `.p8` 인증 키만 지원되며, `.p12` 및 `.pem` 인증서는 이 엔드포인트에서 지원되지 않습니다. |
| `jwt_key_id` | 필수 | 문자열 | `.p8` 인증 키의 키 ID입니다. |
| `jwt_team_id` | 필수 | 문자열 | Apple Developer 팀 ID입니다. |
| `jwt_bundle_id` | 필수 | 문자열 | 앱의 번들 ID입니다. |
| `apns_gateway` | 필수 | 문자열 | APNs 환경입니다. 사용 가능한 값은 `prod` 및 `dev`입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="iOS (APNs) 매개변수" }

### Android (Firebase Cloud Messaging) 매개변수 {#android-firebase-cloud-messaging-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `credential` | 필수 | 문자열 | Base64 인코딩된 Firebase 서비스 계정 JSON입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Android (Firebase Cloud Messaging) 매개변수" }

### Android (Huawei Mobile Services) 매개변수 {#android-huawei-mobile-services-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `app_id` | 필수 | 문자열 | Huawei 앱 ID입니다. |
| `app_secret` | 필수 | 문자열 | Huawei 앱 시크릿입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Android (Huawei Mobile Services) 매개변수" }

### Kindle (Amazon Device Messaging) 매개변수 {#kindle-amazon-device-messaging-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
|---|---|---|---|
| `client_id` | 필수 | 문자열 | Amazon Device Messaging 클라이언트 ID입니다. |
| `client_secret` | 필수 | 문자열 | Amazon Device Messaging 클라이언트 시크릿입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Kindle (Amazon Device Messaging) 매개변수" }

## 요청 예시 {#example-requests}

### iOS (APNs)

`apple.certificate` 값은 Base64 인코딩되어야 하며, `apple.apns_gateway`는 `prod` 또는 `dev`로 설정해야 합니다.

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "apple": {
    "certificate": "{BASE64_ENCODED_STRING}",
    "jwt_key_id": "{YOUR_KEY_ID}",
    "jwt_team_id": "{YOUR_TEAM_ID}",
    "jwt_bundle_id": "{YOUR_BUNDLE_ID}",
    "apns_gateway": "prod"
  }
}'
```

### Android (Firebase Cloud Messaging)

`firebase.credential` 값은 Base64 인코딩되어야 합니다.

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "firebase": {
    "credential": "{BASE64_ENCODED_STRING}"
  }
}'
```

### Android (Huawei Mobile Services)

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "huawei": {
    "app_id": "{YOUR_HUAWEI_APP_ID}",
    "app_secret": "{YOUR_HUAWEI_APP_SECRET}"
  }
}'
```

### Kindle (Amazon Device Messaging)

```
curl --location --request POST 'https://rest.iad-01.braze.com/apps/push_credential/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "app_id": "{YOUR_APP_IDENTIFIER}",
  "kindle": {
    "client_id": "{YOUR_ADM_CLIENT_ID}",
    "client_secret": "{YOUR_ADM_CLIENT_SECRET}"
  }
}'
```

## 응답 예시 {#example-response}

자격 증명이 성공적으로 업데이트되면 상태 코드 `201`과 함께 응답을 받게 됩니다.

```json
{
  "message": "success"
}
```

{% endapi %}