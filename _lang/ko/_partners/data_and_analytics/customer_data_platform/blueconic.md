---
nav_title: BlueConic
article_title: BlueConic
description: "이 참조 문서에서는 Braze와 선도적인 순수 고객 데이터 플랫폼인 BlueConic 간의 파트너십을 설명합니다. 이 파트너십을 통해 영구적인 개별 프로필 전반에서 데이터를 통합하고 Amazon Web Services S3 서버를 통해 가져오기 목표를 위해 두 시스템 간에 동기화할 수 있습니다."
alias: /partners/blueconic/
page_type: partner
search_tag: Partner

---

# BlueConic

> [BlueConic](https://www.blueconic.com/)은 선도적인 순수 고객 데이터 플랫폼으로, 기업의 퍼스트파티 데이터를 분산된 시스템에서 해방하고 고객 관계를 혁신하며 비즈니스 성장을 촉진하는 데 필요한 곳에서 언제든지 접근할 수 있도록 합니다.

_이 통합은 Blueconic에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 BlueConic 통합을 통해 사용자는 영구적인 개별 프로필 전반에서 데이터를 통합하고 Amazon Web Services S3 서버를 통해 가져오기 목표를 위해 두 시스템 간에 동기화할 수 있습니다. 잠재적인 목표에는 성장 중심 이니셔티브, 고객 생애주기 오케스트레이션, 모델링 및 분석, 디지털 제품 및 경험, 오디언스 기반 수익 창출 등이 포함됩니다. 이 통합은 스케줄된 배치 가져오기와 내보내기를 모두 지원합니다.

{% alert important %}
통합을 사용할 때 BlueConic은 각 동기화 시 델타(변경된 데이터)를 전송합니다. 여기에는 마지막 전송 이후 변경된 모든 프로필과 해당 프로필의 모든 속성이 포함됩니다. 이에 따라 데이터 포인트 사용량을 모니터링하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| BlueConic 계정 | 이 파트너십을 활용하려면 [BlueConic 계정](https://www.blueconic.com/)이 필요합니다. 플러그인에 접근하려면 BlueConic 계정 내에서 [연결을 보고 편집](https://support.blueconic.com/hc/en-us/articles/202607121-BlueConic-Roles)할 수 있는 권한이 필요합니다. |
| Braze REST API 키 | `users.track`, `users.export.segment`, `campaigns.list`, `campaigns.details`, `segments.lists`, `segments.details` 권한이 있는 Braze REST API 키. <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL. 엔드포인트는 [인스턴스의 Braze URL](https://portal.aws.amazon.com/billing/signup#/start)에 따라 달라집니다. |
| S3 인증 | 데이터를 내보내고 가져오려면 Amazon Web Services(S3) 서버에 대한 접근 권한이 필요합니다. |
| 액세스 키 ID<br>시크릿 액세스 키 | 액세스 키 ID와 시크릿 액세스 키를 사용하여 가져오기 및 내보내기를 위한 S3 서버를 인증할 수 있습니다. |
| AWS 버킷 | 플러그인 내에서 S3에 연결해야 합니다. 인증 후 사용 가능한 버킷이 드롭다운 메뉴에 표시됩니다. 여기에 가져오거나 내보낼 파일이 저장됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Braze 연결 생성 {#step-1-creating-a-braze-connection}

BlueConic에서 내비게이션 바의 **Connections**를 선택한 다음 **Add Connection**을 선택합니다. 표시되는 프롬프트에서 **Braze**를 검색하고 **Braze connection**을 선택합니다.

회색 셰브론 아이콘을 클릭하여 연결에서 사용 가능한 메타데이터 필드를 확장하거나 축소합니다. 이 필드에서 연결을 즐겨찾기에 추가하고, 연결 이름을 지정하고, 레이블을 추가하고, 설명을 포함하고, 연결이 [실행되거나 실행에 실패](https://support.blueconic.com/hc/en-us/articles/205957522#h_01F4VR7SG7NKB3FMQXCB2Q8JNZ)할 경우 이메일 알림을 받도록 선택할 수 있습니다.

설정을 저장합니다.

### 2단계: Braze 연결 구성 {#step-2-configuring-a-braze-connection}

BlueConic과 Braze 간의 연결을 구성하려면 Braze 계정 자격 증명과 Amazon Web Services(S3) 계정 정보를 추가하여 연결을 인증해야 합니다.

1. BlueConic에서 왼쪽 패널의 **Setup** 섹션에서 **Set up and run**을 선택합니다.<br><br>
2. 열리는 Braze 인증 페이지에서 Braze REST API 엔드포인트와 Braze API 키를 입력합니다.<br>
![]({% image_buster /assets/img/blueconic/braze2.png %}){: style="max-width:80%;"}<br><br>
3. S3 설정 및 인증 섹션에서 다음 자격 증명을 입력합니다: Amazon Web Services(S3) 액세스 키 ID, 시크릿 액세스 키, S3 버킷. 이는 Braze와 Amazon S3 통합을 설정할 때 구성한 [동일한 자격 증명]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)이어야 합니다. 설정을 저장합니다. <br>![]({% image_buster /assets/img/blueconic/braze3.png %}){: style="max-width:80%;"}

### 3단계: 가져오기 또는 내보내기 목표 생성(가져오기 매핑) {#step-3-creating-import-or-export-goals-import-mapping}

인증이 완료되면 하나 이상의 가져오기 또는 내보내기 목표를 생성하고, 연결을 켜고, 연결을 스케줄하거나 실행해야 합니다.

{% tabs %}
{% tab 가져오기 %}

1. 왼쪽 패널에서 **Import data into BlueConic**을 선택하여 Braze 데이터 구성 페이지를 엽니다.<br><br>
2. Braze에서 데이터의 위치를 선택합니다. 여기에서 Braze 오디언스를 선택하여 가져올 데이터를 찾을 위치를 BlueConic에 알려줄 수 있습니다.<br>![BlueConic Braze 오디언스가 "BlueConic Test Users"로 설정된 화면]({% image_buster /assets/img/blueconic/braze4.png %}){: style="max-width:80%;"}<br><br>
3. 다음으로, Braze와 BlueConic 간의 식별자를 매핑합니다. <br>![Braze 필드 "External ID"가 BlueConic "Braze external ID" 필드에 매핑되도록 설정된 화면]({% image_buster /assets/img/blueconic/braze5.png %}){: style="max-width:80%;"}<br><br> 두 시스템 간의 고객 데이터를 연결하려면 하나 이상의 고객 식별자를 입력합니다.<br>**Allow creation...** 체크박스를 사용하여 기존 BlueConic 프로필과 일치하지 않는 데이터에 대해 BlueConic이 새 프로필을 생성하도록 허용합니다.<br><br>
4. 다음으로, 내보내는 BlueConic 데이터 필드를 Braze 필드와 매칭합니다. 드롭다운 필드를 사용하여 왼쪽에서 BlueConic 프로필 식별자 또는 프로필 등록정보를 선택하고 해당하는 Braze 프로필 식별자를 선택합니다. 그런 다음 드롭다운 메뉴를 사용하여 가져온 콘텐츠를 기존 값에 추가하는 방법을 지정합니다: 추가, 합산, 프로필 등록정보가 비어 있는 경우에만 설정, 또는 지우기로 설정(Braze 필드가 비어 있는 경우).<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>**Add Mapping** 버튼을 사용하여 필요에 따라 추가 매핑 행을 생성합니다. **Add remaining fields** 옵션으로 여러 매핑 행을 추가할 수 있습니다. BlueConic이 나머지 Braze 필드를 감지하고 BlueConic 프로필 등록정보와 매칭합니다. 가져오기의 병합 전략(설정, 추가, 합산, 비어 있으면 설정 또는 지우기)을 설정하고 BlueConic 프로필 등록정보 이름에 커스텀 접두사를 제공할 수 있습니다.<br><br>
5. 마지막으로, **Run the connection**을 선택하여 연결을 시작합니다. 연결 스케줄 및 실행에 대해 자세히 알아보려면 [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections)을 방문하세요.
{% endtab %}
{% tab 내보내기 %}

1. 왼쪽 패널에서 **Export data to Braze**를 선택하여 BlueConic에서 Braze로의 데이터 내보내기를 구성합니다.<br><br>
2. 내보내기를 위한 BlueConic Segment를 선택합니다. 이 Segment에서 Braze에 일치하는 식별자가 있는 프로필만 내보내집니다.<br>![20,000개의 프로필로 구성된 BlueConic Segment]({% image_buster /assets/img/blueconic/braze8.png %}){: style="max-width:80%;"}<br><br>
3. 다음으로, BlueConic 프로필과 Braze 필드 간의 식별자를 연결합니다. 기존 일치 항목이 없는 경우 BlueConic이 새 레코드를 생성하도록 선택할 수도 있습니다.<br>![Braze 필드 "External ID"가 BlueConic "Braze external ID" 필드에 매핑되도록 설정된 화면]({% image_buster /assets/img/blueconic/braze7.png %}){: style="max-width:80%;"}<br><br>
4. 다음으로, 내보내는 BlueConic 데이터 필드를 Braze 필드와 매칭합니다. BlueConic 아이콘의 드롭다운 메뉴를 사용하여 내보낼 [정보](https://support.blueconic.com/hc/en-us/articles/4405501836955-Braze-Connection#creating-export-goals) 유형을 선택합니다. 사용 가능한 정보에는 프로필 등록정보, BlueConic 프로필 식별자, 연결된 Segment, 모든 조회된 인터랙션, 권한 수준, 정적 텍스트 값이 포함됩니다.<br>![]({% image_buster /assets/img/blueconic/braze6.png %}){: style="max-width:80%;"}<br><br>
5. 마지막으로, **Run the connection**을 클릭하여 연결을 시작합니다. 연결 스케줄 및 실행에 대해 자세히 알아보려면 [BlueConic](https://support.blueconic.com/hc/en-us/articles/205957522-Scheduling-Connections)을 방문하세요.
{% endtab %}
{% endtabs %}

## 4단계: 연결 토글 켜기 {#step-4-toggle-connection-on}

Braze 연결 제목 옆의 토글을 사용하여 연결을 켜고 끕니다. 스케줄된 시간에 실행하려면 연결이 켜져 있어야 합니다.