---
nav_title: 데이터 수집 옵션 비교
article_title: 영구 및 제로 카피 데이터 수집 옵션 비교
page_order: 1
page_type: reference
description: "Cloud Data Ingestion 표준 동기화, CDI Segments, CDI Canvas 트리거, /users/track API를 비교하여 웨어하우스 또는 애플리케이션 데이터가 Braze 프로필, Segments 및 Canvases에 도달하는 방식을 선택합니다."
---

# 영구 및 제로 카피 데이터 수집 옵션 비교 {#compare-persistent-and-zero-copy-data-ingestion-options}

> 수집 파이프라인을 설계하기 전에, 웨어하우스 또는 애플리케이션의 데이터가 Braze에 도달하는 방식을 선택하세요. 사용자 프로필에 복사할지, 세분화를 위해 그 자리에서 쿼리할지, 또는 일시적으로 Canvas에 전달할지 결정합니다.

## 이 예시 소개 {#about-this-example}

MovieCanon은 가상의 영화 스트리밍 서비스입니다. 고객, 티켓 및 시청 데이터를 웨어하우스에 집중 관리합니다. 데이터 팀은 세 가지 일반적인 요구 사항에 맞춰 Braze에 데이터를 공급하는 방법을 결정해야 합니다.

- **프로필 데이터:** Braze 사용자 프로필에 영구적으로 유지되는 로열티 등급, LTV 및 장르 또는 형식 선호도 속성
- **오디언스 구축:** 모든 열을 Braze에 복사하지 않고 웨어하우스 테이블에서 SQL 기반으로 생성하는 Segments
- **트리거 메시징:** 프로필에 저장할 필요 없는 행별 개인화와 함께 Canvas에 진입해야 하는 웨어하우스 행

Braze는 네 가지 주요 수집 경로를 제공합니다. 표준 Cloud Data Ingestion(CDI) 동기화와 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) API는 모두 프로필에 데이터를 영구 저장합니다. CDI Segments(Connected Sources)와 CDI Canvas 트리거는 제로 카피 옵션으로, 웨어하우스 데이터가 웨어하우스에 그대로 유지되며 Braze 사용자 프로필에 기록되지 않습니다.

아키텍처를 계획하거나, 처리량을 산정하거나, 엔지니어링 및 마케팅 이해관계자에게 트레이드오프를 설명할 때 이 비교를 활용하세요. 각 옵션에 대한 통합 설정 가이드를 대체하지는 않습니다.

## 고려 사항 {#considerations}

- Cloud Data Ingestion은 포괄적인 기능입니다. 표준 CDI 동기화는 데이터를 Braze 프로필로 복사합니다(`/users/track`과 유사). CDI Segments와 CDI Canvas 트리거는 Braze 사용자 프로필에 기록하지 않고 웨어하우스 데이터를 그 자리에 유지합니다.
- CDI 반복 동기화는 최소 15분 간격에서 최대 월 1회까지 실행할 수 있습니다. 15분보다 높은 빈도가 필요한 경우 고객 성공 매니저에게 문의하거나 REST API 수집을 사용하세요. [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)을 참조하세요.
- CDI Canvas 트리거는 해당 엔드포인트에 대한 다른 트래픽과 [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases) REST API 사용량 제한을 공유합니다. `/users/track`에는 자체 제한 및 일괄 처리 규칙이 있습니다. 기본값 제한은 상향 조정할 수 있습니다. **설정** > **API 및 식별자** > **API 제한**으로 이동하고, [API 사용량 제한]({{site.baseurl}}/api/api_limits)을 참조하세요.
- Connected Sources와 CDI 세그먼트 확장은 웨어하우스에서 쿼리를 실행합니다. 웨어하우스 컴퓨팅 비용이 발생하며, Braze는 해당 쿼리에 대해 데이터 포인트를 기록하지 않습니다. [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)를 참조하세요.

## 설정 {#setup}

### 1단계: 사용 사례를 수집 경로에 매핑 {#step-1-map-your-use-case-to-an-ingestion-path}

목표를 권장 수집 경로 및 해당 경로의 Braze 프로필 기록 여부에 매핑합니다.

| 목표 | 권장 경로 | 프로필 기록 여부 |
| --- | --- | --- |
| 웨어하우스의 속성, 이벤트, 구매 또는 카탈로그 항목을 영구 저장 | 표준 CDI 동기화 | 예(데이터가 Braze 프로필 또는 카탈로그에 복사됨) |
| 소스 테이블을 Braze에 복사하지 않고 웨어하우스 SQL로 오디언스 구축 | CDI Segments(Connected Sources) | 아니요(멤버십만 해당) |
| 프로필에 영구 저장하면 안 되는 웨어하우스 행 컨텍스트와 함께 사용자를 Canvas에 진입시키기 | CDI Canvas 트리거 | 아니요(일시적 Canvas 컨텍스트 속성) |
| 앱, 서버 또는 스트리밍 파이프라인에서 거의 실시간으로 데이터 푸시 | [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)(또는 SDK) | 예(데이터가 프로필에 영구 저장됨) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용 사례를 수집 경로에 매핑" }

### 2단계: 영구성, 지연 시간 및 처리량 비교 {#step-2-compare-persistence-latency-and-throughput}

각 경로가 데이터 상주, 지연 시간, 처리량 및 사용자 생성을 처리하는 방식을 비교합니다.

| 차원 | 표준 CDI 동기화 | CDI Segments | CDI Canvas 트리거 | `/users/track` |
| --- | --- | --- | --- | --- |
| 기능 | 웨어하우스 테이블의 예약된 읽기로, 속성, 이벤트, 구매, 사용자 삭제 또는 카탈로그를 기록 | Braze가 SQL 세그먼트 확장을 위해 웨어하우스를 쿼리 | 웨어하우스 행이 행 컨텍스트를 Canvas 컨텍스트 속성으로 사용하여 Canvas 진입을 트리거 | 앱, 서버 또는 스트리밍 파이프라인이 속성, 이벤트 및 구매를 프로필에 기록 |
| 데이터 상주 | Braze 프로필에 복사 및 영구 저장 | 웨어하우스에 유지; 프로필에 기록되지 않음 | Canvas 컨텍스트 속성은 일시적; 프로필에 영구 저장되지 않음 | Braze 프로필에 복사 및 영구 저장 |
| 일반적인 지연 시간 | 실시간이 아님; 최소 15분 동기화 주기(웨어하우스 최신성도 적용됨) | 실시간이 아님; 세그먼트 확장 스케줄에 따라 새로고침(웨어하우스 변경마다 멤버십이 업데이트되지 않음) | 실시간이 아님; 동기화 스케줄에 따라 제한(최소 15분) | 거의 실시간(비동기 처리) |
| 처리량 참고 사항 | 동기화당 전체 쿼리 결과; Braze가 내부적으로 `/users/track`, `/users/delete` 또는 카탈로그 엔드포인트로 일괄 처리 | Connected Source당 60분 쿼리 실행 시간 제한; 요청당 객체 제한 없음 | `/canvas/trigger/send` 사용량 제한 공유; 동기화 실행당 시간당 약 375만 건의 Canvas 진입 | 요청당 최대 75개의 결합된 객체; [API 사용량 제한]({{site.baseurl}}/api/api_limits) 참조 |
| 배치 크기 | 웨어하우스 읽기에 대한 CDI 측 객체별 제한 없음 | 해당 없음(쿼리 출력이 멤버십을 정의) | 동기화 실행당 웨어하우스 행당 하나의 Canvas 진입 | 요청당 75개의 속성, 이벤트 및 구매 결합(기본값) |
| 사용자 생성 | 예(기존 사용자만 업데이트가 설정되지 않은 경우) | 아니요(쿼리 결과의 알 수 없는 사용자는 무시됨) | 아니요(기존 Braze 사용자만 해당) | 예(`_update_existing_only`가 true가 아닌 경우) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="영구성, 지연 시간 및 처리량 비교" }

### 3단계: 스키마 및 식별자 요구 사항 비교 {#step-3-compare-schema-and-identifier-requirements}

각 경로의 필수 열과 지원되는 식별자를 비교합니다. 표준 CDI 동기화당 하나의 데이터 유형을 구성합니다(예: 하나의 통합에 속성, 다른 통합에 이벤트).

| 차원 | 표준 CDI 동기화 | CDI Segments | CDI Canvas 트리거 | `/users/track` |
| --- | --- | --- | --- | --- |
| 필수 열 / 형태 | 사용자 식별자 + `UPDATED_AT` + 행별 `PAYLOAD`(JSON) | SQL은 `external_user_id`만 출력해야 함 | 식별자 + `UPDATED_AT` + `PROPERTIES`(JSON; 비어 있을 때 `{}` 사용) | 표준 `/users/track` 요청 본문 |
| 지원되는 식별자 | `external_id`, 사용자 별칭, `braze_id`, 이메일 또는 전화번호 | `external_user_id`만(문자열) | `external_id` 또는 사용자 별칭만 | `external_id`, 사용자 별칭, `braze_id`, 이메일 또는 전화번호 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="스키마 및 식별자 요구 사항 비교" }

### 4단계: 선택한 경로 구현 {#step-4-implement-the-path-you-selected}

- **표준 CDI 동기화:** 웨어하우스 테이블 또는 뷰를 생성한 다음 [Cloud Data Ingestion 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations) 및 [테이블 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)을 따릅니다.
- **CDI Segments:** [Connected Source]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)를 추가한 다음 [CDI 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)을 생성합니다.
- **CDI Canvas 트리거:** `PROPERTIES`가 포함된 소스 테이블을 설정하고, 대상 Canvas를 구축 및 실행한 다음 [CDI를 사용한 제로 카피 개인화]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)에 따라 동기화를 생성합니다.
- **`/users/track`:** 애플리케이션 또는 미들웨어에서 요청을 전송합니다. [POST: 사용자 생성 및 업데이트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)에 따라 페이로드를 포맷합니다.

MovieCanon의 일반적인 패턴은 다음과 같습니다. 야간 프로필 보강을 위한 표준 CDI 동기화, 웨어하우스 전용 오디언스 규칙을 위한 CDI Segments, 행 수준 컨텍스트가 포함된 티켓 상태 또는 시청 여정을 위한 Canvas 트리거, 실시간 앱 이벤트를 위한 `/users/track`입니다.

## 관련 문서 {#related-articles}

- [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)
- [Connected Sources]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)
- [CDI를 사용한 제로 카피 개인화]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync)
- [CDI 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)
- [Cloud Data Ingestion 테이블 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)
- [POST: 사용자 생성 및 업데이트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)
- [API 사용량 제한]({{site.baseurl}}/api/api_limits)