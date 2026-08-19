---
nav_title: 크로스 도메인 웹 SDK 사용자 연결
article_title: 기기 ID를 통한 크로스 도메인 웹 SDK 사용자 연결
page_order: 1
page_type: reference
description: "Braze 웹 SDK 기기 ID를 Kitchenerie의 마케팅 사이트에서 별도의 쇼핑 도메인으로 전달하여 익명 활동이 하나의 고객 프로필을 공유하도록 합니다."
---

# 기기 ID를 통한 크로스 도메인 웹 SDK 사용자 연결 {#link-cross-domain-web-sdk-users-through-device-id}

> 두 도메인이 쿠키를 공유할 수 없는 경우, 목적지 URL을 통해 Braze 웹 SDK 기기 ID를 전달하면 두 사이트의 익명 세션이 동일한 Braze 고객 프로필에 매핑됩니다.

## 이 예제에 대하여 {#about-this-example}

가상의 주방용품 소매업체인 Kitchenerie는 마케팅 사이트(`kitchenerie.com`)와 쇼핑몰(`kitchenerie.shop`)을 운영하고 있습니다. 각 도메인에는 자체 Braze 웹 SDK 통합이 있습니다. 브라우저 쿠키는 도메인 간에 공유되지 않으므로, 동일한 사용자가 마케팅 사이트에서 쇼핑몰로 이동할 때 Braze는 별도의 기기 ID와 별도의 익명 프로필을 할당합니다.

이 패턴은 다음과 같이 동작합니다:

1. SDK 초기화 후 소스 도메인에서 `getDeviceId`로 기기 ID를 읽습니다.
2. 아웃바운드 링크에 쿼리 파라미터(예: `brazeDeviceId`)로 기기 ID를 추가합니다.
3. 목적지 도메인에서 해당 파라미터를 읽고 `deviceId` 옵션을 통해 `braze.initialize`에 전달합니다.

이 핸드오프는 익명 사용자에게 가장 중요합니다. 사용자가 쇼핑몰에서 로그인한 후에는 `external_id`를 사용한 `changeUser`가 기기 간 영구 식별자가 됩니다. [사용자 ID 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)을 참조하세요.

두 도메인 모두 동일한 Braze 워크스페이스 API 키와 SDK 엔드포인트를 사용해야 이벤트가 하나의 프로필에 기록됩니다.

## 고려 사항 {#considerations}

- 기기 ID는 브라우저별로 고유합니다. 이 패턴은 서로 다른 브라우저, 기기 또는 프로필 간의 활동을 연결하지 않습니다. 인증된 크로스 기기 식별에는 `changeUser`를 통한 `external_id`를 사용하세요.
- 소스 도메인에서 웹 SDK가 초기화된 후에만 기기 ID를 가져올 수 있습니다. `initialize` 전에 `getDeviceId`를 호출하면 값이 반환되지 않습니다.
- 웹 SDK는 `initialize` 시 `deviceId`를 한 번만 읽습니다. 초기화 후 활성 기기 ID를 변경하는 `setDeviceId`는 없습니다. 목적지 도메인에서 `initialize`를 호출하기 전에 URL 파라미터를 읽으세요.
- `brazeDeviceId` 없이 쇼핑몰에 직접 방문하거나, 북마크 또는 서드파티 추천을 통해 방문하는 경우 기본 기기 ID 할당으로 폴백해야 합니다. 이는 상속할 소스 도메인 ID가 없을 때 예상되는 동작입니다.
- 쿼리 파라미터는 브라우저 기록과 서버 로그에 표시됩니다.
- 쿼리 파라미터는 리퍼러 헤더를 통해 유출될 수 있습니다. 기기 ID 자체는 PII가 아니지만, 개인정보 보호 팀에서 요구하는 경우 사용 후 파라미터를 제거하세요(2단계 참조).
- 포괄적인 테스트를 수행하세요. 네트워크 검사를 통해 도메인 2의 이벤트가 예상 기기 ID를 사용하는지 확인하세요.
- 호스트 이름, 링크 셀렉터 및 오류 처리를 사이트에 맞게 조정하세요. 프로덕션 배포 전에 개발 환경에서 테스트하세요.

## 설정 {#setup}

### 1단계: 소스 도메인의 크로스 도메인 링크에 기기 ID 추가 {#step-1-append-the-device-id-to-cross-domain-links-on-the-source-domain}

`kitchenerie.com`(도메인 1)에서 웹 SDK를 평소처럼 초기화한 다음, `kitchenerie.shop`(도메인 2)을 가리키는 링크에 현재 기기 ID를 추가합니다.

사이트와 충돌하지 않는 쿼리 파라미터 이름을 선택하세요(이 예제에서는 `brazeDeviceId`를 사용합니다). 서버 렌더링 링크, 클라이언트 측 내비게이션 또는 제어 가능한 iframe `src` 값에도 동일한 아이디어가 적용됩니다.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
});
braze.openSession();

const destinationHost = "kitchenerie.shop";

braze.getDeviceId(function (deviceId) {
  if (!deviceId) {
    return;
  }

  const links = document.querySelectorAll('a[href*="' + destinationHost + '"]');

  links.forEach(function (link) {
    try {
      const url = new URL(link.href);
      url.searchParams.set("brazeDeviceId", deviceId);
      link.href = url.toString();
    } catch (e) {
      // Skip malformed hrefs (for example, javascript:, mailto:, or unparsable relative paths).
    }
  });
});
```

SDK 버전이 `getDeviceId`를 동기적으로(콜백 없이) 제공하는 경우, 초기화 후 대신 호출하세요:

```javascript
const deviceId = braze.getDeviceId();
```

[웹 SDK 리포지토리 가이드 — 기기 ID 가져오기]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#get-device-id) 및 [초기화 옵션 — `deviceId`]({{site.baseurl}}/developer_guide/sdk_repository_guides/web#initialization-options)를 참조하세요.

### 2단계: 목적지 도메인에서 기기 ID를 읽고 웹 SDK 초기화 {#step-2-read-the-device-id-and-initialize-the-web-sdk-on-the-destination-domain}

`kitchenerie.shop`(도메인 2)에서 `initialize` 전에 쿼리 문자열에서 `brazeDeviceId`를 읽고, 값이 있으면 초기화 옵션에 전달합니다.

```javascript
import * as braze from "@braze/web-sdk";

const urlParams = new URLSearchParams(window.location.search);
const passedDeviceId = urlParams.get("brazeDeviceId");

const initOptions = {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
};

if (passedDeviceId) {
  initOptions.deviceId = passedDeviceId;
}

braze.initialize("YOUR-API-KEY-HERE", initOptions);
braze.openSession();

// Optional: remove the parameter from the visible URL after consumption.
if (passedDeviceId) {
  const cleanUrl = new URL(window.location.href);
  cleanUrl.searchParams.delete("brazeDeviceId");
  window.history.replaceState({}, document.title, cleanUrl.toString());
}
```

사용자가 로그인하면 `external_id`와 함께 `changeUser`를 호출하여 이후 활동이 식별된 프로필에 연결되도록 합니다.

### 3단계: 핸드오프 확인 {#step-3-verify-the-handoff}

1. 로그인하지 않은 브라우저에서 도메인 1을 엽니다.
2. 크로스 도메인 링크를 따라 도메인 2로 이동합니다.
3. 브라우저 네트워크 탭에서 도메인 2가 도메인 1에서 사용한 것과 동일한 기기 ID로 이벤트를 전송하는지 확인합니다.
4. 도메인 2에 직접 방문(쿼리 파라미터 없이)하여 새 기기 ID가 할당되는지 확인합니다.

## 관련 문서 {#related-articles}

- [웹 SDK 리포지토리 가이드]({{site.baseurl}}/developer_guide/sdk_repository_guides/web)
- [Braze 웹 SDK 멀티 도메인 통합]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration)
- [Braze SDK를 통한 사용자 ID 설정]({{site.baseurl}}/developer_guide/analytics/setting_user_ids)
- [익명 사용자]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/anonymous_users)
- [사용자 프로필 수명주기]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [웹 SDK 저장소]({{site.baseurl}}/developer_guide/storage)