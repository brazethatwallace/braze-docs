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

## 사전 요구 사항 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Microsoft Azure 및 Azure 스토리지 계정 | 이 파트너십을 활용하려면 Microsoft Azure 및 Azure 스토리지 계정이 필요합니다. |
| Currents | 데이터를 Currents로 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents)가 설정되어 있어야 합니다. 메시지 아카이빙만 설정하는 경우에는 Currents가 필요하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 통합 {#integration}

Microsoft Azure Blob Storage와 통합하려면 Braze가 Azure로 데이터를 내보내거나 Currents 데이터를 스트리밍할 수 있도록 스토리지 계정과 컨테이너가 필요합니다. Braze는 두 가지 인증 방법을 지원합니다:

- [연결 문자열 방법](#connection-string-auth-method)
- [인증서 서비스 주체 방법](#certificate-service-principal-auth-method) (Currents 전용)

## 연결 문자열 인증 방법 {#connection-string-auth-method}

### 1단계: 스토리지 계정 만들기 {#step-1-create-a-storage-account}

Microsoft Azure에서 사이드바의 **Storage Accounts**로 이동하고 **+ Add**를 클릭하여 새 스토리지 계정을 만듭니다. 그런 다음 스토리지 계정 이름을 입력합니다. 다른 기본 설정은 업데이트할 필요가 없습니다. 마지막으로 **Review + create**를 선택합니다.

이미 스토리지 계정이 있더라도 Braze 데이터 전용으로 새 계정을 만드는 것을 권장합니다.

![Microsoft Azure 스토리지 계정 만들기 페이지의 기본 탭에서 스토리지 계정 이름 필드가 강조 표시되어 있습니다.]({% image_buster /assets/img/azure-currents-step-1.png %})

### 2단계: 연결 문자열 가져오기 {#step-2-get-the-connection-string}

스토리지 계정이 배포되면 스토리지 계정에서 **Access Keys** 메뉴로 이동하여 연결 문자열을 확인합니다.

Microsoft는 하나의 키를 재생성하는 동안 다른 키로 연결을 유지할 수 있도록 두 개의 액세스 키를 제공합니다. 둘 중 하나의 연결 문자열만 있으면 됩니다.

{% alert note %}
Braze는 이 메뉴의 키가 아닌 연결 문자열을 사용합니다.
{% endalert %}

![Azure 스토리지 계정의 액세스 키 페이지에서 key1 아래의 연결 문자열 필드가 강조 표시되어 있습니다.]({% image_buster /assets/img/azure-currents-step-2.png %})

### 3단계: Blob 서비스 컨테이너 만들기 {#step-3-create-a-blob-service-container}

스토리지 계정의 **Blob Service** 섹션 아래에 있는 **Blobs** 메뉴로 이동합니다. 앞서 만든 스토리지 계정 내에 Blob 서비스 컨테이너를 만듭니다.

Blob 서비스 컨테이너의 이름을 입력합니다. 다른 기본 설정은 업데이트할 필요가 없습니다.

![Azure 스토리지 계정의 Blob Service 아래 Blobs 페이지에서 컨테이너를 추가하는 옵션이 표시되어 있습니다.]({% image_buster /assets/img/azure-currents-step-3.png %})

### 4단계: Currents 설정하기 {#step-4-set-up-currents}

Braze에서 **Currents > + Create Current > Azure Blob Data Export**로 이동하여 통합 이름과 연락처 이메일을 입력합니다.

그런 다음 연결 문자열, 컨테이너 이름, BlobStorage 접두사(선택 사항)를 입력합니다.

![Braze의 Microsoft Azure Blob 스토리지 Currents 페이지. 이 페이지에는 통합 이름, 연락처 이메일, 연결 문자열, 컨테이너 이름, 접두사 필드가 있습니다.]({% image_buster /assets/img/maz.png %})

마지막으로 페이지 하단으로 스크롤하여 내보내려는 메시지 인게이지먼트 이벤트 또는 고객 행동 이벤트를 선택합니다. 완료되면 Current를 시작합니다.

### 5단계: Azure 데이터 내보내기 설정하기 {#step-5-set-up-azure-data-export}

다음은 아래 용도로 사용되는 자격 증명을 구성합니다:
1. API를 통한 Segment 내보내기
2. CSV 내보내기(Campaign, Segment, Canvas 사용자 데이터를 대시보드를 통해 내보내기)
3. 참여 보고서

Braze에서 **파트너 통합** > **기술 파트너** > **Microsoft Azure**로 이동하여 연결 문자열, Azure 스토리지 컨테이너 이름, Azure 스토리지 접두사를 입력합니다.

그런 다음 **Make this the default data export destination** 체크박스가 선택되어 있는지 확인합니다. 이렇게 하면 내보낸 데이터가 Azure로 전송됩니다. 완료되면 통합을 저장합니다.

![Braze의 Microsoft Azure 데이터 내보내기 페이지. 이 페이지에는 연결 문자열, 컨테이너 이름, 접두사 필드가 있습니다.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
연결 문자열을 최신 상태로 유지하는 것이 중요합니다. 커넥터의 자격 증명이 만료되면 커넥터가 이벤트 전송을 중지합니다. 이 상태가 48시간 이상 지속되면 커넥터의 이벤트가 삭제되고 데이터가 영구적으로 손실됩니다.
{% endalert %}

## 인증서 서비스 주체 인증 방법 {#certificate-service-principal-auth-method}

이 방법은 인증서를 사용하여 Microsoft Entra ID에 인증한 다음, 공유 계정 키 없이 Azure 역할 기반 액세스 제어(RBAC)를 사용하여 컨테이너에 데이터를 기록합니다. Braze Currents에서만 사용할 수 있습니다.

{% alert note %}
공개 인증서만 Microsoft Entra ID에 업로드하며, 비공개 키는 Azure로 전송되지 않습니다. Braze는 인증서와 비공개 키를 저장 시 암호화하여 보관하고, [Storage Blob Data Contributor](#cert-sp-4) 역할을 통해서만 액세스를 허용하며, Azure의 앱 등록에서 인증서를 제거하면 언제든지 해당 액세스를 취소할 수 있습니다.
{% endalert %}

시작하기 전에 [연결 문자열 방법](#connection-string-auth-method)에 설명된 대로 [스토리지 계정을 생성](#step-1-create-a-storage-account)하고 [Blob 서비스 컨테이너를 생성](#step-3-create-a-blob-service-container)합니다.

### 1단계: 애플리케이션 등록 {#cert-sp-1}

Microsoft Azure에서 **Microsoft Entra ID** > **App registrations** > **+ New registration**으로 이동합니다. 이름을 입력하고(예: `braze-currents`), **Register**를 선택합니다. 자세한 단계는 Microsoft의 [Register an application with the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)을 참조하세요.

새 앱 등록의 **Overview** 페이지에서 다음 값을 기록해 두세요. [6단계](#cert-sp-6)에서 두 값 모두 Braze에 제공해야 합니다.

- **Application (client) ID**
- **Directory (tenant) ID**

### 2단계: 인증서 생성 {#cert-sp-2}

Braze는 인증서를 사용하여 인증합니다. **공개 인증서**를 Azure에 업로드하고, **인증서와 비공개 키**를 Braze에 제공합니다.

자체 서명 인증서와 암호화되지 않은 2048비트 RSA 비공개 키를 생성하려면 다음을 실행합니다:

```bash
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem \
  -days 730 -nodes -subj "/CN=braze-currents"
```

이 명령은 두 개의 파일을 생성합니다:

| 파일 | 용도 |
| ---- | ------- |
| `cert.pem` | 공개 인증서입니다. 다음 단계에서 Azure에 업로드합니다. |
| `key.pem` | 비공개 키입니다. Azure에 업로드하지 마세요. [6단계](#cert-sp-6)에서 Braze에 제공합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="인증서 파일" }

{% alert important %}
비공개 키는 암호화되지 않은 상태여야 하며, 암호로 보호할 수 없습니다. 공개 인증서만 Azure에 업로드하고, 비공개 키는 절대 업로드하지 마세요.
{% endalert %}

**이미 인증서가 있으신가요?** 기존 인증서가 `.pfx` 파일로 있는 경우(예: Azure Key Vault, 인증 기관, 또는 [Microsoft의 PowerShell 방법](https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-self-signed-certificate)에서 발급받은 경우), 새로 생성하는 대신 Braze에서 요구하는 형식으로 변환합니다:

```bash
# The public certificate to upload to Azure (Step 3)
openssl pkcs12 -in your-cert.pfx -nokeys -out cert.pem

# The certificate and its unencrypted private key to give to Braze (Step 6)
openssl pkcs12 -in your-cert.pfx -nodes -out braze-currents.pem
```

프롬프트가 표시되면 `.pfx` 비밀번호를 입력합니다. `-nodes` 플래그는 Braze에서 요구하는 대로 비공개 키를 암호화되지 않은 상태로 내보냅니다.

### 3단계: 인증서 업로드 {#cert-sp-3}

앱 등록에서 **Certificates & secrets** > **Certificates** > **Upload certificate**로 이동한 다음, 이전 단계에서 생성한 `cert.pem` 파일을 업로드합니다. 설명을 추가하고 **Add**를 선택합니다. 자세한 단계는 Microsoft의 [Add and manage app credentials in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/how-to-add-credentials)를 참조하세요.

인증서의 만료 날짜를 기록해 두세요. [Currents의 Azure 자격 증명 업데이트](#updating-currents-credentials)를 참조하세요.

### 4단계: 스토리지 계정에 대한 액세스 권한 부여 {#cert-sp-4}

다음으로, 앱 등록에 컨테이너에 쓸 수 있는 권한을 부여합니다.

스토리지 계정으로 이동하여 **Access Control (IAM)** > **+ Add** > **Add role assignment**를 선택합니다. 그런 다음:

1. **Role** 탭에서 **[Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/storage#storage-blob-data-contributor)**를 선택합니다.
2. **Members** 탭에서 **User, group, or service principal**을 선택하고, **+ Select members**를 선택한 다음, [1단계](#cert-sp-1)에서 생성한 앱 등록 이름을 검색합니다.
3. **Review + assign**을 선택합니다.

자세한 단계는 Microsoft의 [Assign an Azure role for access to blob data](https://learn.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access)를 참조하세요.

![스토리지 계정의 Access Control(IAM) 역할 할당 탭으로, 서비스 주체와 그룹에 Storage Blob Data Contributor 역할이 할당된 모습을 보여줍니다.]({% image_buster /assets/img/azure-currents-cert-sp-1.png %})

{% alert note %}
개별 컨테이너가 아닌 **스토리지 계정** 수준에서 역할을 할당합니다.
{% endalert %}

{% alert important %}
이 역할 할당이 없으면 Braze는 Microsoft Entra ID에 인증할 수 있지만 컨테이너에 데이터를 기록할 수 없습니다.
{% endalert %}

### 5단계: 계정 엔드포인트 가져오기 {#cert-sp-5}

스토리지 계정에서 **Settings** > **Endpoints**로 이동하여 **Blob service** 엔드포인트를 기록합니다. `https://<your-storage-account>.blob.core.windows.net` 형식입니다.

![Blob 서비스 엔드포인트가 강조 표시된 스토리지 계정 엔드포인트 페이지입니다.]({% image_buster /assets/img/azure-currents-cert-sp-2.png %})

{% alert note %}
인증서 서비스 주체 인증은 공용 Azure 클라우드만 지원합니다. Blob 엔드포인트는 `.blob.core.windows.net`으로 끝나야 합니다.
{% endalert %}

### 6단계: Currents 설정 {#cert-sp-6}

Braze에는 인증서와 암호화되지 않은 비공개 키가 포함된 단일 PEM 파일이 필요합니다. [2단계](#cert-sp-2)에서 새 인증서를 생성한 경우, 두 파일을 하나로 결합합니다:

```bash
cat cert.pem key.pem > braze-currents.pem
```

[2단계](#cert-sp-2)에서 기존 `.pfx`를 변환한 경우, 이미 `braze-currents.pem` 파일이 있습니다.

Braze에서 **Currents** > **+ Create Current** > **Azure Blob Data Export**로 이동한 다음, 통합 이름과 연락처 이메일을 입력합니다. **Credentials**에서 **Certificate Service Principal**을 선택하고 다음을 입력합니다:

| 필드 | 값 |
| ----- | ----- |
| Tenant ID | [1단계](#cert-sp-1)의 **Directory (tenant) ID**입니다. |
| Client ID | [1단계](#cert-sp-1)의 **Application (client) ID**입니다. |
| Account Endpoint | [5단계](#cert-sp-5)의 **Blob service** 엔드포인트입니다. |
| Certificate | 인증서와 암호화되지 않은 비공개 키가 포함된 `braze-currents.pem` 파일입니다. |
| Container Name | Blob 컨테이너의 이름입니다. |
| Prefix | 선택 사항입니다. 컨테이너 내 내보낸 데이터의 경로 접두사입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="인증서 서비스 주체 필드" }

![Braze의 Azure Blob Data Export 페이지에서 Certificate Service Principal이 선택되어 있으며, Tenant ID, Client ID, Account Endpoint, Certificate, Container Name, Prefix 필드가 표시됩니다.]({% image_buster /assets/img/azure-currents-cert-sp-3.png %})

저장하면 Braze가 입력한 자격 증명을 검증합니다.

마지막으로 페이지 하단으로 스크롤하여 내보낼 메시지 인게이지먼트 이벤트 또는 고객 행동 이벤트를 선택합니다. 완료되면 Current를 시작합니다.

## Currents의 Azure 자격 증명 업데이트 {#updating-currents-credentials}

기존 Braze Currents 커넥터에서 통합을 중단하거나 이미 컨테이너로 내보낸 데이터를 잃지 않고 Azure 자격 증명을 업데이트할 수 있습니다.

자격 증명을 갱신하거나 **Connection String** 방식과 **Certificate Service Principal** 방식 간에 전환하려면, 이 문서 앞부분에서 선택한 방식에 대한 Azure 측 단계를 먼저 완료하세요. 그런 다음 Braze에서 **Currents**로 이동하여 목록에서 Azure Blob 커넥터를 찾고 **Edit Current**를 선택한 후 **Credentials**를 업데이트하고 **Update Current**를 선택합니다. Braze가 입력한 자격 증명을 검증하며, 커넥터는 계속 실행되고 컨테이너에 이미 있는 데이터도 그대로 사용할 수 있습니다. 자세한 내용은 [Currents 설정의 Currents 업데이트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents#updating-currents)를 참조하세요.

{% alert important %}
인증서를 최신 상태로 유지하는 것이 중요합니다. 인증서가 만료되면 유효한 인증서를 제공할 때까지 커넥터가 이벤트 전송을 중단하며, 장기간 중단되면 데이터 손실이 발생할 수 있습니다.
{% endalert %}

## 내보내기 동작 {#export-behavior}

클라우드 데이터 스토리지 솔루션을 통합한 사용자가 API, 대시보드 보고서 또는 CSV 보고서를 내보내려고 하면 다음과 같은 동작이 발생합니다:

- 모든 API 내보내기는 응답 본문에 다운로드 URL을 반환하지 않으며, 데이터 스토리지를 통해 검색해야 합니다.
- 모든 대시보드 보고서 및 CSV 보고서는 다운로드를 위해 사용자의 이메일로 전송되며(스토리지 권한 불필요), 데이터 스토리지에 백업됩니다.

{% alert important %}
**JSON 형식 요구 사항**: JSON 내보내기의 경우, Braze는 [JSONL](https://jsonlines.org/)(줄바꿈으로 구분된 JSON) 형식을 사용하며, 각 줄에 별도의 JSON 객체가 포함됩니다. 이 형식은 단일 JSON 배열 또는 객체인 표준 JSON과 다릅니다. 내보낸 파일의 각 줄은 유효한 JSON 객체이지만, 파일 전체는 단일 유효 JSON 문서가 아닙니다. 이러한 파일을 처리할 때는 전체 파일을 단일 JSON 문서로 파싱하려고 하지 말고, 각 줄을 별도의 JSON 객체로 개별 파싱하세요. <br><br> Currents 내보내기는 JSON이 아닌 [Apache Avro](https://avro.apache.org/) 형식(`.avro` 파일)을 사용합니다. 이 JSON 형식 요구 사항은 JSON 형식을 사용하는 대시보드 데이터 내보내기 및 API 내보내기에 적용됩니다.
{% endalert %}

## FAQ

### Braze에서 Azure Blob Storage에 대한 허용 목록용 IP 주소를 제공할 수 있나요? {#can-braze-provide-ip-addresses-to-allowlist-for-azure-blob-storage}

Braze는 Currents 또는 대시보드 내보내기를 위한 Azure Blob Storage용 고정 IP 허용 목록을 게시하지 않습니다. Braze는 사용자가 제공한 자격 증명과 컨테이너 이름을 사용하여 컨테이너에 데이터를 기록하며, Azure는 스토리지 계정 설정(예: 스토리지 계정의 방화벽 규칙 또는 프라이빗 엔드포인트)을 통해 네트워크 액세스를 제어합니다.

보안 팀에서 IP 기반 제한이 필요한 경우, Braze의 IP 목록 대신 스토리지 계정의 Azure 네트워킹 기능을 사용하세요. 설정 단계는 [Azure Storage 보안에 대한 Microsoft 설명서](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security)를 참조하세요.