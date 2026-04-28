---
nav_title: API 및 SDK 엔드포인트
article_title: API 및 SDK 엔드포인트
page_order: 5
page_type: reference
description: "Braze 인스턴스에 맞는 올바른 대시보드 URL, REST API 엔드포인트, SDK 엔드포인트를 확인하세요."

---

# API 및 SDK 엔드포인트 {#api-and-sdk-endpoints}

> Braze 인스턴스에 맞는 올바른 대시보드 URL, REST API 엔드포인트, SDK 엔드포인트를 확인하세요. 로그인, API 호출, SDK 통합을 위해 이 URL이 필요합니다.

Braze는 대시보드, SDK, REST 엔드포인트를 위해 여러 인스턴스를 관리하며, 이를 "클러스터"라고 부릅니다. Braze 온보딩 매니저가 어떤 클러스터에 속해 있는지 알려드립니다. Braze SDK에 대해 자세히 알아보려면 [Braze 101](https://learning.braze.com/braze-101) Braze 학습 과정을 확인하세요.

[dashboard.braze.com](https://dashboard.braze.com)에서 로그인하면 자동으로 올바른 클러스터 주소로 이동합니다.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
SDK를 통합할 때는 SDK 엔드포인트를 사용하세요. REST API를 호출할 때는 REST 엔드포인트를 사용하세요.
{% endalert %}

API 접근에 대한 자세한 내용은 [API 개요 문서]({{site.baseurl}}/api/basics/)를 참조하세요.