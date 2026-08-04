---
nav_title: 고유 할인 코드
article_title: 고유 할인 코드 보내기
alias: /shopify_discount_codes/
page_order: 7
description: "이 참조 문서에서는 Braze 프로모션 코드와 Shopify Bulk Discount Code Bot을 사용하여 Campaigns 및 Canvases를 통해 고유 할인 코드를 보내는 커뮤니티 제출 사용 사례를 다룹니다."
---

# Shopify를 통해 고유 할인 코드 보내기 {#send-unique-discount-codes-through-shopify}

> 이 커뮤니티 제출 사용 사례에서는 Braze [프로모션 코드]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes)와 Shopify Bulk Discount Code Bot을 사용하여 Campaigns 및 Canvases에 사용할 고유 할인 코드를 생성하는 방법을 보여줍니다. 고유 할인 코드는 일반 프로모션 코드의 악용을 방지하는 데 도움이 됩니다.

{% alert important %}
이것은 커뮤니티에서 제출한 통합이며 Braze에서 직접 지원하지 않습니다. Bulk Discount Code Bot은 Shopify에서 직접 지원합니다. Braze 프로모션 코드만 Braze에서 지원됩니다.
{% endalert %}

## 요구 사항 {#requirements}

| 요구 사항 | 설명 |
| --- | --- |
| Shopify 스토어 설정 | [Braze와 Shopify 스토어를 설정]({{site.baseurl}}/shopify_overview)했는지 확인합니다. |
| Bulk Discount Code Bot 앱 설치 | Shopify 앱 스토어에서 [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) 앱을 다운로드합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="요구 사항" }

## 고유 할인 코드 생성하기 {#generating-unique-discount-codes}

### 1단계: 할인 코드 구성하기 {#step-1-configure-your-discount-codes}

Bulk Discount Code Bot을 사용하여 생성할 코드 수, 코드 길이, 할인 값 등을 기반으로 할인 코드를 구성합니다.

![할인 세트의 구성 옵션.][1]

### 2단계: 코드 내보내기 {#step-2-export-your-codes}

Bulk Discount Code Bot의 검색창에서 할인 세트를 찾은 다음 **Export Codes** > **Download Codes**를 선택하여 CSV 파일을 다운로드 폴더에 다운로드합니다.

![할인 세트가 표시된 드롭다운과 선택할 수 있는 버튼 행이 있는 검색창.][2]{: style="max-width:70%;"}

CSV 파일에서 1행을 삭제하여 열 헤더 "Promo"를 제거합니다. 이렇게 하면 "Promo"가 Braze에서 할인 코드로 등록되는 것을 방지할 수 있습니다.

![CSV 파일에서 행 헤더 "Promo" 제거를 보여주는 순서도.][3]{: style="max-width:60%;"}

### 3단계: Braze에 할인 코드 추가하기 {#step-3-add-your-discount-codes-to-braze}

Braze에서 **데이터 설정** > **프로모션 코드** > **프로모션 코드 목록 생성**으로 이동하여 [할인 코드 목록을 구성]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/promotion_codes/create#create)합니다. Bulk Discount Code Bot에서 구성한 만료 날짜와 일치하는지 확인합니다.

그런 다음 CSV 파일을 업로드하고 **목록 저장**을 선택합니다.

### 4단계: Braze Campaign 또는 캔버스 단계에 할인 코드 추가하기 {#step-4-add-your-discount-codes-to-a-braze-campaign-or-canvas-step}

단일 발송 Campaign에서 고유 할인 코드를 사용하거나, 사용자가 여러 Campaign 또는 캔버스 단계에서 여러 고유 코드를 받는 것이 괜찮다면, 저장한 프로모션 코드 목록에서 코드의 Liquid 스니펫을 복사합니다.

![복사 버튼이 있는 Liquid 코드 스니펫.][4]{: style="max-width:60%;"}

Liquid 스니펫을 Campaign 또는 캔버스 단계에 붙여넣습니다.

<video autoplay muted loop playsinline loading="lazy" style="max-width:100%;" aria-label="Liquid 스니펫이 캔버스 단계에 추가되는 것을 보여주는 동영상.">
  <source src="{% image_buster /assets/img/shopify/liquid_promo_code.mp4 %}" type="video/mp4">
</video>

Campaigns 또는 Canvases에서 할인 코드가 몇 번 참조되더라도 사용자가 하나의 고유 할인 코드만 받도록 하려면, 첫 번째 메시지 단계 바로 앞에 "Promo Code"와 같은 커스텀 속성에 할인 코드를 할당하는 [사용자 업데이트]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) 단계를 생성합니다.

{% alert tip %}
**데이터 설정** > **커스텀 속성**으로 이동하여 [커스텀 속성을 생성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)할 수도 있습니다.
{% endalert %}

사용자 업데이트 단계에서 각 필드에 대해 다음을 수행합니다:
- **Attribute Name:** **Promo Code**를 선택합니다.
- **Action:** **Update**를 선택합니다.
- **Key Value:** Liquid 코드 스니펫을 붙여넣습니다.

![Liquid 스니펫으로 "Promo Code" 속성을 업데이트하는 사용자 업데이트 단계.][6]

이제 커스텀 속성 {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}를 모든 메시지에 추가할 수 있으며, 할인 코드가 템플릿으로 삽입됩니다.

## 할인 코드 동작 {#discount-code-behavior}

{% details 멀티채널 Campaign 또는 캔버스 단계 %}

멀티채널 Campaign 또는 캔버스 단계에서 할인 코드 스니펫을 사용하면 사용자는 항상 고유 코드를 받습니다. 사용자가 둘 이상의 채널을 통해 코드를 받을 자격이 있는 경우, 각 채널을 통해 동일한 코드를 받게 됩니다. 즉, 자격이 있는 사용자는 해당 Campaign 또는 캔버스 단계에서 보낸 모든 메시지에 대해 하나의 코드만 받게 됩니다.

{% enddetails %}

{% details 서로 다른 캔버스 단계 또는 별도의 Campaigns %}

동일한 Canvas의 여러 단계 또는 별도의 Campaigns에서 할인 코드가 참조되는 경우, 자격이 있는 사용자는 여러 개의 고유 프로모션 코드를 받게 됩니다(각 캔버스 단계 또는 Campaign당 하나의 코드).

{% enddetails %}

[1]: {% image_buster /assets/img/shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/shopify/liquid_code_snippet.png %}
[6]: {% image_buster /assets/img/shopify/user_update_step.png %}