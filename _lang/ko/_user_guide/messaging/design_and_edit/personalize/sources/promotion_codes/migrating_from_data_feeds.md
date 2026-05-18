---
nav_title: 데이터 피드에서 마이그레이션
article_title: 데이터 피드에서 프로모션 코드로 마이그레이션
page_order: 10
description: "이 참조 문서에서는 데이터 피드에서 프로모션 코드로 마이그레이션하는 방법에 대한 안내를 제공합니다."
---

# 데이터 피드에서 프로모션 코드로 마이그레이션 {#migrate-from-data-feeds-to-promotion-codes}

> 이 페이지에서는 데이터 피드에서 프로모션 코드로 마이그레이션하는 방법을 안내합니다. 데이터 피드의 정보를 사용하여 프로모션 코드 목록을 수동으로 생성하고 메시지 참조를 업데이트하는 간단한 프로세스입니다.

{% alert note %}
데이터 피드는 지원이 중단될 예정입니다. Braze는 데이터 피드를 사용하는 고객이 프로모션 코드 목록으로 전환할 것을 권장합니다.
{% endalert %}

## 기능 및 특징 {#features-and-functionality}

프로모션 코드 목록과 데이터 피드 사이에는 몇 가지 차이점이 있습니다.

| 기능 | 프로모션 코드 | 데이터 피드 |
|------------------|-----------------|--------------|
| 설명 | 예 | 아니요 |
| 만료일 | 예 | 아니요 |
| 생성 방법 | CSV 업로드 | 텍스트 붙여넣기 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Features and functionality" }

## 마이그레이션 방법 {#how-to-migrate}

데이터 피드를 프로모션 코드 목록으로 대체하려면 다음을 수행합니다:

1. **Data Settings**으로 이동하여 **Create Promotion Code List**를 선택합니다.
2. [프로모션 코드 목록을 설정합니다]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/).
3. 이전에 데이터 피드를 참조했던 메시지로 이동하여 프로모션 코드 목록을 사용하도록 업데이트합니다.