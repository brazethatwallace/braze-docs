---
nav_title: Copy Pastd
article_title: Copy Pastd
alias: /partners/copy_pastd/
description: "이 참조 문서에서는 Braze와 Copy Pastd 간의 파트너십을 설명합니다. Copy Pastd는 Liquid 기반 Content Blocks와 템플릿을 Braze 워크스페이스로 직접 푸시하는 드래그 앤 드롭 이메일 빌더입니다."
page_type: partner
search_tag: Partner
---

# Copy Pastd

> [Copy Pastd](https://copypastd.com/) Building Blocks는 Liquid 기반 Content Blocks와 전체 템플릿을 Braze 워크스페이스로 직접 푸시하는 드래그 앤 드롭 이메일 빌더입니다. 한 번 디자인하고 Braze에 동기화하면, 매번 HTML을 다시 작성할 필요 없이 Campaigns, Canvases, 트리거 플로우 전반에서 동일한 구성요소를 재사용할 수 있습니다.

_이 통합은 Copy Pastd에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Copy Pastd 통합을 사용하면 Building Blocks에서 이메일을 작성할 수 있습니다. Building Blocks는 깔끔한 Liquid, Content Blocks 참조, 그리고 별도의 변환 없이 모든 Campaign 또는 Canvas에 바로 적용할 수 있는 템플릿 등 Braze 네이티브 출력을 생성하는 호스팅 이메일 빌더입니다.

재사용 가능한 블록으로 이메일을 조립하고, 한 번의 클릭으로 Braze에 푸시하면, 동일한 브랜드 스타일, 구성요소, 동적 콘텐츠가 모든 발송에서 일관되게 렌더링됩니다. 결과적으로 수작업으로 코딩하는 템플릿이 줄어들고, 이메일 생성 및 발송에 소요되는 시간이 단축되며, 변경 시 모든 곳에서 업데이트되는 중앙 집중식 라이브러리를 갖추게 됩니다.

## 필수 조건 {#prerequisites}

이 통합을 사용하려면 다음이 필요합니다.

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Copy Pastd 계정 | Building Blocks를 사용하려면 필수입니다. [copypastd.com](https://copypastd.com)에서 가입하세요. 각 고객에게는 워크스페이스, 스타일시트 라이브러리, 5개의 빌더 시트, 블록 라이브러리가 제공됩니다. |
| 이메일 템플릿용 Braze REST API 키 | `templates.email.create`, `templates.email.update`, `templates.email.list` 권한이 있는 API 키.<br><br>Braze 대시보드의 **Settings** > **API Keys**에서 키를 생성하세요. |
| Content Blocks용 Braze REST API 키 | `content_blocks.create`, `content_blocks.update`, `content_blocks.info`, `content_blocks.list` 권한이 있는 API 키.<br><br>Braze 대시보드의 **Settings** > **API Keys**에서 키를 생성하세요. |
| 카탈로그용 Braze REST API 키(선택 사항) | `catalogs.get`, `catalogs.get_item`, `catalogs.get_selections`에 대한 읽기 권한이 있는 API 키. 블록을 Braze 카탈로그에 바인딩할 계획인 경우에만 필요합니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. Building Blocks는 선택한 클러스터에 따라 엔드포인트를 자동으로 선택합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

* **대규모 브랜드 일관성 유지 저작.** Building Blocks 스타일시트를 모든 템플릿에 적용하면 색상, 글꼴, 버튼 스타일, 패딩 스케일이 수백 개의 이메일에서 동일하게 렌더링됩니다. 브랜드가 변경되면 스타일시트를 한 번 업데이트하고 재동기화하여 모든 이메일에 한꺼번에 업데이트를 적용하세요.
* **연결된 콘텐츠 및 카탈로그 바인딩 제품 템플릿.** 빌더 내에서 이메일 블록 필드를 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) 엔드포인트 및 [Braze 카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/)에 직접 바인딩하세요. Liquid를 건드리지 않고도 신제품 출시, 시즌 컬렉션, 콘텐츠 새로고침에 동일한 템플릿을 재사용할 수 있습니다.
* **비기술 마케터를 위한 셀프서비스 이메일 제작.** Liquid 개인화 및 로직을 포함한 승인된 블록으로 전체 이메일을 작성하고, HTML이나 Liquid를 작성하거나 품질 보증을 수행할 개발자 지원 없이 Braze에 푸시하여 검토를 받으세요.
* **중앙 헤더 및 푸터, 한 번의 클릭으로 업데이트.** Building Blocks 빌더에서 헤더 또는 푸터를 한 번 만들고 Braze에 푸시하세요. 이를 참조하는 모든 템플릿이 동기화 상태를 유지하므로, 로고 교체, 법적 문구 변경, 새 소셜 링크 추가가 Building Blocks 내에서 한 번의 업데이트만으로 Braze에 있는 모든 이메일에 반영됩니다.
* **모든 이메일에 걸친 중앙 집중식 콘텐츠.** 히어로, 푸터 또는 프로모 카드를 Building Blocks 스마트 블록으로 한 번 만드세요. 업데이트하고 동기화하면, 이를 참조하는 Braze의 모든 이메일이 다음 발송 시 변경 사항을 반영합니다. 웰컴 플로우, 주간 뉴스레터, 트리거 여정이 각 Campaign을 편집하지 않아도 항상 최신 상태를 유지합니다.
* **기여자가 셀프서비스할 수 있는 잠긴 템플릿.** 템플릿을 만들고 선택한 필드를 잠근 다음, 다른 팀이 사용자 대면 도구에 대한 접근 권한을 부여하지 않고도 기여자 인터페이스에서 자체 이메일을 작성하도록 초대하세요.

## 통합 {#integration}

### 1단계: Building Blocks를 Braze에 연결 {#step-1-connect-building-blocks-to-braze}

{% alert note %}
Building Blocks를 Braze에 연결하는 것은 일회성 설정입니다. 자격 증명이 검증되면 Building Blocks가 이후 모든 동기화 및 템플릿 푸시를 위해 자격 증명을 저장합니다.
{% endalert %}

1. [blocks.copypastd.com](https://blocks.copypastd.com)에서 Building Blocks에 로그인하거나, [copypastd.com](https://copypastd.com)에서 **Login**을 선택하세요.
2. 대시보드에서 **Set up your Braze connection**을 선택하세요. (이 필은 관리자의 첫 로그인 시 표시되며 완료될 때까지 유지됩니다. **Team Settings** > **Connect** > **Braze API Keys**에서도 해당 페이지에 접근할 수 있습니다.)
3. 드롭다운에서 Braze 클러스터를 선택하세요. 일치하는 REST 엔드포인트가 자동으로 입력됩니다.
4. 템플릿 API 키, Content Blocks API 키, 그리고 (선택 사항으로) 카탈로그 API 키를 해당 필드에 붙여넣으세요.
5. **Validate and save**를 선택하세요. Building Blocks가 Braze를 호출하여 키가 작동하고 권한 범위가 올바른지 확인합니다. 누락된 항목이 있으면 인라인 오류가 어떤 범위가 잘못되었는지 표시합니다.

### 2단계: 라이브러리를 Braze에 동기화 {#step-2-sync-your-library-to-braze}

1. 키가 검증되면 설정 모달에서 **Sync now**를 선택하세요. (**Settings** > **Connect** > **Braze** > **Sync library**에서 언제든지 재동기화할 수도 있습니다.) <br> Building Blocks가 스타일시트와 블록을 Braze Content Blocks로 Braze 워크스페이스에 푸시합니다. Braze에서 `CP_`(예: `CP_Hero_1`) 또는 스타일시트의 경우 `cp_`(예: `cp_default_style`) 접두사가 붙은 이름으로 표시됩니다.
2. 동기화가 완료되면 빌더에서 **Push to Braze**를 사용하여 개별 템플릿을 푸시할 수 있습니다.

## Building Blocks 커스터마이즈 {#customize-building-blocks}

### 1단계: 스타일시트 설정 {#step-1-set-up-your-stylesheet}

1. Building Blocks에서 **Settings** > **Build** > **Stylesheets**로 이동하세요.
2. 기본 스타일시트를 편집하거나 새로 만드세요. 색상 팔레트(24개의 명명된 색상), 글꼴(Google Fonts 지원), 버튼 스타일, 링크 스타일, 반경, 패딩 스케일을 설정하세요.
3. **Save**를 선택하세요. Building Blocks가 이 스타일시트를 사용하는 모든 블록의 Liquid를 재생성합니다.
4. **Sync now**를 선택하여 업데이트된 스타일을 Braze 워크스페이스에 푸시하세요.

### 2단계: 연결된 콘텐츠 엔드포인트 활성화(선택 사항) {#step-2-enable-connected-content-endpoints-optional}

1. Building Blocks에서 **Settings** > **Connect** > **Connected Content endpoints**로 이동하세요.
2. 엔드포인트 URL을 추가하고 이름을 지정한 후 저장하세요. Building Blocks는 표준 JSON 형식 외에 Google Sheets 응답 형식도 지원합니다.
3. 빌더에서 **Personalize** 패널의 연결된 콘텐츠 변수에 텍스트, 이미지 또는 링크 필드를 바인딩하세요. 내보내기 시 올바른 {% raw %}`{% connected_content %}`{% endraw %} Liquid가 생성됩니다.

### 3단계: Braze 카탈로그에 바인딩(선택 사항) {#step-3-bind-to-braze-catalogs-optional}

1. Building Blocks에서 **Settings** > **Connect** > **Catalogs**로 이동하세요. Building Blocks가 카탈로그 API 키를 사용하여 카탈로그 목록을 읽습니다.
2. 호환되는 블록(예: 제품 그리드)을 여세요.
3. 카탈로그와 선택 항목을 선택한 다음 블록 필드를 카탈로그 항목 속성에 매핑하세요.
4. 템플릿을 푸시하세요. Building Blocks가 Braze가 발송 시 해석할 올바른 {% raw %}`{% catalog_items %}`{% endraw %} 및 {% raw %}`{% catalog_selection_items %}`{% endraw %} Liquid를 생성합니다.

### 4단계: Braze 커스텀 속성 추가(선택 사항) {#step-4-add-your-braze-custom-attributes-optional}

Building Blocks에는 기본 Braze 사용자 속성(`first_name`, `email`, `country` 등)이 포함되어 있습니다. 블록을 자체 커스텀 속성에 바인딩하려면 Building Blocks에 한 번 가져오기만 하면 모든 **Personalize** 드롭다운에서 사용할 수 있습니다.

1. Building Blocks에서 **Team Settings** > **Connect** > **Custom Attributes**로 이동하세요.
2. 다음 방법 중 하나를 사용하여 커스텀 속성을 가져오세요:
* **일괄 가져오기(권장).** Braze에서 **Data Settings** > **Custom Attributes**로 이동하고 **Export**(오른쪽 상단)를 선택하세요. Building Blocks에서 CSV를 업로드하세요.
* **속성을 하나씩 추가.** 속성 이름(예: `loyalty_tier`)을 입력하고 **Add**를 선택하세요. 이 방법은 몇 개의 속성만 추가하거나 Braze 내보내기 사이에 새 속성을 추가하려는 경우에 유용합니다.

저장하면 커스텀 속성이 빌더의 **Personalize** 드롭다운에 기본값과 함께 표시됩니다. 하나를 삽입하면 내보내기 시 올바른 {% raw %}`{{custom_attribute.${name}}}`{% endraw %} Liquid가 렌더링되므로, Braze가 발송 시 수신자별로 값을 해석합니다.

## 통합 사용 {#use-the-integration}

### 1단계: 템플릿을 Braze에 푸시 {#step-1-push-a-template-to-braze}

1. Building Blocks 빌더에서 이메일을 여세요.
2. **Push to Braze**(오른쪽 상단)를 선택하세요.
3. 워크스페이스를 선택하고 확인하세요. Building Blocks가 렌더링된 Liquid와 함께 Braze에 이메일 템플릿을 생성합니다.

템플릿은 Braze의 **Templates & Media** > **Email Templates**에 이메일 이름과 이메일 설정에서 선택한 날짜로 명명되어 표시됩니다.

### 2단계: Campaign 또는 Canvas에서 템플릿 사용 {#step-2-use-the-template-in-a-campaign-or-canvas}

1. Braze에서 새 이메일 Campaign 또는 캔버스 단계를 생성하세요.
2. **Templates**를 선택하고 Building Blocks가 푸시한 템플릿을 선택하세요.

템플릿은 모든 Building Blocks 참조(스타일시트, Content Blocks)를 라이브 {% raw %}`{{content_blocks.${...}}}`{% endraw %} Liquid로 포함하므로, Building Blocks에서의 업데이트가 템플릿을 다시 가져오지 않아도 전파됩니다.

### 3단계: 콘텐츠를 중앙에서 업데이트 {#step-3-update-content-centrally}

1. Building Blocks에서 관련 블록 또는 스타일시트를 편집하세요.
2. **Sync**를 선택하여 업데이트된 Content Block을 Braze에 다시 푸시하세요.

이를 참조하는 Braze의 모든 이메일(에버그린, 트리거, 웰컴 플로우)이 다음 발송 시 새 버전을 반영합니다. 각 Campaign을 편집할 필요가 없습니다.

### 4단계: 콘텐츠 풀 구축 {#step-4-build-content-pools}

콘텐츠 풀은 이메일이 정적 카피를 포함하는 대신 참조하는 콘텐츠 행의 테이블입니다. Building Blocks에서 풀을 업데이트하면, 이를 사용하는 Braze의 모든 이메일이 다음 발송 시 새 콘텐츠를 제공합니다. 주간 뉴스레터, 웰컴 플로우, 윈백 시퀀스, 시즌 Campaign, 구매 후 여정 등 동일한 콘텐츠가 여러 이메일에서 항상 최신 상태를 유지해야 하는 모든 곳에서 콘텐츠 풀을 사용하세요.

1. Building Blocks에서 기본 내비게이션의 **Content**를 선택하세요.
2. **New Pool**을 선택하세요. 풀이 담고 있는 내용을 설명하는 이름을 입력하세요(예: Weekly Offers, Product Catalog, News Articles).
3. 풀이 공급하는 블록 유형을 선택하세요(예: Hero, Grid, Card). 이렇게 하면 각 행에서 사용할 수 있는 필드가 설정됩니다.
4. 행을 추가하세요. 각 행은 하나의 콘텐츠입니다. 필드(헤드라인, 이미지, CTA 텍스트, CTA 링크 등)를 완성하세요.
5. 행을 위아래로 드래그하여 우선순위를 설정하세요. 각 행을 활성 또는 비활성으로 토글하고, 선택적으로 시작 및 종료 날짜를 설정하세요. 발송 시 날짜가 유효한 가장 높은 우선순위의 활성 행이 선택됩니다.
6. **Save**를 클릭하세요. 이제 스마트 블록이 이 풀을 참조할 수 있습니다.

### 5단계: 스마트 블록을 사용하여 이메일에서 풀 콘텐츠 렌더링 {#step-5-use-smart-blocks-to-render-pool-content-in-your-emails}

스마트 블록은 정적 콘텐츠를 보유하는 대신 하나 이상의 콘텐츠 풀을 참조하는 빌더 캔버스의 블록입니다. 발송 시 Braze는 가장 높은 우선순위이며 활성 상태이고 날짜가 유효한 풀 행을 렌더링합니다. 내보낸 Liquid가 이 작업을 수행합니다. 추가적인 Braze 설정은 필요하지 않습니다.

1. Building Blocks에서 스마트 블록을 캔버스에 드래그하세요(일치하는 풀이 있는 모든 블록 유형).
2. 속성 패널에서 캐스케이드 편집기를 여세요.
3. 하나 이상의 콘텐츠 풀을 우선순위 순서로 추가하세요. 이것이 워터폴입니다: 활성이고 날짜가 유효한 행이 있는 첫 번째 풀이 렌더링됩니다. 라이브 항목이 없으면 스마트 블록이 다음 풀로, 그 다음 풀로 넘어갑니다. 일반적인 패턴은 Flash Sale > Weekly Offers > Evergreen Favorites로, 항상 표시할 콘텐츠가 있습니다.
4. 템플릿을 Braze에 푸시하세요. 내보낸 Liquid가 전체 캐스케이드를 포함하므로, Braze가 매 발송 시 풀 우선순위와 날짜를 평가합니다.

이제부터는 이메일이 아닌 풀을 업데이트하면 됩니다. 트리거 플로우, 에버그린 뉴스레터, 시즌 Campaign 모두 풀이 최신 상태인 한 최신 상태를 유지합니다.

업로드된 Building Blocks 템플릿은 Braze의 **Templates & Media** > **Email Templates**에서 찾을 수 있습니다. 동기화된 스타일시트와 블록은 **Templates & Media** > **Content Blocks**에서 확인할 수 있습니다.

## 고려 사항 {#considerations}

- **Building Blocks 팀 스페이스당 하나의 Braze 인스턴스.** 각 Building Blocks 팀은 단일 Braze 인스턴스에 연결됩니다. 여러 워크스페이스(별도의 브랜드, 지역 또는 환경)를 운영하는 고객은 동일한 팀에 추가하여 블록을 공유할 수 있습니다.
- **API 키 권한은 별도로 범위가 지정됩니다.** 템플릿 키와 Content Blocks 키는 분리되어 있습니다. 키에 필수 범위가 누락되면 검증이 즉시 실패하므로, Braze에서 어떤 권한을 추가해야 하는지 정확히 알 수 있습니다.
- **Content Blocks 이름에 네임스페이스가 적용됩니다.** Building Blocks는 Braze에서 직접 생성한 Content Blocks와의 충돌을 방지하기 위해 `CP_`(블록) 및 `cp_`(스타일시트) 접두사를 사용하여 Content Blocks를 푸시합니다.
- **스타일시트 편집은 모든 이메일을 업데이트합니다.** 스타일시트는 모든 템플릿이 참조하는 단일 Braze Content Block으로 렌더링됩니다. Building Blocks에서의 변경은 이미 스케줄된 이메일을 포함하여 이를 사용하는 Braze의 모든 이메일을 업데이트합니다. 동기화하기 전에 초안 템플릿에서 스타일시트 변경 사항을 테스트하세요.
- **카탈로그 바인딩은 읽기 전용입니다.** Building Blocks는 바인딩 UI를 채우기 위해 카탈로그를 읽습니다. Braze 카탈로그에 쓰기 작업은 수행하지 않습니다. 모든 카탈로그 관리는 여전히 Braze 대시보드에서 이루어집니다.
- **사용량 제한 및 재시도.** 모든 아웃바운드 요청은 지수 백오프, 지터, Retry-After 처리를 통해 Braze의 사용량 제한을 준수합니다. 파트너 기여도를 위해 모든 호출에 `User-Agent: partner-CopyPastd` 헤더가 전송됩니다.
- **사용자 데이터는 전송되지 않습니다.** Building Blocks는 콘텐츠 저작 도구입니다. 사용자 속성, 이벤트, 구매 또는 Segment 데이터를 Braze에 푸시하지 않으며, Braze 데이터 포인트를 소비하지 않습니다.

## 문제 해결 {#troubleshooting}

- **API 키 검증 실패.** 각 키가 필수 조건에 나열된 정확한 권한을 가지고 있는지 확인하세요. 템플릿과 Content Blocks 범위는 별도로 확인됩니다. Braze에서 키를 재생성한 경우 새 값을 Building Blocks에 붙여넣고 다시 검증하세요.
- **REST 엔드포인트 불일치.** 템플릿과 Content Blocks 키는 동일한 Braze 워크스페이스에서 가져와야 하며, REST 엔드포인트는 클러스터와 일치해야 합니다. Building Blocks 드롭다운이 이를 자동으로 설정하므로, 검증이 실패하면 클러스터 선택을 확인하세요.
- **Braze에 푸시 시 오류 반환.** **Settings** > **Build** > **Activity log**를 열어 마지막 동기화 시도와 Braze가 반환한 응답을 확인하세요. 대부분의 실패는 권한 관련(누락된 범위) 또는 할당량 관련(사용량 제한, 자동 재시도)입니다.
- **Braze에서 Content Block이 업데이트되지 않음.** **Settings** > **Connect** > **Braze** > **Sync library**에서 수동 재동기화를 트리거하세요. Building Blocks는 비교 후 교체를 수행하므로, 변경되지 않은 블록은 건너뜁니다.
- **템플릿이 Braze에 아직 존재하지 않는 Content Block을 참조함.** **Sync library**를 사용하여 종속성(스타일시트, 스마트 블록)을 먼저 푸시한 다음 템플릿을 푸시하세요.
- **기타 모든 문제.** [help@copypastd.com](mailto:help@copypastd.com)으로 Copy Pastd에 문의하세요. 팀 이름과 실패한 작업의 시간을 포함하면 Copy Pastd가 일치하는 활동 로그를 확인할 수 있습니다.