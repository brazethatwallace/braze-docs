---
nav_title: Nexla
article_title: Nexla
description: "이 참조 문서에서는 Braze와 Nexla의 파트너십에 대해 설명합니다. Nexla는 Braze 커런츠 사용자가 데이터 레이크 데이터를 추출, 변환 및 커스텀 형식으로 다른 위치에 로드할 수 있도록 하는 통합 데이터 운영 플랫폼입니다."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> [Nexla](https://www.nexla.com)는 통합 데이터 운영 분야의 리더이자 2021 Gartner Cool Vendor입니다. Nexla 플랫폼은 확장 가능한 데이터 흐름을 생성하고, 비즈니스 및 데이터 팀을 위해 관리되는 데이터 운영, 협업, 민첩성을 제공하기 위한 도구를 제공합니다. 데이터를 다루는 팀은 노코드/로우코드 통합 환경을 통해 모든 사용 사례에 대해 데이터를 통합, 변환, 프로비저닝 및 모니터링할 수 있습니다.

Braze와 Nexla 통합을 통해 [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)를 사용하는 고객은 Nexla를 활용하여 데이터 레이크 데이터를 추출, 변환 및 커스텀 형식으로 다른 위치에 로드할 수 있으므로, 전체 에코시스템에서 데이터에 쉽게 접근할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Nexla 계정 | 이 파트너십을 활용하려면 [Nexla 계정](https://www.nexla.com/get-demo)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints))에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 사용 사례 {#use-cases}

Nexla의 제품형 데이터인 [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information)를 사용하면 메타데이터 관리 없이도 모든 형식의 데이터로 작업할 수 있습니다. Nexla로 Braze와 주고받는 데이터 흐름을 설정하면 몇 분 안에 노코드 도구를 사용할 수 있습니다. 데이터 흐름이 대상에 설정되면 Nexla는 흐름을 모니터링하고 데이터의 양에 따라 확장합니다.

## 통합 {#integration}

### 1단계: Nexla 계정 생성 {#step-1-create-a-nexla-account}

아직 Nexla 계정이 없다면 Nexla [웹사이트](https://www.nexla.com)에서 무료 데모 및 체험판을 요청하세요. 그런 다음 [www.dataops.nexla.io](https://www.dataops.nexla.io)에 로그인하고 새 자격 증명으로 로그인합니다.

### 2단계: 소스 추가 {#step-2-add-your-source}

#### Braze가 데이터 소스인 경우 {#if-braze-is-your-data-source}
1. Nexla 플랫폼에서 탐색 도구 모음의 **Flows** > **Create a New Flow**로 이동합니다.
2. **Create New Source**를 클릭하고 Braze 커넥터를 선택한 다음 **Next**를 클릭합니다.
3. **Add a New Credential**을 선택하고 자격 증명 이름을 지정한 후 Braze API 키와 REST 엔드포인트를 추가하고 **Save**를 클릭합니다.
4. 마지막으로 데이터를 선택하고 **Save**를 클릭합니다.

Nexla는 데이터 소스에서 사용 가능한 데이터를 검색하고 변환 또는 대상에 전송하기 위한 [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information)을 생성합니다.

#### Braze가 대상인 경우 {#if-braze-is-your-destination}

[Nexla에 소스 연결하기](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source)에 대한 Nexla 설명서를 참조하세요.

### 3단계: 변환(선택 사항) {#step-3-transform-optional}

데이터에 커스텀 [변환](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations)을 수행하거나 Nexla의 사전 구축된 커넥터를 사용하려면 데이터셋에서 **Transform** 버튼을 클릭하여 Transform Builder로 진입합니다. Transform Builder 사용에 대한 안내는 [Nexla 설명서](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data)에서 확인할 수 있습니다.

### 4단계: 대상으로 전송 {#step-4-send-to-destination}

데이터를 대상으로 전송하려면 데이터셋에서 **Send to Destination** 화살표를 클릭하고 Nexla의 대상 커넥터 중 하나를 선택하거나, 다른 소스를 사용한 경우 Braze를 선택합니다. 자격 증명을 입력하고 대상 옵션을 구성한 다음 **Save**를 클릭합니다. 지정한 형식으로 선택한 대상에 데이터가 즉시 흐르기 시작합니다.

## 이 통합 사용하기 {#using-this-integration}

흐름이 설정되면 추가 작업이 필요하지 않습니다. Nexla는 소스 데이터의 변경 사항을 처리하고, 새로운 데이터에 맞게 확장하며, 스키마 변경이나 오류가 발생하면 분류를 위해 알림을 보냅니다. 변환, 소스 또는 대상을 변경하려면 해당 옵션을 클릭하여 변경하면 되며, Nexla가 즉시 흐름을 업데이트합니다.