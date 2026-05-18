---
nav_title: API 내보내기
article_title: API 내보내기
page_order: 5
page_type: reference
description: "이 참조 문서에서는 대시보드에서 CSV를 다운로드하는 대신 내보내기 API를 사용해야 하는 경우를 판단하는 데 도움을 줍니다."
platform: API

---

# API 내보내기 {#export-apis}

> 이 페이지에서는 대시보드에서 CSV를 다운로드하는 대신 내보내기 API를 사용해야 하는 경우를 판단하는 데 도움을 줍니다.

Braze 내보내기 API를 사용하면 Braze 데이터를 JSON 형식으로 프로그래밍 방식으로 내보낼 수 있습니다. 내보낼 수 있는 항목, 필수 조건, 전달 방식에 대한 자세한 내용은 [내보내기 엔드포인트]({{site.baseurl}}/api/endpoints/export/)를 참조하세요.

## CSV 다운로드 대신 내보내기 API를 사용해야 하는 경우 {#when-to-use-export-apis-instead-of-csv-downloads}

다음 표에서는 대시보드 CSV 다운로드보다 내보내기 API를 사용하는 것이 더 나은 일반적인 시나리오를 설명합니다.

| 시나리오 | 세부 정보 |
| --- | --- |
| 내보내기 데이터가 대시보드에서 처리하기에 너무 큰 경우 | 대시보드 CSV 내보내기는 500,000행으로 제한됩니다. 사용자가 500,000명이 넘는 Segment의 데이터를 내보내는 경우, 내보낼 수 있는 양에 제한이 없는 내보내기 API를 사용하세요. |
| 반복 보고서를 자동화하려는 경우 | 통합을 통해 API 내보내기를 스케줄하여 수동으로 대시보드를 조작하지 않고도 정기적으로 데이터를 가져올 수 있습니다. |
| 외부 도구에 데이터를 전달해야 하는 경우 | 내보내기 데이터를 BI 도구, 데이터 웨어하우스 또는 기타 분석 플랫폼에 직접 가져올 수 있습니다. |
| 대시보드 CSV 내보내기로 제공되지 않는 데이터가 필요한 경우 | KPI, 매출 시계열, 커스텀 이벤트 분석, 세션 데이터 등 일부 데이터 카테고리는 API를 통해서만 사용할 수 있습니다. |
| 데이터를 프로그래밍 방식으로 처리하려는 경우 | JSON 출력을 커스텀 처리, 변환 또는 통합에 활용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="CSV 다운로드 대신 내보내기 API를 사용해야 하는 경우" }

{% alert tip %}
CSV 및 API 내보내기에 대한 도움말은 [내보내기 문제 해결]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/)을 참조하세요.
{% endalert %}