---
nav_title: 제품 블록
article_title: 드래그 앤 드롭 제품 블록
page_order: 5
description: "이 참조 문서에서는 사용자가 카탈로그 항목의 동적 또는 정적 쇼케이스를 신속하게 추가하고 구성할 수 있는 드래그 앤 드롭 제품 블록을 다룹니다."
tool:
    - Campaigns
    - Canvas
alias: /dnd_product_blocks/
---

# 드래그 앤 드롭 제품 블록 {#drag-and-drop-product-blocks}

> 드래그 앤 드롭 편집기를 사용하면 커스텀 Liquid 코드를 만들 필요 없이 메시지에 제품 블록을 신속하게 추가하고 구성하여 원활한 제품 쇼케이스를 만들 수 있습니다.

{% alert important %}
드래그 앤 드롭 제품 블록 기능은 얼리 액세스 중이며 현재 이메일에만 제공됩니다. 얼리 액세스에 참여하고 싶다면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 요구 사항 {#requirements}

| 요구 사항 | 설명 |
| --- | --- |
| eCommerce 추천 이벤트 | [eCommerce 추천 이벤트]({{site.baseurl}}/ecommerce_events)는 주문이 이루어지기 전후에 발생하는 주요 행동 이벤트에 대한 표준화된 데이터 스키마를 제공합니다. 이 이벤트는 궁극적으로 레거시 Braze 구매 이벤트를 대체하고 상거래 관련 행동 추적의 표준이 될 것입니다. <br><br> eCommerce 추천 이벤트는 동적 제품 블록에 필요합니다. |
| eCommerce 캔버스 템플릿 | eCommerce 추천 이벤트는 방치된 탐색, 유기한 장바구니 및 주문 확인과 같은 필수 사용 사례를 위해 설계된 eCommerce 캔버스 템플릿을 포함한 미리 구축된 템플릿을 지원합니다. <br><br>[eCommerce 캔버스 템플릿]({{site.baseurl}}/ecommerce_use_cases)을 사용하여 이러한 필수 eCommerce 사용 사례 중 하나를 구현할 계획이라면 제공된 캔버스 템플릿을 사용하거나 따라야 합니다. |
| Braze 카탈로그 | Braze 카탈로그를 생성해야 하며, 여기에는 제품 블록 구성에서 사용하는 다음 필드가 포함되어야 합니다:{::nomarkdown}<code><ul><li>product_title</li><li>product_url</li><li>variant_image_url</li></ul></code>{:/} |
| 카탈로그 선택 | 정적 제품 블록의 경우, 제품 블록에 포함할 제품을 지정하기 위해 [카탈로그 선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 생성해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요구 사항" }

## 드래그 앤 드롭 제품 블록의 유형 {#types-of-drag-and-drop-product-blocks}

| 제품 블록 | 목적 | 활용 사례 | 사용 가능 여부 |
| --- | --- | --- | --- |
| 동적 | [eCommerce 추천 이벤트]({{site.baseurl}}/ecommerce_events)와 카탈로그를 [eCommerce 캔버스 템플릿]({{site.baseurl}}/ecommerce_use_cases) 내에서 사용하여 고객 상호작용을 기반으로 제품 쇼케이스로 메시징을 개인화합니다. | {::nomarkdown}<ul><li>방치된 탐색</li><li>유기한 장바구니</li><li>유기한 결제</li><li>주문 확인</li></ul>{:/} | Canvas에서만 사용 가능합니다. |
| 정적 | Braze 카탈로그에 저장된 데이터를 사용하여 제품을 개인화합니다. 포함할 제품을 지정하려면 [카탈로그 선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 사용해야 합니다. | 신제품 출시 또는 카테고리별 상품을 쇼케이스하는 데 적합합니다. | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="드래그 앤 드롭 제품 블록의 유형" }

## 제품 블록 콘텐츠 구성 {#product-block-content-configuration}

각 블록 유형에는 서로 다른 콘텐츠 구성이 있습니다.

### 제품 필드 {#product-fields}

**Product Fields** 섹션에서 제품 블록 유형을 선택한 다음, 각 제품에 포함할 필드를 토글로 켜세요. 각 필드는 선택한 제품 블록 유형에 따라 다른 소스에서 가져옵니다.

#### 동적 제품 블록 {#dynamic-product-block}

| 제품 필드 | 소스 |
| --- | --- |
| 배리언트 이미지 | 카탈로그 |
| 제품 제목 | 카탈로그 |
| 제품 URL 버튼 | 카탈로그 |
| 가격 | eCommerce 추천 이벤트 속성정보 |
| 수량 | eCommerce 추천 이벤트 속성정보 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="동적 제품 블록" }

![카탈로그 데이터와 이벤트 데이터로 구분된 동적 제품 블록의 제품 필드]({% image_buster /assets/img/product_blocks/dynamic_fields.png %}){: style="max-width:50%;"}

#### 정적 제품 블록 {#static-product-block}

| 제품 필드 | 소스 |
| --- | --- |
| 배리언트 이미지 | 카탈로그 |
| 제품 제목 | 카탈로그 |
| 제품 URL 버튼 | 카탈로그 |
| 가격 | 카탈로그 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="정적 제품 블록" }

![모두 카탈로그 데이터로 분류된 정적 제품 블록의 제품 필드]({% image_buster /assets/img/product_blocks/static_fields.png %}){: style="max-width:50%;"}

### 레이아웃 옵션 {#layout-options}

레이아웃 옵션을 사용하여 제품 블록 내에서 제품이 표시되는 방식을 커스터마이즈하세요.

| 옵션 | 설명 |
| --- | --- |
| 제품 방향 | 블록 내에서 이미지와 제품 필드의 방향을 선택합니다. |
| 정렬 | 블록 내에서 텍스트 필드와 버튼의 정렬을 조정합니다. |
| 행당 최대 제품 수 | 행당 최대 3개의 제품을 표시하며, 정적 제품 블록은 총 최대 12개, 동적 제품 블록은 총 최대 24개의 제품을 표시할 수 있습니다. |
| 제품 간격 | 제품 간의 간격을 설정합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="레이아웃 옵션" }

![제품 방향, 정렬, 행당 최대 제품 수, 제품 간격에 대한 레이아웃 옵션]({% image_buster /assets/img/product_blocks/layout_options.png %}){: style="max-width:50%;"}

### 글로벌 이메일 스타일 설정 {#global-email-style-settings}

[글로벌 이메일 스타일 설정]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings)을 사용하면 Braze 내에서 이메일에 일관된 스타일을 적용할 수 있습니다. 즉, 글꼴, 색상, 버튼 디자인 등 특정 스타일을 정의하면 모든 이메일에 자동으로 적용됩니다.

#### 글로벌 이메일 스타일 설정이 제품 블록과 작동하는 방식 {#how-global-email-style-settings-work-with-product-blocks}

단락과 버튼에 대한 기존 스타일이 제품 블록 내의 텍스트 및 버튼 요소에 자동으로 적용됩니다. 즉, 단락과 버튼에 설정한 서식이 제품 블록에서도 일관되게 사용되어 이메일 전체에서 통일된 외관을 유지합니다.

## 제품 블록 설정 {#setting-up-product-blocks}

### 카탈로그 설정 {#catalog-setup}

{% alert important %}
[제품 동기화]({{site.baseurl}}/shopify_catalogs)를 위해 Braze와 Shopify 통합을 사용하고 있다면 드래그 앤 드롭 제품 블록을 사용하기 위한 추가 단계가 필요하지 않습니다.<br><br> 제품 배리언트 정보가 없는 경우, 이벤트 페이로드와 카탈로그 내의 제품 및 제품 배리언트 필드 모두에 최상위 제품 정보를 복제해야 합니다. 즉, 제품 블록이 올바르게 작동하도록 두 식별자 모두에 동일한 제품 세부 정보를 제공하여 일관성을 유지해야 합니다.
{% endalert %}

드래그 앤 드롭 제품 블록을 사용하려면 특정 필드 값을 포함하는 Braze 카탈로그를 설정해야 합니다. 이 필드는 제품 블록 구성에 사용됩니다. 카탈로그에 다음 필드가 포함되어 있는지 확인하세요:

| 필드 | 설명 |
| --- | --- |
| `product_title` | 제품의 제목입니다. |
| `product_url` | 고객이 제품을 보거나 구매할 수 있는 URL입니다. |
| `variant_image_url` | 배리언트 이미지의 URL입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="카탈로그 설정" }

필수 필드가 포함된 이 [샘플 제품 카탈로그](/docs/assets/download_file/ecommerce_product_catalog_sample.csv)를 활용하여 빠르게 시작하세요.

![필수 필드와 기타 필드가 포함된 샘플 CSV 파일]({% image_buster /assets/img/ecommerce/sample_product_catalog.png %})

#### 카탈로그 필드에 매핑 {#mapping-to-catalog-fields}

카탈로그의 **설정** 탭에서 **Product blocks** 토글을 선택하여 카탈로그의 특정 필드와 정보에 매핑할 수 있습니다. 이를 통해 제품 제목, 제품 URL, 이미지 URL로 사용할 필드를 선택할 수 있습니다. Shopify 카탈로그 필드는 기본적으로 매핑되어 있으며 변경할 수 없습니다.

{% alert note %}
Shopify를 사용하지 않는 경우, 계정 매니저에게 문의하여 필드 매핑을 활성화할 수 있습니다. 이를 통해 모든 카탈로그를 제품 블록에 연결하고 해당 필드를 `product_title`, `product_url`, `variant_image_url`에 매핑할 수 있습니다.
{% endalert %}

## 제품 블록 생성 {#creating-product-blocks}

이 가이드에서는 이메일 드래그 앤 드롭 편집기를 사용하여 동적 또는 정적 제품 블록을 생성, 테스트하고 기능을 확인하는 단계를 안내합니다.

### 1단계: 이메일 Campaign 또는 이메일 캔버스 단계 생성 {#step-1-create-an-email-campaign-or-email-canvas-step}

#### 동적 제품 블록

{% alert note %}
동적 제품 블록은 [eCommerce 추천 이벤트]({{site.baseurl}}/ecommerce_events)가 필요하며 [Canvases]({{site.baseurl}}/ecommerce_use_cases) 내에서만 사용할 수 있습니다. Braze Shopify 사용자의 경우 이러한 이벤트가 통합의 일부로 자동 포함됩니다. Shopify를 사용하지 않는 사용자의 경우 개발자와 협력하여 이러한 이벤트를 Braze에 전달하고 이벤트 내의 기본 제품 식별자가 카탈로그 항목 ID로 추가되었는지 확인해야 합니다.
{% endalert %}

특정 활용 사례에 맞는 Braze 템플릿 중 하나를 사용하여 새 Canvas를 생성하세요:
- 방치된 탐색
- 유기한 장바구니
- 유기한 결제
- 주문 확인

eCommerce Canvas 생성에 대한 자세한 안내는 [eCommerce 활용 사례]({{site.baseurl}}/ecommerce_use_cases)를 참조하세요.

#### 정적 제품 블록

드래그 앤 드롭 이메일 Campaign, 액션 기반 Canvas 또는 드래그 앤 드롭 이메일 메시지 단계가 있는 템플릿을 생성하세요.

### 2단계: 제품 블록 추가 {#step-2-add-a-product-block}

{% tabs %}
{% tab 동적 제품 블록 %}

메시지 단계 내에서 드래그 앤 드롭 이메일 작성기를 사용하여 이메일을 생성하거나 기존 템플릿을 수정하세요.
제품 블록을 이메일 메시지로 드래그하세요.
동적 블록 유형이 선택되어 있는지 확인하세요.
개인화에 사용할 제품 카탈로그를 선택하세요. 타겟팅하는 인바운드 이벤트의 제품과 일치하는지 확인하세요.

{% endtab %}
{% tab 정적 제품 블록 %}

제품 블록을 이메일 메시지로 드래그하고 정적 블록 유형을 선택하세요.
제품 블록에 사용할 카탈로그를 선택하세요. 제품 블록에 표시할 제품을 지정하려면 카탈로그 선택을 선택해야 합니다.

{% endtab %}
{% endtabs %}

![제품 블록 등의 편집기 블록이 포함된 콘텐츠 탭]({% image_buster /assets/img/product_blocks/product_block.png %}){: style="max-width:40%;"}

### 3단계: 제품 필드 구성 {#step-3-configure-product-fields}

제품 블록에 표시할 [제품 필드](#product-fields)를 선택하세요. 변경할 때마다 **Apply Settings**를 선택하여 편집기에서 업데이트를 확인하세요.

Liquid 태그 앞에 텍스트를 커스터마이즈할 수도 있습니다. 예를 들어, 항목 가격 앞에 달러 기호($)를 추가하거나 수량 용어를 "amount" 또는 다른 선호하는 레이블로 변경할 수 있습니다.

![항목 가격 앞에 달러 기호가 추가된 제품 블록]({% image_buster /assets/img/product_blocks/liquid.png %}){: style="max-width:45%;"}

### 4단계: 레이아웃 설정 구성 {#step-4-configure-layout-settings}

[레이아웃 옵션](#layout-options)을 변경하여 제품 블록 내에서 제품이 표시되는 방식을 업데이트하고, 변경할 때마다 **Apply settings**를 선택하세요.

### 5단계: 메시지 미리보기 및 테스트 {#step-5-preview-and-test-your-message}

{% tabs %}
{% tab 동적 제품 블록 %}

1. **Preview & Test** 섹션에서 커스텀 사용자로 메시지를 미리보기하세요.
2. 미리보기에서 렌더링할 항목 수를 지정하세요.
3. 올바른 수의 항목이 표시되고 레이아웃 옵션이 올바르게 적용되었는지 확인하세요. 표시되는 항목은 무작위로 선택됩니다.

![4개의 항목을 표시하도록 지정된 동적 제품 블록 드롭다운 섹션이 있는 사용자로 미리보기 탭]({% image_buster /assets/img/product_blocks/preview_as_a_user.png %}){: style="max-width:40%;"}

{% endtab %}
{% tab 정적 제품 블록 %}

제품 블록에 변경 사항을 적용하면 드래그 앤 드롭 작성기 내에서 미리보기가 생성됩니다.

![다양한 항목 타일이 있는 생성된 제품 블록을 보여주는 이메일 드래그 앤 드롭 작성기]({% image_buster /assets/img/product_blocks/static_block_preview.png %})

{% endtab %}
{% endtabs %}

메시지 작성을 완료하고 예상대로 보이는지 확인한 후 전송할 준비가 되었습니다!