---
nav_title: Celebrus
article_title: Celebrus 통합
description: "Braze와 Celebrus 통합."
---

# Celebrus

> Celebrus는 웹 및 모바일 앱 채널 전반에서 Braze SDK와 원활하게 통합되어 채널 활동 데이터로 Braze를 채울 수 있도록 지원합니다. 여기에는 지정된 기간 동안 디지털 자산 전반의 방문자 트래픽에 대한 포괄적인 인사이트가 포함됩니다. <br><br>또한 Celebrus는 개별 고객에 대한 풍부한 프로필 데이터를 캡처하여 Braze와 동기화할 수 있습니다. 이를 통해 포괄적이고 정확하며 상세한 퍼스트파티 데이터를 기반으로 효과적인 Braze 분석 및 커뮤니케이션 전략을 수립할 수 있습니다. 이 기능은 Celebrus의 머신 러닝 기반 Signals를 통해 더욱 강화되어, 광범위한 태깅 없이도 손쉽게 데이터를 캡처할 수 있습니다. 강력한 퍼스트파티 ID 그래프가 구축되면 모든 데이터를 즉시 사용할 수 있습니다.

_이 통합은 Celebrus에서 유지 관리합니다._

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Celebrus 계정 | 이 파트너십을 활용하려면 Celebrus 계정이 필요합니다. |
| 데이터 웨어하우스(선택 사항) | Braze 커스텀 속성용 Celebrus 커넥터를 사용하는 경우, Braze 클라우드 데이터 수집(CDI) 통합에서 지원하는 데이터 웨어하우스가 있어야 하며, Braze 대시보드에서 CDI를 구성해야 합니다. |
| Braze SDK 구성 설정(선택 사항) | Braze SDK용 Celebrus 커넥터를 사용하는 경우, SDK 엔드포인트와 SDK API 키를 전달해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 구현 {#implementation}
Celebrus 구현을 설치한 후, Braze용 Celebrus 커넥터를 사용하여 Celebrus 데이터를 Braze에 통합합니다. Braze용 Celebrus 통합에는 Braze SDK와 Braze 커스텀 속성이라는 두 가지 요소가 있습니다. Braze 사용 방식과 필요한 사용 사례에 따라 둘 중 하나 또는 둘 다 배포할 수 있습니다.

웹 채널에 Braze SDK가 아직 구현되어 있지 않은 경우, Celebrus를 사용하여 Braze SDK를 배포할 수 있습니다. Celebrus는 웹 페이지에 Braze SDK를 추가하고, Celebrus ID 그래프를 사용하여 웹 방문자의 Braze ID를 설정합니다. 고객 속성은 클라우드 데이터 수집(CDI)을 통해 Braze와 동기화할 수 있습니다. 이를 위해서는 Braze CDI에서 지원하는 데이터 웨어하우스와 Braze에서의 CDI 구성이 필요합니다.

### Braze SDK용 Celebrus 커넥터 {#celebrus-connector-for-braze-sdk}

Braze SDK용 Celebrus 커넥터는 Braze에 대한 상위 수준의 웹 및 모바일 앱 채널 데이터를 제공합니다. Braze SDK에서는 Celebrus ID 그래프의 Celebrus `System Identity`가 Braze 통합의 식별자로 사용됩니다. Braze 커스텀 속성 Celebrus 커넥터를 통해 커스텀 속성을 동기화하기 위한 다른 식별자도 지원됩니다.

이 커넥터는 채널에 Braze SDK를 배포하고 구성하므로, Braze SDK 데이터 스트림에서 일부 설정을 구성하고 다음 세 가지 설정에 대한 값을 제공해야 합니다:

```
    response.addParameter("sdk_endpoint", "sdk.xxxxxx.braze.com");
    response.addParameter("api_key", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
    response.addParameter("app_id", "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxx");
```

{% alert important %}
Braze SDK용 Celebrus 커넥터는 Braze SDK를 삽입하고 초기화하여 사용자를 식별하고 Celebrus의 ID 그래프에 식별자를 추가합니다. 이 커넥터는 고객 프로필에 데이터를 기록하거나 다른 Braze SDK 메서드를 트리거하지 않습니다. <br><br>[Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web)를 통해 데이터를 기록하거나 Braze SDK에서 지원하는 다른 기능을 활용하려면 코드베이스 내에서 원하는 메서드를 직접 호출할 수 있습니다.
{% endalert%}

### Braze 커스텀 속성용 Celebrus 커넥터 {#celebrus-connector-for-braze-custom-attributes}

#### 1단계: Celebrus에서 연결 세부 정보 구성 {#step-1-configure-connected-details-in-celebrus}

Braze 커스텀 속성용 Celebrus 커넥터는 Braze가 수신할 것으로 예상하는 형식으로 사전 포맷된 커스텀 속성을 중간 데이터베이스로 전송합니다. Celebrus에서 데이터베이스의 연결 세부 정보를 구성하며, 이는 사용 중인 데이터베이스 유형(예: Snowflake 또는 Redshift)에 따라 달라집니다.

#### 2단계: Braze 대시보드에서 클라우드 데이터 수집 구성 {#step-2-configure-cloud-data-ingestion-in-your-braze-dashboard}

이 통합은 Braze 클라우드 데이터 수집을 사용합니다. [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)의 지침에 따라 사용 중인 웨어하우스 유형에 맞게 [클라우드 데이터 수집 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 설정하고 구성합니다.

#### 3단계: Celebrus에서 Braze로 데이터 동기화 {#step-3-sync-data-from-celebrus-to-braze}

Celebrus는 이메일, 전화번호, `external_id` 또는 사용자 별칭과 같은 고유 식별자를 개인에게 캡처하고 할당한 후 CDI를 통해 Braze로 전송합니다. 이를 통해 동일한 개인에 대한 데이터를 Braze와 동기화할 수 있습니다.

Celebrus는 정의된 식별자를 사용하여 Celebrus 프로필 빌더에 정의된 고객 속성을 전송하지만, 속성 값이 변경된 경우에만 전송합니다. Celebrus 프로필 빌더에 정의된 속성 이름은 기본적으로 Braze에서 사용됩니다. 따라서 [Braze 명명 규칙]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)을 준수하도록 이러한 이름을 업데이트해야 합니다.

{% alert important %}
현재 이 릴리스는 이벤트와 구매를 지원하지 않습니다.<br><br> 이 통합은 속성을 문자열 값으로 전송하므로 일부 속성은 리스트(예: signals)입니다. 현재 리스트를 배열로 변환할 수 없습니다. 중첩된 속성은 없습니다.
{% endalert%}