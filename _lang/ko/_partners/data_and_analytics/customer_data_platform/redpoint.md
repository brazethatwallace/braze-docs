---
nav_title: Redpoint
article_title: Redpoint
description: "Redpoint와 Braze의 통합을 통해 퍼스트파티 데이터를 사용하여 Braze 고객 프로필을 온보딩하고 보강할 수 있습니다."
alias: /partners/redpoint/
page_type: partner
search_tag: Redpoint
---

# Redpoint

> [Redpoint](https://www.redpointglobal.com)는 마케터에게 완전히 통합된 Campaign 오케스트레이션 플랫폼을 제공하는 기술 플랫폼입니다. Redpoint의 세분화, 스케줄링 및 자동화 기능을 활용하여 CDP 데이터를 Braze로 가져오는 방법과 시기를 제어할 수 있습니다.

_이 통합은 Redpoint에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Redpoint 통합을 통해 Redpoint CDP 데이터를 기반으로 Braze Segments를 생성할 수 있습니다. Redpoint는 Braze로 데이터를 전달하는 두 가지 모드를 제공합니다:

1. **Braze Onboarding and Upsert** 모드: Redpoint에서 Braze로 고객 프로필을 "업서트"합니다. 이 모드는 데이터가 변경되었을 때 사용자 레코드를 온보딩하거나 업데이트하는 데 사용됩니다.
2. **Braze Append** 모드: 해당 사용자가 이미 Braze에 존재하는 경우에만 고객 프로필을 업데이트합니다.

각 모드에 대해 내보내기 템플릿과 아웃바운드 채널을 구성합니다.

{% alert note %}
"업서트(Upsert)"는 "업데이트(update)"와 "삽입(insert)"의 합성어입니다. 데이터베이스 테이블에 새 레코드가 존재하지 않으면 삽입하고, 이미 존재하면 업데이트하려는 경우에 사용됩니다. 기본적으로 업서트는 특정 레코드가 데이터베이스에 있는지 확인합니다. 레코드가 있으면 업데이트되고, 없으면 새 레코드가 삽입됩니다.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Redpoint Data Management 아티팩트 | Braze 통합은 Redpoint Data Management 아티팩트 세트로 지원됩니다. [Redpoint 고객지원](https://support.redpointglobal.com/hc/en-us/restricted?return_to=https%3A%2F%2Fsupport.redpointglobal.com%2Fhc%2Fen-us)에 문의하여 사용 중인 Redpoint Data Management 버전에 맞는 아티팩트를 요청하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Redpoint CDP 커스텀 속성 {#redpoint-cdp-custom-attributes}

다음 Redpoint 커스텀 속성을 Braze 고객 프로필에 추가할 수 있습니다.

| 필드               | 설명                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `rpi_cdp_attributes` | Redpoint CDP 프로필 속성 오브젝트                                                                                  |
| `rpi_audience_outputs`| Redpoint Outbound Delivery Braze 채널 실행에서 사용자가 타겟팅된 오디언스 출력 태그 배열         |
| `rpi_offers`         | Redpoint Outbound Delivery Braze 채널 실행에서 사용자가 타겟팅된 오퍼 태그 배열                   |
| `rpi_contact_ids`    | Redpoint Outbound Delivery Braze 채널 실행에서 사용자가 타겟팅된 오퍼 이력 연락처 ID 배열     |
| `rpi_channel_exec_ids`| Redpoint Outbound Delivery Braze 채널 실행에서 사용자가 타겟팅된 채널 실행 ID 배열       |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Redpoint CDP custom attributes" }

![Braze 고객 프로필에 추가된 필드를 보여주는 Redpoint CDP 커스텀 속성 테이블.]({% image_buster /assets/img/redpoint/rpi_to_braze_custom_attributes.png %}){: style="max-width:75%;"}

## 통합 {#integration}

### 1단계: 템플릿 설정 {#step-1-set-up-templates}

#### 1a단계: Braze Onboarding and Upsert 템플릿 생성 {#step-1a-create-the-braze-onboarding-and-upsert-template}

Redpoint Interaction(RPI)에서 새 내보내기 템플릿을 생성하고 **Braze Onboarding and Upsert**로 이름을 지정합니다. 이 템플릿은 Redpoint CDP와 Braze 고객 프로필 간의 핵심 매핑과 Braze의 고객 프로필에 추가하려는 추가 커스텀 속성을 정의합니다.

Redpoint CDP 속성을 **Attribute** 열로 드래그합니다. 각 **Header Row Value**를 해당하는 Braze [사용자 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)으로 설정합니다.

다음 표는 Redpoint CDP 속성과 해당하는 Braze 속성을 나열합니다:

| Redpoint 속성 | Header Row Value |
|--------------------|------------------|
| PID                | `external_id`    |
| First Name          | `first_name`     |
| Last Name          | `last_name`      |
| Primary Email      | `email`          |
| Primary Country    | `country`        |
| DOB                | `dob`            |
| Gender             | `gender`         |
| Primary City       | `home_city`      |
| Primary Phone      | `phone`          |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1a: Create the Braze Onboarding and Upsert template" }

**Offer History** 테이블에서 **Output Name** 속성을 추가합니다. 마지막으로 Braze에 병합하려는 추가 커스텀 Redpoint 속성을 추가합니다. 예를 들어, 다음은 학력, 소득, 결혼 여부를 추가 속성으로 포함한 온보딩 및 업서트 템플릿입니다.

![속성-헤더 매핑을 보여주는 Redpoint 온보딩 및 업서트 내보내기 템플릿.]({% image_buster /assets/img/redpoint/rpi_to_braze_upsert_export_format.png %}){: style="max-width:75%;"}

#### 1b단계: Braze Append 템플릿 생성 {#step-1b-create-the-braze-append-template}

추가 전용 작업을 위한 두 번째 내보내기 템플릿을 **Braze Append**라는 이름으로 생성합니다.

이 템플릿에는 두 가지 속성만 설정합니다. **PID**의 경우 **Header Row Value**를 `external_id`로 설정합니다. **Output Name**의 경우 **Header Row**를 `output_name`으로 설정합니다.

![`external_id` 및 출력 이름 속성이 포함된 샘플 내보내기 템플릿.]({% image_buster /assets/img/redpoint/rpi_to_braze_append_export_format.png %}){: style="max-width:75%;"}

#### 1c단계: 날짜 형식 설정 {#step-1c-set-date-format}

두 내보내기 템플릿 모두에서 **Options** 탭으로 이동하여 **Date Format**을 **Custom Format** 값으로 설정합니다. 형식을 **yyyy-MM-dd**로 설정합니다.

![yyyy-MM-dd로 설정된 날짜 형식을 보여주는 옵션 탭.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_format_config.png %}){: style="max-width:75%;"}

### 2단계: 아웃바운드 채널 생성 {#step-2-create-outbound-channels}

RPI에서 두 개의 새 채널을 생성합니다. 두 채널 모두 **Outbound Delivery**로 설정합니다. 하나의 채널 이름을 **Braze Onboarding and Upsert**로, 다른 하나를 **Braze Append**로 지정합니다.

![Redpoint 아웃바운드 전달 채널 구성 일반 탭.]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_general.png %}){: style="max-width:75%;"}

{% alert note %}
CDP 레코드를 Braze에 처음 온보딩한 후, Braze Onboarding and Upsert 채널을 사용하는 후속 Redpoint Interaction 워크플로가 초기 온보딩 동기화 이후 변경된 레코드만 선택하도록 설계되었는지 확인하세요.
{% endalert %}

### 3단계: 채널 구성 {#step-3-configure-the-channels}

#### 3a단계: 템플릿 및 내보내기 경로 형식 설정 {#step-3a-set-template-and-export-path-format}

채널 **Configuration** 화면의 **General** 탭으로 이동합니다. 각 채널에 해당하는 내보내기 템플릿을 설정합니다.

다음으로, 두 채널 모두에서 Redpoint Interaction과 Redpoint Data Management 모두 접근 가능한 공유 네트워크, 파일 전송 프로토콜 또는 외부 콘텐츠 제공자 위치를 가리키는 **Export path format**을 정의합니다.

![내보내기 템플릿 및 내보내기 경로 형식 필드가 포함된 Redpoint 채널 구성.]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_specific.png %}){: style="max-width:75%;"}

두 채널의 내보내기 디렉토리 형식은 동일하며 `\\[Channel]\\[Offer]\\[Workflow ID]`로 끝나야 합니다.

![채널, 오퍼, 워크플로 ID로 끝나는 Redpoint 내보내기 디렉토리 경로 형식.]({% image_buster /assets/img/redpoint/rpi_to_braze_export_directory_setup.png %}){: style="max-width:50%;"}

#### 3b단계: 사후 실행 구성 {#step-3b-configure-post-execution}

채널 **Configuration** 화면의 **Post Execution** 탭으로 이동합니다.

**Post-execution** 체크박스를 선택하여 채널 실행 후 서비스 URL을 호출합니다. Redpoint Data Management 웹 서비스 URL을 입력합니다. 이 항목은 Onboarding 채널과 Append 채널 모두에서 동일합니다.

![서비스 URL이 구성된 Redpoint 사후 실행 설정.]({% image_buster /assets/img/redpoint/rpi_to_braze_channel_config_post_execution.png %}){: style="max-width:75%;"}

### 4단계: Redpoint Data Management에서 Braze 구성요소 설정 {#step-4-set-up-braze-components-in-redpoint-data-management}

Braze 통합을 지원하는 Redpoint Data Management(RPDM) 아티팩트가 포함된 아카이브에는 필수 구성요소 설정에 대한 자세한 지침이 담긴 README가 포함되어 있습니다. 통합을 구성할 때 다음 세부 사항을 유의하세요.

#### 4a단계: Braze REST 엔드포인트 및 기본 RPI 출력 디렉토리로 RPI to Braze 자동화 업데이트 {#step-4a-update-the-rpi-to-braze-automation-with-your-braze-rest-endpoint-and-base-rpi-output-directory}

Braze 관련 아티팩트를 Redpoint Data Management로 가져온 후, **AUTO_Process_RPI_to_Braze**라는 이름의 자동화를 열고 다음 두 자동화 변수를 사용자 환경에 맞는 값으로 업데이트합니다:

* **BRAZE_API_URL**: Braze REST 엔드포인트
* **BASE_OUTPUT_DIRECTORY**: Redpoint Interaction과 Redpoint Data Management 간의 공유 출력 디렉토리

![BRAZE_API_URL 및 BASE_OUTPUT_DIRECTORY 값을 보여주는 Redpoint 자동화 변수.]({% image_buster /assets/img/redpoint/rpi_to_braze_auto_variables.png %}){: style="max-width:40%;"}

#### 4b단계: RPI to Braze Append 프로젝트 업데이트 {#step-4b-update-the-rpi-to-braze-append-project}

**PROJ_RPI_to_Braze_Append**라는 이름의 Redpoint Data Management 프로젝트에는 Braze의 `rpi_cdp_attributes` 커스텀 속성 오브젝트에 대한 아웃바운드 전달 내보내기 파일 스키마 및 매핑이 포함되어 있습니다.

내보내기 파일 템플릿에 정의된 추가 커스텀 CDP 속성으로 파일 입력 스키마와 **RPI to Braze Document Injector**라는 이름의 문서 인젝터 도구를 업데이트합니다. 이 예시는 학력, 소득, 결혼 여부의 추가 매핑을 보여줍니다:

![Braze 커스텀 CDP 속성에 대한 Redpoint 문서 인젝터 매핑.]({% image_buster /assets/img/redpoint/rpi_to_braze_doc_injector_mappings.png %}){: style="max-width:40%;"}

## 통합 사용 {#using-the-integration}

이제 Outbound Delivery Braze 채널을 Redpoint Interaction 워크플로 내에서 활용할 수 있습니다. RPI에서 선택 규칙과 오디언스를 생성하고, 관련 워크플로 스케줄 및 트리거를 구축하는 표준 방법을 따르세요.

RPI 오디언스 출력을 Braze에 동기화하려면 아웃바운드 전달 오퍼를 생성하고 **Braze Onboarding and Upsert** 또는 **Braze Append** 채널에 연결합니다. 이는 Braze에서 새 레코드를 생성하거나 병합하려는 것인지, 아니면 레코드가 이미 Braze에 존재하는 경우에만 캠페인 데이터를 추가하려는 것인지에 따라 달라집니다.

![Braze 아웃바운드 전달 채널을 사용하는 Redpoint Interaction Canvas 워크플로.]({% image_buster /assets/img/redpoint/rpi_to_braze_rpi_canvas.png %}){: style="max-width:80%;"}

RPI에서 워크플로가 성공적으로 실행되면, RPI에서 소싱된 오케스트레이션 및 CDP 데이터를 사용하여 Braze에서 Segments를 생성할 수 있습니다.

![Redpoint에서 동기화된 오디언스 데이터를 사용하는 Braze Segment 빌더.]({% image_buster /assets/img/redpoint/rpi_to_braze_build_braze_segment.png %}){: style="max-width:80%;"}

고객 프로필에서 Redpoint 관련 속성을 확인할 수 있습니다.

![Redpoint 관련 커스텀 속성을 보여주는 Braze 고객 프로필.]({% image_buster /assets/img/redpoint/rpi_to_braze_record_example.png %}){: style="max-width:80%;"}