---
nav_title: 사용자 가져오기
article_title: 사용자 가져오기
page_order: 3
description: "CSV 가져오기, REST API, 클라우드 데이터 수집 등 Braze의 다양한 사용자 가져오기 옵션에 대해 알아보세요."

---
# 사용자 가져오기 {#import-users}

> CSV 가져오기, REST API, 클라우드 데이터 수집 등 Braze의 다양한 사용자 가져오기 옵션에 대해 알아보세요.

## 가져오기 옵션 {#import-options}

Braze에서 CSV 가져오기, 서버리스 S3 Lambda CSV 가져오기 스크립트, 직접 API 호출 또는 데이터 웨어하우스에서의 클라우드 데이터 수집을 통해 사용자 속성과 이벤트를 업로드할 수 있습니다.

### Braze CSV 가져오기 {#braze-csv-import}

CSV 가져오기를 사용하여 다음 사용자 속성과 커스텀 이벤트를 기록하고 업데이트할 수 있습니다. 시작하려면 [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/)를 참조하세요.

| 유형 | 정의 | 예시 | 최대 파일 크기 |
|---|---|---|---|
| 기본 속성 | Braze에서 인식하는 예약된 사용자 속성입니다. | `first_name`, `email` | 500 MB |
| 커스텀 속성 | 비즈니스에 고유한 사용자 속성입니다. | `last_destination_searched` | 500 MB |
| 커스텀 이벤트 | 사용자 행동을 나타내는 비즈니스 고유 이벤트입니다. | `trip_booked` | 50 MB |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Braze CSV 가져오기" }

#### CSV 구성하기 {#constructing-your-csv}

Braze는 표준 CSV 형식의 사용자 데이터를 허용합니다. 기본 및 커스텀 속성 가져오기는 최대 500 MB 파일을 지원하며, 커스텀 이벤트 가져오기는 최대 50 MB 파일을 지원합니다. 식별자, 열 헤더, 유효성 검사 규칙 및 예시에 대해서는 [CSV 가져오기]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import/)를 참조하세요.

대시보드에서 **사용자 가져오기**를 통해 대용량 CSV를 업로드하면, Braze가 파일을 수신하고 계산 단계를 실행하는 동안 페이지가 응답하지 않거나 느리게 응답할 수 있습니다. 업로드와 계산이 완료될 때까지 기다려 주세요. 총 소요 시간은 파일 크기에 따라 몇 분에서 몇 시간까지 걸릴 수 있으며, 파일이 클수록 계산 시간이 더 오래 걸립니다.

{% alert note %}
속성이 포함된 커스텀 이벤트를 가져올 때는 CSV 열 헤더에 점 표기법을 사용해야 합니다. 커스텀 이벤트 형식에 대한 자세한 내용은 [커스텀 이벤트 형식 이해하기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/?tab=custom%20events#understanding-custom-event-formatting)를 참조하세요.
{% endalert %}

### Lambda 사용자 CSV 가져오기 {#lambda-user-csv-import}

서버리스 S3 Lambda CSV 가져오기 스크립트를 사용하여 사용자 속성을 Braze에 업로드할 수 있습니다. 이 솔루션은 CSV 업로더로 작동하며, S3 버킷에 CSV를 드롭하면 스크립트가 API를 통해 업로드합니다.

1,000,000행이 포함된 파일의 예상 실행 시간은 약 5분입니다. 자세한 내용은 [사용자 속성 CSV를 Braze로 가져오기]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)를 참조하세요.

### REST API

[`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 사용하여 사용자의 커스텀 이벤트, 사용자 속성 및 구매를 기록할 수 있습니다.

### 클라우드 데이터 수집 {#cloud-data-ingestion}

Braze [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)을 사용하여 사용자 속성을 가져오고 유지 관리할 수 있습니다.

## HTML 유효성 검사 {#html-validation}

Braze는 가져오기 중에 HTML 데이터를 정리, 유효성 검사 또는 재포맷하지 않으므로, 웹 개인화에 사용하는 모든 가져오기 데이터에서 스크립트 태그를 제거해야 합니다.

웹 브라우저에서 개인화 용도로 사용하기 위해 Braze로 데이터를 가져올 때는 HTML, JavaScript 또는 웹 브라우저에서 렌더링될 때 악의적으로 활용될 수 있는 기타 스크립트 태그가 제거되었는지 확인하세요.

또는 HTML의 경우 Braze Liquid 필터(`strip_html`)를 사용하여 렌더링된 텍스트에서 HTML을 제거할 수 있습니다. 예시:

{% tabs local %}
{% tab 입력 %}
{% raw %}
```liquid
{{ "Have <em>you</em> read <strong>Ulysses</strong>?" | strip_html }}
```
{% endraw %}
{% endtab %}
{% tab 출력 %}
{% raw %}
```liquid
Have you read Ulysses?
```
{% endraw %}
{% endtab %}
{% endtabs %}