---
nav_title: Clarisights
article_title: Clarisights
description: "이 참조 문서에서는 셀프서비스 성과 마케팅 보고 플랫폼인 Clarisights와 Braze 간의 파트너십을 설명합니다. 이 통합을 통해 Braze Campaigns 및 Canvases에서 데이터를 가져와 성과 및 CRM/리텐션 마케팅의 통합 보고 인터페이스를 구현할 수 있습니다."
alias: /partners/clarisights/
page_type: partner
search_tag: Partner

---

# Clarisights

> [Clarisights](https://clarisights.com)는 데이터 중심 조직을 위한 셀프서비스 성과 마케팅 보고 플랫폼입니다. 마케팅, 분석 및 기여도 소스의 모든 데이터를 자동으로 통합, 처리 및 시각화합니다.

_이 통합은 Clarisights에서 유지 관리합니다._

## 통합 소개 {#about-the-integration}

Braze와 Clarisights 통합을 사용하면 Braze Campaigns 및 Canvases에서 데이터를 가져와 성과 및 CRM/리텐션 마케팅의 통합 보고 인터페이스를 구현할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Clarisights 계정 | 이 파트너십을 활용하려면 Clarisights 워크스페이스가 필요합니다 |
| Braze REST API 키 | 다음 권한이 있는 Braze REST API 키:  <br> - `campaigns.list` <br>  - `campaigns.details`<br> - `campaigns.data_series` <br> - `canvas.details`<br> - `canvas.list` <br>  - `canvas.data_series` <br><br> Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Braze 워크스페이스 이름 | Braze API 키와 연결된 워크스페이스의 이름입니다. 이 이름은 Clarisights에서 워크스페이스 통합을 식별하는 데 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Braze와 Clarisights 통합을 통해 사용자는 생성한 캠페인에서 인사이트를 얻기 위한 다양한 시각화 및 테이블을 만들 수 있습니다. 주요 활용 사례는 다음과 같습니다.

{% tabs %}
{% tab 향상된 가시성 %}
전체 Campaigns 및 Canvases 성과에 대한 향상된 가시성.

![Clarisights 플랫폼에서 향상된 가시성의 예를 보여주는 그래픽. 이 그래픽에는 Campaign 및 Canvas 열기, 클릭 수, 발송, 전환 등의 통계가 포함되어 있습니다.]({{site.baseurl}}/assets/img/clarisights/overall_view.png)
{% endtab %}
{% tab 세분화된 보고 %}
Campaigns 및 Canvases에 대한 세분화된 보고.

![발송 채널별 전체 발송 및 전환율과 같은 세분화된 보고를 보여주는 그래픽.]({{site.baseurl}}/assets/img/clarisights/unified_dashboard.png)
{% endtab %}
{% tab 통합 대시보드 %}
CMO 및 CXO를 위한 통합 대시보드.

![통합 대시보드의 예를 보여주는 그래픽.]({{site.baseurl}}/assets/img/clarisights/granular_reporting.png)
{% endtab %}
{% endtabs %}

## 통합 {#integration}

Braze 데이터를 Clarisights에 동기화하려면 Braze 커넥터를 구축하고 Braze 워크스페이스를 연결해야 합니다.

1. Clarisights에서 **Integrations** 페이지로 이동하여 **Braze** 커넥터를 찾고 **+ Connect**를 선택합니다.<br>![Clarisights 통합 마켓플레이스에서 사용 가능한 커넥터 목록.]({{site.baseurl}}/assets/img/clarisights/integrations.png)<br><br>
2. 다음으로, 통합 플로우를 사용하여 Clarisights 계정을 Braze에 연결합니다. Braze REST API 키, Braze 워크스페이스 이름 및 Braze REST 엔드포인트를 제공하면 됩니다.<br>![Clarisights 플랫폼의 Braze 워크스페이스 커넥터. 이 페이지에는 Braze 워크스페이스 이름, Braze REST API 키 및 Braze REST 엔드포인트 필드가 있습니다.]({{site.baseurl}}/assets/img/clarisights/braze_flow.png)<br><br>통합이 성공적으로 완료되면 사용자는 동일한 페이지에서 연결된 워크스페이스를 확인할 수 있습니다.<br>!['Braze Accounts' 내에서 연결된 워크스페이스 목록을 확인할 수 있습니다.]({{site.baseurl}}/assets/img/clarisights/connected.png)<br><br>

## 이 통합 사용하기 {#using-this-integration}

Clarisights 보고서에 Braze를 데이터 소스로 포함하려면 **Create New Report**로 이동합니다. 보고서 이름을 지정하고 표시되는 프롬프트에서 **Braze**를 데이터 소스로 선택합니다. 보고서에 포함할 측정기준과 차원을 선택할 수도 있습니다. 완료되면 **Create Report**를 선택합니다.

Braze의 데이터는 다음 예약된 데이터 가져오기 시점부터 유입되기 시작합니다. 더 긴 기간의 백필을 요청하려면 Clarisights 고객 성공 매니저에게 문의하세요.

![이름 및 데이터 소스 필드를 보여주는 Clarisights 보고서 설정. 이 예에서는 'Braze'가 데이터 소스로 선택되어 있습니다.]({{site.baseurl}}/assets/img/clarisights/braze_report.png)

사용 가능한 [측정기준 및 차원](https://help.clarisights.com/en/articles/5670864-braze-metrics-and-dimensions) 또는 [보고서 생성](https://help.clarisights.com/en/articles/1421478-creating-a-report-using-clarisights)에 대한 자세한 내용은 Clarisights를 방문하세요.