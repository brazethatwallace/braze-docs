---
nav_title: Hightouch
article_title: Hightouch
description: "이 참조 문서에서는 고객 데이터를 웨어하우스에서 비즈니스 도구로 동기화하는 플랫폼인 Hightouch와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Hightouch

> [Hightouch](https://hightouch.io)는 IT 또는 엔지니어링 팀의 도움 없이 웨어하우스나 데이터 레이크에서 원하는 앱으로 고객, 제품 또는 독점 데이터를 동기화할 수 있는 최신 데이터 통합 플랫폼입니다.

Braze와 Hightouch 통합을 사용하면 데이터 웨어하우스의 최신 고객 데이터를 활용하여 Braze에서 더 나은 Campaign(캠페인)을 구축할 수 있습니다. 고객 데이터를 Braze로 자동 동기화하면 데이터 일관성에 대해 걱정할 필요 없이 세계 최고 수준의 고객 경험을 구축하는 데 집중할 수 있습니다.

이 통합을 통해 [사용자 코호트를 Braze로 가져와]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/hightouch_cohort_import) 웨어하우스에만 존재할 수 있는 데이터를 기반으로 타겟 Campaign을 발송할 수도 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Hightouch 계정 | 이 파트너십을 활용하려면 Hightouch 계정이 필요합니다.
| Braze REST API 키 | `users.track` 및 `users.export.ids` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)에 따라 달라집니다.<br><br>Hightouch는 Braze 인스턴스가 위치한 클러스터 이름이 필요합니다. 예를 들어, Braze 엔드포인트가 `https://rest.iad-01.braze.com`인 경우 `iad-01`만 필요합니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 사용 사례 {#use-cases}

* 사용자 및 계정 데이터를 Braze로 동기화하여 초개인화된 Campaign을 구축합니다.
* 웨어하우스의 최신 데이터로 Braze Segments를 자동으로 업데이트합니다.
* 다른 고객 터치포인트의 데이터를 Braze로 가져와 더 나은 경험을 제공합니다.
* 사용자 코호트를 Braze로 가져와 타겟 Campaign 및 Canvases를 발송할 수 있습니다.

## 통합 {#integration}

### 1단계: Hightouch Braze 대상 생성 {#step-1-create-your-hightouch-braze-destination}

1. Hightouch 플랫폼의 **Destinations** 섹션에서 **Add destination**을 클릭합니다.
2. 사용 가능한 대상 목록에서 **Braze**를 선택합니다.
3. Braze REST 엔드포인트("https://rest." 제외)와 Braze REST API 키를 입력합니다.<br><br>![엔드포인트 및 API 키 필드가 있는 Hightouch Braze 대상 설정 양식.]({% image_buster /assets/img/hightouch/hightouch_braze_setup.png %})

### 2단계: 오브젝트 및 이벤트 동기화 {#step-2-object-and-event-syncing}

Hightouch는 사용자 오브젝트와 이벤트 모두에 대한 동기화를 지원합니다.

| 대상 | 설명 | 지원 모드 |
|---|---|---|
| 오브젝트 | 대상의 사용자 또는 조직과 같은 오브젝트에 레코드를 동기화합니다. | Upsert 또는 update |
| 이벤트 | 대상에 이벤트로 레코드를 동기화합니다. 일반적으로 track 호출 형태입니다. | Track event 또는 track purchase |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Step 2: Object and event syncing" }

{% alert note %}
동기화가 데이터 포인트 기록 방식에 미치는 영향에 대한 자세한 내용은 [Hightouch](https://hightouch.com/docs/destinations/braze#syncing-and-data-point-consumption)를 참조하세요.
{% endalert %}

#### Braze 오브젝트 동기화 {#syncing-braze-objects}

Hightouch 오브젝트(사용자 필드)를 동등한 Braze 기본 또는 커스텀 필드에 동기화할 수 있습니다. 레코드 매칭을 수행하여 두 플랫폼 간의 데이터를 통합하는 데 도움을 줄 수도 있습니다.

#### Braze 이벤트 동기화 {#syncing-braze-events}

Hightouch를 사용하면 이벤트 및 구매 데이터를 추적하고 Braze에 동기화할 수 있습니다. Hightouch에서 추적 데이터 설정 및 존재하지 않는 사용자 동작 정의 등 동기화 동작에 영향을 미치는 여러 옵션을 설정할 수 있습니다.

{% alert important %}
오브젝트 및 이벤트 동기화에 대한 자세한 지침은 [Hightouch 설명서](https://hightouch.io/docs/destinations/braze/)에서 확인할 수 있습니다.
{% endalert %}



## 통합 데모 {#integration-demo}

<div class="video-container">
    <iframe width="560" height="315" src="https://drive.google.com/file/d/1KQdCwZzV88hXMx7AMWgh8izqkldtNv5p/preview" title="Hightouch 통합 데모" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>