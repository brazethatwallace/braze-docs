---
nav_title: Microsoft Azure Blob Storage
article_title: Microsoft Azure Blob Storage
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "이 참조 문서에서는 Braze Currents와 Microsoft Azure Blob Storage 간의 파트너십에 대해 설명합니다. Microsoft Azure Blob Storage는 Microsoft가 Azure 제품군의 일부로 제공하는 비정형 데이터를 위한 대규모 확장 가능한 오브젝트 스토리지입니다."
page_type: partner
tool: Currents
search_tag: Partner

---

# Microsoft Azure Blob Storage

> [Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)는 Microsoft가 Azure 제품군의 일부로 제공하는 비정형 데이터를 위한 대규모 확장 가능한 오브젝트 스토리지입니다.

{% alert important %}
클라우드 스토리지 제공업체 간에 전환하는 경우, 새로운 통합을 설정하고 검증하는 데 추가 지원이 필요하면 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

Braze와 Microsoft Azure Blob Storage 통합을 사용하면 데이터를 Azure로 다시 내보내고 Currents 데이터를 스트리밍할 수 있습니다. 이후 ETL 프로세스(추출, 변환, 로드)를 사용하여 데이터를 다른 위치로 전송할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Microsoft Azure 및 Azure 스토리지 계정 | 이 파트너십을 활용하려면 Microsoft Azure 및 Azure 스토리지 계정이 필요합니다. |
| Currents | Currents로 데이터를 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents)가 설정되어 있어야 합니다. 메시지 아카이브만 설정하는 경우에는 Currents가 필요하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합 {#integration}

Microsoft Azure Blob Storage와 통합하려면 Braze가 Azure로 데이터를 내보내거나 Currents 데이터를 스트리밍할 수 있도록 스토리지 계정과 연결 문자열이 필요합니다.

### 1단계: 스토리지 계정 생성 {#step-1-create-a-storage-account}

Microsoft Azure에서 사이드바의 **Storage Accounts**로 이동하고 **+ Add**를 클릭하여 새 스토리지 계정을 생성합니다. 다음으로 스토리지 계정 이름을 입력합니다. 다른 기본값 설정은 업데이트할 필요가 없습니다. 마지막으로 **Review + create**를 선택합니다.

이미 스토리지 계정이 있더라도 Braze 데이터 전용으로 새 계정을 생성하는 것을 권장합니다.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### 2단계: 연결 문자열 가져오기 {#step-2-get-the-connection-string}

스토리지 계정이 배포되면 스토리지 계정에서 **Access Keys** 메뉴로 이동하여 연결 문자열을 확인합니다.

Microsoft는 하나의 키를 재생성하는 동안 다른 키를 사용하여 연결을 유지할 수 있도록 두 개의 액세스 키를 제공합니다. 둘 중 하나의 연결 문자열만 있으면 됩니다.

{% alert note %}
Braze는 이 메뉴의 키가 아닌 연결 문자열을 사용합니다.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### 3단계: Blob 서비스 컨테이너 생성 {#step-3-create-a-blob-service-container}

스토리지 계정의 **Blob Service** 섹션 아래에 있는 **Blobs** 메뉴로 이동합니다. 앞서 생성한 스토리지 계정 내에 Blob 서비스 컨테이너를 생성합니다.

Blob 서비스 컨테이너의 이름을 입력합니다. 다른 기본값 설정은 업데이트할 필요가 없습니다.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### 4단계: Currents 설정 {#step-4-set-up-currents}

Braze에서 **Currents > + Create Current > Azure Blob Data Export**로 이동하여 통합 이름과 연락처 이메일을 입력합니다.

다음으로 연결 문자열, 컨테이너 이름, BlobStorage 접두사(선택 사항)를 입력합니다.

![Braze의 Microsoft Azure Blob Storage Currents 페이지. 이 페이지에는 통합 이름, 연락처 이메일, 연결 문자열, 컨테이너 이름 및 접두사 필드가 있습니다.]({% image_buster /assets/img/maz.png %})

마지막으로 페이지 하단으로 스크롤하여 내보내려는 메시지 참여 이벤트 또는 고객 행동 이벤트를 선택합니다. 완료되면 Current를 시작합니다.

### 5단계: Azure 데이터 내보내기 설정 {#step-5-set-up-azure-data-export}

다음은 아래 용도로 사용되는 자격 증명을 구성합니다:
1. API를 통한 Segment 내보내기
2. CSV 내보내기(Campaign, Segment, Canvas 사용자 데이터를 대시보드를 통해 내보내기)
3. 참여 보고서

Braze에서 **파트너 통합** > **기술 파트너** > **Microsoft Azure**로 이동하여 연결 문자열, Azure 스토리지 컨테이너 이름, Azure 스토리지 접두사를 입력합니다.

다음으로 **Make this the default data export destination** 체크박스가 선택되어 있는지 확인합니다. 이렇게 하면 내보낸 데이터가 Azure로 전송됩니다. 완료되면 통합을 저장합니다.

![Braze의 Microsoft Azure 데이터 내보내기 페이지. 이 페이지에는 연결 문자열, 컨테이너 이름 및 접두사 필드가 있습니다.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
연결 문자열을 최신 상태로 유지하는 것이 중요합니다. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지합니다. **48시간** 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

## 내보내기 동작 {#export-behavior}

클라우드 데이터 스토리지 솔루션을 통합한 사용자가 API, 대시보드 보고서 또는 CSV 보고서를 내보내려고 하면 다음과 같은 결과가 나타납니다:

- 모든 API 내보내기는 응답 본문에 다운로드 URL을 반환하지 않으며 데이터 스토리지를 통해 검색해야 합니다.
- 모든 대시보드 보고서 및 CSV 보고서는 다운로드를 위해 사용자의 이메일로 전송되며(스토리지 권한 불필요) 데이터 스토리지에 백업됩니다.

{% alert important %}
**JSON 형식 요구 사항**: JSON 내보내기의 경우 Braze는 각 줄에 별도의 JSON 오브젝트가 포함되는 JSONL(줄 바꿈으로 구분된 JSON) 형식을 사용합니다. 이 형식은 단일 JSON 배열 또는 오브젝트인 표준 JSON과는 다릅니다. 내보낸 파일의 각 줄은 유효한 JSON 오브젝트이지만 파일 전체가 하나의 유효한 JSON 문서는 아닙니다. 이러한 파일을 처리할 때는 전체 파일을 하나의 JSON 문서로 구문 분석하지 말고 각 줄을 별도의 JSON 오브젝트로 개별적으로 구문 분석하세요.

Currents 내보내기는 JSON이 아닌 Apache Avro 형식(`.avro` 파일)을 사용합니다. 이 JSON 형식 요구 사항은 JSON 형식을 사용하는 대시보드 데이터 내보내기 및 API 내보내기에 적용됩니다.
{% endalert %}

## FAQ

### Braze에서 Azure Blob Storage에 대한 허용 목록용 IP 주소를 제공할 수 있나요? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Braze는 Currents 또는 대시보드 내보내기를 위한 Azure Blob Storage용 고정 IP 허용 목록을 게시하지 않습니다. Braze는 사용자가 제공한 연결 문자열과 컨테이너 이름을 사용하여 컨테이너에 데이터를 기록하며, Azure는 스토리지 계정 설정(예: 스토리지 계정의 방화벽 규칙 또는 프라이빗 엔드포인트)을 통해 네트워크 액세스를 제어합니다.

보안 팀에서 IP 기반 제한이 필요한 경우, Braze의 IP 목록 대신 스토리지 계정의 Azure 네트워킹 기능을 사용하세요. 설정 단계는 [Azure Storage 보안에 대한 Microsoft 설명서](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)를 참조하세요.