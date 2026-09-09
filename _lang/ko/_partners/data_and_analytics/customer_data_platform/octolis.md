---
nav_title: Octolis
article_title: Octolis
description: "이 참조 문서에서는 데이터를 Braze에 통합할 수 있는 데이터 활성화 플랫폼인 Octolis와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis](http://octolis.com)는 강력한 데이터 활성화 플랫폼(또는 헤드리스 고객 데이터 플랫폼)입니다. 사용자가 소유한 데이터베이스 위에서 작동하는 Octolis는 비즈니스 도구에서 데이터를 통합, 준비, 스코어링 및 동기화하는 간편한 방법입니다.

_이 통합은 Octolis에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Octolis 통합은 원시 데이터 소스와 Braze 사이의 미들웨어 역할을 하며, 온라인 및 오프라인의 다양한 소스에서 데이터를 검색하고 통합할 수 있도록 합니다.
1. Eshop, CRM, POS 시스템 등의 소스에서 데이터를 통합하고 결합합니다.
2. 정규화 및 스코어링을 수행합니다.
3. 계산된 필드와 이벤트를 Braze에 실시간으로 동기화합니다.

![Octolis 데이터 소스, 처리 및 Braze로의 동기화 흐름을 보여주는 아키텍처 다이어그램.]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Octolis 계정 | 이 파트너십을 활용하려면 Octolis 계정이 필요합니다. |
| Braze REST API 키 | [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track) 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze 앱 키 | 앱 식별자 키입니다. **Braze 대시보드 > 설정 관리 > API 키**에서 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

통합을 시작하기 전에 연결, 소스, 오디언스 및 동기화에 대한 다음 섹션을 참조하세요.

자세한 내용은 Octolis [시작하기](https://help.octolis.com/) 섹션을 참조하세요.

### 1단계: Octolis를 데이터 소스에 연결하기 {#step-1-connect-octolis-to-your-data-sources}

Braze에 데이터를 전송하려면 최소 하나의 [오디언스](https://help.octolis.com/audiences/create-a-no-code-audience)를 생성해야 합니다. 오디언스는 여러 데이터 소스를 결합하고, 준비 단계를 적용하며, 계산된 필드를 추가합니다.

이러한 오디언스는 여러 데이터 소스를 기반으로 구축해야 합니다. 소스는 다음 중 하나일 수 있습니다.
- Salesforce 오브젝트(연락처, 계정 등)
- Zendesk 오브젝트(티켓)
- SFTP 내의 파일(연락처가 포함된 CSV 파일, 이벤트가 포함된 JSON 파일 등)
- 데이터베이스의 테이블/뷰
- 시스템 중 하나가 웹훅 또는 API 호출을 통해 레코드를 전송

### 2단계: Braze를 대상으로 추가하기 {#step-2-add-braze-as-a-destination}

다음으로, Braze를 새 대상으로 설정하려면 메인 화면의 현재 대상 상단에서 **+ Add more**를 선택하고 사용 가능한 비즈니스 도구에서 **Braze**를 선택합니다.

![사용 가능한 비즈니스 도구에서 Braze가 선택된 Octolis 대상 선택 화면.]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

선택한 후 다음 정보를 입력합니다.

- Braze API 키: Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다.
- 시간 기간: Octolis가 지정된 기간 동안 사용량 제한을 적용합니다.
- 요청 볼륨: 이 시간 범위 내에서 수행할 수 있는 요청 수입니다.
- 커스텀 속성: 여기에서 Braze에 전송할 새 필드, 형식(문자열, 정수, 플로트)을 지정하고, 동기화에 필수로 지정하려면 **Required for syncs**를 선택합니다.

![API 키, 사용량 제한 및 커스텀 속성에 대한 Octolis Braze 대상 구성 필드.]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

설정이 완료되면 홈 화면에 Braze가 새 대상으로 표시됩니다.

### 3단계: 새 동기화 생성하기 {#step-3-create-a-new-sync}

메뉴에서 **Syncs**를 클릭하고 액션 바에서 **Add sync**를 선택합니다. 이전에 생성한 오디언스에서 원하는 오디언스를 선택합니다.
다음으로, 대상으로 **Braze**를 선택하고 데이터를 전송할 엔티티를 선택합니다.

![오디언스 및 Braze 대상 선택을 보여주는 Octolis 동기화 생성 화면.]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### 4단계: 출력 설정 구성하기 {#step-4-set-output-settings}

기본적으로 Braze는 전송하는 모든 속성을 생성하지만, 동기화할 필드 목록을 문서화해야 합니다.

![Braze 필드 매핑 및 동기화 스케줄링을 위한 Octolis 출력 설정 화면.]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

다음은 설정 필드에 대한 구체적인 정의입니다.

| 필드 | 설명 |
| --- | --- |
| 오디언스를 어디에 동기화하시겠습니까? | 레코드를 생성하거나 업데이트할 Braze 엔티티입니다. |
| 레코드를 식별하는 데 사용되는 필드는 무엇입니까? | Braze에 레코드가 이미 존재하는 경우 Octolis가 레코드를 식별하는 데 사용할 필드입니다. |
| 각 레코드를 얼마나 자주 전송하시겠습니까? | 기본적으로 모든 통합(API, 데이터베이스, FTP)에 대해 동기화는 증분 방식으로 수행됩니다. 즉, 마지막 업데이트 이후의 새 값만 업데이트됩니다. 필요한 경우 정기적으로 전체 테이블을 전송할 수도 있습니다. 초기화 시 Octolis는 전체 테이블을 전송합니다. |
| 어떤 필드를 동기화해야 합니까? | Octolis에서 Braze로의 필드 매핑입니다. 사용 가능한 모든 필드 목록이 드롭다운 메뉴에 표시됩니다. 계산된 필드를 Braze에 전송하려면 먼저 Braze 엔티티 내에 해당 열을 생성했는지 확인해야 합니다. |
| 오디언스를 언제 동기화하시겠습니까? | 데이터가 Braze에 전송되는 방식: 수동, 실시간 또는 예약. |
| 레코드가 다음일 때 동기화... | 생성: 옵트인의 경우 Braze 테이블이 마스터로 유지되는 것이 중요합니다. 필드가 업데이트될 때 Octolis가 동기화를 트리거하는 것을 원하지 않습니다.<br><br>업데이트: 반면에, 예를 들어 이름 필드의 경우 고객이 새 항목을 제공할 때마다 Braze 테이블의 필드를 업데이트할 수 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="4단계: 출력 설정 구성하기" }

## 다중 키 중복 제거 {#multi-keys-deduplication}

중복 제거는 여러 소스, 특히 온라인과 오프라인의 데이터를 조정할 때 주요 과제입니다. Octolis의 고급 노코드 모듈을 통해 여러 키를 사용하여 [중복 제거](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work)를 수행할 수 있습니다. 이 모듈은 각 마스터 테이블에서 사용할 수 있으므로 각 엔티티에 맞게 로직을 조정할 수 있습니다.