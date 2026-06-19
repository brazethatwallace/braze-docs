---
nav_title: Lytics
article_title: Lytics
description: "이 참조 문서에서는 Braze와 Lytics 통합에 대해 다룹니다. Lytics는 마케터, 분석가, 기술자를 위한 엔터프라이즈 고객 데이터 플랫폼입니다. 이 통합을 통해 브랜드는 Lytics 데이터를 Braze에 직접 동기화하고 매핑할 수 있습니다."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics](https://www.lytics.com/)는 차세대 고객 중심 비즈니스를 위한 고객 데이터 플랫폼(CDP)입니다. Lytics Decision Engine, Conductor, Cloud Connect 솔루션은 마케터와 데이터 팀에게 실시간으로 개인정보 보호를 준수하면서 ID 확인, 오케스트레이션, 캠페인 최적화를 수행할 수 있는 기회를 제공합니다.

_이 통합은 Lytics에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Lytics 통합은 고객에 대한 통합 뷰를 제공하여 강력한 개인화를 가능하게 하고, 최적의 다음 행동 오케스트레이션과 의사결정을 활용하여 최적화된 캠페인을 추진합니다.

이 통합을 통해 브랜드는 다음을 수행할 수 있습니다:

- Lytics에서 Braze로 직접 오디언스 내보내기
- Braze Campaigns 또는 Canvases에서 Lytics로 실시간 이벤트를 전송하여 개인화된 캠페인을 구성하고 풍부한 고객 프로필을 구축

## 활용 사례 {#use-cases}

Braze를 Lytics에 연결하여 이메일, SMS, 푸시 활동을 [가져와](#importing-data-from-braze-to-lytics) Lytics 고객 프로필을 강화할 수 있습니다. Braze와 Lytics를 함께 사용하면 Lytics의 크로스채널, 행동 기반 오디언스를 [내보내](#integration) 퍼스트파티 데이터를 활용한 고도로 개인화된 Braze 고객 여정을 구축할 수도 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Lytics 계정 | 이 통합을 활용하려면 Lytics 계정이 필요합니다. |
| Lytics 계정 번호 | 웹훅 엔드포인트 URL을 구성하려면 Lytics 계정 번호가 필요합니다. |
| Lytics API 토큰 | Data Manager 권한이 있는 Lytics REST API 토큰입니다. <br><br> Lytics 대시보드에서 **Account Settings Console** > **Access Tokens** > **Create New Token**으로 이동하여 생성할 수 있습니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드에서 **설정** > **API 키**로 이동하여 생성할 수 있습니다. |
| Braze 인스턴스 | 사용 중인 [Braze 인스턴스]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints/)입니다. 확실하지 않은 경우 Braze 온보딩 매니저에게 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

이 섹션에서는 Lytics 데이터를 Braze로 내보내는 방법을 설명합니다.

### 1단계: 승인 생성 {#step-1-create-an-authorization}

Lytics에서 내비게이션 바의 **Data** 콘솔 내 **Authorization** 대시보드로 이동합니다. **Create New Authorization**를 선택하고 **Braze**를 검색하여 선택합니다.

표시되는 **Configure Authorization** 프롬프트에서 레이블과 설명을 입력하고 REST API 키와 Braze 인스턴스를 입력합니다. 완료되면 **Complete**를 선택합니다.

![레이블, 설명, REST API 키, Braze 인스턴스 필드가 있는 Braze용 Lytics 승인 구성 프롬프트.]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### 2단계: 새 작업 생성 {#step-2-create-a-new-job}

Lytics에서 내비게이션 바의 **Data** 콘솔 내 **Jobs** 대시보드로 이동합니다. **Create New Job**을 선택하고 **Braze**를 검색하여 선택합니다. 표시되는 **Select Job Type** 프롬프트에서 **Export Audience**를 선택합니다.

![Export Audience가 선택된 새 Braze 작업의 Lytics 작업 유형 선택 프롬프트.]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

다음으로, **Select Authorization** 옵션에서 승인을 선택합니다.

![내보내기 작업에 사용할 Braze 승인을 보여주는 Lytics 승인 선택 단계.]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### 3단계: 작업 구성 {#step-3-configure-the-job}

**Configure Job** 프롬프트에서 레이블과 선택적 설명을 입력합니다. 다음으로, **Braze External User ID Field** 입력란에서 Braze 외부 사용자 ID(`braze_id`)가 포함된 Lytics 필드를 선택합니다. 다음 단계가 가장 중요합니다—같은 프롬프트의 오디언스 선택기를 사용하여 Braze로 내보낼 오디언스를 선택합니다.

마지막으로, **Existing Users** 체크박스에서 원하는 옵션을 선택합니다. 이 체크박스를 선택한 상태로 두면 선택한 Lytics 오디언스에 이미 존재하는 사용자가 추가됩니다. 선택을 해제하면 워크플로가 시작된 후 오디언스에 진입하거나 이탈하는 사용자만 Braze로 내보내집니다.

{% alert note %}
이 체크박스를 선택하면 선택한 오디언스의 모든 기존 사용자가 Braze로 전송됩니다. Braze 요금제에 데이터 포인트가 포함된 경우 그에 따라 데이터 포인트 사용량을 모니터링하세요.
{% endalert %}

완료되면 **Complete**를 선택하여 내보내기를 시작하고 저장합니다.

![Complete 컨트롤과 Braze 오디언스 내보내기를 저장하거나 실행하는 옵션이 표시된 Lytics 내보내기 작업 요약.]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

내보내기 작업이 구성되면 Lytics는 네이티브 통합을 통해 선택한 오디언스를 Braze로 전송합니다. 다음은 Braze로 전송되는 오디언스의 JSON 구조를 보여주는 샘플 오디언스입니다.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

오디언스 내보내기에 포함된 `external_id` 중 Braze에 아직 존재하지 않는 항목에 대해 새 사용자가 Braze에 생성됩니다.

## Braze에서 Lytics로 데이터 가져오기 {#importing-data-from-braze-to-lytics}

다음 방법을 사용하여 Braze에서 Lytics로 오디언스 데이터를 가져올 수 있습니다:

- [웹훅 사용](#using-webhooks)
- [CSV 파일에서 가져오기](#from-a-csv-file)

### 웹훅 사용 {#using-webhooks}

#### 1단계: Lytics API 토큰 생성 {#step-1-create-a-lytics-api-token}

왼쪽 하단의 계정 이름을 선택하여 Lytics 계정 메뉴로 이동하고, 드롭다운 메뉴에서 **Access Tokens**를 선택합니다. 다음으로, **Create API Token**을 선택합니다.

![계정 메뉴에서 Create API Token이 선택된 Lytics Access Tokens 화면.]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

이름, 선택적 설명, 토큰 만료 기간을 입력합니다. 다음으로, API 권한에서 **Data Manager** 범위를 토글하고 **Generate Token**을 선택합니다. 토큰을 복사하여 안전한 곳에 보관합니다.

![토큰 생성 전 Data Manager 범위가 활성화된 Lytics API 토큰 권한 화면.]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### 2단계: Lytics 웹훅 URL 구성 {#step-2-configure-the-lytics-webhook-url}

Lytics 웹훅 URL은 Braze에서 Lytics API로 메시지를 전송하는 데 사용됩니다. 이 메시지는 Lytics에서 캠페인을 개인화하거나 Lytics 고객 프로필을 강화하는 데 사용할 수 있습니다. Lytics 웹훅 URL에 다음 두 가지 매개변수를 추가해야 합니다:

- Lytics 계정 번호
- Lytics API 토큰

웹훅 URL을 다음과 같이 구성합니다:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

`<ACCOUNT-NUMBER>`를 계정 번호로, `<LYTICS-API-TOKEN>`을 Lytics API 토큰으로 교체합니다.

#### 3단계: Braze에서 웹훅 생성 {#step-3-create-a-webhook-on-braze}

Braze에서 새 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)을 생성합니다. **Webhook URL** 필드에 Lytics 웹훅 URL을 추가합니다.

요청 유형(HTTP `POST` 메서드)을 정의하고 나머지 웹훅 세부 정보를 구성하면 웹훅을 테스트하고 배포할 준비가 됩니다. 다음은 Braze에서 웹훅을 구성한 후의 POST 요청 본문 샘플입니다:

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "John",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@email.com",
  "braze_id": "xxxxxx"
}
```

### CSV 파일에서 가져오기 {#from-a-csv-file}

이 섹션에서는 Braze 사용자 데이터를 세그먼트에서 Lytics로 가져오는 방법을 설명합니다.

#### 1단계: 승인 생성

Lytics에서 내비게이션 바의 **Data** 콘솔 내 **Authorization** 대시보드로 이동합니다. **Create New Authorization**를 선택하고 **Custom Integrations**를 검색하여 선택합니다.

비즈니스 및 보안 요구 사항에 따라 원하는 SFTP 승인 유형을 선택합니다. SFTP를 통해 Lytics로 파일을 가져오기 위해 지원되는 승인 유형은 다음과 같습니다:

- Client SFTP Server Authorization
- Client SFTP Server Authorization with PGP Private Key
- Lytics Managed SFTP Server Authorization

공개 키 SFTP 승인은 SFTP 내보내기 전용입니다.

![클라이언트 및 Lytics 관리 서버 선택을 포함한 Custom Integrations 가져오기용 Lytics SFTP 승인 방법 옵션.]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

표시되는 **Configure Authorization** 프롬프트에서 레이블과 설명을 입력하고 나머지 구성 요구 사항을 완료합니다. 완료되면 **Complete**를 선택합니다.

#### 2단계: 세그먼트 데이터를 CSV로 내보내기 {#step-2-export-your-segment-data-to-csv}

Braze에서 **오디언스** > **Segments**로 이동합니다. 내보내려는 세그먼트를 찾은 다음 <i class="fas fa-gear" aria-label="설정"></i>을 선택하고 **CSV Export User Data**를 선택합니다. 세그먼트에서 최대 500,000명의 사용자를 내보낼 수 있습니다. 자세한 내용은 [세그먼트 데이터를 CSV로 내보내기]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv/)를 참조하세요.

#### 3단계: CSV 가져오기 작업 구성 {#step-3-configure-a-csv-import-job}

Lytics에서 내비게이션 바의 **Data** 콘솔 내 **Jobs** 대시보드로 이동합니다. **Create New Job**을 선택하고 **Custom Integrations**를 검색하여 선택합니다.

다음으로, 작업 유형을 선택합니다. Braze CSV 파일을 Lytics로 가져오려면 작업 유형으로 **Import CSV**를 선택합니다.

![Import CSV가 작업 유형으로 선택된 Lytics Custom Integrations 작업 설정.]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

마지막으로, 작업의 레이블과 선택적 설명을 입력하고 기타 필요한 세부 정보를 구성합니다. **Complete**를 선택하여 작업을 시작하고 저장합니다.